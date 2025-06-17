# 📊 Time Value of Money (TVM) – Math Cheat Sheet

Longhand math reference for core financial formulas.  
💡 See `time_value_money.py` for Python code examples.

---

## 📌 Variables

- \( PV \): Present Value  
- \( FV \): Future Value  
- \( PMT \): Annuity Payment  
- \( r \): Interest Rate per period  
- \( n \): Number of periods  
- \( m \): Compounding frequency per year  
- \( t \): Time in years  

---

## 1. Simple Interest

- **Future Value**

$$
FV = PV \times (1 + r \times n)
$$

- **Present Value**

$$
PV = \frac{FV}{1 + r \times n}
$$

---

## 2. Compound Interest (Annual)

- **Future Value**

$$
FV = PV \times (1 + r)^n
$$

- **Present Value**

$$
PV = \frac{FV}{(1 + r)^n}
$$

---

## 3. Compound Interest (Compounded \( m \) times per year)

- **Future Value**

$$
FV = PV \times \left(1 + \frac{r}{m} \right)^{n \cdot m}
$$

- **Present Value**

$$
PV = \frac{FV}{\left(1 + \frac{r}{m} \right)^{n \cdot m}}
$$

---

## 4. Ordinary Annuity (Payments at End of Period)

- **Future Value**

$$
FV = PMT \times \frac{(1 + r)^n - 1}{r}
$$

- **PMT from FV**

$$
PMT = \frac{FV \cdot r}{(1 + r)^n - 1}
$$

- **Present Value**

$$
PV = PMT \times \frac{1 - (1 + r)^{-n}}{r}
$$

- **PMT from PV**

$$
PMT = \frac{PV \cdot r}{1 - (1 + r)^{-n}}
$$

---

## 5. Annuity Due (Payments at Beginning of Period)

- **Future Value**

$$
FV = PMT \times \frac{(1 + r)^n - 1}{r} \times (1 + r)
$$

- **PMT from FV**

$$
PMT = \frac{FV \cdot r}{[(1 + r)^n - 1] \cdot (1 + r)}
$$

- **Present Value**

$$
PV = PMT \times \frac{1 - (1 + r)^{-n}}{r} \times (1 + r)
$$

- **PMT from PV**

$$
PMT = \frac{PV \cdot r}{[1 - (1 + r)^{-n}] \cdot (1 + r)}
$$

---

## 6. Perpetuity

- **Present Value of Perpetuity**

$$
PV = \frac{PMT}{r}
$$

---

## 7. Continuous Compounding

- **Future Value**

$$
FV = PV \cdot e^{r \cdot n}
$$

- **Present Value**

$$
PV = \frac{FV}{e^{r \cdot n}}
$$

---

> 📎 Code examples available in  
> [time_value_money.py](FinTech/TVM/time_value_money.py)
