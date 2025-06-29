# 🧠 Overview: Backtesting Approaches

| Aspect             | Vectorized                               | Event-Driven                                |
|--------------------|-------------------------------------------|----------------------------------------------|
| **How it works**   | Operates on entire dataset at once        | Simulates tick-by-tick or bar-by-bar         |
| **Data format**    | Tabular (e.g., DataFrame)                 | Stream of events (e.g., one bar at a time)   |
| **Execution style**| Applies logic with array math             | Executes logic per event (like live)         |
| **Speed**          | 🟢 Fast (for simple logic)                 | 🟡 Slower (but realistic)                     |
| **Flexibility**    | 🔴 Limited                                 | 🟢 High — handles slippage, fills, etc.       |
| **Use case**       | Quick prototypes, basic strategies        | Live-like strategies, realistic sim          |

---

## ⚡️ 1. Vectorized Backtesting

### ✅ What it is
A **mathematical**, NumPy/pandas-style approach.  
You apply formulas to **whole arrays** to compute signals, returns, etc.  
No concept of individual trade execution or fills.

---

### 📊 Example

```python
import pandas as pd
df = pd.read_csv("prices.csv")

df['signal'] = df['Close'].rolling(20).mean() > df['Close'].rolling(50).mean()
df['returns'] = df['Close'].pct_change()
df['strategy_returns'] = df['signal'].shift(1) * df['returns']
```

---

### 🟢 Pros
- Super fast  
- Simple to implement

### 🔴 Cons
- Can’t simulate real execution (e.g., partial fills, order delays)  
- No slippage, latency, or live behavior

---

## 🧭 2. Event-Driven Backtesting

### ✅ What it is
You write a **backtesting engine** that **reacts to events** (price updates, fills, news, etc.).  
This mimics how a live trading system would behave.

---

### 📦 How it works
You loop through each bar (or tick), e.g., minute by minute.  
At each step:

1. Receive new market data  
2. Evaluate strategy  
3. Place order (if needed)  
4. Update portfolio based on fills

---

### 🧠 Pseudocode

```python
for bar in data:
    strategy.update(bar)
    signals = strategy.generate_signals()
    broker.execute(signals)
    portfolio.update(bar)
```

---

### 🟢 Pros
- Realistic: Can simulate delays, slippage, order books  
- Flexible: Good for intraday, high-frequency, and complex logic

### 🔴 Cons
- More complex to code  
- Slower than vectorized

---

## 🧪 Which One Should You Use?

| Situation                              | Use             |
|----------------------------------------|-----------------|
| Simple moving average backtest         | ✅ Vectorized   |
| Backtesting on daily bars              | ✅ Vectorized   |
| Trading on news, volume spikes         | ✅ Event-driven |
| Simulating stop-loss or trailing stop  | ✅ Event-driven |
| Testing fill delays or order queues    | ✅ Event-driven |

---

## 📌 Summary

| Vectorized                          | Event-Driven                          |
|-------------------------------------|----------------------------------------|
| Fast, simple, limited realism       | Slower, complex, very realistic        |
| Think: **Spreadsheet logic**        | Think: **Simulation loop**             |
| Best for: **Prototyping**           | Best for: **Execution accuracy**       |
