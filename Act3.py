# %%
import pandas as pd

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
df.head()
df.dropna()
#print(df)

# %%
df.describe()

# %%
import seaborn as sns

sns.set_theme(style="white")

# %%
sns.boxplot(x="weekday",y="total_items",data=df,palette="rainbow")

# %%
sns.boxplot(x="weekday",y="Drinks%",data=df,palette="rainbow")

# %%
sns.boxplot(x="weekday",y="Food%",data=df,palette="rainbow")

# %%
sns.displot(x="hour", data=df)

# %%
sns.displot(x="weekday", data=df)

# %%
sns.displot(x="total_items", data=df)

# %%
df.corr()

# %%
sns.heatmap(df.corr())

# %%
g = sns.histplot(data=df, x="weekday")
for q in df.weekday.quantile([.25, .5, .75]):
    g.axvline(q, linestyle=":")
    g.text(q, 5, q)

# %%
sns.scatterplot(data=df, x="total_items", y="hour", hue="discount%")

# %%
sns.scatterplot(data=df, x="total_items", y="weekday", hue="discount%")
