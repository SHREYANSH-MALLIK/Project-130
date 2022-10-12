import pandas as pd
import csv

df = pd.read_csv("dwarf_stars.csv")
print(df.shape)

print(df.shape)

print(list(df))

print(list(df))

df.to_csv("main.csv")