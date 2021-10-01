import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv"

covid_death_overall = pd.read_csv(url,
                                  usecols=["Country_Region", "Confirmed", "Deaths", "Recovered", "Active"])

total_deaths_sweden = covid_death_overall.iloc[617:639]["Deaths"].sum()
total_recovered_sweden = covid_death_overall.iloc[617:639]["Recovered"].sum()
total_active_sweden = covid_death_overall.iloc[617:639]["Active"].sum()

total_deaths_stockholm = covid_death_overall.iloc[631]["Deaths"]
total_recovered_stockholm = covid_death_overall.iloc[631]["Recovered"]
total_active_stockholm = covid_death_overall.iloc[631]["Active"]

total_deaths_vgl = covid_death_overall.iloc[637]["Deaths"]
total_recovered_vgl = covid_death_overall.iloc[637]["Recovered"]
total_active_vgl = covid_death_overall.iloc[637]["Active"]

total_deaths_skane = covid_death_overall.iloc[629]["Deaths"]
total_recovered_skane = covid_death_overall.iloc[629]["Recovered"]
total_active_skane = covid_death_overall.iloc[629]["Active"]

places = ["Sweden", "Stockholm", "Västra Götaland", "Skåne"]
country = ["Sweden"]
region_deaths = [total_deaths_sweden, total_deaths_stockholm, total_deaths_vgl, total_deaths_skane]
region_recovered = [total_recovered_sweden, total_recovered_vgl, total_recovered_vgl, total_recovered_skane]
region_active = [total_active_sweden, total_active_stockholm, total_active_vgl, total_active_vgl]

X = np.arange(len(region_deaths))

plt.figure(dpi=120, figsize=(12, 8))
ax = plt.axes()
ax.set_facecolor('black')
ax.grid(linewidth=0.6, color='#8f8f8f')
plt.tick_params(axis='both', which='major', labelsize=10, color="white")

plt.ylabel("No. of cases", fontsize=15, alpha=0.7, color='#4bb4f2')
plt.xlabel("Region/Country", fontsize=12, alpha=0.9, color='#4bb4f2')

plt.tick_params(size=20, color='white')

plt.bar(X, region_active, width=0.25, label='re', edgecolor="pink")
plt.bar(X + 0.25, region_recovered, width=0.25, label='re', color='green', edgecolor="pink")
plt.bar(X + 0.5, region_deaths, width=0.25, label='re', color='red', edgecolor="pink")
plt.xticks([i + 0.25 for i in range(len(places))], places)

i = 1
j = 2000
for i in range(len(region_active)):
    plt.annotate(region_active[i], (-0.1 + i, region_active[i] + j), color="white")

for i in range(len(region_recovered)):
    plt.annotate(region_recovered[i], (0.22 + i, region_recovered[i] + j), color="white")

for i in range(len(region_deaths)):
    plt.annotate(region_deaths[i], (0.42 + i, region_deaths[i] + j), color="white")

plt.legend(['Confirmed', 'Recovered', 'Deceased'],
           fontsize=16)


plt.savefig("graph", dpi=200)