# Phi
# Language: Python
# Input: CSV (file of abundances)
# Output: CSV (proportionalities)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin that runs the proportionality algorithm of Lovell et al, 2015,
which was proposed as an alternative to correlations for relative data.

The plugin accepts as input a CSV file of abundances, where rows
correspond to samples, columns to entities and entry (i, j) the abundance
of entitity j in sample i.

It then produces a CSV file of proportionalities, where both rows
and columns correspond to entities and entry (i, j) becomes the proportionality
of entity i with respect to entitity j.
