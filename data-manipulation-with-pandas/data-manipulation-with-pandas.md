**Course Description**

pandas is the world’s most popular Python library, used for everything
from data manipulation to data analysis. In this course, you’ll learn
how to manipulate DataFrames, as you extract, filter, and transform
real-world datasets for analysis. Using pandas you’ll explore all the
core data science concepts. Using real-world data, including Walmart
sales figures and global temperature time series, you’ll learn how to
import, clean, calculate statistics, and create visualizations—using
pandas to add to the power of Python!

# Transforming DataFrames

Let’s master the pandas basics. Learn how to inspect DataFrames and
perform fundamental manipulations, including sorting rows, subsetting,
and adding new columns.

## Introducing DataFrames

### Inspecting a DataFrame

When you get a new DataFrame to work with, the first thing you need to
do is explore it and see what it contains. There are several useful
methods and attributes for this.

- `.head()` returns the first few rows (the “head” of the DataFrame).
- `.info()` shows information on each of the columns, such as the data
  type and number of missing values.
- `.shape` returns the number of rows and columns of the DataFrame.
- `.describe()` calculates a few summary statistics for each column.

`homelessness` is a DataFrame containing estimates of homelessness in
each U.S. state in 2018. The `individual` column is the number of
homeless individuals not part of a family with children. The
`family_members` column is the number of homeless individuals part of a
family with children. The `state_pop` column is the state’s total
population.

`pandas` is imported for you.

- Print the head of the `homelessness` DataFrame.
- Print information about the column types and missing values in
  `homelessness`.
- Print the number of rows and columns in `homelessness`.
- Print some summary statistics that describe the `homelessness`
  DataFrame.

``` python
# edited/added
import pandas as pd
homelessness = pd.read_csv('homelessness.csv', index_col=0)

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())
```

### Parts of a DataFrame

To better understand DataFrame objects, it’s useful to know that they
consist of three components, stored as attributes:

- `.values`: A two-dimensional NumPy array of values.
- `.columns`: An index of columns: the column names.
- `.index`: An index for the rows: either row numbers or row names.

You can usually think of indexes as a list of strings or numbers, though
the pandas `Index` data type allows for more sophisticated options.
(These will be covered later in the course.)

`homelessness` is available.

- Import `pandas` using the alias `pd`.
- Print a 2D NumPy array of the values in `homelessness`.
- Print the column names of `homelessness`.
- Print the index of `homelessness`.

``` python
# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)
```

## Sorting and subsetting

### Sorting rows

Finding interesting bits of data in a DataFrame is often easier if you
change the order of the rows. You can sort the rows by passing a column
name to `.sort_values()`.

In cases where rows have the same value (this is common if you sort on a
categorical variable), you may wish to break the ties by sorting on
another column. You can sort on multiple columns in this way by passing
a list of column names.

| Sort on …        | Syntax                                   |
|------------------|------------------------------------------|
| one column       | `df.sort_values("breed")`                |
| multiple columns | `df.sort_values(["breed", "weight_kg"])` |

By combining `.sort_values()` with `.head()`, you can answer questions
in the form, “What are the top cases where…?”.

`homelessness` is available and `pandas` is loaded as `pd`.

- Sort `homelessness` by the number of homeless individuals, from
  smallest to largest, and save this as `homelessness_ind`.
- Print the head of the sorted DataFrame.

<!-- -->

- Sort `homelessness` by the number of homeless `family_members` in
  descending order, and save this as `homelessness_fam`.
- Print the head of the sorted DataFrame.

<!-- -->

- Sort `homelessness` first by region (ascending), and then by number of
  family members (descending). Save this as `homelessness_reg_fam`.
- Print the head of the sorted DataFrame.

``` python
# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Print the top few rows
print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())
```

### Subsetting columns

When working with data, you may not need all of the variables in your
dataset. Square brackets (`[]`) can be used to select only the columns
that matter to you in an order that makes sense to you. To select only
`"col_a"` of the DataFrame `df`, use

    df["col_a"]

To select `"col_a"` and `"col_b"` of `df`, use

    df[["col_a", "col_b"]]

`homelessness` is available and `pandas` is loaded as `pd`.

- Create a DataFrame called `individuals` that contains only the
  `individuals` column of `homelessness`.
- Print the head of the result.

<!-- -->

- Create a DataFrame called `state_fam` that contains only the `state`
  and `family_members` columns of `homelessness`, in that order.
- Print the head of the result.

<!-- -->

