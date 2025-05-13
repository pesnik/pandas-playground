import marimo

__generated_with = "0.13.7"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""# Loading""")
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    df = pd.read_excel("data/customer-transaction-dataset/Online Retail.xlsx")
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `read_excel` Options""")
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""# Inspection""")
    return


@app.cell
def _(df):
    df.where(df['Quantity'] < 3).dropna()
    return


@app.cell
def _(df):
    less_revenue = df[ df['Quantity'] < 30 ]
    less_revenue
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""# Plotting""")
    return


@app.cell
def _(df):
    import matplotlib.pyplot as plt

    df['Quantity'].plot(kind='hist')
    plt.title('Quantity Over Index')
    plt.xlabel('Index')
    plt.ylabel('Quantity')
    plt.grid(True)
    plt.show()

    return (plt,)


@app.cell
def _(df, plt):
    import seaborn as sns

    sns.histplot(df['Quantity'], bins=20, kde=True)
    plt.title('Distribution of Quantity')
    plt.xlabel('Quantity')
    plt.ylabel('Frequency')
    plt.show()
    return


if __name__ == "__main__":
    app.run()
