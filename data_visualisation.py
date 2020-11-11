# %%
import pandas as pd
from matplotlib import pyplot as plt

# %%
# Add world total population for each year in dataset
data = pd.read_csv("countries.csv")
for x in data.year.unique():
    year = data[data.year == x]
    sum = round(year.population.sum())
    row = {"country": "World", "year": x, "population": sum}
    data = data.append(row, ignore_index=True)

# %%
# Add year-on-year growth for each nation
for ind, row in data.iterrows():
    if data.loc[ind]["year"] == 1952:
        data.loc[ind, "yearly_growth"] = 0
        continue

    current_year = row["population"]
    prev_year = data.loc[ind-1]["population"]
    change = (current_year - prev_year) / prev_year
    data.loc[ind, "yearly_growth"] = round(change * 100, 1)

data.to_csv("countries_modified.csv")
data = pd.read_csv("countries_modified.csv")
us = data[data.country == "United States"]
china = data[data.country == "China"]
world = data[data.country == "World"]

# %%
# Plot population change
plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.plot(world.year, world.population / 10**6, linestyle='--', dashes=(5, 1))
plt.title("Population change by nation")
plt.xlabel("Year")
plt.ylabel("Population, millions")
plt.legend(["US", "China", "World"])
plt.show()

# %%
# Plot population growth
plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.plot(world.year, world.population / world.population.iloc[0] * 100,linestyle='--', dashes=(5, 1))
plt.title("Population growth by nation")
plt.xlabel("Year")
plt.ylabel("Population growth (Year 1 = 0)")
plt.legend(["US", "China", "World"])
plt.show()

# %%
# Plot year-on-year population growth
plt.plot(us.year, us.yearly_growth)
plt.plot(china.year, china.yearly_growth)
plt.plot(world.year, world.yearly_growth, linestyle='--', dashes=(5, 1))
plt.title("Year-on-year population growth by nation")
plt.xlabel("Year")
plt.ylabel("Growth on previous year, %")
plt.legend(["US", "China", "World"])
plt.show()

# %%
