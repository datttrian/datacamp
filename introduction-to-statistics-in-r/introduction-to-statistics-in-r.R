## ---- eval=F-----------------------------------------------------------------------
## # edited/added
## library(tidyverse)
## food_consumption <- readRDS('food_consumption.rds')
## 
## # Filter for Belgium
## belgium_consumption <- food_consumption %>%
##   filter(country == "Belgium")
## # edited/added
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

# Calculate the quartiles of co2_emission
quantile(food_consumption$co2_emission)

# Calculate the quintiles of co2_emission
quantile(food_consumption$co2_emission, probs = c(0, 0.2, 0.4, 0.6, 0.8, 1))

# Calculate the deciles of co2_emission
quantile(food_consumption$co2_emission, probs = seq(0, 1, 0.1))

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

# Probability of closing 3 out of 3 deals
dbinom(3, 3, 0.3)

# Probability of closing <= 1 deal out of 3 deals
pbinom(1, 3, 0.3)

# Probability of closing > 1 deal out of 3 deals
pbinom(1, 3, 0.3, lower.tail = FALSE)

# Expected number won with 30% win rate
won_30pct <- 3 * 0.3
won_30pct

# Expected number won with 25% win rate
won_25pct <- 3 * 0.25
won_25pct

# Expected number won with 35% win rate
won_35pct <- 3 * 0.35
won_35pct

# Histogram of amount with 10 bins
ggplot(amir_deals, aes(amount)) +
  geom_histogram(bins = 10)

# Probability of deal < 7500
pnorm(7500, mean = 5000, sd = 2000)

# Probability of deal > 1000
pnorm(1000, mean = 5000, sd = 2000, lower.tail = FALSE)

# Probability of deal between 3000 and 7000
pnorm(7000, mean = 5000, sd = 2000) - pnorm(3000, mean = 5000, sd = 2000)

# Calculate amount that 75% of deals will be more than
qnorm(0.75, mean = 5000, sd = 2000, lower.tail = FALSE)

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

# Probability of 5 responses
dpois(5, lambda = 4)

# Probability of 5 responses from coworker
dpois(5, lambda = 5.5)

# Probability of 2 or fewer responses
ppois(2, lambda = 4)

# Probability of > 10 responses
ppois(10, lambda = 4, lower.tail = FALSE)

# Probability response takes < 1 hour
pexp(1, rate = 1/2.5)

# Probability response takes > 4 hours
pexp(4, rate = 1/2.5, lower.tail = FALSE)

# Probability response takes 3-4 hours
pexp(4, rate = 1/2.5) - pexp(3, rate = 1/2.5)

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

# Scatterplot of gdp_per_cap and life_exp
ggplot(world_happiness, aes(gdp_per_cap, life_exp)) +
  geom_point()

# Scatterplot of gdp_per_cap and life_exp
ggplot(world_happiness, aes(gdp_per_cap, life_exp)) +
  geom_point()

# Correlation between gdp_per_cap and life_exp
cor(world_happiness$gdp_per_cap, world_happiness$life_exp)

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

# Scatterplot of grams_sugar_per_day and happiness_score
ggplot(world_happiness, aes(grams_sugar_per_day, happiness_score)) +
  geom_point()

# Correlation between grams_sugar_per_day and happiness_score
cor(world_happiness$grams_sugar_per_day, world_happiness$happiness_score)

## # Filter for USA
## usa_consumption <- food_consumption %>%
##   filter(country == "USA")
## 
## # Calculate mean and median consumption in Belgium
## mean(belgium_consumption$consumption)
## median(belgium_consumption$consumption)
## 
## # Calculate mean and median consumption in USA
## mean(usa_consumption$consumption)
## median(usa_consumption$consumption)
## 
## food_consumption %>%
##   # Filter for Belgium and USA
##   filter(country %in% c("Belgium", "USA")) %>%
##   # Group by country
##   group_by(country) %>%
##   # Get mean_consumption and median_consumption
##   summarize(mean_consumption = mean(consumption),
##            median_consumption = median(consumption))


## ---- eval=F-----------------------------------------------------------------------
## food_consumption %>%
##   # Filter for rice food category
##   filter(food_category == "rice") %>%
##   # Create histogram of co2_emission
##   ggplot(aes(co2_emission)) +
##     geom_histogram()
## 
## food_consumption %>%
##   # Filter for rice food category
##   filter(food_category == "rice") %>%
##   # Create histogram of co2_emission
##   ggplot(aes(co2_emission)) +
##     geom_histogram()
## 
## food_consumption %>%
##   # Filter for rice food category
##   filter(food_category == "rice") %>%
##   # Get mean_co2 and median_co2
##   summarize(mean_co2 = mean(co2_emission),
##             median_co2 = median(co2_emission))


