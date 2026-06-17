# Excel Feature Coverage

| Feature | Coverage | Notes |
|---|---:|---|
| `.xlsx` formulas and values | Full static | Primary target. |
| `.xlsm` formulas and values | Full static | Macros are inventoried and never executed. |
| `.csv` | Data hygiene subset | Formula graph checks do not apply. |
| A1 references | Full static | Includes quoted sheet names for common cases. |
| Named ranges | Partial | Inventory and simple resolution only. |
| Structured references | Partial | Unsupported formulas are reported as coverage limitations. |
| Dynamic arrays | Coverage flag | Do not claim full support. |
| Data tables | Coverage flag | Not evaluated. |
| External workbook links | Inventory | Do not follow by default. |
| Power Query / Data Model | Inventory only | Not evaluated. |
| VBA/macros/UDFs | Inventory only | Never execute. |
| Recalculation | Optional | LibreOffice-backed when available; static-only otherwise. |
