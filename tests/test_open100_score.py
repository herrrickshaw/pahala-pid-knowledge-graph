"""Tests for benchmarks/open100/score.py using small synthetic GraphML ground truth
and synthetic extraction JSON (no OPEN100 data and no real drawing is read)."""
import json
import os

import networkx as nx
import pytest
from PIL import Image

import score as S


def bbox(cx, cy, d=0.01):
    return {"xmin": cx - 5, "xmax": cx + 5, "ymin": cy - 5, "ymax": cy + 5}


def write_gt(path, nodes, edges):
    g = nx.Graph()
    for nid, label, cx, cy in nodes:
        g.add_node(nid, label=label, **bbox(cx, cy))
    for a, b in edges:
        g.add_edge(a, b)
    nx.write_graphml(g, path)


# ---------------------------------------------------------------- small helpers
def test_prf_zero_denominators_give_zero():
    assert S.prf(0, 0, 0) == (0.0, 0.0, 0.0)
    assert S.prf(0, 3, 0) == (0.0, 0.0, 0.0)


def test_prf_values():
    p, r, f = S.prf(2, 2, 6)
    assert (p, r) == (0.5, 0.25)
    assert f == pytest.approx(2 * 0.5 * 0.25 / 0.75)


def test_ctr_is_bbox_midpoint_and_parses_strings():
    assert S.ctr({"xmin": "10", "xmax": "20", "ymin": "0", "ymax": "4"}) == (15.0, 2.0)


# ---------------------------------------------------------------- ground truth
def test_load_gt_collapses_connector_chains_into_semantic_edges(tmp_path):
    p = tmp_path / "g.graphml"
    write_gt(
        p,
        [("t", "tank", 10, 10), ("c1", "connector", 20, 10), ("x", "crossing", 30, 10),
         ("v", "valve", 40, 10), ("bg", "background", 0, 0), ("pu", "pump", 90, 90)],
        [("t", "c1"), ("c1", "x"), ("x", "v"), ("v", "bg"), ("pu", "bg")],
    )
    sem, edges = S.load_gt(str(p))
    assert set(sem) == {"t", "v", "pu"}
    # tank and valve are joined through connector+crossing; background links are ignored,
    # so the pump stays isolated.
    assert edges == {("t", "v")}


def test_load_gt_direct_semantic_edge_is_sorted_pair(tmp_path):
    p = tmp_path / "g.graphml"
    write_gt(p, [("b", "valve", 0, 0), ("a", "pump", 5, 5)], [("b", "a")])
    _, edges = S.load_gt(str(p))
    assert edges == {("a", "b")}


def test_load_gt_three_way_junction_makes_all_pairs(tmp_path):
    p = tmp_path / "g.graphml"
    write_gt(
        p,
        [("a", "tank", 0, 0), ("b", "valve", 1, 1), ("c", "pump", 2, 2), ("j", "connector", 3, 3)],
        [("a", "j"), ("b", "j"), ("c", "j")],
    )
    _, edges = S.load_gt(str(p))
    assert edges == {("a", "b"), ("a", "c"), ("b", "c")}


def test_load_gt_drop_turns_a_semantic_node_into_a_pass_through(tmp_path):
    p = tmp_path / "g.graphml"
    write_gt(
        p,
        [("a", "tank", 0, 0), ("m", "general", 1, 1), ("b", "pump", 2, 2)],
        [("a", "m"), ("m", "b")],
    )
    sem, edges = S.load_gt(str(p))
    assert set(sem) == {"a", "m", "b"}
    assert edges == {("a", "m"), ("b", "m")}
    sem2, edges2 = S.load_gt(str(p), drop={"m"})
    assert set(sem2) == {"a", "b"}
    assert edges2 == {("a", "b")}


def test_load_gt_ignores_unlisted_labels_when_unconnected(tmp_path):
    p = tmp_path / "g.graphml"
    write_gt(p, [("a", "tank", 0, 0), ("b", "text", 1, 1)], [])
    sem, edges = S.load_gt(str(p))
    assert set(sem) == {"a"} and edges == set()


@pytest.mark.xfail(strict=True, raises=KeyError,
                   reason="an edge to a node whose label is not semantic/primitive/background creates a label-less node in load_gt")
