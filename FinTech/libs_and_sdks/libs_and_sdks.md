# 🚀 Python Fintech & Quant Tech Stack – Cheat Sheet

This cheat sheet gathers top Python libraries for **quant research**, financial engineering, ML, trading, and more—all in one place.

---

## 📊 Core Numerics & Data

- `numpy`, `scipy` – fundamental for numerical computing :contentReference[oaicite:1]{index=1}  
- `pandas`, `polars` – structured data & time series :contentReference[oaicite:2]{index=2}  
- `sympy` – symbolic math  
- `statsmodels` – statistical modeling & econometrics  
- `scikit-multiflow` – stream learning (online ML) :contentReference[oaicite:3]{index=3}  

---

## 💹 Quant Finance & Pricing

- `QuantLib-Python` – industry-grade models & pricing :contentReference[oaicite:4]{index=4}  
- `qfin`, `FinancePy`, `tf-quant-finance`, `pymc3` – for pricing, risk, tensor models :contentReference[oaicite:5]{index=5}  
- `vollib`, `pysabr`, `finoptions` – options pricing & Greeks :contentReference[oaicite:6]{index=6}  
- `rateslib` – fixed-income/bond modeling :contentReference[oaicite:7]{index=7}  
- `Q-Fin`, `QuantPy`, `ffn`, `pynance` – analytics & data pipelines :contentReference[oaicite:8]{index=8}  

---

## 📈 Technical Analysis & Strategies

- `pandas_talib`, `finta`, `TA‑Lib`, `tulipy`, `talipp` – technical indicators :contentReference[oaicite:9]{index=9}  

---

## 🧠 Backtesting & Trading

- `backtrader`, `zipline(-reloaded)`, `bt`, `pyalgotrade`, `QSTrader`, `pyfolio`, `FinRL`, `vectorbt` – backtesting & strategy testing :contentReference[oaicite:10]{index=10}  
- `FinRL` – deep reinforcement learning for finance :contentReference[oaicite:11]{index=11}  
- `mlfinlab` – advanced financial ML (Lopez de Prado) :contentReference[oaicite:12]{index=12}  
- `Qlib` – full ML pipeline by Microsoft :contentReference[oaicite:13]{index=13}  
- `Fast‑Trade`, `Backtesting.py`, `alkobroker`, `sage`, etc. :contentReference[oaicite:14]{index=14}  

---

## 🤖 Machine Learning / Deep Learning

- `scikit-learn` – core supervised/manifold learning :contentReference[oaicite:15]{index=15}  
- `TensorFlow`, `PyTorch`, `fastai`, `CatBoost` – DL and gradient boosting :contentReference[oaicite:16]{index=16}  
- `scikit-multiflow` – streaming ML :contentReference[oaicite:17]{index=17}  
- `mlfinlab`, `PiML`, `Orange3` – interpretability, autoML, explainability :contentReference[oaicite:18]{index=18}  

---

## 🌐 APIs & Data SDKs

- `tda-api` – TD Ameritrade  
- Brokers/API wrappers (`IBKR`, `alpaca`, `ccxt`) – market & crypto data  
- `PyQL`, `OpenBB Terminal`, `QuantConnect Lean` – research & execution :contentReference[oaicite:19]{index=19}  

---

## 🏦 Fintech & Web Tech

- `Django`, `Flask`, `FastAPI` – fintech platform frameworks :contentReference[oaicite:20]{index=20}  
- `pybitcointools`, payment SDKs (Stripe, Plaid) :contentReference[oaicite:21]{index=21}  

---

## 💡 Suggested Workflow for Quant Research

1. Ingest & preprocess raw market data (`pandas`, `polars`, `numpy`)  
2. Feature-engineer with `ffn`, `talib`, `mlfinlab`  
3. Backtest strategies via `backtrader`, `zipline`, or `vectorbt`  
4. Model using `scikit-learn`, `PyTorch`, `TensorFlow`  
5. Integrate reinforcement learning using `FinRL`, `Qlib`  
6. Deploy via APIs (`FastAPI`) or platforms (QuantConnect Lean)  

---

## ✅ Pro Tips

- Use `NumPy/Pandas` + `SciPy` as foundational layers  
- For pricing: `QuantLib` + `FinancePy` or TensorFlow‑based libs  
- For ML: start with `scikit-learn`, then use DL/GBM frameworks  
- For RL: use `FinRL`, `Qlib`, or `AlphaPy`  
- Use bot/backtest frameworks to convert models into strategies  

---

## 📚 Learn More

- **Awesome‑quant** GitHub repo (20k+ stars) for curated quant libraries :contentReference[oaicite:22]{index=22}  
- FinRL & AI4Finance projects & papers :contentReference[oaicite:23]{index=23}  
- QuantStart and QuantStart guides for practical overviews :contentReference[oaicite:24]{index=24}  
- Medium & Upplabs for Fintech library rundowns :contentReference[oaicite:25]{index=25}  

---

Grab any stack from this sheet to build your own **quant research platform**. Let me know if you'd like me to generate a `requirements.txt` or set up a `conda` environment tailored to your workflow!
::contentReference[oaicite:26]{index=26}
