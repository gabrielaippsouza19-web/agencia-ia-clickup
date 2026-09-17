#!/usr/bin/env python3
"""Validate the internal Agencia IA + ClickUp package before a backup tag."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    ROOT / ".codex-plugin" / "plugin.json",
    ROOT / ".agents" / "plugins" / "marketplace.json",
    ROOT / "README.md",
    ROOT / "SETUP.md",
]
REQUIRED_SKILLS = [
    ROOT / "skills" / "clickup-midias-orquestrador" / "SKILL.md",
    ROOT / "skills" / "formatar-task-editor-video" / "SKILL.md",
    ROOT / "skills" / "arte" / "SKILL.md",
]


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION_FAILED: {message}")


for path in REQUIRED_FILES + REQUIRED_SKILLS:
    if not path.is_file():
        fail(f"arquivo ausente: {path.relative_to(ROOT)}")

try:
    manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
except json.JSONDecodeError as exc:
    fail(f"plugin.json inválido: {exc}")

if manifest.get("name") != "agencia-ia-clickup":
    fail("nome do plugin diferente de agencia-ia-clickup")
if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
    fail("versão do plugin não está em semver")
if manifest.get("skills") != "./skills/":
    fail("manifesto não aponta para ./skills/")

try:
    marketplace = json.loads(
        (ROOT / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8")
    )
except json.JSONDecodeError as exc:
    fail(f"marketplace.json inválido: {exc}")

entries = marketplace.get("plugins", [])
entry = next((item for item in entries if item.get("name") == "agencia-ia-clickup"), None)
if entry is None:
    fail("plugin não encontrado no marketplace")
if entry.get("source", {}).get("path") != "./":
    fail("marketplace precisa apontar para a raiz do plugin")

for skill in REQUIRED_SKILLS:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---") or "name:" not in text or "description:" not in text:
        fail(f"frontmatter ausente ou incompleto: {skill.relative_to(ROOT)}")
    if "[TODO:" in text:
        fail(f"placeholder TODO encontrado: {skill.relative_to(ROOT)}")

print("VALIDATION_OK: pacote, marketplace e skills estão íntegros")