def test_load_gt_edge_to_unlisted_label_does_not_crash(tmp_path):
    p = tmp_path / "g.graphml"
    write_gt(p, [("a", "tank", 0, 0), ("b", "text", 1, 1)], [("a", "b")])
    S.load_gt(str(p))


# ---------------------------------------------------------------- our_class
@pytest.mark.parametrize(
    "group,kind,expected",
    [
        ("instruments", None, "instrumentation"),
        ("off_page_connectors", None, "inlet/outlet"),
        ("boundaries", None, "boundary"),
        ("components", "Gate Valve", "valve"),
        ("components", "PRV-2", "valve"),
        ("components", "psv", "valve"),
        ("components", "Relief device", "valve"),
        ("components", "reducer", "general"),
        ("components", None, "general"),
        ("equipment", "Surge Tank", "tank"),
        ("equipment", "pressure VESSEL", "tank"),
        ("equipment", "sump", "tank"),
        ("equipment", "Basin", "tank"),
        ("equipment", "drum", "tank"),
        ("equipment", "clarifier", "tank"),
        ("equipment", "Feed Pump", "pump"),
        ("equipment", "blower", "general"),
        ("equipment", None, "general"),
    ],
)
def test_our_class(group, kind, expected):
    assert S.our_class(group, {"kind": kind}) == expected


def test_our_class_unknown_group_is_none():
    assert S.our_class("signals", {}) is None


# ---------------------------------------------------------------- load_ours
def item(i, kind=None, box=(0.1, 0.1, 0.2, 0.2), tag=None):
    return {"id": i, "kind": kind, "bbox": list(box), "tag": tag}


def write_ex(path, **doc):
    path.write_text(json.dumps(doc))
    return str(path)


def test_load_ours_items_classes_and_clique_edges(tmp_path):
    f = write_ex(
        tmp_path / "p.json",
        equipment=[item("E1", "tank"), item("E2", "pump")],
        components=[item("V1", "valve")],
        instruments=[item("I1")],
        off_page_connectors=[item("O1")],
        boundaries=[item("B1")],
        lines=[
            {"id": "L1", "from": "E1", "to": "V1", "path": []},
            {"id": "L2", "from": "V1", "to": "E2", "path": []},
        ],
    )
    items, edges = S.load_ours(f)
    assert {k: v["cls"] for k, v in items.items()} == {
        "E1": "tank", "E2": "pump", "V1": "valve", "I1": "instrumentation",
        "O1": "inlet/outlet", "B1": "boundary",
    }
    assert items["E1"]["grp"] == "equipment"
    assert edges == {("E1", "V1"), ("E2", "V1")}


def test_load_ours_path_elements_make_adjacent_segments(tmp_path):
    f = write_ex(
        tmp_path / "p.json",
        equipment=[item("A", "tank"), item("B", "pump")],
        components=[item("V", "valve")],
        lines=[{"id": "L", "from": "A", "to": "B", "path": ["V"]}],
    )
    items, edges, adj = S.load_ours(f, return_adj=True)
    # each segment is its own component, so A and B (two segments apart) are not joined
    assert edges == {("A", "V"), ("B", "V")}
    assert adj == {("A", "V"), ("B", "V")}


def test_load_ours_tee_joins_branch_to_trunk_segment(tmp_path):
    f = write_ex(
        tmp_path / "p.json",
        equipment=[item("E1", "tank"), item("E3", "pump")],
        components=[item("V1", "valve")],
        lines=[
            {"id": "L1", "from": "E1", "to": "V1", "path": []},
            {"id": "L3", "from": {"line": "L1", "after": "E1"}, "to": "E3", "path": []},
        ],
    )
    items, edges, adj = S.load_ours(f, return_adj=True)
    assert edges == {("E1", "V1"), ("E1", "E3"), ("E3", "V1")}
    assert adj == {("E1", "V1"), ("E1", "E3"), ("E3", "V1")}


