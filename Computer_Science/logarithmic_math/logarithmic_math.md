# 📐 Logarithmic Math Cheatsheet (Algorithmic Algebra Edition)

A comprehensive guide to understanding and solving logarithmic expressions, especially in the context of algorithm analysis, data allocation, and space/time complexity.

---

## 🔢 What is a Logarithm?

A **logarithm** answers the question:

> "To what power must a base be raised to get a certain number?"

Mathematically:

$\log_b(x) = y \iff b^y = x$

* $b$: the **base**
* $x$: the **result**
* $y$: the **exponent** (what the log gives you)

---

## 📘 Common Logarithmic Bases

| Notation       | Base | Name                          |
| -------------- | ---- | ----------------------------- |
| $\log_{10}(x)$ | 10   | Common Logarithm              |
| $\log_2(x)$    | 2    | Binary Logarithm (used in CS) |
| $\ln(x)$       | e    | Natural Logarithm             |

---

## ✍️ How to Solve Logs by Hand

### Example: $\log_2(8)$

**Question:** What power do we raise 2 to in order to get 8?

$\log_2(8) = y \Rightarrow 2^y = 8 \Rightarrow y = 3$

### Example: $\log_{10}(1000)$

$\log_{10}(1000) = y \Rightarrow 10^y = 1000 \Rightarrow y = 3$

### Solving Unknown Logs by Factorization:

$\log_2(32) = ?$

Factor 32:
$32 = 2^5 \Rightarrow \log_2(32) = 5$

If the number isn’t an exact power:

$\log_2(20)$

Use log change of base formula:
$\log_2(20) = \frac{\log_{10}(20)}{\log_{10}(2)} \approx \frac{1.3010}{0.3010} \approx 4.32$

---

## 📊 Application in Computer Science

### ⏱️ Time Complexity (Big-O Notation)

Logarithms appear often in time complexity:

| Algorithm Type      | Time Complexity |
| ------------------- | --------------- |
| Binary Search       | $O(\log_2 n)$   |
| Balanced BST Search | $O(\log n)$     |
| Divide & Conquer    | $O(n \log n)$   |

**Why log?**

* With each step, we cut the problem size in half (or a fraction)
* Number of steps $\approx \log_2(n)$

---

### 💾 Space & Memory Allocation

* For memory blocks or chunks, powers of 2 are often used: 2, 4, 8, 16...
* To find how many bits are needed:
  $\text{Bits needed} = \lceil \log_2(n) \rceil$

Example:

* To represent 64 items: $\log_2(64) = 6$ bits
* To represent 1000 items: $\log_2(1000) \approx 9.97 \Rightarrow 10$ bits

---

## 🧠 Properties of Logarithms

| Property       | Formula                                       |
| -------------- | --------------------------------------------- |
| Product Rule   | $\log_b(xy) = \log_b(x) + \log_b(y)$          |
| Quotient Rule  | $\log_b(\frac{x}{y}) = \log_b(x) - \log_b(y)$ |
| Power Rule     | $\log_b(x^n) = n \cdot \log_b(x)$             |
| Change of Base | $\log_b(x) = \frac{\log_k(x)}{\log_k(b)}$     |
| Identity       | $\log_b(b) = 1$, $\log_b(1) = 0$              |

---

## 🧮 Estimation Tips

| $x$  | $\log_{10}(x)$ | $\log_2(x)$ |
| ---- | -------------- | ----------- |
| 1    | 0              | 0           |
| 10   | 1              | \~3.32      |
| 100  | 2              | \~6.64      |
| 1024 | \~3.01         | 10          |

Use these for mental math or back-of-the-envelope calculations.

---

## 🧰 Practice Questions

1. $\log_2(1) = ?$
2. $\log_2(64) = ?$
3. How many bits to store 500 values?
4. If binary search takes $\log_2(n)$ time, how many steps for 1024 values?

---

Let me know if you want a follow-up for exponential functions or translating between logs and code!
