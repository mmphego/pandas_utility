# -*- coding: utf-8 -*-

"""Main module."""

import numpy as np
import pandas as pd


class PandasUtilities:

    """Some useful functions for dealing with Pandas DataFrames
    """

    __version__ = pd.__version__

    @staticmethod
    def show_version():
        return pd.show_versions()

    @staticmethod
    def create_random_df(rows, cols, cols_name=None):
        """Create a random dataframe with n-rows and n-columns

        Parameters
        ----------
        rows : int
            number of rows
        cols : int
            number of columns
        cols_name : None, optional
            Columns names

        Returns
        -------
        `pandas.core.frame.DataFrame`
            Data frame containing random values
        """
        if cols_name:
            cols_name = list(cols_name)
            assert len(cols_name) == cols
        return pd.DataFrame(np.random.rand(rows, cols), columns=cols_name)

    @staticmethod
    def rename_cols(df, new_names=[], prefix=None, suffix=None):
        """Rename column names as well as add prefix and suffix

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        new_names : list, optional
            list of new names matching the current length of cols
        prefix : None, optional
            Add prefix on column name
        suffix : None, optional
            Add suffix on column name

        Returns
        -------
        `pandas.core.frame.DataFrame`
            DataFrame with new column names.
        """

        if new_names and (len(df.columns) == len(new_names)):
            df.columns = new_names
            df.columns = df.columns.str.replace(" ", "_")
        if prefix:
            df = df.add_prefix(prefix)
        if suffix:
            df = df.add_suffix(suffix)
        return df

    @staticmethod
    def reverse_row_order(df, reset_index=False):
        """Reverse the order of the dataframe, and reset the indices (optional)

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        reset_index : bool, optional
            Reset the index of the DataFrame to start at '0'

        Returns
        -------
        `pandas.core.frame.DataFrame`
            Reversed order of rows in DataFrame
        """
        return df.loc[::-1].reset_index(drop=True) if reset_index else df.loc[::-1]

    @staticmethod
    def reverse_col_order(df):
        """Summary

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data

        Returns
        -------
        `pandas.core.frame.DataFrame`
            Reversed order of cols in DataFrame
        """
        return df.loc[:, ::-1]

    @staticmethod
    def select_by_datatype(df, include_datatype=[], exclude_datatype=[]):
        """

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        include_datatype : list, optional
            A list containing data-type to include.
        exclude_datatype : list, optional
            A list containing data-type to exclude.

        Returns
        -------
        `pandas.core.frame.DataFrame`
            DataFrame containing included/excluded data-types
        """
        return (
            df.select_dtypes(include=include_datatype, exclude=exclude_datatype)
            if include_datatype or exclude_datatype
            else df
        )

    @staticmethod
    def build_df_from_csvs(csv_files, axis, ignore_index=True):
        """Build a DataFrame from multiple files (row-wise)

        Parameters
        ----------
        csv_files : list
            List of csv files
        axis : int
            Concatenate csv files according to columns or rows.
        ignore_index : bool, optional
            Resets indices

        Returns
        -------
        `pandas.core.frame.DataFrame`
            DataFrame containing data from CSV files(s)
        """
        return pd.concat(
            (pd.read_csv(file) for file in csv_files),
            axis=axis,
            ignore_index=ignore_index,
        )

    @staticmethod
    def split_df_into_subsets(df, fraction=0.5, random_state=1234):
        """Return a random sample of items from an axis of object.

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        fraction : float, optional
            Fraction of axis items to return.
            Cannot be used with `n`.
        random_state : int or numpy.random.RandomState, optional
            Seed for the random number generator (if int),
            or numpy RandomState object.

        Returns
        -------
        List
            List of data frame
        """
        df_1 = df.sample(frac=fraction, random_state=random_state)
        df_2 = df.drop(df_1.index)
        return df_1, df_2

    @staticmethod
    def filter_by_multiple_categories(df, column_name, filter_by=[], exclude=False):
        """Filter a DataFrame by multiple categories

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        column_name : str
            Column name to filter
        filter_by : list, optional
            List of categories to filter
        exclude : bool, optional
            Exclude the filter

        Returns
        -------
        TYPE
            Description

        Deleted Parameters
        ------------------
        head : bool, optional
            Only show head of the data frame
        """
        _filtered = df[column_name].isin(filter_by)
        return df[_filtered] if not exclude else df[~_filtered]

    @staticmethod
    def filter_by_large_categories(df, column_name, count=3):
        """Filter a DataFrame by largest categories

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        column_name : str
            Column name to filter
        count : int, optional
            Number of largest values in the Series

        Returns
        -------
        `pandas.core.frame.DataFrame`
            DataFrame containing included/excluded
            data-types

        Deleted Parameters
        ------------------
        head : bool, optional
            Only show head of the data frame
        """
        counts = df[column_name].value_counts()
        _filtered = df[column_name].isin(counts.nlargest(count).index)
        return df[_filtered]

    @staticmethod
    def drop_cols_with_NaNs(df, threshold=0.1):
        """Remove columns with missing values

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        threshold : float, optional
            Only drop columns in which more than x% of the
            values are missing.

        Returns
        -------
        `pandas.core.frame.DataFrame`
            DataFrame without NaN's
        """
        return df.dropna(thresh=len(df) * threshold, axis="columns")

    @staticmethod
    def aggregate_by_functions(df, column_name, group_by, functions=["sum", "count"]):
        """Aggregate by multiple functions

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        column_name : TYPE
        group_by : TYPE
            Description
        functions : list, optional
            Description

        Returns
        -------
        `pandas.core.frame.DataFrame`
            DataFrame

        Example
        -------
        # Lets say, you want the total price of each order as well as the
        # number of items in each order.
        >> Orders.head(5)
            order_id | quantity | item_name | choice_description | item_price
            1 | 1 | Chips and Fresh Tomato Salsa          | NaN          | 2.39
            1 | 1 | Izze                                  | [Clementine] | 3.39
            1 | 1 | Nantucket Nectar                      | [Apple]      | 3.39
            1 | 1 | Chips and Tomatillo-Green Chili Salsa | NaN          | 2.39
            2 | 2 | Chicken Bowl                          | NaN          | 16.98
        >> aggregate_by_functions(orders, 'item_price', 'order_id').head()
            order_id  | sum   | count
                    1 | 11.56 | 4
                    2 | 16.98 | 1
                    3 | 12.67 | 2
                    4 | 21.00 | 2
                    5 | 13.70 | 2
        """
        return df.groupby(group_by)[column_name].agg(functions)

    @staticmethod
    def continous_to_categorical_data(df, column_name, bins=[], labels=[]):
        """Summary

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        column_name : str
            Description
        bins : list
            Description
        labels : list
            Description

        Returns
        -------
        TYPE
            Description

        Example
        -------
        >> data['age']
            0 | 22.0
            1 | 38.0
            2 | 26.0
            3 | 35.0
            4 | 35.0
            5 |  NaN
            6 | 54.0
            7 |  2.0
            8 | 27.0
            9 | 14.0
            Name: Age, dtype: float64
        >> continuous_to_categorical_data(
        data, 'age', bins=[0, 18, 25, 99], labels==['child', 'young adult', 'adult'])

            0 | young adult
            1 | adult
            2 | adult
            3 | adult
            4 | adult
            5 | NaN
            6 | adult
            7 | child
            8 | adult
            9 | child
            Name: Age, dtype: category
            Categories (3, object): [child < young adult < adult]

        # This assigned each value to a bin with a label.
        # Ages 0 to 18 were assigned the label "child", ages 18 to 25 were assigned the
        # label "young adult", and ages 25 to 99 were assigned the label "adult".
        """
        return pd.cut(df[column_name], bins=bins, labels=labels)

    @staticmethod
    def change_display_opt(
        option="display.float_format", _format="{:.2f}".format, reset=False
    ):
        """Standardize the display of the DataFrame

        Parameters
        ----------
        option : str, optional
            Regexp which should match a single option.
        _format : str, optional
            new formatting option
        reset : bool, optional
            Description

        Returns
        -------


        """
        return pd.set_option(option, _format) if not reset else pd.reset_option(option)

    @staticmethod
    def remove_rows_with_nan(df, column_name):
        """Remove all rows containing NaN values

        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        column_name : str
            Remove all the rows where column_name has NaN values.

        Returns
        -------
        `pandas.core.frame.DataFrame`
            DataFrame
        """

        return df[pd.notna(df[column_name])]

    @staticmethod
    def col_to_datetime(df, column_name, date_format="%Y-%m-%d"):
        """
        Parameters
        ----------
        df : pandas.core.frame.DataFrame
            Two-dimensional size-mutable,
            potentially heterogeneous tabular data
        column_name : TYPE
            Column to change datetime
        date_format : str, optional
            Description

        Returns
        -------
        `pandas.core.frame.DataFrame`
            DataFrame
        """
        return pd.to_datetime(df[column_name], format=date_format)

    @staticmethod
    def binning_column_by_group_names(
        df,
        column_name,
        num_samples,
        group_names=["Low", "Medium", "High"],
        include_lowest=True,
    ):
        """

        Parameters
        ----------
        df : TYPE
            Description
        column_name : TYPE
            Description
        num_samples : TYPE
            Description
        group_names : list, optional
            Description
        include_lowest : bool, optional
            Description

        Returns:
        --------
        """
        bins = np.linspace(min(df[column_name]), max(df[column_name]), num_samples)
        return pd.cut(
            df[column_name], bins, labels=group_names, include_lowest=include_lowest
        )

    @staticmethod
    def open_google_sheet(token):
        """Google Spreadsheet CSV into A Pandas Dataframe

        Parameters
        ----------
        token : str
            Google Spreadsheet token ID

        Returns
        -------
        `pandas.core.frame.DataFrame`
            DataFrame
        """
        url = 'https://docs.google.com/spreadsheets/d/{}/export?format=csv'.format(token)
        return pd.read_csv(url)
