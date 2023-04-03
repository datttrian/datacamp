# edited/added
library(tidyverse)
counties <- readRDS("counties.rds")

counties %>%
  # Select the columns
  select(state, county, population, poverty)

counties_selected <- counties %>%
  select(state, county, population, private_work, public_work, self_employed)

counties_selected %>%
  # Add a verb to sort in descending order of public_work
  arrange(desc(public_work))

counties_selected <- counties %>%
  select(state, county, population)

counties_selected %>%
  # Filter for counties with a population above 1000000
  filter(population > 1000000)

counties_selected <- counties %>%
  select(state, county, population)

counties_selected %>%
  # Filter for counties with a population above 1000000
  filter(state == "California",
         population > 1000000)

counties_selected <- counties %>%
  select(state, county, population, private_work, public_work, self_employed)

counties_selected %>%
  # Filter for Texas and more than 10000 people
  filter(state == "Texas",
         population > 10000) %>%
  # Sort in descending order of private_work
  arrange(desc(private_work))

counties_selected <- counties %>%
  select(state, county, population, public_work)

counties_selected %>%
  # Add a new column public_workers with the number of people employed in public work
  mutate(public_workers = public_work * population / 100)

counties_selected %>%
  mutate(public_workers = public_work * population / 100) %>%
  # Sort in descending order of the public_workers column
  arrange(desc(public_workers))

counties_selected <- counties %>%
  # Select the columns state, county, population, men, and women
  select(state, county, population, men, women)

counties_selected %>%
  # Calculate proportion_women as the fraction of the population made up of women
  mutate(proportion_women = women / population)

counties %>%
  # Select the five columns
  select(state, county, population, men, women) %>%
  # Add the proportion_men variable
  mutate(proportion_men = men / population) %>%
  # Filter for population of at least 10,000
  filter(population >= 10000) %>%
  # Arrange proportion of men in descending order
  arrange(desc(proportion_men))

# edited/added
counties_selected <- counties %>%
  select(county, region, state, population, citizens)

# Use count to find the number of counties in each region
counties_selected %>%
  count(region, sort = TRUE)

# Find number of counties per state, weighted by citizens, sorted in descending order
counties_selected %>%
  count(state, wt = citizens, sort = TRUE)

# edited/added
counties_selected <- counties %>%
  select(county, region, state, population, walk)

counties_selected %>%
  # Add population_walk containing the total number of people who walk to work
  mutate(population_walk = population * walk / 100) %>%
  # Count weighted by the new column, sort in descending order
  count(state, wt = population_walk, sort = TRUE)

# edited/added
counties_selected <- counties %>%
  select(county, population, income, unemployment)

counties_selected %>%
  # Summarize to find minimum population, maximum unemployment, and average income
  summarize(min_population = min(population),
            max_unemployment = max(unemployment),
            average_income = mean(income))

# edited/added
counties_selected <- counties %>%
  select(state, county, population, land_area)

counties_selected %>%
  # Group by state
  group_by(state) %>%
  # Find the total area and population
  summarize(total_area = sum(land_area),
            total_population = sum(population))

counties_selected %>%
  group_by(state) %>%
  summarize(total_area = sum(land_area),
            total_population = sum(population)) %>%
  # Add a density column
  mutate(density = total_population / total_area) %>%
  # Sort by density in descending order
  arrange(desc(density))

# edited/added
counties_selected <- counties %>%
  select(region, state, county, population)

counties_selected %>%
  # Group and summarize to find the total population
  group_by(region, state) %>%
  summarize(total_pop = sum(population))

counties_selected %>%
  # Group and summarize to find the total population
  group_by(region, state) %>%
  summarize(total_pop = sum(population)) %>%
  # Calculate the average_pop and median_pop columns
  summarize(average_pop = mean(total_pop),
            median_pop = median(total_pop))

# edited/added
counties_selected <- counties %>%
  select(region, state, county, metro, population, walk)

counties_selected %>%
  # Group by region
  group_by(region) %>%
  # Find the county with the highest percentage of people who walk to work
  slice_max(walk, n = 1)

# edited/added
counties_selected <- counties %>%
  select(region, state, county, population, income)

counties_selected %>%
  group_by(region, state) %>%
  # Calculate average income
  summarize(average_income = mean(income)) %>%
  # Find the lowest income state in each region
  slice_min(average_income, n = 1)

# edited/added
counties_selected <- counties %>%
  select(state, metro, population)

counties_selected %>%
  # Find the total population for each combination of state and metro
  group_by(state, metro) %>%
  summarize(total_pop = sum(population))

counties_selected %>%
  # Find the total population for each combination of state and metro
  group_by(state, metro) %>%
  summarize(total_pop = sum(population)) %>%
  # Extract the most populated row for each state
  slice_max(total_pop, n = 1)

