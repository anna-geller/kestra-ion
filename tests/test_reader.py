import pytest
from kestra_ion import read_ion
import os


@pytest.fixture
def load_ion_data():
    def _load_ion_data(file_name):
        file_path = os.path.join(os.path.dirname(__file__), "data", file_name)
        return read_ion(file_path)

    return _load_ion_data


def test_basic_ion_file(load_ion_data):
    result = load_ion_data("basic.ion")
    expected = [{'key': 'value', 'list': [1, 2, 3]}]  # Adjusted expectation
    assert result == expected, f"The parsed data is not as expected: {result}"


def test_datetime_parsing(load_ion_data):
    result = load_ion_data("datetime.ion")
    print(result)  # Debugging output
    from datetime import datetime

    expected_date = datetime(2024, 4, 21, 13, 43, 24, 340000)
    assert (
        result[0]["start_date"] == expected_date
    ), "Datetime parsing failed: {result[0]}"


def test_empty_file(load_ion_data):
    # Test behavior with an empty Ion file
    result = load_ion_data("empty.ion")
    assert result == [], "Expected an empty list for empty Ion file."


def test_error_handling(load_ion_data):
    # Test handling of corrupted data files
    with pytest.raises(
        Exception
    ):  # Expect some kind of Exception, specify further as needed
        load_ion_data("corrupted.ion")
