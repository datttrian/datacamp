**Course Description**

Statistics is the study of how to collect, analyze, and draw conclusions
from data. It’s a hugely valuable tool that you can use to bring the
future into focus and infer the answer to tons of questions. For
example, what is the likelihood of someone purchasing your product, how
many calls will your support team receive, and how many jeans sizes
should you manufacture to fit 95% of the population? In this course,
you’ll use sales data to discover how to answer questions like these as
you grow your statistical skills and learn how to calculate averages,
use scatterplots to show the relationship between numeric values, and
calculate correlation. You’ll also tackle probability, the backbone of
statistical reasoning, and learn how to conduct a well-designed study to
draw your own conclusions from data.

# Summary Statistics

Summary statistics gives you the tools you need to boil down massive
datasets to reveal the highlights. In this chapter, you’ll explore
summary statistics including mean, median, and standard deviation, and
learn how to accurately interpret them. You’ll also develop your
critical thinking skills, allowing you to choose the best summary
statistics for your data.

## What is statistics?

### Descriptive and inferential statistics

Statistics can be used to answer lots of different types of questions,
but being able to identify which type of statistics is needed is
essential to drawing accurate conclusions. In this exercise, you’ll
sharpen your skills by identifying which type is needed to answer each
question.

- Identify which questions can be answered with descriptive statistics
  and which questions can be answered with inferential statistics.

##### Descriptive

- Given data on all 100,000 people who viewed an ad, what percent of
  people clicked on it?
- Given data on every customer service request made, what’s the average
  time it took to respond?

##### Inferential

- After interviewing 100 customers, what percent of *all* your customers
  are satisfied with your product?
- Given data on 20 fish caught in a lake, what’s the average weight of
  all fish in the lake?

### Data type classification

In the video, you learned about two main types of data: numeric and
categorical. Numeric variables can be classified as either discrete or
continuous, and categorical variables can be classified as either
nominal or ordinal. These characteristics of a variable determine which
ways of summarizing your data will work best.

- Map each variable to its data type by dragging and dropping.

##### Continuous numeric

- Air temperature
- Kilowatts of electricity used

##### Discrete numeric

- Number of items in stock Number of clicks on an ad
- Number of DataCamp courses taken

##### Categorical

- Brand of a product
- Postal code

## Measures of center

### Mean and median

