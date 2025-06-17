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

- **Future Va**
