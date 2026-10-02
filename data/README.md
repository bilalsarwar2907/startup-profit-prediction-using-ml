# Dataset: 50 Startups

**Source:** Public "50 Startups" dataset (Kaggle), used for learning purposes.
**Size:** 50 rows, 5 columns. No missing values.

## Columns
| Column | Type | Role | Meaning |
|---|---|---|---|
| R&D Spend | float | Feature | Money spent on research & development |
| Administration | float | Feature | Money spent on administration (office, salaries) |
| Marketing Spend | float | Feature | Money spent on marketing |
| State | text (categorical) | Feature | The US state where the startup is based |
| Profit | float | Target | The profit the startup earned |

## Key findings
- R&D has the strongest correlation with Profit (0.97, close to 1): more R&D spending usually means more profit.
- Marketing has a strong correlation (0.75); Administration is weak (0.20).
- State is balanced: New York 17, California 17, Florida 16.

## Limitations
- Only 50 rows, so results can change a lot depending on which rows end up in the test set.
- Some 0 values (rows 19, 47, 48, 49) might be missing data saved as 0. All rows are kept, and these are checked again in error analysis.
- The CSV is sorted by Profit (highest first), so the data must be shuffled before splitting into train and test.