# Import the matplotlib.pyplot submodule and name it plt

import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots

fig, ax = plt.subplots()

# Call the show function to show the result

plt.show()

# edited/added

import pandas as pd

import calendar

austin_weather = pd.read_csv('austin_weather.csv')

austin_weather['MONTH'] = austin_weather['DATE']

seattle_weather = pd.read_csv('seattle_weather.csv')

seattle_weather = seattle_weather[seattle_weather['STATION'] == 'USW00094290']

seattle_weather['MONTH'] = seattle_weather['DATE']

# Import the matplotlib.pyplot submodule and name it plt

import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots

fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against MONTH

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH

ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Call the show function

plt.show()

# edited/added

fig, ax = plt.subplots()

# Plot Seattle data, setting data appearance

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"],

        color='b', marker='o', linestyle='--')

# Plot Austin data, setting data appearance

ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],

        color='r', marker='v', linestyle='--')

# Call show to display the resulting plot

plt.show()

# edited/added

fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label

ax.set_xlabel("Time (months)")

# Customize the y-axis label

ax.set_ylabel("Precipitation (inches)")

# Add the title

ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure

plt.show()

# Create a Figure and an array of subplots with 2 rows and 2 columns

fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation

ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures

ax[0, 1].plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations

ax[1, 0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot month and Austin temperatures

ax[1, 1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])

plt.show()

# Create a figure and an array of axes: 2 rows, 1 column with shared y axis

fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation in the top axes

ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')

ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color='b', linestyle='--')

ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color='b', linestyle='--')

# Plot Austin precipitation in the bottom axes

ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r')

ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color='r', linestyle='--')

ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color='r', linestyle='--')

plt.show()

# Import pandas

import pandas as pd

# Read the data from file using read_csv

climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot

ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label

ax.set_xlabel('Time')

# Set the y-axis label

ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure

plt.show()

import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax

fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"

seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot

ax.plot(seventies.index, seventies["co2"])

# Show the figure

plt.show()

import matplotlib.pyplot as plt

# Initalize a Figure and Axes

fig, ax = plt.subplots()

# Plot the CO2 variable in blue

ax.plot(climate_change.index, climate_change["co2"], color='blue')

# Create a twin Axes that shares the x-axis

ax2 = ax.twinx()

# Plot the relative temperature in red

ax2.plot(climate_change.index, climate_change["relative_temp"], color='red')

plt.show()

# Define a function called plot_timeseries

def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color

  axes.plot(x, y, color=color)

  # Set the x-axis label

  axes.set_xlabel(xlabel)

  # Set the y-axis label

  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis

  axes.tick_params('y', colors=color)

fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue

plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

# Create a twin Axes object that shares the x-axis

ax2 = ax.twinx()

# Plot the relative temperature data in red

plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', "Time (years)", "Relative temperature (Celsius)")

plt.show()

fig, ax = plt.subplots()

# Plot the relative temperature data

ax.plot(climate_change.index, climate_change['relative_temp'])

# Annotate the date at which temperatures exceeded 1 degree

ax.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1))

plt.show()

fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue

plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

# Create an Axes object that shares the x-axis

ax2 = ax.twinx()

# Plot the relative temperature data in red

plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', "Time (years)", "Relative temp (Celsius)")

# Annotate the point with relative temperature >1 degree

ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1), xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops={'arrowstyle':'->', 'color':'gray'})

plt.show()

# edited/added

import pandas as pd

import matplotlib.pyplot as plt

medals = pd.read_csv('medals_by_country_2016.csv', index_col = 0)

fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country

ax.bar(medals.index, medals["Gold"])

# Set the x-axis tick labels to the country names

ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label

ax.set_ylabel("Number of medals")

plt.show()

# edited/added

fig, ax = plt.subplots()

# Add bars for "Gold" with the label "Gold"

ax.bar(medals.index, medals["Gold"], label="Gold")

# Stack bars for "Silver" on top with label "Silver"

ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")