- Create a DataFrame called `ind_state` that contains the `individuals`
  and `state` columns of `homelessness`, in that order.
- Print the head of the result.

``` python
# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

# Print the head of the result
print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())
```

### Subsetting rows

A large part of data science is about finding which bits of your dataset
are interesting. One of the simplest techniques for this is to find a
subset of rows that match some criteria. This is sometimes known as
*filtering rows* or *selecting rows*.

There are many ways to subset a DataFrame, perhaps the most common is to
use relational operators to return `True` or `False` for each row, then
pass that inside square brackets.

    dogs[dogs["height_cm"] > 60]
    dogs[dogs["color"] == "tan"]

You can filter for multiple conditions at once by using the “bitwise
and” operator, `&`.

    dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]

`homelessness` is available and `pandas` is loaded as `pd`.

Filter `homelessness` for cases where the number of individuals is
greater than ten thousand, assigning to `ind_gt_10k`. *View the printed
result.*

Filter `homelessness` for cases where the USA Census region is
`"Mountain"`, assigning to `mountain_reg`. *View the printed result.*

Filter `homelessness` for cases where the number of `family_members` is
less than one thousand and the `region` is “Pacific”, assigning to
`fam_lt_1k_pac`. *View the printed result.*

``` python
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]

# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]

# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)
```

### Subsetting rows by categorical variables

Subsetting data based on a categorical variable often involves using the
“or” operator (`|`) to select rows from multiple categories. This can
get tedious when you want all states in one of three different regions,
for example. Instead, use the `.isin()` method, which will allow you to
tackle this problem by writing one condition instead of three separate
ones.

    colors = ["brown", "black", "tan"]
    condition = dogs["color"].isin(colors)
    dogs[condition]

`homelessness` is available and `pandas` is loaded as `pd`.

Filter `homelessness` for cases where the USA census region is “South
Atlantic” or it is “Mid-Atlantic”, assigning to `south_mid_atlantic`.
*View the printed result.*

Filter `homelessness` for cases where the USA census `state` is in the
list of Mojave states, `canu`, assigning to `mojave_homelessness`. *View
the printed result.*

``` python
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]

# See the result
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)
```

## New columns

### Adding new columns

You aren’t stuck with just the data you are given. Instead, you can add
new columns to a DataFrame. This has many names, such as *transforming*,
*mutating*, and *feature engineering*.

You can create new columns from scratch, but it is also common to derive
them from other columns, for example, by adding columns together or by
changing their units.

`homelessness` is available and `pandas` is loaded as `pd`.

- Add a new column to `homelessness`, named `total`, containing the sum
  of the `individuals` and `family_members` columns.
- Add another column to `homelessness`, named `p_individuals`,
  containing the proportion of homeless people in each state who are
  individuals.

``` python
# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of total that are individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]

# See the result
print(homelessness)
```

### Combo-attack!

You’ve seen the four most common types of data manipulation: sorting
rows, subsetting columns, subsetting rows, and adding new columns. In a
real-life data analysis, you can mix and match these four manipulations
to answer a multitude of questions.

In this exercise, you’ll answer the question, “Which state has the
highest number of homeless individuals per 10,000 people in the state?”
Combine your new `pandas` skills to find out.

- Add a column to `homelessness`, `indiv_per_10k`, containing the number
  of homeless individuals per ten thousand people in each state.
- Subset rows where `indiv_per_10k` is higher than `20`, assigning to
  `high_homelessness`.
- Sort `high_homelessness` by descending `indiv_per_10k`, assigning to
  `high_homelessness_srt`.
- Select only the `state` and `indiv_per_10k` columns of
  `high_homelessness_srt` and save as `result`. *Look at the `result`.*

``` python
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)
```

# Aggregating DataFrames

In this chapter, you’ll calculate summary statistics on DataFrame
columns, and master grouped summary statistics and pivot tables.

## Summary statistics

### Mean and median

Summary statistics are exactly what they sound like - they summarize
many numbers in one statistic. For example, mean, median, minimum,
maximum, and standard deviation are summary statistics. Calculating
summary statistics allows you to get a better sense of your data, even
if there’s a lot of it.

`sales` is available and `pandas` is loaded as `pd`.

- Explore your new DataFrame first by printing the first few rows of the
  `sales` DataFrame.
- Print information about the columns in `sales`.
- Print the mean of the `weekly_sales` column.
- Print the median of the `weekly_sales` column.

``` python
# edited/added
sales = pd.read_csv('sales_subset.csv', index_col=0)

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())
```

### Summarizing dates