def test_load_ours_tee_at_end_of_branch(tmp_path):
    # branch whose *to* end is the tee: uses the last segment of the branch
    f = write_ex(
        tmp_path / "p.json",
        equipment=[item("E1", "tank"), item("E3", "pump")],
        components=[item("V1", "valve")],
        lines=[
            {"id": "L1", "from": "E1", "to": "V1", "path": []},
            {"id": "L3", "from": "E3", "to": {"line": "L1", "after": "E1"}, "path": []},
        ],
    )
    items, edges, adj = S.load_ours(f, return_adj=True)
    assert edges == {("E1", "V1"), ("E1", "E3"), ("E3", "V1")}


def test_load_ours_tee_with_unknown_after_falls_back_to_first_segment(tmp_path):
    f = write_ex(
        tmp_path / "p.json",
        equipment=[item("E1", "tank"), item("E3", "pump")],
        components=[item("V1", "valve")],
        lines=[
            {"id": "L1", "from": "E1", "to": "V1", "path": []},
            {"id": "L3", "from": {"line": "L1", "after": "nope"}, "to": "E3", "path": []},
        ],
    )
    _, edges, adj = S.load_ours(f, return_adj=True)
    assert ("E1", "E3") in edges
    assert ("E3", "V1") in adj and ("E1", "E3") not in adj


def test_load_ours_tee_to_missing_line_is_ignored(tmp_path):
    f = write_ex(
        tmp_path / "p.json",
        equipment=[item("E3", "pump"), item("E1", "tank")],
        lines=[{"id": "L3", "from": {"line": "GONE", "after": "x"}, "to": "E3", "path": []}],
    )
    items, edges, adj = S.load_ours(f, return_adj=True)
    assert edges == set() and adj == set()


def test_load_ours_instrument_measures_item_and_line(tmp_path):
    f = write_ex(
        tmp_path / "p.json",
        equipment=[item("E1", "tank"), item("E2", "pump")],
        components=[item("V1", "valve")],
        instruments=[
            {**item("I1"), "measures": {"item": "E1"}},
            {**item("I2"), "measures": {"line": "L1", "after": "E1"}},
            # measuring a component (valve) is not an item-link
            {**item("I3"), "measures": {"item": "V1"}},
            {**item("I4"), "measures": None},
            item("I5"),
        ],
        lines=[{"id": "L1", "from": "E1", "to": "E2", "path": []}],
    )
    _, edges = S.load_ours(f)
    assert ("E1", "I1") in edges
    assert {("E1", "I2"), ("E2", "I2"), ("E1", "E2")} <= edges
    assert not any("I3" in e or "I4" in e or "I5" in e for e in edges)


def test_load_ours_signals_link_known_items_only(tmp_path):
    f = write_ex(
        tmp_path / "p.json",
        equipment=[item("E1", "tank")],
        instruments=[item("I1")],
        signals=[{"from": "I1", "to": "E1"}, {"from": "I1", "to": "ghost"}],
    )
    _, edges = S.load_ours(f)
    assert edges == {("E1", "I1")}


def test_load_ours_item_without_bbox_is_kept(tmp_path):
    f = write_ex(tmp_path / "p.json", equipment=[{"id": "E1", "kind": "tank"}])
    items, _ = S.load_ours(f)
    assert items["E1"]["bbox"] is None


def test_load_ours_empty_document(tmp_path):
    items, edges = S.load_ours(write_ex(tmp_path / "p.json"))
    assert items == {} and edges == set()


# ---------------------------------------------------------------- match
GT = {"g1": {"label": "valve", "xmin": 95, "xmax": 105, "ymin": 95, "ymax": 105},
      "g2": {"label": "pump", "xmin": 495, "xmax": 505, "ymin": 495, "ymax": 505}}


def ours_at(x, y, cls, size=0.002):
    return {"cls": cls, "bbox": [x - size, y - size, x + size, y + size]}


def test_match_requires_same_class_by_default():
    ours = {"o1": ours_at(0.1, 0.1, "pump")}
    assert S.match(GT, ours, 1000, 1000, 0.05) == {}
    assert S.match(GT, ours, 1000, 1000, 0.05, same_class=False) == {"o1": "g1"}


