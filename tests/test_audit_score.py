"""audit/score.py is a top-level script (reads key/ and result_NN.json from the cwd).
It is run here on synthetic inputs, and once on the committed audit data."""
import json
import os
import runpy
import shutil

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "audit", "score.py")


FILLER = (
    {"F": {"true": True, "type": "filler", "text": "filler"}},
    {"F": {"v": "correct", "evidence": "ok"}},
)


def make_audit(dirpath, per_page, filler=True):
    # the script scores pages 9..25 and divides by each page's true-claim count,
    # so pages the test does not care about carry one agreeing filler claim.
    os.makedirs(dirpath / "key")
    for pg in range(9, 26):
        key, res = per_page.get(pg, FILLER if filler else ({}, {}))
        (dirpath / "key" / f"audit_key_{pg:02d}.json").write_text(json.dumps(key))
        (dirpath / f"result_{pg:02d}.json").write_text(json.dumps({"verdicts": res}))


def run(dirpath, monkeypatch, capsys):
    monkeypatch.chdir(dirpath)
    runpy.run_path(SCRIPT, run_name="__main__")
    return capsys.readouterr().out, json.load(open(dirpath / "disagreements.json"))


def test_audit_counts_agreement_decoys_and_disagreements(tmp_path, monkeypatch, capsys):
    key = {
        "C1": {"true": True, "type": "tag", "text": "tag t1"},
        "C2": {"true": True, "type": "tag", "text": "tag t2"},
        "C3": {"true": False, "type": "flow", "text": "decoy d1"},
        "C4": {"true": False, "type": "flow", "text": "decoy d2"},
        "C5": {"true": True, "type": "signal", "text": "no verdict"},
    }
    res = {
        "C1": {"v": "correct", "evidence": "e1"},
        "C2": {"v": "wrong", "evidence": "e2"},
        "C3": {"v": "wrong", "evidence": "e3"},
        "C4": {"v": "correct", "evidence": "e4"},
    }
    make_audit(tmp_path, {9: (key, res)})
    out, fails = run(tmp_path, monkeypatch, capsys)
    assert "TOTAL" in out
    assert "true 19 {'correct': 89.5, 'wrong': 5.3, 'missing': 5.3}" in out
    assert "filler 16 {'correct': 16} agree 100%" in out
    assert "decoy 2 {'wrong': 50.0, 'correct': 50.0}" in out
    assert "tag 2 {'correct': 1, 'wrong': 1} agree 50%" in out
    assert "signal 1 {'missing': 1} agree 0%" in out
    assert "9 3 33% decoy rejected 1 / 2" in out
    assert "2 disagreements" in out
    # a true claim judged wrong, and a decoy that was accepted
    assert fails == [[9, "C2", "tag", "tag t2", "e2"], [9, "C4", "DECOY-ACCEPTED", "decoy d2", "e4"]]


@pytest.mark.xfail(strict=True, raises=ZeroDivisionError,
                   reason="a page whose key has no true claims divides by zero in the per-page summary")
def test_audit_page_without_true_claims_does_not_crash(tmp_path, monkeypatch, capsys):
    make_audit(tmp_path, {}, filler=False)
    run(tmp_path, monkeypatch, capsys)


def test_audit_script_on_committed_data_reproduces_committed_disagreements(tmp_path, monkeypatch, capsys):
    src = os.path.join(ROOT, "audit")
    shutil.copytree(os.path.join(src, "key"), tmp_path / "key")
    for pg in range(9, 26):
        shutil.copy(os.path.join(src, f"result_{pg:02d}.json"), tmp_path)
    out, fails = run(tmp_path, monkeypatch, capsys)
    assert fails == json.load(open(os.path.join(src, "disagreements.json")))
    assert f"{len(fails)} disagreements" in out
