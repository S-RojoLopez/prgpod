# %%
import numpy as np
import pandas as pd

# %%
df = pd.read_csv("insurance.csv")
#print(df)

# %%
df.head()

# %%
df.shape

# %%
print ("El promedio de edad es: ", df["age"].mean())

# %%
