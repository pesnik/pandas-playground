# pandas-playground

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![pandas Version](https://img.shields.io/badge/pandas-1.0+-brightgreen.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A repository for hands-on experimentation and skill-building with the pandas library in Python. This playground is designed to guide you through mastering pandas, from foundational concepts to advanced techniques, using practical examples, exercises, and real-world datasets.

## Table of Contents

* [Introduction](#introduction)
* [Purpose](#purpose)
* [Structure](#structure)
* [Getting Started](#getting-started)
    * [Installation](#installation)
    * [Dependencies](#dependencies)
    * [Usage](#usage)
* [Learning Roadmap](#learning-roadmap)
* [Datasets](#datasets)
* [Contributing](#contributing)
* [License](#license)
* [Author](#author)

## Introduction

Pandas is a powerful Python library for data manipulation and analysis, widely used in data science and analytics. This repository provides a structured environment to learn and practice pandas through hands-on scripts, exercises, and diverse datasets, catering to beginners and advanced learners alike.

## Purpose

The primary goals of this repository are to:

* Offer a hands-on environment for learning pandas from basics to advanced techniques.
* Provide practical examples and exercises to reinforce understanding.
* Serve as a personal learning space to master pandas.
* Create a reusable resource for others to learn and explore pandas.

## Structure

The repository is organized to support a progressive learning journey:

```
pandas-playground/
├── data/                      # Directory for sample datasets
│   └── ...
├── 01_data_loading_and_inspection.py  # Marimo script for data loading
├── 02_data_selection_and_indexing.py  # Marimo script for data selection
├── 03_data_cleaning.py          # Marimo script for data cleaning
├── 04_data_manipulation.py      # Marimo script for data manipulation
├── 05_data_aggregation.py       # Marimo script for data aggregation
├── 06_time_series_analysis.py   # Marimo script for time series
├── 07_plotting_with_pandas.py   # Marimo script for plotting
├── exercises/                  # Directory for practice exercises
│   ├── exercise_1.py
│   ├── exercise_2.py
│   └── ...
└── README.md                  # This file
```

## Getting Started

### Installation

1. **Install `uv`**:
   Ensure you have `uv` installed, a fast Python package and project manager. Follow the instructions at [uv documentation](https://docs.astral.sh/uv/) or install via:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**:

   ```bash
   git clone https://github.com/pesnik/pandas-playground.git
   cd pandas-playground
   ```

3. **Set up the project with `uv`**:
   Create a virtual environment and install dependencies using `uv`:

   ```bash
   uv init
   uv sync
   ```

   This will create a virtual environment and install dependencies listed in `pyproject.toml` (if present) or a default setup.

### Dependencies

* Python (3.9 or higher)
* pandas (1.0 or higher)
* Marimo (for running interactive scripts)

To ensure dependencies are installed, add them explicitly with `uv`:

```bash
uv add pandas marimo
```

This updates the virtual environment with the required packages. You can verify the installed packages with:

```bash
uv pip list
```

### Usage

* **Activate the Virtual Environment**:
   If not already activated, activate the `uv`-managed virtual environment:

   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

* **Run Marimo Scripts**:
   Execute the provided Marimo scripts to explore pandas concepts interactively. For example:

   ```bash
   uv run marimo run 01_data_loading_and_inspection.py
   ```

* **Exercises**:
   Work through the exercises in the `exercises/` directory to test your skills.

* **Datasets**:
   Download datasets from the links in the [Datasets](#datasets) section and place them in the `data/` directory for use with the scripts.

## Learning Roadmap

This repository is designed as a roadmap to master pandas. Follow these steps to progress from beginner to advanced:

1. **Start with Basics**: Run `01_data_loading_and_inspection.py` to learn how to load data (CSV, Excel, JSON) and inspect DataFrames using methods like `.head()`, `.info()`, and `.describe()`.

2. **Master Selection and Indexing**: Use `02_data_selection_and_indexing.py` to practice accessing data with `.loc`, `.iloc`, and boolean indexing.

3. **Clean Data**: Explore `03_data_cleaning.py` to handle missing values, duplicates, and data type conversions.

4. **Manipulate Data**: Use `04_data_manipulation.py` to add/remove columns, sort, filter, and apply functions.

5. **Aggregate Data**: Run `05_data_aggregation.py` to group data and compute summary statistics (e.g., mean, sum).

6. **Work with Time Series**: Use `06_time_series_analysis.py` to handle time-based data, including resampling and rolling windows.

7. **Visualize Data**: Explore `07_plotting_with_pandas.py` to create plots (line, bar, scatter) directly from DataFrames.

8. **Practice with Exercises**: Solve problems in the `exercises/` directory to reinforce each topic.

9. **Apply to Real Datasets**: Use the datasets listed below to practice on real-world data, combining multiple skills (e.g., cleaning, aggregating, and plotting).

10. **Contribute**: Add your own examples or exercises to the repository to deepen your understanding and help others.

**Tip**: Work through the scripts in order, as they build on each other. Refer to the [pandas documentation](https://pandas.pydata.org/docs/) for details, and use the exercises to test your knowledge.

## Datasets

The following datasets are recommended for practice. Download them and place them in the `data/` directory. Some datasets may require a free Kaggle account.

- **Customer Transaction Dataset**:
  - [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online%2Bretail): Transactions from a UK online retail store, 2010–2011.
  - [Kaggle Customer Transactions](https://www.kaggle.com/datasets/bkcoban/customer-transactions): Synthetic data with customer purchases.

- **E-commerce Product Catalog**:
  - [Kaggle eCommerce Item Data](https://www.kaggle.com/datasets/cclark/product-item-data): 500 SKUs with product descriptions.
  - [Kaggle Amazon Product Dataset](https://www.kaggle.com/datasets/piyushjain16/amazon-product-data): Amazon product details, including names and prices.

- **Social Media Engagement**:
  - [Kaggle Social Media Engagement Report](https://www.kaggle.com/datasets/aliredaelblgihy/social-media-engagement-report): Trends in reactions, comments, and shares.
  - [Kaggle Social Media Usage Dataset](https://www.kaggle.com/datasets/bhadramohit/social-media-usage-datasetapplications): Insights into usage metrics like likes and follows.

- **Financial Market Data**:
  - [Kaggle Stock Market Dataset](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset): Daily prices of Nasdaq stocks and ETFs.
  - [Kaggle Huge Stock Market Dataset](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs): Historical prices for U.S. stocks and ETFs.

- **Healthcare Records**:
  - [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset): Anonymized clinical features for stroke prediction.
  - [Kaggle U.S. Healthcare Data](https://www.kaggle.com/datasets/maheshdadhich/us-healthcare-data): Population health and disease data.

- **Geospatial Data**:
  - [Kaggle India GIS Data](https://www.kaggle.com/datasets/nehaprabhavalkar/india-gis-data): Geospatial files with coordinates and city names.
  - [Kaggle Geospatial Environmental and Socioeconomic Data](https://www.kaggle.com/datasets/cathetorres/geospatial-environmental-and-socioeconomic-data): Global environmental and socioeconomic data.

- **Energy Consumption Data**:
  - [Kaggle Hourly Energy Consumption](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption): 10+ years of hourly data from PJM.
  - [Kaggle World Energy Consumption](https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption): Energy use by country.

- **Traffic Data**:
  - [Kaggle Traffic Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/traffic-prediction-dataset): Hourly traffic at four junctions.
  - [Kaggle Road Traffic Dataset](https://www.kaggle.com/datasets/arashnic/road-trafic-dataset): Traffic figures for Great Britain.

- **Weather Data**:
  - [Kaggle The Weather Dataset](https://www.kaggle.com/datasets/guillemservera/global-daily-climate-data): Weather for 1200+ cities worldwide.
  - [Kaggle Daily Climate Time Series Data](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data): Daily climate data for Delhi, 2013–2017.

- **E-book Sales Data**:
  - [Kaggle Books Sales and Ratings](https://www.kaggle.com/datasets/thedevastator/books-sales-and-ratings): Book sales and ratings, potentially including e-books.
  - [Kaggle Best-selling Books Dataset](https://www.kaggle.com/datasets/mansivasantpatel/best-selling-books-dataset): Data on best-selling books, possibly including e-books.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your changes (`git checkout -b feature/your-feature`).
3. Make changes and commit with descriptive messages (`git commit -m "Add new exercise"`).
4. Push to your fork (`git push origin feature/your-feature`).
5. Submit a pull request to the main branch.

Suggestions, bug fixes, new examples, or additional exercises are appreciated. Open an issue to discuss ideas before submitting large changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Created by [pesnik](https://github.com/pesnik). Feel free to reach out with feedback or questions!
