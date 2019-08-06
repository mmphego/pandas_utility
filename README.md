# Pandas Utility

[![GitHub](https://img.shields.io/github/license/mmphego/pandas_utility.svg)](LICENSE)
[![Build Status](https://travis-ci.com/mmphego/pandas_utility.svg?token=BFdkPYZWCqwEmQMyYDLi&branch=master)](https://travis-ci.com/mmphego/pandas_utility)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/43713e0b78f547e8912ff05c9350cffb)](https://app.codacy.com/app/mmphego/pandas_utility?utm_source=github.com&utm_medium=referral&utm_content=mmphego/pandas_utility&utm_campaign=Badge_Grade_Dashboard)
[![Python](https://img.shields.io/badge/Python-3.6%2B-red.svg)](https://www.python.org/downloads/)
![PyPI](https://img.shields.io/pypi/v/>pandas_utility.svg?color=green&label=pypi%20release)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pandas_utility.svg?label=PyPi%20Downloads)
[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/mmphego)

Some useful Pandas utility functions.

# Installation

To install Pandas Utility, run this command in your terminal:

```python
    pip install pandas_utility
```

This is the preferred method to install Pandas Utility,
as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed,
this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.

## From sources

The sources for Pandas Utility can be downloaded from the [Github repo](https://github.com/mmphego/pandas_utility).

You can either clone the public repository:

```bash
git clone git://github.com/mmphego/pandas_utility
```

Or download the [tarball](https://github.com/mmphego/pandas_utility/tarball/master):

```bash
curl  -OL https://github.com/mmphego/pandas_utility/tarball/master
```

Once you have a copy of the source, you can install it with:

```bash
pip install -U .
```

# Usage

```python
In [1]: from pandas_utility import PandasUtilities as utils
   ...:
   ...: df = utils.create_random_df(3, 5)

In [2]: df
Out[2]:
          0         1         2         3         4
0  0.056019  0.608052  0.434670  0.712330  0.602797
1  0.050986  0.458700  0.899288  0.783495  0.683170
2  0.232940  0.707126  0.639882  0.675283  0.793030

In [3]: df = utils.rename_cols(df, new_names=['col A', 'col B', 'col C', 'col D', 'col E'])

In [4]: df
Out[4]:
      col_A     col_B     col_C     col_D     col_E
0  0.056019  0.608052  0.434670  0.712330  0.602797
1  0.050986  0.458700  0.899288  0.783495  0.683170
2  0.232940  0.707126  0.639882  0.675283  0.793030

```

# Oh, Thanks!

By the way...
Click if you'd like to [saythanks](https://saythanks.io/to/>mmphego)... :) else *Star* it.

✨🍰✨

# Feedback

Feel free to fork it or send me PR to improve it.

# Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [mmphego/cookiecutter-python-package](https://github.com/mmphego/cookiecutter-python-package) project template.
