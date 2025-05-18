import marimo

__generated_with = "0.13.7"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    import numpy as np
    return np, pd


@app.cell
def _(pd):
    df = pd.read_csv('data/customer-transaction-dataset/sample_dataset.csv')
    df
    return (df,)


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    df.columns = [name.lower() for name in df.columns]
    df.columns
    return


@app.cell
def _(np, pd):
    s = pd.Series(np.arange(10))
    div, rem = divmod(s, 3)
    print(rem)
    div
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Missing data / operations with fill values""")
    return


@app.cell
def _(pd):
    series_df = pd.DataFrame({
        'one': [1, 2, 9, 4],
        'two': [5, 6, 7, None]
    }, index=list('abcd'))

    series_df
    return (series_df,)


@app.cell
def _(series_df):
    series_df['one'].add(series_df['two'], fill_value=0)
    return


@app.cell
def _(series_df):
    series_df['one'].add(series_df['two'], fill_value=55)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Flexible comparisons
    ### ```eq, ne, lt, gt, le, and ge```
    """
    )
    return


@app.cell
def _(series_df):
    series_df['one'].gt(series_df['two'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Boolean reductions
    ### ```empty, any(), all(), and bool()```
    """
    )
    return


@app.cell
def _(np):
    np.nan == np.nan
    return


@app.cell
def _(series_df):
    (series_df + series_df).equals(series_df * 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Combining overlapping data sets
    ### ```combine_first()```
    """
    )
    return


if __name__ == "__main__":
    app.run()
