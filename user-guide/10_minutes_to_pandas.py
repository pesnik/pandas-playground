import marimo

__generated_with = "0.13.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Basic Data Structure in Pandas""")
    return


@app.cell
def _():
    import pandas as pd

    # Series
    print(pd.Series([1, None, 2, 'hello']))
    print(pd.Series([1, 2, 3], index=['a', 'b', 'c']))
    return (pd,)


@app.cell
def _(pd):
    # Dataframe
    messy_series = pd.Series([1, None, True, "message"])
    print(type(messy_series))

    print(messy_series)

    messy_df = messy_series.to_frame()
    print(messy_df)
    print(type(messy_df))
    return messy_df, messy_series


@app.cell
def _(messy_df, messy_series):
    # Accessing Values [df vs series]
    print("Series")
    print(messy_series[0])
    print(messy_series.iloc[2])
    print(messy_series.loc[2])

    print("\n")

    print("Dataframe")
    print(messy_df[0])
    print(messy_df.loc[2])
    print(messy_df.loc[2, 0])
    return


@app.cell
def _(pd):
    # iloc vs loc
    table = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

    print(table)
    print(table['A'])
    print(table['A'].values)

    # print(table[0]) # KeyError: 0
    print(table.loc[0:1])

    indexex_table = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }, index=['x', 'y', 'z'])
    print(indexex_table)

    print(indexex_table['A'])
    print(indexex_table.loc['y']['B'])
    print(indexex_table.loc['y', 'B'])
    print(indexex_table.iloc[1])


    # Use Case	
    # [iloc] Positional access, programmatic loops	Label-based access
    # [loc] named indices

    indexex_table
    return


@app.cell
def _(pd):
    # dataset builder
    dates = pd.date_range('20250510', periods=6)
    dates
    return (dates,)


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _(dates, np, pd):
    date_indexed_df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    date_indexed_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Viewing Dataframe""")
    return


@app.cell
def _(pd):
    fruits = ['Apple', 'Banana', 'Jackfruit', 'Lichi']
    price_list = {
        'Mirpur 1' : [150, 50, 230, 200],
        'Swopno': [152, 60, 250, 180]
    }

    fruit_table = pd.DataFrame(price_list, index=fruits)
    fruit_table
    return (fruit_table,)


@app.cell
def _(fruit_table):
    fruit_table.tail(1)
    return


@app.cell
def _(fruit_table):
    fruit_table.head(2)
    return


@app.cell
def _(fruit_table):
    print(fruit_table.index)

    print(fruit_table.columns)
    return


@app.cell
def _(fruit_table):
    fruit_table.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### Axis""")
    return


@app.cell
def _(fruit_table):
    fruit_table.mean(axis=0)
    return


@app.cell
def _(fruit_table):
    fruit_table.mean(axis=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Boolean Indexing""")
    return


@app.cell
def _(fruit_table):
    fruit_table[fruit_table['Mirpur 1'] < fruit_table['Swopno']]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Setting""")
    return


@app.cell
def _(pd):
    s1 = pd.Series([1, 2, 3, 3], index=pd.date_range('20250510', periods=4))
    s1
    return


@app.cell
def _(fruit_table):
    fruit_table.at['Apple', 'Mirpur 1'] = 156

    fruit_table.iloc[:4, 0:2]
    return


@app.cell
def _(fruit_table):
    fruit_table.iat[0, 1] = 160

    fruit_table
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### UDF""")
    return


@app.cell
def _(fruit_table):
    def udf(x):
        print(x)
        return x + x * .5

    fruit_table.agg(axis=0, func=udf)
    return


@app.cell
def _(fruit_table):
    def for_mirpur_only(x):
        print(x)
        x['Mirpur 1'] = int(x['Swopno'] * .05 + x['Mirpur 1'])
        return x
    
    fruit_table.agg(axis=1, func=for_mirpur_only)
    return


@app.cell
def _(fruit_table):
    print(fruit_table)
    fruit_table.transform(axis=1, func=lambda x: x * 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### String Methods""")
    return


@app.cell
def _(pd):
    stringer = pd.Series(["Apple", "Samsung", "Vivo"])

    stringer.str.lower()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Merge""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### Pivot Table""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### Time Series""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### Categorical""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### Plotting""")
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(np, pd):
    ts = pd.DataFrame(np.random.randn(1000), index=pd.date_range("2025/05/15", periods=1000))
    ts.cumsum().plot()
    return (ts,)


@app.cell
def _(np, pd, plt, ts):
    df = pd.DataFrame(
        np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
    )

    df = df.cumsum()

    # plt.figure();

    df.plot();

    plt.legend(loc='best');

    plt.show();
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Importing and exporting data""")
    return


@app.cell
def _():
    # df.read_csv("loc")
    # df.to_csv("loc")
    # df.to_parquet("loc")
    # df.read_parquet("")
    # df.read_excel("loc")
    # df.to_excel("")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Gotchas""")
    return


if __name__ == "__main__":
    app.run()
