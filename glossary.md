# Glossary

Running vocabulary from daily practice, in term/definition pairs. Kept as a
markdown table so it's easy to copy into a spreadsheet and export as CSV for
import into RemNote (Term column → front of card, Definition column → back).

| Term | Definition |
|---|---|
| Equivalence partitioning (EP) | Grouping inputs into "partitions" the system under test should treat the same way, then testing one representative value from each group instead of every possible input. Partitions can be valid (should succeed) or invalid (should be rejected). |
| Boundary value analysis (BVA) | A refinement of EP: bugs disproportionately hide at the edges between partitions (off-by-one errors, `<` vs `<=`, empty-input handling), so you deliberately test the value at a boundary, one just below it, and one just above it, rather than any representative value from the partition. |