Summary statistics can also be calculated on date columns that have
values with the data type `datetime64`. Some summary statistics — like
mean — don’t make a ton of sense on dates, but others are super helpful,
for example, minimum and maximum, which allow you to see what time range
your data covers.

`sales` is available and `pandas` is loaded as `pd`.

- Print the maximum of the `date` column.
- Print the minimum of the `date` column.

``` python
# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())
```

### Efficient summaries

While pandas and NumPy have tons of functions, sometimes, you may need a
different function to summarize your data.

The `.agg()` method allows you to apply your own custom functions to a
DataFrame, as well as apply functions to more than one column of a
DataFrame at once, making your aggregations super-efficient. For
example,

    df['column'].agg(function)

In the custom function for this exercise, “IQR” is short for
inter-quartile range, which is the 75th percentile minus the 25th
percentile. It’s an alternative to standard deviation that is helpful if
your data contains outliers.

`sales` is available and `pandas` is loaded as `pd`.

- Use the custom `iqr` function defined for you along with `.agg()` to
  print the IQR of the `temperature_c` column of `sales`.

<!-- -->

- Update the column selection to use the custom `iqr` function with
  `.agg()` to print the IQR of `temperature_c`, `fuel_price_usd_per_l`,
  and `unemployment`, in that order.

<!-- -->

- Update the aggregation functions called by `.agg()`: include `iqr` and
  `np.median` in that order.

``` python
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))

# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))
```

### Cumulative statistics

Cumulative statistics can also be helpful in tracking summary statistics
over time. In this exercise, you’ll calculate the cumulative sum and
cumulative max of a department’s weekly sales, which will allow you to
identify what the total sales were so far as well as what the highest
weekly sales were so far.

A DataFrame called `sales_1_1` has been created for you, which contains
the sales data for department 1 of store 1. `pandas` is loaded as `pd`.

- Sort the rows of `sales_1_1` by the `date` column in ascending order.
- Get the cumulative sum of `weekly_sales` and add it as a new column of
  `sales_1_1` called `cum_weekly_sales`.
- Get the cumulative maximum of `weekly_sales`, and add it as a column
  called `cum_max_sales`.
- Print the `date`, `weekly_sales`, `cum_weekly_sales`, and
  `cum_max_sales` columns.

``` python
# edited/added
sales_1_1 = sales[(sales["department"] == 1) & (sales["store"] == 1)]

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date")

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
```

## Counting

### Dropping duplicates

Removing duplicates is an essential skill to get accurate counts because
often, you don’t want to count the same thing multiple times. In this
exercise, you’ll create some new DataFrames using unique values from
`sales`.

`sales` is available and `pandas` is imported as `pd`.

- Remove rows of `sales` with duplicate pairs of `store` and `type` and
  save as `store_types` and print the head.
- Remove rows of `sales` with duplicate pairs of `store` and
  `department` and save as `store_depts` and print the head.
- Subset the rows that are holiday weeks using the `is_holiday` column,
  and drop the duplicate `date`s, saving as `holiday_dates`.
- Select the `date` column of `holiday_dates`, and print.

``` python
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")

# Print date col of holiday_dates
print(holiday_dates["date"])
```

### Counting categorical variables

Counting is a great way to get an overview of your data and to spot
curiosities that you might not notice otherwise. In this exercise,
you’ll count the number of each type of store and the number of each
department number using the DataFrames you created in the previous
exercise:

    # Drop duplicate store/type combinations
    store_types = sales.drop_duplicates(subset=["store", "type"])

    # Drop duplicate store/department combinations
    store_depts = sales.drop_duplicates(subset=["store", "department"])

The `store_types` and `store_depts` DataFrames you created in the last
exercise are available, and `pandas` is imported as `pd`.

- Count the number of stores of each store `type` in `store_types`.
- Count the proportion of stores of each store `type` in `store_types`.
- Count the number of different `department`s in `store_depts`, sorting
  the counts in descending order.
- Count the proportion of different `department`s in `store_depts`,
  sorting the proportions in descending order.

``` python
# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)
```

## Grouped summary statistics

### What percent of sales occurred at each store type?

While `.groupby()` is useful, you can calculate grouped summary
statistics without it.

Walmart distinguishes three types of stores: “supercenters,” “discount
stores,” and “neighborhood markets,” encoded in this dataset as type
“A,” “B,” and “C.” In this exercise, you’ll calculate the total sales
made at each store type, without using `.groupby()`. You can then use
these numbers to see what proportion of Walmart’s total sales were made
at each type.

