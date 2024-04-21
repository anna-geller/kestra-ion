# kestra-ion

Read and write Amazon Ion files

# Usage example

```python
from kestra_ion import read_ion
import pandas as pd

file_path = "tests/data/employees.ion"
data = read_ion(file_path)

df = pd.DataFrame(data)
print(df.dtypes)
print(df.info())
```