## ---- eval=F-----------------------------------------------------------------------
## # Calculate the quartiles of co2_emission
## quantile(food_consumption$co2_emission)
## 
## # Calculate the quintiles of co2_emission
## quantile(food_consumption$co2_emission, probs = c(0, 0.2, 0.4, 0.6, 0.8, 1))
## 
## # Calculate the deciles of co2_emission
## quantile(food_consumption$co2_emission, probs = seq(0, 1, 0.1))


## ---- eval=F-----------------------------------------------------------------------
## # Calculate variance and sd of co2_emission for each food_category
## food_consumption %>%
##   group_by(food_category) %>%
##   summarize(var_co2 = var(co2_emission),
##            sd_co2 = sd(co2_emission))
## 
## # Create subgraphs for each food_category: histogram of co2_emission
## ggplot(food_consumption, aes(co2_emission)) +
##   # Create a histogram
##   geom_histogram() +
##   # Create a separate sub-graph for each food_category
##   facet_wrap(~ food_category)


## ---- eval=F-----------------------------------------------------------------------
## # Calculate total co2_emission per country: emissions_by_country
## emissions_by_country <- food_consumption %>%
##   group_by(country) %>%
##   summarize(total_emission = sum(co2_emission))
## 
## emissions_by_country
## 
## # Calculate total co2_emission per country: emissions_by_country
## emissions_by_country <- food_consumption %>%
##   group_by(country) %>%
##   summarize(total_emission = sum(co2_emission))
## 
## # Compute the first and third quartiles and IQR of total_emission
## q1 <- quantile(emissions_by_country$total_emission, 0.25)
## q3 <- quantile(emissions_by_country$total_emission, 0.75)
## iqr <- q3 - q1
## 
## # Calculate total co2_emission per country: emissions_by_country
## emissions_by_country <- food_consumption %>%
##   group_by(country) %>%
##   summarize(total_emission = sum(co2_emission))
## 
## # Compute the first and third quartiles and IQR of total_emission
## q1 <- quantile(emissions_by_country$total_emission, 0.25)
## q3 <- quantile(emissions_by_country$total_emission, 0.75)
## iqr <- q3 - q1
## 
## # Calculate the lower and upper cutoffs for outliers
## lower <- q1 - 1.5 * iqr
## upper <- q3 + 1.5 * iqr
## 
## # Calculate total co2_emission per country: emissions_by_country
## emissions_by_country <- food_consumption %>%
##   group_by(country) %>%
##   summarize(total_emission = sum(co2_emission))
## 
## # Compute the first and third quartiles and IQR of total_emission
## q1 <- quantile(emissions_by_country$total_emission, 0.25)
## q3 <- quantile(emissions_by_country$total_emission, 0.75)
## iqr <- q3 - q1
## 
## # Calculate the lower and upper cutoffs for outliers
## lower <- q1 - 1.5 * iqr
## upper <- q3 + 1.5 * iqr


## ---- eval=F-----------------------------------------------------------------------
## # edited/added
## amir_deals <- readRDS('seller_1.rds') %>%
##   select(product, client, status, amount, num_users)
## 
## # Count the deals for each product
## amir_deals %>%
##   count(product)
## 
## # Calculate probability of picking a deal with each product
## amir_deals %>%
##   count(product) %>%
##   mutate(prob = n/sum(n))


## ---- eval=F-----------------------------------------------------------------------
## # Set random seed to 31
## set.seed(31)
## 
## # Sample 5 deals without replacement
## amir_deals %>%
##   sample_n(5)
## 
## # Set random seed to 31
## set.seed(31)
## 
## # Sample 5 deals with replacement
## amir_deals %>%
##   sample_n(5, replace = TRUE)


## ---- eval=F-----------------------------------------------------------------------
## # edited/added
## restaurant_groups <- read.csv('restaurant_groups.csv')
## 
## # Create a histogram of restaurant_groups
## ggplot(restaurant_groups, aes(group_size)) +
##   geom_histogram(bins = 5)
## 
## # Create probability distribution
## size_distribution <- restaurant_groups %>%
##   # Count number of each group size
##   count(group_size) %>%
##   # Calculate probability
##   mutate(probability = n / sum(n))
## 
## size_distribution
## 
## # Create probability distribution
## size_distribution <- restaurant_groups %>%
##   count(group_size) %>%
##   mutate(probability = n / sum(n))
## 
## # Calculate expected group size
## expected_val <- sum(size_distribution$group_size *
##                     size_distribution$probability)
## expected_val
## 
## # Create probability distribution
## size_distribution <- restaurant_groups %>%
##   count(group_size) %>%
##   mutate(probability = n / sum(n))
## 
## # Calculate probability of picking group of 4 or more
## size_distribution %>%
##   # Filter for groups of 4 or larger
##   filter(group_size >= 4) %>%
##   # Calculate prob_4_or_more by taking sum of probabilities
##   summarize(prob_4_or_more = sum(probability))


