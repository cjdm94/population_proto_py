# %%
import pandas as pd
from matplotlib import pyplot as plt

# %%
# Compare population growth in the US and China
data = pd.read_csv("countries.csv")
us = data[data.country == "United States"]
china = data[data.country == "China"]

# %%
plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.title("Population change, US vs China")
plt.xlabel("Year")
plt.ylabel("Population, millions")
plt.legend(["US", "China"])
plt.show()

# %%
plt.plot(us.year, us.population / us.population.iloc[0] * 100 )
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.title("Population growth, US vs China")
plt.xlabel("Year")
plt.ylabel("Population growth (Year 1 = 0)")
plt.legend(["US", "China"])
plt.show()

# %%
for ind, row in data.iterrows():
    if data.loc[ind]["year"] == 1952:
        data.loc[ind, "yearly_growth"] = 0
        continue

    current_year = row["population"]
    prev_year = data.loc[ind-1]["population"]
    change = (current_year - prev_year) / prev_year
    data.loc[ind, "yearly_growth"] = change * 100
# %%
data.to_csv("countries_updated.csv", index=False)
new_data = pd.read_csv('countries_updated.csv')

us = new_data[new_data.country == "United States"]
china = new_data[new_data.country == "China"]
# %%
plt.plot(us.year, us.yearly_growth)
plt.plot(china.year, china.yearly_growth)
plt.title("Year-on-year population growth, US vs China")
plt.xlabel("Year")
plt.ylabel("Growth on previous year, %")
plt.legend(["US", "China"])
plt.show()
# %%
# TODO add Britain and plot against global average