`sales` is available and `pandas` is imported as `pd`.

- Calculate the total `weekly_sales` over the whole dataset.
- Subset for `type` `"A"` stores, and calculate their total weekly
  sales.
- Do the same for `type` `"B"` and `type` `"C"` stores.
- Combine the A/B/C results into a list, and divide by `sales_all` to
  get the proportion of sales by type.

``` python
# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)
```

### Calculations with .groupby()

The `.groupby()` method makes life much easier. In this exercise, you’ll
perform the same calculations as last time, except you’ll use the
`.groupby()` method. You’ll also perform calculations on data grouped by
two variables to see if sales differ by store type depending on if it’s
a holiday week or not.

`sales` is available and `pandas` is loaded as `pd`.

- Group `sales` by `"type"`, take the sum of `"weekly_sales"`, and store
  as `sales_by_type`.
- Calculate the proportion of sales at each store type by dividing by
  the sum of `sales_by_type`. Assign to `sales_propn_by_type`.
- Group `sales` by `"type"` and “`is_holiday`”, take the sum of
  `weekly_sales`, and store as `sales_by_type_is_holiday`.

``` python
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)
```

### Multiple grouped summaries

Earlier in this chapter, you saw that the `.agg()` method is useful to
compute multiple statistics on multiple variables. It also works with
grouped data. NumPy, which is imported as `np`, has many different
summary statistics functions, including: `np.min`, `np.max`, `np.mean`,
and `np.median`.

`sales` is available and `pandas` is imported as `pd`.

- Import `numpy` with the alias `np`.
- Get the min, max, mean, and median of `weekly_sales` for each store
  type using `.groupby()` and `.agg()`. Store this as `sales_stats`.
  Make sure to use `numpy` functions!
- Get the min, max, mean, and median of `unemployment` and
  `fuel_price_usd_per_l` for each store type. Store this as
  `unemp_fuel_stats`.

``` python
# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)
```

## Pivot tables

### Pivoting on one variable

Pivot tables are the standard way of aggregating data in spreadsheets.

In pandas, pivot tables are essentially another way of performing
grouped calculations. That is, the `.pivot_table()` method is an
alternative to `.groupby()`.

In this exercise, you’ll perform calculations using `.pivot_table()` to
replicate the calculations you performed in the last lesson using
`.groupby()`.

`sales` is available and `pandas` is imported as `pd`.

- Get the mean `weekly_sales` by `type` using `.pivot_table()` and store
  as `mean_sales_by_type`.

<!-- -->

- Get the mean and median (using NumPy functions) of `weekly_sales` by
  `type` using `.pivot_table()` and store as `mean_med_sales_by_type`.

<!-- -->

- Get the mean of `weekly_sales` by `type` and `is_holiday` using
  `.pivot_table()` and store as `mean_sales_by_type_holiday`.

``` python
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table("weekly_sales", "type", aggfunc = [np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table("weekly_sales", "type", "is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)
```

### Fill in missing values and sum values with pivot tables

The `.pivot_table()` method has several useful arguments, including
`fill_value` and `margins`.