In this chapter, you’ll be working with the [2018 Food Carbon Footprint
Index](https://www.nu3.de/blogs/nutrition/food-carbon-footprint-index-2018)
from nu3. The `food_consumption` dataset contains information about the
kilograms of food consumed per person per year in each country in each
food category (`consumption`) as well as information about the carbon
footprint of that food category (`co2_emissions`) measured in kilograms
of carbon dioxide, or CO\\\_2\\, per person per year in each country.

In this exercise, you’ll compute measures of center to compare food
consumption in the US and Belgium using your `dplyr` skills.

`dplyr` is loaded for you and `food_consumption` is available.

- Create two data frames: one that holds the rows of `food_consumption`
  for `"Belgium"` and the another that holds rows for `"USA"`. Call
  these `belgium_consumption` and `usa_consumption`.
- Calculate the mean and median of kilograms of food consumed per person
  per year for both countries.

<!-- -->

- Filter `food_consumption` for rows with data about Belgium and the
  USA.
- Group the filtered data by `country`.
- Calculate the mean and median of the kilograms of food consumed per
  person per year in each country. Call these columns `mean_consumption`
  and `median_consumption`.

``` r
# edited/added
library(tidyverse)
food_consumption <- readRDS('food_consumption.rds')

# Filter for Belgium
belgium_consumption <- food_consumption %>%
  filter(country == "Belgium")

# Filter for USA
usa_consumption <- food_consumption %>%
  filter(country == "USA")

# Calculate mean and median consumption in Belgium
mean(belgium_consumption$consumption)
median(belgium_consumption$consumption)

# Calculate mean and median consumption in USA
mean(usa_consumption$consumption)
median(usa_consumption$consumption)

food_consumption %>%
  # Filter for Belgium and USA
  filter(country %in% c("Belgium", "USA")) %>%
  # Group by country
  group_by(country) %>%
  # Get mean_consumption and median_consumption
  summarize(mean_consumption = mean(consumption),
           median_consumption = median(consumption))
```

### Mean vs. median

In the video, you learned that the mean is the sum of all the data
points divided by the total number of data points, and the median is the
middle value of the dataset where 50% of the data is less than the
median, and 50% of the data is greater than the median. In this
exercise, you’ll compare these two measures of center.

`dplyr` and `ggplot2` are loaded and `food_consumption` is available.

- Filter `food_consumption` to get the rows where `food_category` is
  `"rice"`.
- Create a histogram using `ggplot2` of `co2_emission` for rice.

Take a look at the histogram of the CO<sub>2</sub> emissions for rice
you just plotted. Which of the following terms best describes the shape
of the data?

- [ ] No skew

- [ ] Left-skewed

- [x] Right-skewed

- Filter `food_consumption` to get the rows where `food_category` is
  `"rice"`.

- Summarize the data to get the mean and median of `co2_emission`,
  calling them `mean_co2` and `median_co2.`

Given the skew of this data, what measure of central tendency best
summarizes the kilograms of CO<sub>2</sub> emissions per person per year
for rice?

- [ ] Mean
- [x] Median
- [ ] Both mean and median

``` r
food_consumption %>%
  # Filter for rice food category
  filter(food_category == "rice") %>%
  # Create histogram of co2_emission
  ggplot(aes(co2_emission)) +
    geom_histogram()

food_consumption %>%
  # Filter for rice food category
  filter(food_category == "rice") %>%
  # Create histogram of co2_emission
  ggplot(aes(co2_emission)) +
    geom_histogram()

food_consumption %>%
  # Filter for rice food category
  filter(food_category == "rice") %>% 
  # Get mean_co2 and median_co2
  summarize(mean_co2 = mean(co2_emission),
            median_co2 = median(co2_emission))
```

## Measures of spread

### Quartiles, quantiles, and quintiles

Quantiles are a great way of summarizing numerical data since they can
be used to measure center and spread, as well as to get a sense of where
a data point stands in relation to the rest of the dataset. For example,
you might want to give a discount to the 10% most active users on a
website.

In this exercise, you’ll calculate quartiles, quintiles, and deciles,
which split up a dataset into 4, 5, and 10 pieces, respectively.

The `dplyr` package is loaded and `food_consumption` is available.

- Calculate the quartiles of the `co2_emission` column of
  `food_consumption`.

<!-- -->

- Calculate the six quantiles that split up the data into 5 pieces
  (quintiles) of the `co2_emission` column of `food_consumption`.

<!-- -->

- Calculate the eleven quantiles of `co2_emission` that split up the
  data into ten pieces (deciles).

``` r
# Calculate the quartiles of co2_emission
quantile(food_consumption$co2_emission)

# Calculate the quintiles of co2_emission
quantile(food_consumption$co2_emission, probs = c(0, 0.2, 0.4, 0.6, 0.8, 1))

# Calculate the deciles of co2_emission
quantile(food_consumption$co2_emission, probs = seq(0, 1, 0.1))
```

### Variance and standard deviation

Variance and standard deviation are two of the most common ways to
measure the spread of a variable, and you’ll practice calculating these
in this exercise. Spread is important since it can help inform
expectations. For example, if a salesperson sells a mean of 20 products
a day, but has a standard deviation of 10 products, there will probably
be days where they sell 40 products, but also days where they only sell
one or two. Information like this is important, especially when making
predictions.

Both `dplyr` and `ggplot2` are loaded, and `food_consumption` is
available.

- Calculate the variance and standard deviation of `co2_emission` for
  each `food_category` by grouping by and summarizing variance as
  `var_co2` and standard deviation as `sd_co2`.
- Create a histogram of `co2_emission` for each `food_category` using
  `facet_wrap()`.

``` r
# Calculate variance and sd of co2_emission for each food_category
food_consumption %>% 
  group_by(food_category) %>% 
  summarize(var_co2 = var(co2_emission),
           sd_co2 = sd(co2_emission))

# Create subgraphs for each food_category: histogram of co2_emission
ggplot(food_consumption, aes(co2_emission)) +
  # Create a histogram
  geom_histogram() +
  # Create a separate sub-graph for each food_category
  facet_wrap(~ food_category)
```

### Finding outliers using IQR

Outliers can have big effects on statistics like mean, as well as
statistics that rely on the mean, such as variance and standard
deviation. Interquartile range, or IQR, is another way of measuring
spread that’s less influenced by outliers. IQR is also often used to
find outliers. If a value is less than \\ - 1.5 \\ or greater than \\ +
1.5 \\, it’s considered an outlier. In fact, this is how the lengths of
the whiskers in a `ggplot2` box plot are calculated.

![Diagram of a box plot showing median, quartiles, and
outliers](https://assets.datacamp.com/production/repositories/5758/datasets/ca7e6e1832be7ec1842f62891815a9b0488efa83/Screen%20Shot%202020-04-28%20at%2010.04.54%20AM.png)

In this exercise, you’ll calculate IQR and use it to find some outliers.
Both `dplyr` and `ggplot2` are loaded and `food_consumption` is
available.

- Calculate the total `co2_emission` per country by grouping by country
  and taking the sum of `co2_emission`. Call the sum `total_emission`
  and store the resulting data frame as `emissions_by_country`.
- Compute the first and third quartiles of `total_emission` and store
  these as `q1` and `q3`.
- Calculate the interquartile range of `total_emission` and store it as
  `iqr`.
- Calculate the lower and upper cutoffs for outliers of
  `total_emission`, and store these as `lower` and `upper`.
- Use `filter()` to get countries with a `total_emission` greater than
  the `upper` cutoff or a `total_emission` less than the `lower` cutoff.

``` r
# Calculate total co2_emission per country: emissions_by_country
emissions_by_country <- food_consumption %>%
  group_by(country) %>%
  summarize(total_emission = sum(co2_emission))

emissions_by_country

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country <- food_consumption %>%
  group_by(country) %>%
  summarize(total_emission = sum(co2_emission))

# Compute the first and third quartiles and IQR of total_emission
q1 <- quantile(emissions_by_country$total_emission, 0.25)
q3 <- quantile(emissions_by_country$total_emission, 0.75)
iqr <- q3 - q1

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country <- food_consumption %>%
  group_by(country) %>%
  summarize(total_emission = sum(co2_emission))

# Compute the first and third quartiles and IQR of total_emission
q1 <- quantile(emissions_by_country$total_emission, 0.25)
q3 <- quantile(emissions_by_country$total_emission, 0.75)
iqr <- q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower <- q1 - 1.5 * iqr
upper <- q3 + 1.5 * iqr

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country <- food_consumption %>%
  group_by(country) %>%
  summarize(total_emission = sum(co2_emission))

# Compute the first and third quartiles and IQR of total_emission
q1 <- quantile(emissions_by_country$total_emission, 0.25)
q3 <- quantile(emissions_by_country$total_emission, 0.75)
iqr <- q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower <- q1 - 1.5 * iqr
upper <- q3 + 1.5 * iqr
```

# Random Numbers and Probability

In this chapter, you’ll learn how to generate random samples and measure
chance using probability. You’ll work with real-world sales data to
calculate the probability of a salesperson being successful. Finally,
you’ll use the binomial distribution to model events with binary
outcomes.

## What are the chances?

### With or without replacement?

In the video, you learned about two different ways of taking samples:
with replacement and without replacement. Although it isn’t always easy
to tell which best fits various situations, it’s important to correctly
identify this so that any probabilities you report are accurate. In this
exercise, you’ll put your new knowledge to the test and practice
figuring this out.

- For each scenario, decide whether it’s sampling with replacement or
  sampling without replacement.

##### With replacement

- Flipping a coin 3 times
- Rolling a die twice

##### Without replacement

- From a deck of cards, dealing 3 players 7 cards each
- Randomly picking 3 people to work on the weekend from a group of 20
  people
- Randomly selecting 5 products from the assembly line to test for
  quality assurance

### Calculating probabilities

You’re in charge of the sales team, and it’s time for performance
reviews, starting with Amir. As part of the review, you want to randomly
select a few of the deals that he’s worked on over the past year so that
you can look at them more deeply. Before you start selecting deals,
you’ll first figure out what the chances are of selecting certain deals.

Recall that the probability of an event can be calculated by $$
P(\text{event}) = \frac{\text{# ways event can happen}}{\text{total \#
of possible outcomes}} $$

`dplyr` is loaded and `amir_deals` is available.

- Count the number of deals Amir worked on for each `product` type.
- Create a new column called `prob` by dividing `n` by the total number
  of deals Amir worked on.

If you randomly select one of Amir’s deals, what’s the probability that
the deal will involve `Product C`?

- [ ] 15%
- [ ] 80.43%
- [x] 8.43%
- [ ] 22.5%

``` r
# edited/added
amir_deals <- readRDS('seller_1.rds') %>% 
  select(product, client, status, amount, num_users)

# Count the deals for each product
amir_deals %>%
  count(product)

# Calculate probability of picking a deal with each product
amir_deals %>%
  count(product) %>%
  mutate(prob = n/sum(n))
```

### Sampling deals

In the previous exercise, you counted the deals Amir worked on. Now it’s
time to randomly pick five deals so that you can reach out to each
customer and ask if they were satisfied with the service they received.
You’ll try doing this both with and without replacement.

Additionally, you want to make sure this is done randomly and that it
can be reproduced in case you get asked how you chose the deals, so
you’ll need to set the random seed before sampling from the deals.

`dplyr` is loaded and `amir_deals` is available.

- Set the random seed to `31`.
- Take a sample of 5 deals **without** replacement.
- Take a sample of 5 deals **with** replacement.

What type of sampling is better to use for this situation?

- [ ] With replacement
- [ ] Without replacement
- [ ] It doesn’t matter

``` r
# Set random seed to 31
set.seed(31)

# Sample 5 deals without replacement
amir_deals %>%
  sample_n(5)

# Set random seed to 31
set.seed(31)

# Sample 5 deals with replacement
amir_deals %>%
  sample_n(5, replace = TRUE)
```

## Discrete distributions

### Creating a probability distribution

A new restaurant opened a few months ago, and the restaurant’s
management wants to optimize its seating space based on the size of the
groups that come most often. On one night, there are 10 groups of people
waiting to be seated at the restaurant, but instead of being called in
the order they arrived, they will be called randomly. In this exercise,
you’ll investigate the probability of groups of different sizes getting
picked first. Data on each of the ten groups is contained in the
`restaurant_groups` data frame.

Remember that expected value can be calculated by multiplying each
possible outcome with its corresponding probability and taking the sum.
The `restaurant_groups` data is available and `dplyr` and `ggplot2` are
loaded.

- Create a histogram of the `group_size` column of `restaurant_groups`,
  setting the number of bins to `5`.

<!-- -->

- Count the number of each `group_size` in `restaurant_groups`, then add
  a column called `probability` that contains the probability of
  randomly selecting a group of each size. Store this in a new data
  frame called `size_distribution`.

<!-- -->

- Calculate the expected value of the `size_distribution`, which
  represents the expected group size.

<!-- -->

- Calculate the probability of randomly picking a group of 4 or more
  people by filtering and summarizing.

``` r
# edited/added
restaurant_groups <- read.csv('restaurant_groups.csv')

# Create a histogram of restaurant_groups
ggplot(restaurant_groups, aes(group_size)) +
  geom_histogram(bins = 5)

# Create probability distribution
size_distribution <- restaurant_groups %>%
  # Count number of each group size
  count(group_size) %>%
  # Calculate probability
  mutate(probability = n / sum(n))

size_distribution

# Create probability distribution
size_distribution <- restaurant_groups %>%
  count(group_size) %>%
  mutate(probability = n / sum(n))

# Calculate expected group size
expected_val <- sum(size_distribution$group_size *
                    size_distribution$probability)
expected_val

# Create probability distribution
size_distribution <- restaurant_groups %>%
  count(group_size) %>%
  mutate(probability = n / sum(n))

# Calculate probability of picking group of 4 or more
size_distribution %>%
  # Filter for groups of 4 or larger
  filter(group_size >= 4) %>%
  # Calculate prob_4_or_more by taking sum of probabilities
  summarize(prob_4_or_more = sum(probability))
```

### Identifying distributions

# Identifying distributions

Which sample is most likely to have been taken from a uniform
distribution?

![A: bell-shaped distribution, B: relatively flat distribution, C: lots
of lower values, fewer high
values](https://assets.datacamp.com/production/repositories/5758/datasets/bd64d4775ec28f36b081d92aa38a391033c03b8f/Screen%20Shot%202020-05-04%20at%204.35.58%20PM.png)

- [ ] A
- [x] B
- [ ] C

## Expected value vs. sample mean

The app to the right will take a sample from a discrete uniform
distribution, which includes the numbers 1 through 9, and calculate the
sample’s mean. You can adjust the size of the sample using the slider.
Note that the expected value of this distribution is 5.

A sample is taken, and you win twenty dollars if the sample’s mean is
less than 4. There’s a catch: you get to pick the sample’s size.

Which sample size is ***most likely*** to win you the twenty dollars?

- [x] 10
- [ ] 100
- [ ] 1000
- [ ] 5000
- [ ] 10000

## Continuous distributions

### Which distribution?

At this point, you’ve learned about the two different variants of the
uniform distribution: the discrete uniform distribution, and the
continuous uniform distribution. In this exercise, you’ll decide which
situations follow which distribution.

![Illustration of discrete and continuous uniform
distributions](https://assets.datacamp.com/production/repositories/5758/datasets/fe928d4c840f66544c6228b8b755e9bf15361b9f/Screen%20Shot%202020-05-04%20at%205.18.16%20PM.png)

- Map each situation to the probability distribution it would best be
  modeled by.

##### Discrete uniform

- The outcome of rolling a 4-sided die.
- The ticket number of a raffle winner, assuming there is one ticket for
  each number from 1 to 100.

##### Continuous uniform

- The time you’ll have to wait for a geyser to erupt if you show up at a
  random time, knowing that the geyser erupts exactly every ten minutes.
- The time of day a baby will be born.

##### Other

- The height of a random person.

### Data back-ups

The sales software used at your company is set to automatically back
itself up, but no one knows exactly what time the back-ups happen. It is
known, however, that back-ups happen exactly every 30 minutes. Amir
comes back from sales meetings at random times to update the data on the
client he just met with. He wants to know how long he’ll have to wait
for his newly-entered data to get backed up. Use your new knowledge of
continuous uniform distributions to model this situation and answer
Amir’s questions.

- To model how long Amir will wait for a back-up using a continuous
  uniform distribution, save his lowest possible wait time as `min` and
  his longest possible wait time as `max`. Remember that back-ups happen
  every 30 minutes.

<!-- -->

- Calculate the probability that Amir has to wait less than 5 minutes,
  and store in a variable called `prob_less_than_5`.

<!-- -->

- Calculate the probability that Amir has to wait more than 5 minutes,
  and store in a variable called `prob_greater_than_5`.

<!-- -->

- Calculate the probability that Amir has to wait between 10 and 20
  minutes, and store in a variable called `prob_between_10_and_20`.

``` r
# Min and max wait times for back-up that happens every 30 min
min <- 0
max <- 30

# Min and max wait times for back-up that happens every 30 min
min <- 0
max <- 30

# Calculate probability of waiting less than 5 mins
prob_less_than_5 <- punif(5, min, max)
prob_less_than_5

# Min and max wait times for back-up that happens every 30 min
min <- 0
max <- 30

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 <- punif(5, min, max, lower.tail = FALSE)
prob_greater_than_5

# Min and max wait times for back-up that happens every 30 min
min <- 0
max <- 30

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 <- punif(20, min, max) - punif(10, min, max)
prob_between_10_and_20
```

### Simulating wait times

To give Amir a better idea of how long he’ll have to wait, you’ll
simulate Amir waiting 1000 times and create a histogram to show him what
he should expect. Recall from the last exercise that his minimum wait
time is 0 minutes and his maximum wait time is 30 minutes.

A data frame called `wait_times` is available and `dplyr` and `ggplot2`
are loaded.

- Set the random seed to `334`.
- Generate 1000 wait times from the continuous uniform distribution that
  models Amir’s wait time. Add this as a new column called `time` in the
  `wait_times` data frame.
- Create a histogram of the simulated wait times with 30 bins.

``` r
# edited/added
wait_times <- data.frame(simulation_nb = 1:1000)

# Set random seed to 334
set.seed(334)

# Set random seed to 334
set.seed(334)

# Generate 1000 wait times between 0 and 30 mins, save in time column
wait_times %>%
  mutate(time = runif(1000, min = 0, max = 30))

# Set random seed to 334
set.seed(334)

# Generate 1000 wait times between 0 and 30 mins, save in time column
wait_times %>%
  mutate(time = runif(1000, min = 0, max = 30)) %>%
  # Create a histogram of simulated times
  ggplot(aes(time)) +
  geom_histogram(bins = 30)
```

## The binomial distribution

### Simulating sales deals

Assume that Amir usually works on 3 deals per week, and overall, he wins
30% of deals he works on. Each deal has a binary outcome: it’s either
lost, or won, so you can model his sales deals with a binomial
distribution. In this exercise, you’ll help Amir simulate a year’s worth
of his deals so he can better understand his performance.

- Set the random seed to 10 and simulate a single deal.

<!-- -->

- Simulate a typical week of Amir’s deals, or one week of 3 deals.

<!-- -->

- Simulate a year’s worth of Amir’s deals, or 52 weeks of 3 deals each,
  and store in `deals`.
- Calculate the mean number of deals he won per week.

``` r
# Set random seed to 10
set.seed(10)

# Simulate a single deal
rbinom(1, 1, 0.3)

# Set random seed to 10
set.seed(10)

# Simulate 1 week of 3 deals
rbinom(1, 3, 0.3)

# Set random seed to 10
set.seed(10)

# Simulate 52 weeks of 3 deals
deals <- rbinom(52, 3, 0.3)

# Calculate mean deals won per week
mean(deals)
```

### Calculating binomial probabilities

Just as in the last exercise, assume that Amir wins 30% of deals. He
wants to get an idea of how likely he is to close a certain number of
deals each week. In this exercise, you’ll calculate what the chances are
of him closing different numbers of deals using the binomial
distribution.

- What’s the probability that Amir closes all 3 deals in a week?
- What’s the probability that Amir closes 1 or fewer deals in a week?
- What’s the probability that Amir closes more than 1 deal?

``` r
# Probability of closing 3 out of 3 deals
dbinom(3, 3, 0.3)

# Probability of closing <= 1 deal out of 3 deals
pbinom(1, 3, 0.3)

# Probability of closing > 1 deal out of 3 deals
pbinom(1, 3, 0.3, lower.tail = FALSE)
```

### How many sales will be won?

Now Amir wants to know how many deals he can expect to close each week
if his win rate changes. Luckily, you can use your binomial distribution
knowledge to help him calculate the expected value in different
situations. Recall from the video that the expected value of a binomial
distribution can be calculated by \n p\\.

- Calculate the expected number of sales out of the **3** he works on
  that Amir will win each week if he maintains his 30% win rate.
- Calculate the expected number of sales out of the 3 he works on that
  he’ll win if his win rate drops to 25%.
- Calculate the expected number of sales out of the 3 he works on that
  he’ll win if his win rate rises to 35%.

``` r
# Expected number won with 30% win rate
won_30pct <- 3 * 0.3
won_30pct

# Expected number won with 25% win rate
won_25pct <- 3 * 0.25
won_25pct

# Expected number won with 35% win rate
won_35pct <- 3 * 0.35
won_35pct
```

# More Distributions and the Central Limit Theorem

It’s time to explore one of the most important probability distributions
in statistics, normal distribution. You’ll create histograms to plot
normal distributions and gain an understanding of the central limit
theorem, before expanding your knowledge of statistical functions by
adding the Poisson, exponential, and t-distributions to your repertoire.

## The normal distribution

### Distribution of Amir’s sales

Since each deal Amir worked on (both won and lost) was different, each
was worth a different amount of money. These values are stored in the
`amount` column of `amir_deals` As part of Amir’s performance review,
you want to be able to estimate the probability of him selling different
amounts, but before you can do this, you’ll need to determine what kind
of distribution the `amount` variable follows.

Both `dplyr` and `ggplot2` are loaded and `amir_deals` is available.

- Create a histogram with 10 bins to visualize the distribution of the
  `amount`.

Which probability distribution do the sales `amounts` most closely
follow?

- [ ] Uniform
- [ ] Binomial
- [x] Normal
- [ ] None of the above

``` r
# Histogram of amount with 10 bins
ggplot(amir_deals, aes(amount)) +
  geom_histogram(bins = 10)
```

### Probabilities from the normal distribution

Since each deal Amir worked on (both won and lost) was different, each
was worth a different amount of money. These values are stored in the
`amount` column of `amir_deals` and follow a normal distribution with a
mean of 5000 dollars and a standard deviation of 2000 dollars. As part
of his performance metrics, you want to calculate the probability of
Amir closing a deal worth various amounts.

- What’s the probability of Amir closing a deal worth less than \$7500?

<!-- -->

- What’s the probability of Amir closing a deal worth more than \$1000?

<!-- -->

- What’s the probability of Amir closing a deal worth between \$3000 and
  \$7000?

<!-- -->

- What amount will 75% of Amir’s sales be *more than*?

``` r
# Probability of deal < 7500
pnorm(7500, mean = 5000, sd = 2000)

# Probability of deal > 1000
pnorm(1000, mean = 5000, sd = 2000, lower.tail = FALSE)

# Probability of deal between 3000 and 7000
pnorm(7000, mean = 5000, sd = 2000) - pnorm(3000, mean = 5000, sd = 2000)

# Calculate amount that 75% of deals will be more than
qnorm(0.75, mean = 5000, sd = 2000, lower.tail = FALSE)
```

### Simulating sales under new market conditions

The company’s financial analyst is predicting that next quarter, the
worth of each sale will increase by 20% and the volatility, or standard
deviation, of each sale’s worth will increase by 30%. To see what Amir’s
sales might look like next quarter under these new market conditions,
you’ll simulate new sales amounts using the normal distribution and
store these in the `new_sales` data frame, which has already been
created for you.

In addition, `dplyr` and `ggplot2` are loaded.

- Currently, Amir’s average sale amount is \$5000. Calculate what his
  new average amount will be if it increases by 20% and store this in
  `new_mean`.
- Amir’s current standard deviation is \$2000. Calculate what his new
  standard deviation will be if it increases by 30% and store this in
  `new_sd`.
- Add a new column called `amount` to the data frame `new_sales`, which
  contains 36 simulated amounts from a normal distribution with a mean
  of `new_mean` and a standard deviation of `new_sd`.
- Plot the distribution of the `new_sales` `amount`s using a histogram
  with 10 bins.

``` r
# edited/added
new_sales <- data.frame(sale_num = 1:36)

# Calculate new average amount
new_mean <- 5000 * 1.2

# Calculate new standard deviation
new_sd <- 2000 * 1.3

# Simulate 36 sales
new_sales <- new_sales %>% 
  mutate(amount = rnorm(36, mean = new_mean, sd = new_sd))

# Create histogram with 10 bins
ggplot(new_sales, aes(amount)) +
  geom_histogram(bins = 10)
```

### Which market is better?

The key metric that the company uses to evaluate salespeople is the
percent of sales they make over \$1000 since the time put into each sale
is usually worth a bit more than that, so the higher this metric, the
better the salesperson is performing.

Recall that Amir’s current sales amounts have a mean of \$5000 and a
standard deviation of \$2000, and Amir’s predicted amounts in next
quarter’s market have a mean of \$6000 and a standard deviation of
\$2600.

Based only on the metric of **percent of sales over \$1000**, does Amir
perform better in the current market or the predicted market?

- [ ] Amir performs much better in the current market.
- [ ] Amir performs much better in next quarter’s predicted market.
- [x] Amir performs about equally in both markets.

## The central limit theorem

### Visualizing sampling distributions

On the right, try creating *sampling distributions* of different summary
statistics from samples of different distributions. Which distribution
does the central limit theorem **not** apply to?

- [ ] Discrete uniform distribution
- [ ] Continuous uniform distribution
- [ ] Binomial distribution
- [ ] All of the above
- [x] None of the above

### The CLT in action

The central limit theorem states that a sampling distribution of a
sample statistic approaches the normal distribution as you take more
samples, no matter the original distribution being sampled from.

In this exercise, you’ll focus on the sample mean and see the central
limit theorem in action while examining the `num_users` column of
`amir_deals` more closely, which contains the number of people who
intend to use the product Amir is selling.

Both `dplyr` and `ggplot2` are loaded and `amir_deals` is available.

- Create a histogram of the `num_users` column of `amir_deals`. Use 10
  bins.
- Set the seed to `104`.
- Take a sample of size `20` with replacement from the `num_users`
  column of `amir_deals`, and take the mean.
- Repeat this 100 times and store as `sample_means`. This will take 100
  different samples and calculate the mean of each.
- A data frame called `samples` has been created for you with a column
  `mean`, which contains the values from `sample_means`. Create a
  histogram of the `mean` column with 10 bins.

``` r
# Create a histogram of num_users
ggplot(amir_deals, aes(num_users)) +
  geom_histogram(bins = 10)

# Set seed to 104
set.seed(104)

# Sample 20 num_users with replacement from amir_deals
sample(amir_deals$num_users, size = 20, replace = TRUE) %>%
  # Take mean
  mean()

# Set seed to 104
set.seed(104)

# Sample 20 num_users from amir_deals and take mean
sample(amir_deals$num_users, size = 20, replace = TRUE) %>%
  mean()

# Repeat the above 100 times
sample_means <- replicate(100, sample(amir_deals$num_users, size = 20, replace = TRUE) %>% mean())

# Set seed to 104
set.seed(104)

# Sample 20 num_users from amir_deals and take mean
sample(amir_deals$num_users, size = 20, replace = TRUE) %>%
  mean()

# Repeat the above 100 times
sample_means <- replicate(100, sample(amir_deals$num_users, size = 20, replace = TRUE) %>% mean())

# Create data frame for plotting
samples <- data.frame(mean = sample_means)

# Histogram of sample means
ggplot(samples, aes(mean)) +
  geom_histogram(bins = 10)
```

### The mean of means

You want to know what the average number of users (`num_users`) is per
deal, but you want to know this number for the entire company so that
you can see if Amir’s deals have more or fewer users than the company’s
average deal. The problem is that over the past year, the company has
worked on more than ten thousand deals, so it’s not realistic to compile
all the data. Instead, you’ll estimate the mean by taking several random
samples of deals, since this is much easier than collecting data from
everyone in the company.

The user data for all the company’s deals is available in `all_deals`.

- Set the random seed to `321`.
- Take 30 samples of size 20 from `all_deals$num_users` and take the
  mean of each sample. Store the sample means in `sample_means`.
- Take the mean of `sample_means`.
- Take the mean of the `num_users` column of `amir_deals`.

``` r
# edited/added
all_deals <- read.csv('all_deals.csv')

# Set seed to 321
set.seed(321)

# Take 30 samples of 20 values of num_users, take mean of each sample
sample_means <- replicate(30, sample(all_deals$num_users, 20) %>% mean())

# Calculate mean of sample_means
mean(sample_means)

# Calculate mean of num_users in amir_deals
mean(amir_deals$num_users)
```

## The Poisson distribution

## Identifying lambda

Now that you’ve learned about the Poisson distribution, you know that
its shape is described by a value called lambda. In this exercise,
you’ll match histograms to lambda values.

##### lambda = 1

![highest probabilities at 0 and 1](https://bit.ly/2B7aidP)

##### lambda = 4

![highest probabilities at 3 and 4](https://bit.ly/2M8ZFtf)

##### lambda = 8

![highest probabilities at 7 and 8](https://bit.ly/2TMUvYe)

### Tracking lead responses

Your company uses sales software to keep track of new sales leads. It
organizes them into a queue so that anyone can follow up on one when
they have a bit of free time. Since the number of lead responses is a
countable outcome over a period of time, this scenario corresponds to a
Poisson distribution. On average, Amir responds to 4 leads each day. In
this exercise, you’ll calculate probabilities of Amir responding to
different numbers of leads.

- What’s the probability that Amir responds to 5 leads in a day, given
  that he responds to an average of 4?

<!-- -->

- Amir’s coworker responds to an average of 5.5 leads per day. What is
  the probability that she answers 5 leads in a day?

<!-- -->

- What’s the probability that Amir responds to 2 or fewer leads in a
  day?

<!-- -->

- What’s the probability that Amir responds to more than 10 leads in a
  day?

``` r
# Probability of 5 responses
dpois(5, lambda = 4)

# Probability of 5 responses from coworker
dpois(5, lambda = 5.5)

# Probability of 2 or fewer responses
ppois(2, lambda = 4)

# Probability of > 10 responses
ppois(10, lambda = 4, lower.tail = FALSE)
```

## More probability distributions

### Too many distributions

By this point, you’ve learned about so many different probability
distributions that it can be difficult to remember which is which. In
this exercise, you’ll practice distinguishing between distributions and
identifying the distribution that best matches different scenarios.

- Match each situation to the distribution that best models it.

##### Poisson

- Number of customers that enter a store each hour
- Number of products sold each week

##### Exponential

- Amount of time until someone pays off their loan
- Amount of time until the next customer makes a purchase

##### Binomial

- Number of people from a group of 30 that pass their driving test

### Modeling time between leads

To further evaluate Amir’s performance, you want to know how much time
it takes him to respond to a lead after he opens it. On average, it
takes 2.5 hours for him to respond. In this exercise, you’ll calculate
probabilities of different amounts of time passing between Amir
receiving a lead and sending a response.

- What’s the probability it takes Amir less than an hour to respond to a
  lead?

<!-- -->

- What’s the probability it takes Amir more than 4 hours to respond to a
  lead?

<!-- -->

- What’s the probability it takes Amir 3-4 hours to respond to a lead?

``` r
# Probability response takes < 1 hour
pexp(1, rate = 1/2.5)

# Probability response takes > 4 hours
pexp(4, rate = 1/2.5, lower.tail = FALSE)

# Probability response takes 3-4 hours
pexp(4, rate = 1/2.5) - pexp(3, rate = 1/2.5)
```

### The t-distribution

Which statement is **not** true regarding the t-distribution?

- [ ] The t-distribution has thicker tails than the normal distribution.
- [ ] A t-distribution with high degrees of freedom resembles the normal
  distribution.
- [ ] The number of degrees of freedom affects the distribution’s
  variance.
- [x] The t-distribution is skewed.

# Correlation and Experimental Design

In this chapter, you’ll learn how to quantify the strength of a linear
relationship between two variables, and explore how confounding
variables can affect the relationship between two other variables.
You’ll also see how a study’s design can influence its results, change
how the data should be analyzed, and potentially affect the reliability
of your conclusions.

## Correlation

### Guess the correlation

On the right, use the scatterplot to estimate what the correlation is
between the variables `x` and `y`. Once you’ve guessed it correctly, use
the **New Plot** button to try out a few more scatterplots. When you’re
ready, answer the question below to continue to the next exercise.

Which of the following statements is NOT true about correlation?

- [ ] If the correlation between \`x\` and \`y\` has a high magnitude,
  the data points will be clustered closely around a line.
- [ ] Correlation can be written as \*r\*.
- [ ] If \`x\` and \`y\` are negatively correlated, values of \`y\`
  decrease as values of \`x\` increase.
- [x] Correlation cannot be 0.

### Relationships between variables

In this chapter, you’ll be working with a dataset `world_happiness`
containing results from the [2019 World Happiness
Report](https://worldhappiness.report/ed/2019/). The report scores
various countries based on how happy people in that country are. It also
ranks each country on various societal aspects such as social support,
freedom, corruption, and others. The dataset also includes the GDP per
capita and life expectancy for each country.

In this exercise, you’ll examine the relationship between a country’s
life expectancy (`life_exp`) and happiness score (`happiness_score`)
both visually and quantitatively. Both `dplyr` and `ggplot2` are loaded
and `world_happiness` is available.

- Create a scatterplot of `happiness_score` vs. `life_exp` using
  `ggplot2`.
- Add a linear trendline to the scatterplot, setting `se` to `FALSE`.

Based on the scatterplot, which is most likely the correlation between
`life_exp` and `happiness_score`?

- [ ] 0.3

- [ ] -0.3

- [x] 0.8

- [ ] -0.8

- Calculate the correlation between `life_exp` and `happiness_score`.

``` r
# edited/added
world_happiness <- readRDS('world_happiness_sugar.rds')

# Create a scatterplot of happiness_score vs. life_exp
ggplot(world_happiness, aes(life_exp, happiness_score)) +
  geom_point()

# Add a linear trendline to scatterplot
ggplot(world_happiness, aes(life_exp, happiness_score)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE)

# Add a linear trendline to scatterplot
ggplot(world_happiness, aes(life_exp, happiness_score)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE)

# Correlation between life_exp and happiness_score
cor(world_happiness$life_exp, world_happiness$happiness_score)
```

## Correlation caveats

### What can’t correlation measure?

While the correlation coefficient is a convenient way to quantify the
strength of a relationship between two variables, it’s far from perfect.
In this exercise, you’ll explore one of the caveats of the correlation
coefficient by examining the relationship between a country’s GDP per
capita (`gdp_per_cap`) and happiness score.

Both `dplyr` and `ggplot2` are loaded and `world_happiness` is
available.

- Create a scatterplot showing the relationship between `gdp_per_cap`
  (on the x-axis) and `life_exp` (on the y-axis).
- Calculate the correlation between `gdp_per_cap` and `life_exp`.

The correlation between GDP per capita and life expectancy is 0.7. Why
is correlation ***not*** the best way to measure the relationship
between the two variables?

- [ ] Correlation measures how one variable affects another.
- [x] Correlation only measures linear relationships.
- [ ] Correlation cannot properly measure relationships between numeric
  variables.

``` r
# Scatterplot of gdp_per_cap and life_exp
ggplot(world_happiness, aes(gdp_per_cap, life_exp)) +
  geom_point()

# Scatterplot of gdp_per_cap and life_exp
ggplot(world_happiness, aes(gdp_per_cap, life_exp)) +
  geom_point()

# Correlation between gdp_per_cap and life_exp
cor(world_happiness$gdp_per_cap, world_happiness$life_exp)
```

### Transforming variables

When variables have skewed distributions, they often require a
transformation in order to form a linear relationship with another
variable so that correlation can be computed. In this exercise, you’ll
perform a transformation yourself.

Both `dplyr` and `ggplot2` are loaded and `world_happiness` is
available.

- Create a scatterplot of `happiness_score` versus `gdp_per_cap`.
- Calculate the correlation between `happiness_score` and `gdp_per_cap`.

<!-- -->

- Add a new column to `world_happiness` called `log_gdp_per_cap` that
  contains the log of `gdp_per_cap`.
- Create a scatterplot of `happiness_score` versus `log_gdp_per_cap`.
- Calculate the correlation between `happiness_score` and
  `log_gdp_per_cap`.

``` r
# Scatterplot of happiness_score vs. gdp_per_cap
ggplot(world_happiness, aes(gdp_per_cap, happiness_score)) +
  geom_point()

# Calculate correlation
cor(world_happiness$gdp_per_cap, world_happiness$happiness_score)

# Create log_gdp_per_cap column
world_happiness <- world_happiness %>%
  mutate(log_gdp_per_cap = log(gdp_per_cap))

# Scatterplot of happiness_score vs. log_gdp_per_cap
ggplot(world_happiness, aes(log_gdp_per_cap, happiness_score)) +
  geom_point()

# Calculate correlation
cor(world_happiness$log_gdp_per_cap, world_happiness$happiness_score)
```

### Does sugar improve happiness?

A new column has been added to `world_happiness` called
`grams_sugar_per_day`, which contains the average amount of sugar eaten
per person per day in each country. In this exercise, you’ll examine the
effect of a country’s average sugar consumption on its happiness score.

Both `dplyr` and `ggplot2` are loaded and `world_happiness` is
available.

- Create a scatterplot showing the relationship between
  `grams_sugar_per_day` (on the x-axis) and `happiness_score` (on the
  y-axis).
- Calculate the correlation between `grams_sugar_per_day` and
  `happiness_score`.

Based on this data, which statement about sugar consumption and
happiness scores is true?

- [ ] Increased sugar consumption leads to a higher happiness score.
- [ ] Lower sugar consumption results in a lower happiness score
- [x] Increased sugar consumption is associated with a higher happiness
  score.
- [ ] Sugar consumption is not related to happiness.

``` r
# Scatterplot of grams_sugar_per_day and happiness_score
ggplot(world_happiness, aes(grams_sugar_per_day, happiness_score)) +
  geom_point()

# Correlation between grams_sugar_per_day and happiness_score
cor(world_happiness$grams_sugar_per_day, world_happiness$happiness_score)
```

### Confounders

A study is investigating the relationship between neighborhood residence
and lung capacity. Researchers measure the lung capacity of thirty
people from neighborhood A, which is located near a highway, and thirty
people from neighborhood B, which is not near a highway. Both groups
have similar smoking habits and a similar gender breakdown.

Which of the following could be a confounder in this study?

- [ ] Lung capacity
- [ ] Neighborhood
- [x] Air pollution
- [ ] Smoking status
- [ ] Gender

## Design of experiments

### Study types

While controlled experiments are ideal, many situations and research
questions are not conducive to a controlled experiment. In a controlled
experiment, causation can likely be inferred if the control and test
groups have similar characteristics and don’t have any systematic
difference between them. On the other hand, causation cannot usually be
inferred from observational studies, whose results are often
misinterpreted as a result.

In this exercise, you’ll practice distinguishing controlled experiments
from observational studies.

- Determine if each study is a controlled experiment or observational
  study.

##### Controlled experiment

- Subjects are randomly assigned to a diet and weight loss is compared.
- Asthma symptoms are compared between children randomly assigned to
  receive professional home pest management services or pest management
  education.
- Purchasing rates are compared between users of an e-commerce site who
  are randomly directed to a new version of the home page or an old
  version.

##### Observational study

- Prevalence of heart disease is compared between veterans with PTSD and
  veterans without PTSD.
- A week ago, the home page of an e-commerce site was updated.
  Purchasing rates are compared between users who saw the old and new
  home page versions.

### Longitudinal vs. cross-sectional studies

A company manufactures thermometers, and they want to study the
relationship between a thermometer’s age and its accuracy. To do this,
they take a sample of 100 different thermometers of different ages and
test how accurate they are. Is this data longitudinal or
cross-sectional?

- [ ] Longitudinal
- [x] Cross-sectional
- [ ] Both
- [ ] Neither

## Congratulations!

### Congratulations!

Congratulations on completing the course! You now have foundational
statistics skills that you can use in your analyses and build upon
further.

### Overview

In the first chapter of the course, you learned about what statistics
can do, as well as summary statistics to measure the center and spread
of a distribution. In the second chapter, you learned how to measure
chance and how to use and interpret probability distributions. You also
learned about the binomial distribution. In chapter three, you learned
about the normal distribution and the central limit theorem, one of the
most important ideas in statistics. You also saw how the Poisson
distribution can be used to model countable outcomes. In the final
chapter, you saw how to quantify relationships between two variables
using correlation. You also learned about controlled experiments and
observational studies and the conclusions that can and cannot be drawn
from them.

### Build on your skills

There’s still much more that you can do with statistics and much more to
learn. Your new skills will set you up for success in this course on the
foundations of regression.

### Congratulations!

Thanks for accompanying me on this statistical journey. Congratulations
again!
