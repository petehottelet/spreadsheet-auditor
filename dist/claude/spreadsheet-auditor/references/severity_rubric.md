# Severity Rubric

Severity is separate from detection mode and confidence.

## Critical

Use when numbers are wrong or very likely wrong, especially when a finding affects visible outputs, headline metrics, financing balances, totals, or material decision values.

Examples:

- Live `#REF!`, `#DIV/0!`, `#VALUE!`, or similar error in a visible output.
- Total excludes adjacent data that appears to belong in the total.
- Stated total differs from its components beyond tolerance.
- Cross-foot or balance identity fails.

## High

Use when the workbook is likely wrong, fragile, or could materially change outputs.

Examples:

- Formula drift in a projection row.
- Hardcoded plug inside a formula block.
- Broken reference to a missing sheet or external workbook.
- Aggregate includes a subtotal or hidden row.

## Medium

Use when the pattern is risky, ambiguous, or a maintainability issue.

Examples:

- `IFERROR` masking.
- Volatile functions.
- Numbers stored as text in a region that may be summed.
- Hidden structure that does not clearly feed an output.

## Low

Use for style, convention, or documentation issues.

## Escalation

Escalate by one tier, or prioritize within the tier, when:

- The cell feeds a configured headline output.
- The estimated delta exceeds materiality.
- The finding has many downstream dependents.
- The finding affects a visible summary sheet.

Downgrade or mark as `Review` when evidence suggests the pattern may be intentional.
