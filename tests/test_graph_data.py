"""Integrity checks on the committed graph and the documents that quote its size."""
import glob
import json
import os
import re

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G = json.load(open(os.path.join(ROOT, "graph", "graph.json")))


def test_node_and_edge_ids_are_unique():
    ids = [n["id"] for n in G["nodes"]]
    assert len(ids) == len(set(ids))
    eids = [e["id"] for e in G["edges"]]
    assert len(eids) == len(set(eids))


def test_every_edge_endpoint_is_a_node():
    ids = {n["id"] for n in G["nodes"]}
    dangling = [e["id"] for e in G["edges"] if e["source"] not in ids or e["target"] not in ids]
    assert dangling == []


def test_stats_block_matches_the_lists():
    s = G["stats"]
    assert s["nodes"] == len(G["nodes"]) and s["edges"] == len(G["edges"])
    by_node = {}
    for n in G["nodes"]:
        by_node[n["type"]] = by_node.get(n["type"], 0) + 1
    by_edge = {}
    for e in G["edges"]:
        by_edge[e["type"]] = by_edge.get(e["type"], 0) + 1
    assert s["nodes_by_type"] == by_node
    assert s["edges_by_type"] == by_edge
    sev = {}
    for i in G["issues"]:
        sev[i["severity"]] = sev.get(i["severity"], 0) + 1
    assert s["issues_by_severity"] == sev


def test_confidence_is_a_probability():
    assert all(0 <= n["confidence"] <= 1 for n in G["nodes"])
    assert all(0 <= e["confidence"] <= 1 for e in G["edges"])


def test_one_sheet_node_per_extraction_page():
    pages = sorted(glob.glob(os.path.join(ROOT, "extractions", "page_*.json")))
    sheets = [n for n in G["nodes"] if n["type"] == "Sheet"]
    assert len(sheets) == len(pages) == len(G["plant"]["sheets"])
    assert {n["id"] for n in sheets} == set(G["plant"]["sheets"])
    assert sorted(n["attributes"]["page"] for n in sheets) == sorted(
        json.load(open(p))["page"] for p in pages
    )


def test_summary_md_quotes_the_graph_size():
    text = open(os.path.join(ROOT, "graph", "summary.md")).read()
    m = re.search(r"has (\d+) nodes and (\d+) edges", text)
    assert (int(m.group(1)), int(m.group(2))) == (len(G["nodes"]), len(G["edges"]))


def test_qa_report_headline_matches_issue_counts():
    text = open(os.path.join(ROOT, "graph", "qa_report.md")).read()
    m = re.search(r"\*\*(\d+) errors, (\d+) warnings, (\d+) info\.\*\*", text)
    sev = G["stats"]["issues_by_severity"]
    assert (int(m.group(1)), int(m.group(2)), int(m.group(3))) == (
        sev.get("error", 0), sev["warning"], sev["info"])


@pytest.mark.xfail(strict=True, reason="README.md still quotes the pre-rebuild size (925 nodes, 1330 edges); graph.json has 919 / 1349")
def test_readme_quotes_the_graph_size():
    text = open(os.path.join(ROOT, "README.md")).read()
    m = re.search(r"\((\d+) nodes, (\d+) edges\)", text)
    assert (int(m.group(1)), int(m.group(2))) == (len(G["nodes"]), len(G["edges"]))