counties_selected %>%
  # Find the total population for each combination of state and metro
  group_by(state, metro) %>%
  summarize(total_pop = sum(population)) %>%
  # Extract the most populated row for each state
  slice_max(total_pop, n = 1) %>%
  # Count the states with more people in Metro or Nonmetro areas
  ungroup() %>%
  count(metro)

# Glimpse the counties table
glimpse(counties)

counties %>%
  # Select state, county, population, and industry-related columns
  select(state, county, population, professional:production) %>%
  # Arrange service in descending order
  arrange(desc(service))

counties %>%
  # Select the state, county, population, and those ending with "work"
  select(state, county, population, ends_with("work")) %>%
  # Filter for counties that have at least 50% of people engaged in public work
  filter(public_work >= 50)

counties %>%
  # Count the number of counties in each state
  count(state)

counties %>%
  # Count the number of counties in each state
  count(state) %>%
  # Rename the n column to num_counties
  rename(num_counties = n)

counties %>%
  # Select state, county, and poverty as poverty_rate
  select(state, county, poverty_rate = poverty)

counties %>%
  # Keep the state, county, and populations columns, and add a density column
  transmute(state, county, population, density = population / land_area) %>%
  # Filter for counties with a population greater than one million
  filter(population > 1000000) %>%
  # Sort density in ascending order
  arrange(density)

# Change the name of the unemployment column
counties %>%
  rename(unemployment_rate = unemployment)

# Keep the state and county columns, and the columns containing poverty
counties %>%
  select(state, county, contains("poverty"))

# Calculate the fraction_women column without dropping the other columns
counties %>%
  mutate(fraction_women = women / population)

# Keep only the state, county, and employment_rate columns
counties %>%
  transmute(state, county, employment_rate = employed / population)

# edited/added
babynames <- readRDS("babynames.rds")

babynames %>%
  # Filter for the year 1990
  filter(year == 1990) %>%
  # Sort the number column in descending order
  arrange(desc(number))

babynames %>%
  # Find the most common name in each year
  group_by(year) %>%
  slice_max(number, n = 1)

selected_names <- babynames %>%
  # Filter for the names Steven, Thomas, and Matthew
  filter(name %in% c("Steven", "Thomas", "Matthew"))

selected_names <- babynames %>%
  # Filter for the names Steven, Thomas, and Matthew
  filter(name %in% c("Steven", "Thomas", "Matthew"))

# Plot the names using a different color for each name
ggplot(selected_names, aes(x = year, y = number, color = name)) +
  geom_line()

# Calculate the fraction of people born each year with the same name
babynames %>%
  group_by(year) %>%
  mutate(year_total = sum(number)) %>%
  ungroup() %>%
  mutate(fraction = number / year_total)

# Calculate the fraction of people born each year with the same name
babynames %>%
  group_by(year) %>%
  mutate(year_total = sum(number)) %>%
  ungroup() %>%
  mutate(fraction = number / year_total) %>%
  # Find the year each name is most common
  group_by(name) %>%
  slice_max(fraction, n = 1)

babynames %>%
  # Add columns name_total and name_max for each name
  group_by(name) %>%
  mutate(name_total = sum(number),
         name_max = max(number))

babynames %>%
  # Add columns name_total and name_max for each name
  group_by(name) %>%
  mutate(name_total = sum(number),
         name_max = max(number)) %>%
  # Ungroup the table
  ungroup() %>%
  # Add the fraction_max column containing the number by the name maximum
  mutate(fraction_max = number / name_max)

# edited/added
names_normalized <- babynames %>%
  group_by(name) %>%
  mutate(name_total = sum(number),
         name_max = max(number)) %>%
  ungroup() %>%
  mutate(fraction_max = number / name_max)

names_filtered <- names_normalized %>%
  # Filter for the names Steven, Thomas, and Matthew
  filter(name %in% c("Steven", "Thomas", "Matthew"))

# Visualize these names over time
ggplot(names_filtered, aes(x = year, y = fraction_max, color = name)) +
  geom_line()

# edited/added
babynames_fraction <- babynames %>%
  group_by(year) %>%
  mutate(year_total = sum(number)) %>%
  ungroup() %>%
  mutate(fraction = number / year_total)

babynames_fraction %>%
  # Arrange the data in order of name, then year
  arrange(name, year) %>%
  # Group the data by name
  group_by(name) %>%
  # Add a ratio column that contains the ratio of fraction between each year
  mutate(ratio = fraction / lag(fraction))

# edited/added
babynames_ratios_filtered <- babynames_fraction %>%
  arrange(name, year) %>%
  group_by(name) %>%
  mutate(ratio = fraction / lag(fraction)) %>%
  filter(fraction >= 0.00001)

babynames_ratios_filtered %>%
  # Extract the largest ratio from each name
  slice_max(ratio, n = 1) %>%
  # Sort the ratio column in descending order
  arrange(desc(ratio)) %>%
  # Filter for fractions greater than or equal to 0.001
  filter(fraction >= 0.001)
