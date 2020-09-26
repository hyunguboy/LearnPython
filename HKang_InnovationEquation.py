import numpy as np
import matplotlib

# 2020 Hyungu Kang, www.hazykinetics.com, hyunguboy@gmail.com
# Replicate compensation model from "Loonshots" by Safi Bahcall

LevelTot = 4    # Total "levels" of ranks in the company
Level = 1       # Current level
g = 0.10        # Fraction salary raise with rise in level
a = 1           # Percentage of equity owned by an employee
NEU = 1         # Number of equity units owned at a given level
Psh =           # Price per share

# Compensation amounts. Numbers here are an arbitrary base number, not a specific currency.
CompBase0 = 100
CompBase = CompBase0*(1+g)^(Level - 1)
CompEquity = 10
CompTotal = CompBase + CompEquity

print(CompTot)