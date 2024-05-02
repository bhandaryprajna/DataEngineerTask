import pandas as pd
import pytest
from DataEngineerHomework import check_duplicates  # Import the function from my module


@pytest.fixture
def sample_dataframe():
    # Create a sample DataFrame for testing
    df = pd.DataFrame(
        data=[
        ['A', 'a', 'x', 1, 1],
        ['A', 'b', 'x', 1, 2],
        ['A', 'c', 'x', 1, 3],
        ['B', 'a', 'x', 1, 4],
        ['B', 'b', 'x', 1, 5],
        ['B', 'c', 'x', 1, 6],
        ['A', 'a', 'y', 1, 7],
        ],
    columns=['col_1', 'col_2', 'col_3', 'col_4', 'col_5']
    )
    return df

def test_check_duplicates_as_per_givendataset(sample_dataframe):
    columns = ['col_1']
    result = check_duplicates(sample_dataframe, columns)
    assert result['count'] == 5
    assert len(result['samples']) == 2

    columns = ['col_1' , 'col_2']
    result = check_duplicates(sample_dataframe, columns)
    assert result['count'] == 1
    assert len(result['samples']) == 1   

    columns = ['col_1' , 'col_2' , 'col_3']
    result = check_duplicates(sample_dataframe, columns)
    assert result['count'] == 0
    assert len(result['samples']) == 0      

def test_check_duplicates_valid_input(sample_dataframe):
    # Test case for valid input
    columns = ['col_1']
    result = check_duplicates(sample_dataframe, columns)
    assert result['count'] == 5
    assert len(result['samples']) == 2


def test_check_duplicates_invalid_dataframe():
    # Test case for invalid input: non-DataFrame
    with pytest.raises(ValueError,match="Input 'df' must be a pandas DataFrame"):
        check_duplicates(None, ['col_1'])


def test_check_duplicates_invalid_columns(sample_dataframe):
    # Test case for invalid input: columns not in DataFrame
    with pytest.raises(ValueError, match="Column 'col_6' not found in DataFrame"):
        check_duplicates(sample_dataframe, ['col_6'])


def test_check_duplicates_no_duplicates(sample_dataframe):
    # Test case for DataFrame with no duplicates
    columns = ['col_5']
    result = check_duplicates(sample_dataframe, columns)
    assert result['count'] == 0
    assert len(result['samples']) == 0

def test_check_duplicates_column_list(sample_dataframe):
    # Test case for exception handling: check if error message is logged
    with pytest.raises(ValueError, match="Input 'columns' must be a list"):
        check_duplicates(sample_dataframe, 1)
    

