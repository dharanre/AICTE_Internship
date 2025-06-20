{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 📊 Data Preparation Notebook\n",
    "This notebook prepares raw climate data for carbon emission prediction, matching the GitHub project style."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1️⃣ Load raw data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "raw_file = 'climate_change_download.xls'\n",
    "df = pd.read_excel(raw_file)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2️⃣ Clean data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop empty rows and columns\n",
    "df.dropna(how='all', inplace=True)\n",
    "df.dropna(axis=1, how='all', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Standardize column names\n",
    "df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert data types\n",
    "df = df.convert_dtypes()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3️⃣ Export cleaned data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cleaned_csv = 'data_cleaned.csv'\n",
    "df.to_csv(cleaned_csv, index=False)\n",
    "print(f'✅ Cleaned data saved to {cleaned_csv}')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.x"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