## ---- eval=F-----------------------------------------------------------------------
## # Min and max wait times for back-up that happens every 30 min
## min <- 0
## max <- 30
## 
## # Min and max wait times for back-up that happens every 30 min
## min <- 0
## max <- 30
## 
## # Calculate probability of waiting less than 5 mins
## prob_less_than_5 <- punif(5, min, max)
## prob_less_than_5
## 
## # Min and max wait times for back-up that happens every 30 min
## min <- 0
## max <- 30
## 
## # Calculate probability of waiting more than 5 mins
## prob_greater_than_5 <- punif(5, min, max, lower.tail = FALSE)
## prob_greater_than_5
## 
## # Min and max wait times for back-up that happens every 30 min
## min <- 0
## max <- 30
## 
## # Calculate probability of waiting 10-20 mins
## prob_between_10_and_20 <- punif(20, min, max) - punif(10, min, max)
## prob_between_10_and_20


## ---- eval=F-----------------------------------------------------------------------
## # edited/added
## wait_times <- data.frame(simulation_nb = 1:1000)
## 
## # Set random seed to 334
## set.seed(334)
## 
## # Set random seed to 334
## set.seed(334)
## 
## # Generate 1000 wait times between 0 and 30 mins, save in time column
## wait_times %>%
##   mutate(time = runif(1000, min = 0, max = 30))
## 
## # Set random seed to 334
## set.seed(334)
## 
## # Generate 1000 wait times between 0 and 30 mins, save in time column
## wait_times %>%
##   mutate(time = runif(1000, min = 0, max = 30)) %>%
##   # Create a histogram of simulated times
##   ggplot(aes(time)) +
##   geom_histogram(bins = 30)


## ---- eval=F-----------------------------------------------------------------------
## # Set random seed to 10
## set.seed(10)
## 
## # Simulate a single deal
## rbinom(1, 1, 0.3)
## 
## # Set random seed to 10
## set.seed(10)
## 
## # Simulate 1 week of 3 deals
## rbinom(1, 3, 0.3)
## 
## # Set random seed to 10
## set.seed(10)
## 
## # Simulate 52 weeks of 3 deals
## deals <- rbinom(52, 3, 0.3)
## 
## # Calculate mean deals won per week
## mean(deals)


## ---- eval=F-----------------------------------------------------------------------
## # Probability of closing 3 out of 3 deals
## dbinom(3, 3, 0.3)
## 
## # Probability of closing <= 1 deal out of 3 deals
## pbinom(1, 3, 0.3)
## 
## # Probability of closing > 1 deal out of 3 deals
## pbinom(1, 3, 0.3, lower.tail = FALSE)


## ---- eval=F-----------------------------------------------------------------------
## # Expected number won with 30% win rate
## won_30pct <- 3 * 0.3
## won_30pct
## 
## # Expected number won with 25% win rate
## won_25pct <- 3 * 0.25
## won_25pct
## 
## # Expected number won with 35% win rate
## won_35pct <- 3 * 0.35
## won_35pct


## ---- eval=F-----------------------------------------------------------------------
## # Histogram of amount with 10 bins
## ggplot(amir_deals, aes(amount)) +
##   geom_histogram(bins = 10)


## ---- eval=F-----------------------------------------------------------------------
## # Probability of deal < 7500
## pnorm(7500, mean = 5000, sd = 2000)
## 
## # Probability of deal > 1000
## pnorm(1000, mean = 5000, sd = 2000, lower.tail = FALSE)
## 
## # Probability of deal between 3000 and 7000
## pnorm(7000, mean = 5000, sd = 2000) - pnorm(3000, mean = 5000, sd = 2000)
## 
## # Calculate amount that 75% of deals will be more than
## qnorm(0.75, mean = 5000, sd = 2000, lower.tail = FALSE)


## ---- eval=F-----------------------------------------------------------------------
## # edited/added
## new_sales <- data.frame(sale_num = 1:36)
## 
## # Calculate new average amount
## new_mean <- 5000 * 1.2
## 
## # Calculate new standard deviation
## new_sd <- 2000 * 1.3
## 
## # Simulate 36 sales
## new_sales <- new_sales %>%
##   mutate(amount = rnorm(36, mean = new_mean, sd = new_sd))
## 
## # Create histogram with 10 bins
## ggplot(new_sales, aes(amount)) +
##   geom_histogram(bins = 10)


