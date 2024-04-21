# kestra-ion

The `kestra-ion` package provides an easy-to-use interface for reading and writing Amazon Ion data files to integrate this data format into Python applications, particularly for analysis with libraries like pandas or polars.

## Features

- **Read Amazon Ion files**: Convert Ion data into Python data structures.
- **Pandas Integration**: Easily convert Ion data into pandas DataFrames for further analysis.
- **Simple API**: A minimalistic and easy-to-understand API.

## Installation

To install `kestra-ion`, you can use pip:

```bash
pip install kestra-ion
```

Ensure that you have Python 3.6 or later installed. This package depends on `amazon.ion` library, which will be installed during the installation process.

## Usage Example

Here's a quick example to get you started with reading Amazon Ion data and converting it into a pandas DataFrame:

```python
from kestra_ion import read_ion
import pandas as pd
import requests

file_path = "employees.ion"
url = "https://huggingface.co/datasets/kestra/datasets/resolve/main/ion/employees.ion"
response = requests.get(url)
if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
else:
    print(f"Failed to download the file. Status code: {response.status_code}")


data = read_ion(file_path)
df = pd.DataFrame(data)
print(df.info())
```

This example reads data from an Ion file, converts it into a list of dictionaries, and then creates a pandas DataFrame from this list. The output includes details about the types of columns and general information about the DataFrame.

## Contributing

Contributions to `kestra-ion` are welcome! Here are a few ways you can help:

- Report bugs and issues.
- Suggest new features or enhancements.
- Improve documentation.
- Submit pull requests to address known issues.

## License

`kestra-ion` is distributed under Apache 2.0. See the LICENSE file in the GitHub repository for more details.

## Contact

If you have specific questions about the `kestra-ion` package, feel free to reach out via GitHub issues.