- `fill_value` replaces missing values with a real value (known as
  *imputation*). What to replace missing values with is a topic big
  enough to have its own course ([Dealing with Missing Data in
  Python](https://www.datacamp.com/courses/dealing-with-missing-data-in-python)),
  but the simplest thing to do is to substitute a dummy value.
- `margins` is a shortcut for when you pivoted by two variables, but
  also wanted to pivot by each of those variables separately: it gives
  the row and column totals of the pivot table contents.

In this exercise, you’ll practice using these arguments to up your pivot
table skills, which will help you crunch numbers more efficiently!

`sales` is available and `pandas` is imported as `pd`.

- Print the mean `weekly_sales` by `department` and `type`, filling in
  any missing values with `0`.

<!-- -->

- Print the mean `weekly_sales` by `department` and `type`, filling in
  any missing values with `0` and summing all rows and columns.

``` python
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins =True))
```

# Slicing and Indexing DataFrames

Indexes are supercharged row and column names. Learn how they can be
combined with slicing for powerful DataFrame subsetting.

## Explicit indexes

### Setting and removing indexes

pandas allows you to designate columns as an *index*. This enables
cleaner code when taking subsets (as well as providing more efficient
lookup under some circumstances).

In this chapter, you’ll be exploring `temperatures`, a DataFrame of
average temperatures in cities around the world. `pandas` is loaded as
`pd`.

- *Look at `temperatures`*.
- Set the index of `temperatures` to `"city"`, assigning to
  `temperatures_ind`.
- *Look at `temperatures_ind`. How is it different from `temperatures`?*
- Reset the index of `temperatures_ind`, keeping its contents.
- Reset the index of `temperatures_ind`, dropping its contents.

``` python
# edited/added
temperatures = pd.read_csv('temperatures.csv', index_col=0)
temperatures['date'] =  pd.to_datetime(temperatures['date'], infer_datetime_format=True)

# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))
```

### Subsetting with .loc\[\]

The killer feature for indexes is `.loc[]`: a subsetting method that
accepts index values. When you pass it a single argument, it will take a
subset of rows.

The code for subsetting using `.loc[]` can be easier to read than
standard square bracket subsetting, which can make your code less
burdensome to maintain.

`pandas` is loaded as `pd`. `temperatures` and `temperatures_ind` are
available; the latter is indexed by `city`.

- Create a list called `cities` that contains “Moscow” and “Saint
  Petersburg”.
- Use `[]` subsetting to filter `temperatures` for rows where the `city`
  column takes a value in the `cities` list.
- Use `.loc[]` subsetting to filter `temperatures_ind` for rows where
  the city is in the `cities` list.

``` python
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])
```

### Setting multi-level indexes

Indexes can also be made out of multiple columns, forming a *multi-level
index* (sometimes called a *hierarchical index*). There is a trade-off
to using these.

The benefit is that multi-level indexes make it more natural to reason
about nested categorical variables. For example, in a clinical trial,
you might have control and treatment groups. Then each test subject
belongs to one or another group, and we can say that a test subject is
nested inside the treatment group. Similarly, in the temperature
dataset, the city is located in the country, so we can say a city is
nested inside the country.

The main downside is that the code for manipulating indexes is different
from the code for manipulating columns, so you have to learn two
syntaxes and keep track of how your data is represented.

`pandas` is loaded as `pd`. `temperatures` is available.

- Set the index of `temperatures` to the `"country"` and `"city"`
  columns, and assign this to `temperatures_ind`.
- Specify two country/city pairs to keep: `"Brazil"`/`"Rio De Janeiro"`
  and `"Pakistan"`/`"Lahore"`, assigning to `rows_to_keep`.
- Print and subset `temperatures_ind` for `rows_to_keep` using `.loc[]`.

``` python
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])
```

### Sorting by index values

Previously, you changed the order of the rows in a DataFrame by calling
`.sort_values()`. It’s also useful to be able to sort by elements in the
index. For this, you need to use `.sort_index()`.

`pandas` is loaded as `pd`. `temperatures_ind` has a multi-level index
of `country` and `city`, and is available.

- Sort `temperatures_ind` by the index values.
- Sort `temperatures_ind` by the index values at the `"city"` level.
- Sort `temperatures_ind` by ascending country then descending city.

``` python
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending = [True, False]))
```

## Slicing and subsetting with .loc and .iloc

### Slicing index values

Slicing lets you select consecutive elements of an object using
`first:last` syntax. DataFrames can be sliced by index values or by
row/column number; we’ll start with the first case. This involves
slicing inside the `.loc[]` method.

Compared to slicing lists, there are a few things to remember.

- You can only slice an index if the index is sorted (using
  `.sort_index()`).
- To slice at the outer level, `first` and `last` can be strings.
- To slice at inner levels, `first` and `last` should be tuples.
- If you pass a single slice to `.loc[]`, it will slice the rows.

`pandas` is loaded as `pd`. `temperatures_ind` has country and city in
the index, and is available.

- Sort the index of `temperatures_ind`.
- Use slicing with `.loc[]` to get these subsets:
  - from Pakistan to Russia.
  - from Lahore to Moscow. (*This will return nonsense.*)
  - from Pakistan, Lahore to Russia, Moscow.

``` python
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])
```

### Slicing in both directions

You’ve seen slicing DataFrames by rows and by columns, but since
DataFrames are two-dimensional objects, it is often natural to slice
both dimensions at once. That is, by passing two arguments to `.loc[]`,
you can subset by rows and columns in one go.

`pandas` is loaded as `pd`. `temperatures_srt` is indexed by country and
city, has a sorted index, and is available.

- Use `.loc[]` slicing to subset rows from India, Hyderabad to Iraq,
  Baghdad.
- Use `.loc[]` slicing to subset columns from `date` to `avg_temp_c`.
- Slice in both directions at once from Hyderabad to Baghdad, and `date`
  to `avg_temp_c`.

``` python
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"), "date":"avg_temp_c"])
```

### Slicing time series

Slicing is particularly useful for time series since it’s a common thing
to want to filter for data within a date range. Add the `date` column to
the index, then use `.loc[]` to perform the subsetting. The important
thing to remember is to keep your dates in ISO 8601 format, that is,
`"yyyy-mm-dd"` for year-month-day, `"yyyy-mm"` for year-month, and
`"yyyy"` for year.

Recall from Chapter 1 that you can combine multiple Boolean conditions
using logical operators, such as `&`. To do so in one line of code,
you’ll need to add parentheses `()` around each condition.

`pandas` is loaded as `pd` and `temperatures`, with no index, is
available.

- Use Boolean conditions, not `.isin()` or `.loc[]`, and the full date
  `"yyyy-mm-dd"`, to subset `temperatures` for rows in 2010 and 2011 and
  print the results.
- Set the index of `temperatures` to the `date` column and sort it.
- Use `.loc[]` to subset `temperatures_ind` for rows in 2010 and 2011.
- Use `.loc[]` to subset `temperatures_ind` for rows from Aug 2010 to
  Feb 2011.

``` python
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])
```

### Subsetting by row/column number

The most common ways to subset rows are the ways we’ve previously
discussed: using a Boolean condition or by index labels. However, it is
also occasionally useful to pass row numbers.

This is done using `.iloc[]`, and like `.loc[]`, it can take two
arguments to let you subset by rows and columns.

`pandas` is loaded as `pd`. `temperatures` (without an index) is
available.

Use `.iloc[]` on `temperatures` to take subsets.

- Get the 23rd row, 2nd column (index positions 22 and 1).
- Get the first 5 rows (index positions 0 to 5).
- Get all rows, columns 3 and 4 (index positions 2 to 4).
- Get the first 5 rows, columns 3 and 4.

``` python
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])
```

## Working with pivot tables

### Pivot temperature by city and year

It’s interesting to see how temperatures for each city change over
time—looking at every month results in a big table, which can be tricky
to reason about. Instead, let’s look at how temperatures change by year.

You can access the components of a date (year, month and day) using code
of the form `dataframe["column"].dt.component`. For example, the month
component is `dataframe["column"].dt.month`, and the year component is
`dataframe["column"].dt.year`.

Once you have the year column, you can create a pivot table with the
data aggregated by city and year, which you’ll explore in the coming
exercises.

`pandas` is loaded as `pd`. `temperatures` is available.

- Add a `year` column to `temperatures`, from the `year` component of
  the `date` column.
- Make a pivot table of the `avg_temp_c` column, with `country` and
  `city` as rows, and `year` as columns. Assign to
  `temp_by_country_city_vs_year`, and *look at the result*.

``` python
# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")

# See the result
print(temp_by_country_city_vs_year)
```

### Subsetting pivot tables

A pivot table is just a DataFrame with sorted indexes, so the techniques
you have learned already can be used to subset them. In particular, the
`.loc[]` + slicing combination is often helpful.

`pandas` is loaded as `pd`. `temp_by_country_city_vs_year` is available.

Use `.loc[]` on `temp_by_country_city_vs_year` to take subsets.

- From Egypt to India.
- From Egypt, Cairo to India, Delhi.
- From Egypt, Cairo to India, Delhi, and 2005 to 2010.

``` python
# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"]
```

### Calculating on a pivot table

Pivot tables are filled with summary statistics, but they are only a
first step to finding something insightful. Often you’ll need to perform
further calculations on them. A common thing to do is to find the rows
or columns where the highest or lowest value occurs.

Recall from Chapter 1 that you can easily subset a Series or DataFrame
to find rows of interest using a logical condition inside of square
brackets. For example: `series[series > value]`.

`pandas` is loaded as `pd` and the DataFrame
`temp_by_country_city_vs_year` is available.

- Calculate the mean temperature for each year, assigning to
  `mean_temp_by_year`.
- Filter `mean_temp_by_year` for the year that had the highest mean
  temperature.
- Calculate the mean temperature for each city (across columns),
  assigning to `mean_temp_by_city`.
- Filter `mean_temp_by_city` for the city that had the lowest mean
  temperature.

``` python
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
```

# Creating and Visualizing DataFrames

Learn to visualize the contents of your DataFrames, handle missing data
values, and import data from and export data to CSV files.

## Visualizing your data

### Which avocado size is most popular?

Avocados are increasingly popular and delicious in guacamole and on
toast. The Hass Avocado Board keeps track of avocado supply and demand
across the USA, including the sales of three different sizes of avocado.
In this exercise, you’ll use a bar plot to figure out which size is the
most popular.

Bar plots are great for revealing relationships between categorical
(size) and numeric (number sold) variables, but you’ll often have to
manipulate your data first in order to get the numbers you need for
plotting.

`pandas` has been imported as `pd`, and `avocados` is available.

- Print the head of the `avocados` dataset. *What columns are
  available?*
- For each avocado size group, calculate the total number sold, storing
  as `nb_sold_by_size`.
- Create a bar plot of the number of avocados sold by size.
- Show the plot.

``` python
# edited/added
import urllib.request
import pickle
avocados = pd.read_pickle("avoplotto.pkl")

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")

# Show the plot
plt.show()
```

### Changes in sales over time

Line plots are designed to visualize the relationship between two
numeric variables, where each data values is connected to the next one.
They are especially useful for visualizing the change in a number over
time since each time point is naturally connected to the next time
point. In this exercise, you’ll visualize the change in avocado sales
over three years.

`pandas` has been imported as `pd`, and `avocados` is available.

- Get the total number of avocados sold on each date. *The DataFrame has
  two rows for each date—one for organic, and one for conventional*.
  Save this as `nb_sold_by_date`.
- Create a line plot of the number of avocados sold.
- Show the plot.

``` python
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind="line")

# Show the plot
plt.show()
```

### Avocado supply and demand

Scatter plots are ideal for visualizing relationships between numerical
variables. In this exercise, you’ll compare the number of avocados sold
to average price and see if they’re at all related. If they’re related,
you may be able to use one number to predict the other.

`matplotlib.pyplot` has been imported as `plt`, `pandas` has been
imported as `pd`, and `avocados` is available.

- Create a scatter plot with `nb_sold` on the x-axis and `avg_price` on
  the y-axis. Title it `"Number of avocados sold vs. average price"`.
- Show the plot.

``` python
# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()
```

### Price of conventional vs. organic avocados

Creating multiple plots for different subsets of data allows you to
compare groups. In this exercise, you’ll create multiple histograms to
compare the prices of conventional and organic avocados.

`matplotlib.pyplot` has been imported as `plt` and `pandas` has been
imported as `pd`.

- Subset `avocados` for the conventional type, and the average price
  column. Create a histogram.
- Create a histogram of `avg_price` for organic type avocados.
- Add a legend to your plot, with the names “conventional” and
  “organic”.
- Show your plot.
- Modify your code to adjust the transparency of both histograms to
  `0.5` to see how much overlap there is between the two distributions.
- Modify your code to use 20 bins in both histograms.

``` python
# Histogram of conventional avg_price 
avocados[avocados["type"] == "conventional"]["avg_price"].hist()

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

# Modify histogram transparency to 0.5 
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(bins=20, alpha=0.5)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(bins= 20, alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()
```

## Missing values

### Finding missing values

Missing values are everywhere, and you don’t want them interfering with
your work. Some functions ignore missing data by default, but that’s not
always the behavior you might want. Some functions can’t handle missing
values at all, so these values need to be taken care of before you can
use them. If you don’t know where your missing values are, or if they
exist, you could make mistakes in your analysis. In this exercise,
you’ll determine if there are missing values in the dataset, and if so,
how many.

`pandas` has been imported as `pd` and `avocados_2016`, a subset of
`avocados` that contains only sales from 2016, is available.

- Print a DataFrame that shows whether each value in `avocados_2016` is
  missing or not.
- Print a summary that shows whether *any* value in each column is
  missing or not.
- Create a bar plot of the total number of missing values in each
  column.

``` python
# edited/added
avocados_2016 = pd.read_csv('avocados_2016.csv')
cols_with_missing = ['small_sold', 'large_sold', 'xl_sold']

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()
```

### Removing missing values

Now that you know there are some missing values in your DataFrame, you
have a few options to deal with them. One way is to remove them from the
dataset completely. In this exercise, you’ll remove missing values by
removing all rows that contain missing values.

`pandas` has been imported as `pd` and `avocados_2016` is available.

- Remove the rows of `avocados_2016` that contain missing values and
  store the remaining rows in `avocados_complete`.
- Verify that all missing values have been removed from
  `avocados_complete`. Calculate each column that has NAs and print.

``` python
# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())
```

### Replacing missing values

Another way of handling missing values is to replace them all with the
same value. For numerical variables, one option is to replace values
with 0— you’ll do this here. However, when you replace missing values,
you make assumptions about what a missing value means. In this case, you
will assume that a missing number sold means that no sales for that
avocado type were made that week.

In this exercise, you’ll see how replacing missing values can affect the
distribution of a variable using histograms. You can plot histograms for
multiple variables at a time as follows:

    dogs[["height_cm", "weight_kg"]].hist()

`pandas` has been imported as `pd` and `matplotlib.pyplot` has been
imported as `plt`. The `avocados_2016` dataset is available.

- A list has been created, `cols_with_missing`, containing the names of
  columns with missing values: `"small_sold"`, `"large_sold"`, and
  `"xl_sold"`.
- Create a histogram of those columns.
- Show the plot.

``` python
# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()
```

## Creating DataFrames

### List of dictionaries

You recently got some new avocado data from 2019 that you’d like to put
in a DataFrame using the list of dictionaries method. Remember that with
this method, you go through the data row by row.

| date         | small_sold | large_sold |
|--------------|------------|------------|
| “2019-11-03” | 10376832   | 7835071    |
| “2019-11-10” | 10717154   | 8561348    |

`pandas` as `pd` is imported.

- Create a list of dictionaries with the new data called
  `avocados_list`.
- Convert the list into a DataFrame called `avocados_2019`.
- Print your new DataFrame.

``` python
# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)
```

### Dictionary of lists

Some more data just came in! This time, you’ll use the dictionary of
lists method, parsing the data column by column.

| date         | small_sold | large_sold |
|--------------|------------|------------|
| “2019-11-17” | 10859987   | 7674135    |
| “2019-12-01” | 9291631    | 6238096    |

`pandas` as `pd` is imported.

- Create a dictionary of lists with the new data called `avocados_dict`.
- Convert the dictionary to a DataFrame called `avocados_2019`.
- Print your new DataFrame.

``` python
# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)
```

## Reading and writing CSVs

### CSV to DataFrame

You work for an airline, and your manager has asked you to do a
competitive analysis and see how often passengers flying on other
airlines are involuntarily bumped from their flights. You got a CSV file
(`airline_bumping.csv`) from the Department of Transportation containing
data on passengers that were involuntarily denied boarding in 2016 and
2017, but it doesn’t have the exact numbers you want. In order to figure
this out, you’ll need to get the CSV into a pandas DataFrame and do some
manipulation!

`pandas` is imported for you as `pd`. `"airline_bumping.csv"` is in your
working directory.

- Read the CSV file `"airline_bumping.csv"` and store it as a DataFrame
  called `airline_bumping`.
- Print the first few rows of `airline_bumping`.
- For each airline group, select the `nb_bumped`, and `total_passengers`
  columns, and calculate the sum (for both years). Store this as
  `airline_totals`.
- Create a new column of `airline_totals` called `bumps_per_10k`, which
  is the number of passengers bumped per 10,000 passengers in 2016 and
  2017.
- Print `airline_totals` to see the results of your manipulations.

``` python
# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv('airline_bumping.csv') # edited/added

# Take a look at the DataFrame
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)

# Print airline_totals
print(airline_totals)
```

### DataFrame to CSV

You’re almost there! To make things easier to read, you’ll need to sort
the data and export it to CSV so that your colleagues can read it.

`pandas` as `pd` has been imported for you.

- Sort `airline_totals` by the values of `bumps_per_10k` from highest to
  lowest, storing as `airline_totals_sorted`.
- Print your sorted DataFrame.
- Save the sorted DataFrame as a CSV called
  `"airline_totals_sorted.csv"`.

``` python
# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")
```

## Wrap-up

### Wrap-up

Congratulations! You’ve now covered the basics of using pandas.

### Recap

In chapter 1, you saw how to subset and sort DataFrames and how to add
new columns. In chapter 2, you saw several methods for aggregating and
grouping data to calculate summary statistics. In chapter 3, you saw how
using indexing and slicing allows for simpler subsetting. In chapter 4,
you saw how to visualize a DataFrame, and how to read data from and
write data to CSV files.

### More to learn

I hope you are convinced that pandas is a powerful tool to analyze
tabular data. In fact, pandas is so powerful that there are many
features that we didn’t get around to discussing in this course. To
begin with, everything in this course involved a single DataFrame, but
sometimes you need to join or “merge” several DataFrames together.
Reading from CSV files barely scratches the surface of the options for
importing data into pandas. You can also perform very sophisticated
exploratory data analysis using pandas.

### Congratulations!

Congratulations, and have fun learning!
