import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_tools_md_matches_manifest():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    text = (ROOT / "TOOLS.md").read_text()
    headings = set(re.findall(r"^## ([a-z_]+)$", text, re.MULTILINE))
    expected = {tool["name"] for tool in manifest["tools"]}
    assert headings == expected


def test_no_legacy_personal_repo_references():
    forbidden = re.compile(
        "|".join(["n1" + "fan", r"github\.com/n1" + "fan", r"ghcr\.io/n1" + "fan"])
    )
    offenders = []
    for path in ROOT.rglob("*"):
        if (
            path.is_dir()
            or ".git" in path.parts
            or "__pycache__" in path.parts
            or ".pytest_cache" in path.parts
        ):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if forbidden.search(text):
            offenders.append(str(path.relative_to(ROOT)))
    assert offenders == []
