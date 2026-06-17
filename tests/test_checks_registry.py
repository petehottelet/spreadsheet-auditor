"""Plugin/check registry discovery and contract tests."""

from __future__ import annotations

from spreadsheet_auditor.checks import Check, CheckContext, checks, register


def test_registry_discovers_builtin_checks():
    names = {cls.__name__ for cls in checks()}
    expected = {
        "LiveErrorCheck",
        "ReferenceIntegrityCheck",
        "FormulaDriftCheck",
        "HardcodeBreakCheck",
        "CircularReferenceCheck",
        "RangeIssueCheck",
        "RangeLengthMismatchCheck",
        "LiteralConstantCheck",
        "FragileFunctionCheck",
        "TotalMismatchCheck",
        "CrossFootCheck",
        "DataHygieneCheck",
    }
    missing = expected - names
    assert not missing, f"Built-in checks not registered: {missing}"


def test_all_builtins_declare_rule_ids():
    for cls in checks():
        assert isinstance(cls.rule_ids, tuple)
        assert len(cls.rule_ids) >= 1, f"{cls.__name__} declares no rule_ids"


def test_custom_check_can_register_and_run():
    from spreadsheet_auditor.finding import Finding

    @register
    class CustomCheck(Check):
        name = "_test_custom"
        description = "test"
        rule_ids = ("CUSTOM_TEST",)

        def run(self, ctx: CheckContext):
            return [
                Finding(
                    rule_id="CUSTOM_TEST",
                    severity="Low",
                    error_confidence="Review",
                    detection_mode="HEUR",
                    location="Sheet1!A1",
                    title="custom",
                    evidence=["e"],
                    suggested_fix="n/a",
                )
            ]

    # Custom check should now be in the registry
    assert any(c.__name__ == "CustomCheck" for c in checks())
    instance = CustomCheck()
    findings = instance.run(
        CheckContext(
            workbook_path=None,
            formula_wb=None,
            value_wb=None,
            allowed_sheet_names=set(),
            formulas=[],
            config={},
            inventory={},
        )
    )
    assert findings and findings[0].rule_id == "CUSTOM_TEST"


def test_registry_modes_are_DET_or_HEUR():
    for cls in checks():
        assert cls.mode in ("DET", "HEUR")