def test_match_radius_is_fraction_of_width_and_inclusive():
    ours = {"o1": ours_at(0.11, 0.1, "valve")}  # 10 px right of g1
    assert S.match(GT, ours, 1000, 1000, 0.01) == {"o1": "g1"}
    assert S.match(GT, ours, 1000, 1000, 0.009) == {}


def test_match_is_one_to_one_and_nearest_first():
    ours = {"far": ours_at(0.12, 0.1, "valve"), "near": ours_at(0.101, 0.1, "valve")}
    assert S.match(GT, ours, 1000, 1000, 0.05) == {"near": "g1"}


def test_match_coarse_merges_equipment_like_classes():
    ours = {"o": ours_at(0.5, 0.5, "tank")}
    assert S.match(GT, ours, 1000, 1000, 0.01) == {}
    assert S.match(GT, ours, 1000, 1000, 0.01, coarse=True) == {"o": "g2"}


def test_match_skips_items_without_bbox():
    assert S.match(GT, {"o": {"cls": "valve", "bbox": None}}, 1000, 1000, 0.5) == {}


# ---------------------------------------------------------------- main (end to end)
def build_scene(tmp_path, with_second_page=False):
    gtd = tmp_path / "gt"
    ex = tmp_path / "ex"
    gtd.mkdir()
    ex.mkdir()
    Image.new("RGB", (1000, 1000), "white").save(gtd / "0.png")
    write_gt(
        gtd / "0.graphml",
        [("t", "tank", 200, 200), ("c", "connector", 300, 300), ("v", "valve", 500, 500)],
        [("t", "c"), ("c", "v")],
    )
    doc = {
        "equipment": [item("E1", "tank", (0.195, 0.195, 0.205, 0.205))],
        "components": [item("V1", "valve", (0.495, 0.495, 0.505, 0.505))],
        "lines": [{"id": "L1", "from": "E1", "to": "V1", "path": []}],
    }
    (ex / "page_01.json").write_text(json.dumps(doc))
    return str(ex), str(gtd)


def test_main_perfect_extraction_scores_one(tmp_path, monkeypatch, capsys):
    ex, gtd = build_scene(tmp_path)
    monkeypatch.setattr("sys.argv", ["score.py", ex, gtd, "1"])
    S.main()
    out = capsys.readouterr().out
    assert "pages scored: [1]" in out
    for r in (1, 2, 4):
        assert f"=== node match radius {r}% of image width" in out
    assert out.count("ALL nodes      GT    2 ours    2  P 1.00 R 1.00 F1 1.00") == 3
    assert "edges among matched nodes: P 1.00 R 1.00 F1 1.00  (TP 1 FP 0 FN 0);  GT edges total 1, recall vs all GT edges 1.00" in out
    assert "PROCESS edges (no instruments) among matched nodes: P 1.00 R 1.00 F1 1.00 (TP 1 FP 0 FN 0)" in out
    assert "equipment+other symbols: GT 1 ours 1 P 1.00 R 1.00 F1 1.00" in out
    assert "edges[clique] among matched nodes: P 1.00 R 1.00 F1 1.00 (TP 1 FP 0 FN 0)" in out
    assert "edges[adj   ] among matched nodes: P 1.00 R 1.00 F1 1.00 (TP 1 FP 0 FN 0)" in out


def test_main_missing_page_is_skipped_and_wrong_class_counts_as_error(tmp_path, monkeypatch, capsys):
    ex, gtd = build_scene(tmp_path)
    # call the valve a pump: no valve match, and one pump false positive
    p = os.path.join(ex, "page_01.json")
    d = json.load(open(p))
    d["components"] = []
    d["equipment"].append(item("E2", "pump", (0.495, 0.495, 0.505, 0.505)))
    json.dump(d, open(p, "w"))
    monkeypatch.setattr("sys.argv", ["score.py", ex, gtd, "1", "2"])
    S.main()
    out = capsys.readouterr().out
    assert "pages scored: [1]" in out
    assert "valve          GT    1 ours    0  P 0.00 R 0.00 F1 0.00" in out
    assert "pump           GT    0 ours    1  P 0.00 R 0.00 F1 0.00" in out
    assert "tank           GT    1 ours    1  P 1.00 R 1.00 F1 1.00" in out
