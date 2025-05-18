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
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Series""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""> NaN (not a number) is the standard missing data marker used in pandas.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""> Like a NumPy array, a pandas Series has a single dtype.""")
    return


@app.cell
def _(pd):
    # While Series is ndarray-like, if you need an actual ndarray, then use Series.to_numpy().

    numbers = pd.Series(range(11))
    numbers.to_numpy()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Series is dict-like""")
    return


@app.cell
def _(pd):
    labelled_numbers = pd.Series(range(11), index=list("ABCDEFGHIJK"))

    labelled_numbers
    return (labelled_numbers,)


@app.cell
def _(labelled_numbers):
    labelled_numbers['A']
    return


@app.cell
def _(labelled_numbers):
    'A' in labelled_numbers
    return


@app.cell
def _(labelled_numbers):
    'Z' in labelled_numbers
    return


@app.cell
def _(labelled_numbers):
    labelled_numbers['Z']
    return


@app.cell
def _(labelled_numbers):
    labelled_numbers.get('Z', "Not Found")
    return


@app.cell
def _(mo):
    mo.md(r"""## Vectorized operations and label alignment with Series""")
    return


@app.cell
def _(labelled_numbers):
    labelled_numbers ** labelled_numbers # x^x
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Name attribute""")
    return


@app.cell
def _(pd):
    marvel_characters = pd.Series(["groot", "spiderman", "Moon knight"], name="marvel comics")

    marvel_characters_df = pd.DataFrame(marvel_characters)
    marvel_characters_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# DataFrame""")
    return


@app.cell
def _(pd):
    dick_t = {
        "one": pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        "two": pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    }

    dick_df = pd.DataFrame(dick_t)
    dick_df
    return


@app.cell
def _():
    # constructors

    # Dataframe()
    # pd.Dataframe.from_dict()
    # pd.Dataframe.from_record()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Assigning new columns in method chains""")
    return


@app.cell
def _(pd):
    ecom_df = pd.read_csv("data/customer-transaction-dataset/sample_dataset.csv")
    ecom_df['Birthdate'] = pd.to_datetime(ecom_df['Birthdate'])
    ecom_df['Date'] = pd.to_datetime(ecom_df['Date'])
    ecom_df
    return (ecom_df,)


@app.cell
def _(ecom_df):
    ecom_df.assign(FullName=ecom_df['Name'] + ' ' + ecom_df['Surname'])
    return


@app.cell
def _(ecom_df):
    (
        ecom_df
            .query("Gender == 'F' or Gender == 'M'")
            .assign(Gender=lambda df: df['Gender'].map({'F': 'Female', 'M': 'Male'}))
            .groupby(['Category', 'Gender'])
            .size()
            .unstack(fill_value=0)
            .plot(kind='bar', figsize=(10, 6), title="Gender Distribution by Category")
    )
    return


@app.cell
def _(ecom_df):
    ecom_df.info()
    return


if __name__ == "__main__":
    app.run()
