# %%
import numpy as np
import pandas as pd

# %%
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
#print(df)

# %%
print ("El promedio es:\n", df.drop(columns=["order","weekday","hour"]).mean())

# %%
print ("La moda es:\n", df.drop(columns=["order"]).mode())

# %%
print ("La mediana es:\n", df.drop(columns=["order","weekday","hour"]).median())

# %%
print ("La desviación estándar es:\n", df.drop(columns=["order","weekday","hour"]).std())

# %%
print ("El primer cuartil es:\n", df.drop(columns=["order","weekday","hour"]).quantile(.1))
print ("El segundo cuartil es:\n", df.drop(columns=["order","weekday","hour"]).quantile(.25))

# %%
print ("El tercer cuartil es:\n", df.drop(columns=["order","weekday","hour"]).quantile(.50))

# %%
print ("El cuarto cuartil es:\n", df.drop(columns=["order","weekday","hour"]).quantile(.75))