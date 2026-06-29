#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "templates/discovery-output.schema.json",
    "templates/diagnosis-form.md",
    "templates/zero-based-interview.md",
    "templates/validated-interview.md",
    "templates/mixed-interview.md",
    "references/client-types.md",
    "references/interview-paths.md",
    "references/question-design-rules.md",
    "references/material-checklist.md",
    "references/handoff-schema.md",
    "outputs/test-oushijie-discovery.json",
]

ALLOWED_CLIENT_TYPES = {"zero_based", "validated", "mixed"}
ALLOWED_NEXT_MODES = {"validated", "inference_based", "hold_for_more_material"}


def assert_true(condition, message):
    if not condition:
        raise AssertionError(message)


def check_required_files():
    for rel in REQUIRED_FILES:
        assert_true((ROOT / rel).exists(), f"Missing required file: {rel}")


def check_output_json():
    path = ROOT / "outputs/test-oushijie-discovery.json"
    data = json.loads(path.read_text())

    for key in ["meta", "input_snapshot", "diagnosis", "interview_brief", "material_checklist", "handoff"]:
        assert_true(key in data, f"Missing root key: {key}")

    diagnosis = data["diagnosis"]
    assert_true(diagnosis.get("client_type") in ALLOWED_CLIENT_TYPES, "Invalid diagnosis.client_type")
    assert_true(diagnosis.get("confidence") in {"high", "medium", "low"}, "Invalid diagnosis.confidence")
    assert_true(diagnosis.get("recommended_interview_path") in ALLOWED_CLIENT_TYPES, "Invalid recommended_interview_path")

    handoff = data["handoff"]
    assert_true(handoff.get("recommended_next_mode") in ALLOWED_NEXT_MODES, "Invalid handoff.recommended_next_mode")
    assert_true(handoff.get("manual_confirmation_required") is True, "manual_confirmation_required must be true")
    assert_true(len(handoff.get("manual_confirmation_points", [])) >= 1, "At least one manual confirmation point is required")

    for key in ["required", "recommended", "bonus"]:
        assert_true(isinstance(data["material_checklist"].get(key, []), list), f"material_checklist.{key} must be a list")


def main():
    check_required_files()
    check_output_json()
    print("RTA-DISCOVERY smoke test passed")


if __name__ == "__main__":
    main()