## ---- eval=F-----------------------------------------------------------------------
## # Create a histogram of num_users
## ggplot(amir_deals, aes(num_users)) +
##   geom_histogram(bins = 10)
## 
## # Set seed to 104
## set.seed(104)
## 
## # Sample 20 num_users with replacement from amir_deals
## sample(amir_deals$num_users, size = 20, replace = TRUE) %>%
##   # Take mean
##   mean()
## 
## # Set seed to 104
## set.seed(104)
## 
## # Sample 20 num_users from amir_deals and take mean
## sample(amir_deals$num_users, size = 20, replace = TRUE) %>%
##   mean()
## 
## # Repeat the above 100 times
## sample_means <- replicate(100, sample(amir_deals$num_users, size = 20, replace = TRUE) %>% mean())
## 
## # Set seed to 104
## set.seed(104)
## 
## # Sample 20 num_users from amir_deals and take mean
## sample(amir_deals$num_users, size = 20, replace = TRUE) %>%
##   mean()
## 
## # Repeat the above 100 times
## sample_means <- replicate(100, sample(amir_deals$num_users, size = 20, replace = TRUE) %>% mean())
## 
## # Create data frame for plotting
## samples <- data.frame(mean = sample_means)
## 
## # Histogram of sample means
## ggplot(samples, aes(mean)) +
##   geom_histogram(bins = 10)


## ---- eval=F-----------------------------------------------------------------------
## # edited/added
## all_deals <- read.csv('all_deals.csv')
## 
## # Set seed to 321
## set.seed(321)
## 
## # Take 30 samples of 20 values of num_users, take mean of each sample
## sample_means <- replicate(30, sample(all_deals$num_users, 20) %>% mean())
## 
## # Calculate mean of sample_means
## mean(sample_means)
## 
## # Calculate mean of num_users in amir_deals
## mean(amir_deals$num_users)


## ---- eval=F-----------------------------------------------------------------------
## # Probability of 5 responses
## dpois(5, lambda = 4)
## 
## # Probability of 5 responses from coworker
## dpois(5, lambda = 5.5)
## 
## # Probability of 2 or fewer responses
## ppois(2, lambda = 4)
## 
## # Probability of > 10 responses
## ppois(10, lambda = 4, lower.tail = FALSE)


## ---- eval=F-----------------------------------------------------------------------
## # Probability response takes < 1 hour
## pexp(1, rate = 1/2.5)
## 
## # Probability response takes > 4 hours
## pexp(4, rate = 1/2.5, lower.tail = FALSE)
## 
## # Probability response takes 3-4 hours
## pexp(4, rate = 1/2.5) - pexp(3, rate = 1/2.5)


## ---- eval=F-----------------------------------------------------------------------
## # edited/added
## world_happiness <- readRDS('world_happiness_sugar.rds')
## 
## # Create a scatterplot of happiness_score vs. life_exp
## ggplot(world_happiness, aes(life_exp, happiness_score)) +
##   geom_point()
## 
## # Add a linear trendline to scatterplot
## ggplot(world_happiness, aes(life_exp, happiness_score)) +
##   geom_point() +
##   geom_smooth(method = "lm", se = FALSE)
## 
## # Add a linear trendline to scatterplot
## ggplot(world_happiness, aes(life_exp, happiness_score)) +
##   geom_point() +
##   geom_smooth(method = "lm", se = FALSE)
## 
## # Correlation between life_exp and happiness_score
## cor(world_happiness$life_exp, world_happiness$happiness_score)


## ---- eval=F-----------------------------------------------------------------------
## # Scatterplot of gdp_per_cap and life_exp
## ggplot(world_happiness, aes(gdp_per_cap, life_exp)) +
##   geom_point()
## 
## # Scatterplot of gdp_per_cap and life_exp
## ggplot(world_happiness, aes(gdp_per_cap, life_exp)) +
##   geom_point()
## 
## # Correlation between gdp_per_cap and life_exp
## cor(world_happiness$gdp_per_cap, world_happiness$life_exp)


## ---- eval=F-----------------------------------------------------------------------
## # Scatterplot of happiness_score vs. gdp_per_cap
## ggplot(world_happiness, aes(gdp_per_cap, happiness_score)) +
##   geom_point()
## 
## # Calculate correlation
## cor(world_happiness$gdp_per_cap, world_happiness$happiness_score)
## 
## # Create log_gdp_per_cap column
## world_happiness <- world_happiness %>%
##   mutate(log_gdp_per_cap = log(gdp_per_cap))
## 
## # Scatterplot of happiness_score vs. log_gdp_per_cap
## ggplot(world_happiness, aes(log_gdp_per_cap, happiness_score)) +
##   geom_point()
## 
## # Calculate correlation
## cor(world_happiness$log_gdp_per_cap, world_happiness$happiness_score)


## ---- eval=F-----------------------------------------------------------------------
## # Scatterplot of grams_sugar_per_day and happiness_score
## ggplot(world_happiness, aes(grams_sugar_per_day, happiness_score)) +
##   geom_point()
## 
## # Correlation between grams_sugar_per_day and happiness_score
## cor(world_happiness$grams_sugar_per_day, world_happiness$happiness_score)

