# 📈 Polygon Stock Tickers Extractor

This project fetches **active stock tickers** from the Polygon.io API and saves them into a **CSV file** for further analysis. It handles **pagination**, ensures **consistent CSV formatting**, and includes a robust way to handle missing data.

---

## 📝 Features

- Fetches **active stock tickers** from Polygon.io.
- Handles **paginated API responses** automatically.
- Saves data to a CSV file with a **consistent schema**.
- Handles missing fields gracefully.
- Easy to extend for other markets or ticker types.

---

## ⚙️ Technologies Used

- **Python 3.x**
- **requests** – for making HTTP API calls
- **dotenv** – for managing API keys securely
- **csv** – for writing data into CSV format

---
## 🗂 CSV Schema

The CSV file (`tickers.csv`) will contain the following columns:

| Column Name         | Description                                               | Data Type        |
|--------------------|-----------------------------------------------------------|----------------|
| `ticker`           | Stock ticker symbol                                        | String         |
| `name`             | Full company name                                         | String         |
| `market`           | Market type (e.g., stocks)                                | String         |
| `locale`           | Locale of the market (e.g., US)                           | String         |
| `primary_exchange` | Primary stock exchange where the ticker is listed         | String         |
| `type`             | Security type (e.g., CS for common stock)                | String         |
| `active`           | Indicates if the ticker is currently active (`True/False`) | Boolean/String |
| `currency_name`    | Currency used (e.g., USD)                                 | String         |
| `cik`              | Central Index Key (CIK) identifier                        | String         |
| `composite_figi`   | Composite Financial Instrument Global Identifier (FIGI)   | String         |
| `share_class_figi` | Share-class FIGI                                          | String         |
| `last_updated_utc` | Timestamp of last update (UTC)                             | String/Datetime |


Save all tickers into tickers.csv with a structured schema.



