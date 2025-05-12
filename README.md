# pandas-playground

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![pandas Version](https://img.shields.io/badge/pandas-1.0+-brightgreen.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A repository for hands-on experimentation and skill-building with the pandas library in Python. This playground is designed to help you master pandas through practical examples, exercises, and exploration.

## Table of Contents

* [Introduction](#introduction)
* [Purpose](#purpose)
* [Structure](#structure)
* [Getting Started](#getting-started)
    * [Installation](#installation)
    * [Dependencies](#dependencies)
    * [Usage](#usage)
* [Contents](#contents)
* [Contributing](#contributing)
* [License](#license)
* [Author](#author)

## Introduction

Pandas is a powerful and versatile Python library used for data manipulation and analysis. This repository provides a structured environment to learn and practice pandas concepts, from basic data structures to advanced techniques.

## Purpose

The primary goal of this repository is to:

* Provide a hands-on environment for learning pandas.
* Offer practical examples and exercises to reinforce understanding.
* Serve as a personal learning space to master pandas.
* Create a resource that others can use to learn pandas.

## Structure

The repository is organized as follows:

    pandas-playground/
    ├── data/                      # Directory for sample datasets
    │   └── ...
    ├── 01_data_loading_and_inspection.py  # Marimo script for data loading
    ├── 02_data_selection_and_indexing.py # Marimo script for data selection
    ├── 03_data_cleaning.py          # Marimo script for data cleaning
    ├── 04_data_manipulation.py      # Marimo script for data manipulation
    ├── 05_data_aggregation.py       # Marimo script for data aggregation
    ├── 06_time_series_analysis.py  # Marimo script for time series (if applicable)
    ├── 07_plotting_with_pandas.py    # Marimo script for plotting
    ├── exercises/                 # Directory for practice exercises
    │   ├── exercise_1.py
    │   ├── exercise_2.py
    │   └── ...
    └── README.md                  # This file

## Getting Started

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/pesnik/pandas-playground.git
    cd pandas-playground
    ```

### Dependencies

* Python (3.9 or higher)
* pandas (1.0 or higher)
* Marimo

Install the required packages using pip:

    pip install pandas marimo

### Usage

* **Marimo:** To run the Marimo scripts, navigate to the repository directory and run the desired script (e.g., `01_data_loading_and_inspection.py`) using the Marimo CLI:

    ```bash
    marimo run 01_data_loading_and_inspection.py
    ```

## Contents

The repository covers the following pandas topics:

* Data Loading and Inspection: Reading data from various formats (CSV, Excel, JSON, SQL) and exploring its structure.
* Data Selection and Indexing: Accessing and selecting data using labels, integer positions, and boolean conditions.
* Data Cleaning: Handling missing values, duplicates, and data type conversions.
* Data Manipulation: Adding/removing columns, sorting, filtering, and applying functions.
* Data Aggregation: Grouping data and calculating summary statistics.
* Time Series Analysis: Working with time series data (if applicable).
* Data Visualization: Creating plots directly from pandas DataFrames and Series.
* Exercises: Practice problems to reinforce your understanding of each topic.

## Contributing

Contributions are welcome! If you have any suggestions, find any errors, or want to add more examples or exercises, feel free to open an issue or submit a pull request.

Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your changes.
3.  Make your changes and commit them with descriptive commit messages.
4.  Push your changes to your fork.
5.  Submit a pull request to the main branch of the original repository.

## License

This project is licensed under the [MIT License](LICENSE).

