# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at [here](https://github.com/mmphego/pandas_utility/issues).

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Pandas Utility could always use more documentation,
whether as an official Pandas Utility docs,
in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue [here](https://github.com/mmphego/pandas_utility/issues).

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

## Get Started!

Ready to contribute? Here's how to set up pandas_utility for local development.

1.  Fork the pandas_utility repo on GitHub.
2.  Clone your fork locally:
```bash
    git clone git@github.com:your_name_here/pandas_utility.git
```

3.  Install your local copy into a virtualenv. Assuming you have
    `virtualenvwrapper` installed, this is how you set up your fork for
    local development:
    ```bash
        mkvirtualenv pandas_utility
        cd pandas_utility/
        python setup.py develop
    ```

4.  Create a branch for local development:
    ```bash
        git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

5.  When you're done making changes, check that your changes pass `flake8`
    and the tests, and then use `black` to format:
    ```bash
        flake8 pandas_utility
        python setup.py test or py.test
        black -l 90 pandas_utility
    ```
    To get `flake8` and `black`, just pip install them into your `virtualenv`.

6.  Commit your changes and push your branch to GitHub:
    ```bash
        git add .
        git commit --sign-off -m "Your detailed description of your changes."
        git push origin name-of-your-bugfix-or-feature
    ```

7.  Submit a pull request through the GitHub website.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.rst.
3.  The pull request should work for Python 3.6+, and
    for PyPi. Check [travis-ci](https://travis-ci.org/mmphego/pandas_utility/pull_requests) and make sure that the tests pass for supported Python version(s).

### Tips

To run a subset of tests:
```bash
python3 -m unittest tests.test_pandas_utility
```

## Deploying

A reminder for the maintainers on how to publish. Make sure all your
changes are committed (including an entry in CHANGELOG.md).
Then run: `python setup.py publish`
