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
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""# Inspection""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Basic Analysis Queries

    1. **Sales performance analysis**: What are the total sales by country or by month?
    2. **Customer behavior**: Which customers have made the most purchases?
    3. **Product popularity**: What are the top-selling products by quantity?
    4. **Price analysis**: What's the distribution of unit prices across products?

    ## Comprehensive practice guide
    1. **Sales analysis by country** - Learn which markets contribute most to your revenue
    2. **Sales trends over time** - Identify seasonal patterns and growth trends
    3. **Top-selling products** - Discover your revenue drivers by quantity and value
    4. **Customer behavior analysis** - Identify your most valuable customers
    5. **Time-based patterns** - See which days and hours have peak sales
    6. **Market basket analysis** - Find products commonly purchased together
    7. **Price analysis** - Understand your pricing strategy and opportunities
    8. **Geographic analysis** - Compare purchasing behaviors across countries
    9. **Customer segmentation** - Group customers by recency, frequency, and monetary value
    10. **Time series forecasting** - Predict future sales based on historical data

    These exercises will help developing essential pandas skills including:
    - Data cleaning and preparation
    - Grouping and aggregation
    - Time-based analysis
    - Various visualization techniques
    - Advanced analytics like RFM analysis and customer segmentation
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 1: Sales Analysis by Country
    ### Business question: How are sales distributed across different countries?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 2: Monthly Sales Trends
    ### Business question: How do sales vary by month? Are there any seasonal patterns?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 3: Top-Selling Products
    ### Business question: Which products generate the most revenue? Which sell in the highest quantities?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 4: Customer Analysis
    ### Business question: Who are our best customers? How is customer spending distributed?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 5: Sales by Day of Week and Hour
    ### Business question: When do we make most of our sales? What days/times are busiest?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 6: Basket Analysis
    ### Business question: What products are commonly purchased together?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 7: Price Analysis and Optimization
    ### Business question: How are our products priced? Where might we have pricing optimization opportunities?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 8: Geographic Analysis
    ### Business question: How do purchasing behaviors differ across countries?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 9: Customer Segmentation
    ### Business question: How can we segment our customers based on their purchasing behavior?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Query 10: Time Series Forecasting
    ### Business question: Can we predict future sales based on historical patterns?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Key Skills Practiced
    Through these exercises, you'll gain hands-on experience with the following pandas skills:

    - Data cleaning and preparation
    - Grouping and aggregation
    - Time series manipulation
    - Visualization integration
    - Statistical analysis
    - Complex multi-level analysis
    - Business intelligence extraction
    - Customer segmentation
    - Product analysis
    - Sales forecasting
    """
    )
    return


if __name__ == "__main__":
    app.run()
