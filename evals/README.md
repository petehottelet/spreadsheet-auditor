# Agent task evaluations

`review-starter.json` contains three self-contained task prompts, setup steps
and expected behaviors. Its synthetic workbook/config fixtures are committed
under `files/`. `evals.json` contains three additional tasks whose input
acquisition is documented in `files/README.md`.

For each case, create an unrelated temporary working directory, copy the
listed inputs there, perform the stated setup, and give the prompt to an
agent with the installed skill. Record the exact model/version and runtime,
tool calls, final answer, report artifacts, expectation results and source
workbook hashes before and after the run. For the inherited-budget case,
also verify that the pre-existing report files retain their original bytes.

The JSON files specify expected behavior; they are not model run results.
The Python regression suite verifies detector and CLI behavior separately.
