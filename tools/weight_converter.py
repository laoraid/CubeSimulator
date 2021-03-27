# excel -> csv
# csv확률을 가중치로 변경
import pandas as pd
import functools
import sys

data = pd.read_csv(sys.argv[0])

# find number with greatest decimals


dec = 0
for x in data["probability"]:
    xstr = str(x)
    xcount = xstr[::-1].find(".")
    xmod = 10 ** xcount
    if xmod > dec:
        dec = xmod
    else:
        continue
mod_p = [x * dec for x in data["probability"]]
print(mod_p)

# GCD using Euclidean Algortihm. Note that reduce iterates for N arguments


def gcd(a, b):
    while b != 0:
        return gcd(b, a % b)
    else:
        return a


# GCD of modified probabilities.


p_gcd = functools.reduce(gcd, [x for x in mod_p])
print(p_gcd)

# Weight factor & return list of weighted probability


w_factor = dec / p_gcd
wp = [x * w_factor for x in data["probability"]]
wp = [int(x) for x in wp]
print(wp)

# Append new column to table


df = pd.DataFrame(data)
df["weighted probability"] = wp
