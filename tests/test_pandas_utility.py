#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pandas_utility` package."""

import unittest

import numpy as np
import pandas as pd

from pandas_utility import PandasUtilities


class TestPandasUtilities(unittest.TestCase, PandasUtilities):
    """Tests for `pandas_utility` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.rows, self.cols = 2, 2
        self.column_names = ["col A", "col B"]
        self.df = self.create_random_df(self.rows, self.cols, self.column_names)

    def test_create_random_df(self):
        self.assertEqual(self.df.shape, (self.rows, self.cols))
        self.assertIn(self.column_names[0], self.df.columns)
        self.assertIsInstance(self.df.columns.values, np.ndarray)

    def test_rename_cols(self):
        new_column_names = ["column 1", "column 2"]
        new_df = self.rename_cols(self.df, new_names=new_column_names)
        self.assertNotIn(new_column_names[0], self.df.columns)
        self.assertIn(new_column_names[0].replace(" ", "_"), self.df.columns)
        self.assertNotIn(" ", new_df.columns)
        self.assertNotIn("-", new_df.columns)

    def test_reverse_row_order(self):
        new_df = self.reverse_row_order(self.df)
        self.assertTrue(all(self.df.loc[0] == new_df.loc[0]))
        new_df = self.reverse_row_order(self.df)
        self.assertEqual(new_df.loc[1][1], self.df.loc[1][1])
        new_df_rst_index = self.reverse_row_order(self.df, reset_index=True)
        self.assertEqual(new_df_rst_index.loc[1][1], new_df.loc[0][1])

    def test_reverse_col_order(self):
        new_df = self.reverse_col_order(self.df)
        with self.assertRaises(Exception):
            self.assertEqual(self.df.columns.values, new_df.columns.values)

    def test_select_by_datatype(self):
        sample_df_csv = pd.read_csv("http://bit.ly/drinksbycountry")
        data = self.select_by_datatype(sample_df_csv, include_datatype="object")
        self.assertIsInstance(data.dtypes, object)
        with self.assertRaises(Exception):
            self.assertIsInstance(data.dtypes, float)
        new_data = self.select_by_datatype(
            sample_df_csv, include_datatype=["object", "float"]
        )
        self.assertIsInstance(new_data.dtypes[0], object)
        self.assertIsInstance(new_data.dtypes[1], np.dtype)
        new_data = self.select_by_datatype(
            sample_df_csv, exclude_datatype=["object", "float"]
        )
        self.assertTrue(new_data.dtypes[0] == np.int64)
        with self.assertRaises(AssertionError):
            self.assertIsInstance(new_data.dtypes, float)

    def test_build_df_from_csvs(self):
        csv_files = [
            "http://bit.ly/drinksbycountry",
            "http://bit.ly/imdbratings",
            "http://bit.ly/smallstocks",
        ]
        data = self.build_df_from_csvs(csv_files=csv_files, axis=0)
        self.assertTrue(
            all(
                [
                    "Close" in data.columns,
                    "country" in data.columns,
                    "wine_servings" in data.columns,
                ]
            )
        )

    def test_split_df_into_subsets(self):
        pass

    def test_filter_by_multiple_categories(self):
        pass

    def test_filter_by_large_categories(self):
        pass

    def test_drop_cols_with_NaNs(self):
        pass

    def test_aggregate_by_functions(self):
        pass

    def test_continous_to_categorical_data(self):
        pass

    def test_change_display_opt(self):
        pass

    def test_remove_rows_with_nan(self):
        pass

    def test_col_to_datetime(self):
        pass

    def test_binning_column_by_group_names(self):
        pass
