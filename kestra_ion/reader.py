import amazon.ion.simpleion as ion
from amazon.ion.simple_types import (
    IonPyDecimal,
    IonPyNull,
    IonPyBool,
    IonPyBytes,
    IonPyDict,
)
import dateutil.parser


def convert_ion_types(value):
    if isinstance(value, IonPyNull):
        return None
    elif isinstance(value, IonPyDecimal):
        return float(value)
    elif isinstance(value, IonPyBool):
        return bool(value)
    elif isinstance(value, IonPyBytes):
        return value.decode("utf-8")
    elif isinstance(value, IonPyDict) or isinstance(value, dict):
        return {k: convert_ion_types(v) for k, v in value.items()}
    elif isinstance(value, str):
        try:
            # Check if the value follows the expected format e.g. "LocalDateTime::'2024-04-21T13:43:24.34'"
            if value.startswith("LocalDateTime::"):
                date_str = value.split("::")[1].strip('"')
                return dateutil.parser.isoparse(date_str)
            return dateutil.parser.isoparse(value)
        except ValueError:
            return value
    elif isinstance(value, list):
        return [convert_ion_types(item) for item in value]
    else:
        return value


def read_ion(path_):
    with open(path_, "rb") as file:
        ion_content = file.read()
    ion_data = ion.loads(ion_content, single_value=False)
    list_of_dicts = [dict(record) for record in ion_data]
    list_of_dicts = [
        {k: convert_ion_types(v) for k, v in record.items()} for record in list_of_dicts
    ]
    return list_of_dicts
