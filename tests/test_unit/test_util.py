"""Unit tests for functions in src/util.py."""

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal, assert_series_equal

from bibat.util import (
    make_columns_lower_case,
    one_encode,
)


@pytest.mark.parametrize(
    ("s_in", "expected"),
    [
        (
            pd.Series(["8", 1, "????"], index=["a", "b", "c"]),
            pd.Series([1, 2, 3], index=["a", "b", "c"]),
        ),
        (
            pd.Series([1, "????", "????"], index=["a", "b", "c"]),
            pd.Series([1, 2, 2], index=["a", "b", "c"]),
        ),
    ],
)
def test_one_encode(s_in: pd.Series, expected: pd.Series) -> None:
    """Check that the function one_encode works as expected."""
    assert_series_equal(one_encode(s_in), expected)


@pytest.mark.parametrize(
    ("df_in", "expected"),
    [
        (
            pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]}),
            pd.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]}),
        ),
        (
            pd.DataFrame(
                [[1, 1]],
                columns=pd.MultiIndex.from_product([["A"], ["B", "C"]]),
            ),
            pd.DataFrame(
                [[1, 1]],
                columns=pd.MultiIndex.from_product([["a"], ["b", "c"]]),
            ),
        ),
    ],
)
def test_make_columns_lower_case(
    df_in: pd.DataFrame,
    expected: pd.DataFrame,
) -> None:
    """Check that the function make_columns_lower_case works as expected."""
    assert_frame_equal(make_columns_lower_case(df_in), expected)
