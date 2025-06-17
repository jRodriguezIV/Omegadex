# ================================
# 📊 TIME VALUE OF MONEY (TVM) FORMULAS CHEATSHEET
# ================================

# VARIABLES
# PV = Present Value
# FV = Future Value
# PMT = Annuity Payment (AP)
# r = Interest Rate per period (decimal)
# n = Number of periods
# t = Number of years
# m = Compounding frequency per year (for compound freq)

import math

# ----------------------------------------
# 1. SIMPLE INTEREST (Non-Compounding)
# ----------------------------------------

# FV given PV
FV = PV * (1 + r * n)

# PV given FV
PV = FV / (1 + r * n)


# ----------------------------------------
# 2. COMPOUND INTEREST (Lump Sum)
# ----------------------------------------

# FV given PV
FV = PV * (1 + r)**n

# PV given FV
PV = FV / (1 + r)**n


# ----------------------------------------
# 3. COMPOUND INTEREST (Compounded m times per year)
# ----------------------------------------

# FV given PV
FV = PV * (1 + r/m)**(n * m)

# PV given FV
PV = FV / (1 + r/m)**(n * m)


# ----------------------------------------
# 4. ORDINARY ANNUITY (Payments at END of each period)
# ----------------------------------------

# FV given PMT
FV = PMT * ((1 + r)**n - 1) / r

# PMT given FV
PMT = (FV * r) / ((1 + r)**n - 1)

# PV given PMT
PV = PMT * (1 - (1 + r)**-n) / r

# PMT given PV
PMT = (PV * r) / (1 - (1 + r)**-n)


# ----------------------------------------
# 5. ANNUITY DUE (Payments at BEGINNING of each period)
# ----------------------------------------

# FV given PMT
FV = PMT * ((1 + r)**n - 1) / r * (1 + r)

# PMT given FV
PMT = (FV * r) / (((1 + r)**n - 1) * (1 + r))

# PV given PMT
PV = PMT * (1 - (1 + r)**-n) / r * (1 + r)

# PMT given PV
PMT = (PV * r) / ((1 - (1 + r)**-n) * (1 + r))


# ----------------------------------------
# 6. PERPETUITY (Infinite Annuity)
# ----------------------------------------

# PV of Perpetuity
PV = PMT / r


# ----------------------------------------
# 7. CONTINUOUS COMPOUNDING
# ----------------------------------------

# FV
FV = PV * math.exp(r * n)

# PV
PV = FV / math.exp(r * n)

# ----------------------------------------
# ✅ END OF TVM CHEATSHEET
# ----------------------------------------

