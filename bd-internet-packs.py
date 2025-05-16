import marimo

__generated_with = "0.13.7"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import requests
    import pandas as pd
    return pd, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Grameenphone""")
    return


@app.cell
def _(pd, requests):
    gp_internet_packages = requests.get("https://www.grameenphone.com/_next/data/vYWzoOMkamHhm-jC_b-k0/en/personal/plans-offers/internet-packages/internet-packs.json?slug=internet-packs")
    gp_internet_packages = gp_internet_packages.json()

    gp_internet_packages_df = pd.DataFrame(gp_internet_packages["pageProps"]["internet_package_card_data"]["content"])
    gp_internet_packages_df['price'].transform(lambda x: int(x)).describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Banglalink""")
    return


@app.cell
def _(pd, requests):
    bl_internet_packages = requests.get('https://web-api.banglalink.net/api/v1/offers/prepaid/internet')
    packs = bl_internet_packages.json()
    bl_all_packs = packs['data'][0]['packs']

    bl_internet_packages_df = pd.DataFrame(bl_all_packs)
    bl_internet_packages_df.describe()['price_tk']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Robi""")
    return


if __name__ == "__main__":
    app.run()