# Stack bars for "Bronze" on top of that with label "Bronze"

ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"] + medals["Silver"], label="Bronze")

# Display the legend

ax.legend()

plt.show()

# edited/added

import pandas as pd

import matplotlib.pyplot as plt

summer_2016_medals = pd.read_csv('summer2016.csv')

mens_rowing = summer_2016_medals[(summer_2016_medals['Sport'] == 'Rowing') & (summer_2016_medals['Sex'] == 'M')]

mens_gymnastics = summer_2016_medals[(summer_2016_medals['Sport'] == 'Gymnastics') & (summer_2016_medals['Sex'] == 'M')]

fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing

ax.hist(mens_rowing["Weight"])

# Compare to histogram of "Weight" for mens_gymnastics

ax.hist(mens_gymnastics["Weight"])

# Set the x-axis label to "Weight (kg)"

ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"

ax.set_ylabel("# of observations")

plt.show()

fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing

ax.hist(mens_rowing["Weight"], histtype='step', label="Rowing", bins=5)

# Compare to histogram of "Weight" for mens_gymnastics

ax.hist(mens_gymnastics["Weight"], histtype='step', label="Gymnastics", bins=5)

ax.set_xlabel("Weight (kg)")

ax.set_ylabel("# of observations")

# Add the legend and show the Figure

ax.legend()

plt.show()

fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std

ax.bar("Rowing", mens_rowing["Height"].mean(), yerr=mens_rowing["Height"].std())

# Add a bar for the gymnastics "Height" column mean/std

ax.bar("Gymnastics", mens_gymnastics["Height"].mean(), yerr=mens_gymnastics["Height"].std())

# Label the y-axis

ax.set_ylabel("Height (cm)")

plt.show()

fig, ax = plt.subplots()

# Add the Seattle temperature data in each month with standard deviation error bars

ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])

# Add the Austin temperature data in each month with standard deviation error bars

ax.errorbar(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])

# Set the y-axis label

ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()

fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames

ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])

# Add x-axis tick labels:

ax.set_xticklabels(["Rowing", "Gymnastics"])

# Add a y-axis label

ax.set_ylabel("Height (cm)")

plt.show()

fig, ax = plt.subplots()

# Add data: "co2" on x-axis, "relative_temp" on y-axis

ax.scatter(climate_change["co2"], climate_change["relative_temp"])

# Set the x-axis label to "CO2 (ppm)"

ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"

ax.set_ylabel("Relative temperature (C)")

plt.show()

fig, ax = plt.subplots()

# Add data: "co2", "relative_temp" as x-y, index as color

ax.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)

# Set the x-axis label to "CO2 (ppm)"

ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"

ax.set_ylabel("Relative temperature (C)")

plt.show()

# Use the "ggplot" style and create new Figure/Axes

plt.style.use('ggplot')

fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

plt.show()

# Use the "Solarize_Light2" style and create new Figure/Axes

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()

ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])

plt.show()

# edited/added

plt.style.use('default')

fig, ax = plt.subplots()

ax.bar(medals.index, medals['Gold'])

ax.set_xticklabels(medals.index, rotation=90)

ax.set_ylabel('Number of medals')

# Show the figure

plt.show()

# Save as a PNG file

fig.savefig('my_figure.png')

# Save as a PNG file with 300 dpi

fig.savefig('my_figure_300dpi.png', dpi=300)

# Set figure dimensions and save as a PNG

fig.set_size_inches([3, 5])

fig.savefig('figure_3_5.png')

# Set figure dimensions and save as a PNG

fig.set_size_inches([5, 3])

fig.savefig('figure_5_3.png')

# Extract the "Sport" column

sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column

sports = sports_column.unique()

# Print out the unique sports values

print(sports)

fig, ax = plt.subplots()

# Loop over the different sports branches

for sport in sports:

  # Extract the rows only for this sport

  sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]

  # Add a bar for the "Weight" mean with std y error bar

  ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())

ax.set_ylabel("Weight")

ax.set_xticklabels(sports, rotation=90)

# Save the figure to file

fig.savefig("sports_weights.png")
