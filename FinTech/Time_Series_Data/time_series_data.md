# 📈 Time Series Data Cheat Sheet

A quick reference to foundational concepts in time series and market data analysis.

---

## 🕒 Time Series

A **sequence of data points** collected at successive, equally spaced points in time.

```
Time       Value
--------   ------
2024-01-01  102
2024-01-02  108
2024-01-03  105
```

---

## 📊 OHLCV – Market Data Format

Common in financial markets; represents price and volume over time.

| Time     | Open | High | Low | Close | Volume |
| -------- | ---- | ---- | --- | ----- | ------ |
| 10:00 AM | 100  | 105  | 99  | 102   | 5000   |
| 10:05 AM | 102  | 106  | 101 | 104   | 4500   |

* **Open**: First price in interval
* **High**: Highest price in interval
* **Low**: Lowest price in interval
* **Close**: Last price in interval
* **Volume**: Total units traded

---

## 💵 LTP – Last Traded Price

The **most recent price** at which a transaction occurred.

```python
ltp = trades[-1]['price']
```

---

## ⏱ Granularity (Time Intervals)

Refers to the **time step** between data points.

* High granularity: e.g., 1-second or 1-minute data
* Low granularity: e.g., daily, monthly data

```
# High granularity
Time       Price
10:00:01   100.5
10:00:02   100.6

# Low granularity
Date        Price
2024-01-01  101.2
2024-01-02  102.3
```

---

## 📀 Cross-Sectional Data

**One time point, multiple entities.**

| Company | Revenue |
| ------- | ------- |
| A       | 1000    |
| B       | 1200    |
| C       | 800     |

---

## ⏳ Longitudinal Data

**Same entity tracked over time**.

| Date       | Revenue (Company A) |
| ---------- | ------------------- |
| 2024-01-01 | 1000                |
| 2024-02-01 | 1050                |
| 2024-03-01 | 1100                |

---

## 📊 Panel Data

**Multiple entities over time** (cross-sectional + longitudinal).

| Date       | Company | Revenue |
| ---------- | ------- | ------- |
| 2024-01-01 | A       | 1000    |
| 2024-01-01 | B       | 1200    |
| 2024-02-01 | A       | 1050    |
| 2024-02-01 | B       | 1250    |

---

🧠 **Pro Tip**: Use `pandas` for handling all these formats efficiently in Python!

```python
import pandas as pd
df = pd.read_csv('data.csv', parse_dates=['Date'], index_col='Date')
```
