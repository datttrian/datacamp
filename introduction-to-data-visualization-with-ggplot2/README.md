**Course Description**

The ability to produce meaningful and beautiful data visualizations is
an essential part of your skill set as a data scientist. This course,
the first R data visualization tutorial in the series, introduces you to
the principles of good visualizations and the grammar of graphics
plotting concepts implemented in the ggplot2 package. ggplot2 has become
the go-to tool for flexible and professional plots in R. Here, we’ll
examine the first three essential layers for making a plot - Data,
Aesthetics and Geometries. By the end of the course you will be able to
make complex exploratory plots.

# Introduction

In this chapter we’ll get you into the right frame of mind for
developing meaningful visualizations with R. You’ll understand that as a
communications tool, visualizations require you to think about your
audience first. You’ll also be introduced to the basics of ggplot2 - the
7 different grammatical elements (layers) and aesthetic mappings.

## Introduction

### Explore and explain

In this video we made the distinction between plots for exploring and
plots for explaining data. Which of the following are exploratory plots
typically *NOT*?

- [ ] Meant for a specialist audience.
- [ ] Data-heavy.
- [x] Pretty.
- [ ] Rough first drafts.
- [ ] Part of our data science toolkit as graphical data analysis.

### Drawing your first plot

To get a first feel for `ggplot2`, let’s try to run some basic `ggplot2`
commands. The `mtcars` dataset contains information on 32 cars from a
1973 issue of Motor Trend magazine. This dataset is small, intuitive,
and contains a variety of continuous and categorical variables.

- Load the `ggplot2` package using
  [`library()`](http://www.rdocumentation.org/packages/base/functions/library).
- Use
  [`str()`](http://www.rdocumentation.org/packages/utils/functions/str)
  to explore the structure of the `mtcars` dataset.
- Hit submit. This will execute the example code on the right. See if
  you can understand what `ggplot` does with the data.

``` r
# Load the ggplot2 package
library(ggplot2)

# Explore the mtcars data frame with str()
str(mtcars)

# Execute the following command
ggplot(mtcars, aes(cyl, mpg)) +
  geom_point()
```

### Data columns types affect plot types

The plot from the previous exercise wasn’t really satisfying. Although
`cyl` (the number of cylinders) is categorical, you probably noticed
that it is classified as numeric in `mtcars`. This is really misleading
because the representation in the plot doesn’t match the actual data
type. You’ll have to explicitly tell `ggplot2` that `cyl` is a
categorical variable.

- Change the
  [`ggplot()`](http://www.rdocumentation.org/packages/ggplot2/functions/ggplot)
  command by wrapping
  [`factor()`](http://www.rdocumentation.org/packages/base/functions/factor)
  around `cyl`.
- Hit submit and see if the resulting plot is better this time.

``` r
# Load the ggplot2 package
library(ggplot2)

# Change the command below so that cyl is treated as factor
ggplot(mtcars, aes(factor(cyl), mpg)) +
  geom_point()
```

## The grammar of graphics

### Mapping data columns to aesthetics

Let’s dive a little deeper into the three main topics in this course:
The data, aesthetics, and geom layers. We’ll get to making pretty plots
in the last chapter with the themes layer.

We’ll continue working on the 32 cars in the `mtcars` data frame.

Consider how the examples and concepts we discuss throughout these
courses apply to your own data-sets!

Add a color aesthetic mapped to the displacement of the car engine:
inside
[`aes()`](http://www.rdocumentation.org/packages/ggplot2/functions/aes),
add a `color` argument equal to `disp`.

This time, map `disp` to the `size` aesthetic.

``` r
# Edit to add a color aesthetic mapped to disp
ggplot(mtcars, aes(wt, mpg, color = disp)) +
  geom_point()

# Change the color aesthetic to a size aesthetic
ggplot(mtcars, aes(wt, mpg, size = disp)) +
  geom_point()
```

### Understanding variables

In the previous exercise you saw that `disp` can be mapped onto a color
gradient or onto a continuous size scale.

Another argument of
[`aes()`](http://www.rdocumentation.org/packages/ggplot2/functions/aes)
is the `shape` of the points. There are a finite number of shapes which
[`ggplot()`](http://www.rdocumentation.org/packages/ggplot2/functions/ggplot)
can automatically assign to the points. However, if you try this command
in the console:

    ggplot(mtcars, aes(wt, mpg, shape = disp)) +
      geom_point()

It gives an error. What does this mean?

- [ ] `shape` is not a defined argument.
- [x] `shape` only makes sense with categorical data, and disp is
  continuous.
- [ ] `shape` only makes sense with continuous data, and disp is
  categorical.
- [ ] `shape` is not a variable in your dataset.
- [ ] `shape` has to be defined as a function.

## ggplot2 layers

### Adding geometries

The `diamonds` dataset contains details of 1,000 diamonds. Among the
variables included are `carat` (a measurement of the diamond’s size) and
`price`.

You’ll use two common geom layer functions:

- [`geom_point()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_point)
  adds points (as in a scatter plot).
- [`geom_smooth()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_smooth)
  adds a smooth trend curve.

As you saw previously, these are added using the `+` operator.

    ggplot(data, aes(x, y)) +
      geom_*()

Where `*` is the specific geometry needed.

Explore the `diamonds` data frame with the
[`str()`](http://www.rdocumentation.org/packages/utils/functions/str)
function.

Edit the plot code to add a point geom. Use the `+` operator to add
[`geom_point()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_point)
to the
[`ggplot()`](http://www.rdocumentation.org/packages/ggplot2/functions/ggplot)
command.

Add a smooth geom to the plot. Use the `+` operator to add
[`geom_smooth()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_smooth).

``` r
# Explore the diamonds data frame with str()
str(diamonds)

# Add geom_point() with +
ggplot(diamonds, aes(carat, price)) +
  geom_point()

# Add geom_smooth() with +
ggplot(diamonds, aes(carat, price)) +
  geom_point() +
  geom_smooth()
```

### Changing one geom or every geom

If you have multiple geoms, then mapping an aesthetic to data variable
inside the call to `ggplot()` will change *all* the geoms. It is also
possible to make changes to *individual* geoms by passing arguments to
the `geom_*()` functions.

`geom_point()` has an `alpha` argument that controls the opacity of the
points. A value of `1` (the default) means that the points are totally
opaque; a value of `0` means the points are totally transparent (and
therefore invisible). Values in between specify transparency.

The plot you drew last time is provided in the script.

Edit the plot code to map the `color` aesthetic to the `clarity` data
variable.

Make the points translucent by setting the `alpha` argument to `0.4`.

``` r
# Map the color aesthetic to clarity
ggplot(diamonds, aes(carat, price, color = clarity)) +
  geom_point() +
  geom_smooth()

# Make the points 40% opaque
ggplot(diamonds, aes(carat, price, color = clarity)) +
  geom_point(alpha = 0.4) +
  geom_smooth()
```

### Saving plots as variables

Plots can be saved as variables, which can be added to later on using
the `+` operator. This is really useful if you want to make multiple
related plots from a common base.

- Using the `diamonds` dataset, plot the `price` (y-axis) versus the
  `carat` (x-axis), assigning to `plt_price_vs_carat`.
- Using `geom_point()`, add a point layer to `plt_price_vs_carat`.
- Add an `alpha` argument to the point layer to make the points 20%
  opaque, assigning to `plt_price_vs_carat_transparent`.
- Type the plot’s variable name (`plt_price_vs_carat_transparent`) to
  display it.
- Inside `geom_point()`, call `aes()` and map `color` to `clarity`,
  assigning to `plt_price_vs_carat_by_clarity`.
- Type the plot’s variable name (`plt_price_vs_carat_by_clarity`) to
  display it.

``` r
# Draw a ggplot
plt_price_vs_carat <- ggplot(
  # Use the diamonds dataset
  diamonds,
  # For the aesthetics, map x to carat and y to price
  aes(carat, price)
)

# Add a point layer to plt_price_vs_carat
plt_price_vs_carat + geom_point()

# From previous step
plt_price_vs_carat <- ggplot(diamonds, aes(carat, price))

# Edit this to make points 20% opaque: plt_price_vs_carat_transparent
plt_price_vs_carat_transparent <- plt_price_vs_carat + geom_point(alpha = 0.2)

# See the plot
plt_price_vs_carat_transparent

# From previous step
plt_price_vs_carat <- ggplot(diamonds, aes(carat, price))

# Edit this to map color to clarity
# Assign the updated plot to a new object
plt_price_vs_carat_by_clarity <- plt_price_vs_carat + geom_point(aes(color = clarity))

# See the plot
plt_price_vs_carat_by_clarity
```

# Aesthetics

Aesthetic mappings are the cornerstone of the grammar of graphics
plotting concept. This is where the magic happens - converting
continuous and categorical data into visual scales that provide access
to a large amount of information in a very short time. In this chapter
you’ll understand how to choose the best aesthetic mappings for your
data.

## Visible aesthetics

### All about aesthetics: color, shape and size

In the video you saw 9 visible aesthetics. Let’s apply them to a
categorical variable — the cylinders in `mtcars`, `cyl`.

These are the aesthetics you can consider within
[`aes()`](http://www.rdocumentation.org/packages/ggplot2/functions/aes)
in this chapter: `x`, `y`, `color`, `fill`, `size`, `alpha`, `labels`
and `shape`.

One common convention is that you don’t name the `x` and `y` arguments
to `aes()`, since they almost always come first, but you do name other
arguments.

In the following exercise the `fcyl` column is categorical. It is `cyl`
transformed into a `factor`.

Map `mpg` onto the `x` aesthetic, and `fcyl` onto the `y`.

Swap the mappings of the first plot: `fcyl` onto the `x` aesthetic, and
`mpg` onto the `y`.

Map `wt` onto `x`, `mpg` onto `y`, and `fcyl` onto `color`.

Modify the point layer of the previous plot by changing the `shape`
argument to `1` and increasing the `size` to `4`.

``` r
# edited/added
library(tidyverse)
mtcars <- mtcars %>% 
  mutate(fcyl = as.factor(cyl),
         fam = as.factor(am)) %>% 
  mutate(fam = fct_recode(fam,
                          "manual" = "1",
                         "automatic" = "0"))

# Map x to mpg and y to fcyl
ggplot(mtcars, aes(mpg, fcyl)) +
  geom_point()

# Swap mpg and fcyl
ggplot(mtcars, aes(fcyl, mpg)) +
  geom_point()

# Map x to wt, y to mpg and color to fcyl
ggplot(mtcars, aes(wt, mpg, color = fcyl)) +
  geom_point()

ggplot(mtcars, aes(wt, mpg, color = fcyl)) +
  # Set the shape and size of the points
  geom_point(shape = 1, size = 4)
```

### All about aesthetics: color vs. fill

Typically, the `color` aesthetic changes the *outline* of a geom and the
`fill` aesthetic changes the *inside*. `geom_point()` is an exception:
you use `color` (not `fill`) for the point color. However, some shapes
have special behavior.

The default `geom_point()` uses `shape = 19`: a solid circle. An
alternative is `shape = 21`: a circle that allow you to use *both*
`fill` for the inside *and* `color` for the outline. This is lets you to
map two aesthetics to each point.

All shape values are described on the
[`points()`](https://www.rdocumentation.org/packages/graphics/topics/points)
help page.

`fcyl` and `fam` are the `cyl` and `am` columns converted to factors,
respectively.

Change the aesthetics so that `fcyl` maps to `fill` rather than `color`.

In `geom_point()` change the `shape` argument to `21` and add an `alpha`
argument set to `0.6`.

In the `ggplot()` aesthetics, map `fam` to `color`.

``` r
# Map fcyl to fill
ggplot(mtcars, aes(wt, mpg, fill = fcyl)) +
  geom_point(shape = 1, size = 4)

ggplot(mtcars, aes(wt, mpg, fill = fcyl)) +
  # Change point shape; set alpha
  geom_point(shape = 21, size = 4, alpha = 0.6)

# Map color to fam
ggplot(mtcars, aes(wt, mpg, fill = fcyl, color = fam)) +
  geom_point(shape = 21, size = 4, alpha = 0.6)
```

### All about aesthetics: comparing aesthetics

Now that you’ve got some practice with using attributes, be careful of a
major pitfall: these attributes can overwrite the aesthetics of your
plot!

- Using `mtcars`, create a plot base layer, `plt_mpg_vs_wt`. Map `mpg`
  onto `y` and `wt` onto `x`.
- Add a point layer, mapping the categorical no. of cylinders, `fcyl`,
  onto `size`.

Change the mapping. This time `fcyl` should be mapped onto `alpha`.

Change the mapping again. This time `fcyl` should be mapped onto
`shape`.

- Swap the geom layer: change points to text.
- Change the mapping again. This time `fcyl` should be mapped onto
  `label`.

``` r
# Establish the base layer
plt_mpg_vs_wt <- ggplot(mtcars, aes(wt, mpg))

# Map fcyl to size
plt_mpg_vs_wt +
  geom_point(aes(size = fcyl))

# Base layer
plt_mpg_vs_wt <- ggplot(mtcars, aes(wt, mpg))

# Map fcyl to alpha, not size
plt_mpg_vs_wt +
  geom_point(aes(alpha = fcyl))

# Base layer
plt_mpg_vs_wt <- ggplot(mtcars, aes(wt, mpg))

# Map fcyl to shape, not alpha
plt_mpg_vs_wt +
  geom_point(aes(shape = fcyl))

# Base layer
plt_mpg_vs_wt <- ggplot(mtcars, aes(wt, mpg))

# Use text layer and map fcyl to label
plt_mpg_vs_wt +
  geom_text(aes(label = fcyl))
```

### Aesthetics for categorical & continuous variables

Many of the aesthetics can accept either continuous or categorical
variables, but some are restricted to categorical data. Which aesthetics
are only applicable to categorical data?

- [ ] `color` & `fill`
- [ ] `alpha` & `size`
- [x] `label` & `shape`
- [ ] `alpha` & `label`
- [ ] `x` & `y`

## Using attributes

### All about attributes: color, shape, size and alpha

This time you’ll use these arguments to set *attributes* of the plot,
not map variables onto *aesthetics*.

You can specify colors in R using **hex codes**: a hash followed by two
hexadecimal numbers each for red, green, and blue (`"#RRGGBB"`).
Hexadecimal is base-16 counting. You have 0 to 9, and A representing 10
up to F representing 15. Pairs of hexadecimal numbers give you a range
from 0 to 255. `"#000000"` is “black” (no color), `"#FFFFFF"` means
“white”, and \`“\#00FFFF” is cyan (mixed green and blue).

A hexadecimal color variable, `my_blue` has been defined for you.

Set the point color to `my_blue` and the alpha to `0.6`.

- Change the `color` mapping to a `fill` mapping. That is, `fcyl` should
  be mapped onto `fill`.
- Set the `color` of the points to `my_blue`, point `size` to `10` and
  the point `shape` to `1`.

``` r
# A hexadecimal color
my_blue <- "#4ABEFF"

ggplot(mtcars, aes(wt, mpg)) +
  # Set the point color to my_blue
  geom_point(color = my_blue, alpha = 0.6)

# A hexadecimal color
my_blue <- "#4ABEFF"

# Change the color mapping to a fill mapping
ggplot(mtcars, aes(wt, mpg, fill = fcyl)) +
  # Set point size to 10; shape to 1
  geom_point(color = my_blue, size = 10, shape = 1)
```

### All about attributes: conflicts with aesthetics

In the videos you saw that you can use all the aesthetics as attributes.
Let’s see how this works with the aesthetics you used in the previous
exercises: `x`, `y`, `color`, `fill`, `size`, `alpha`, `label` and
`shape`.

In this exercise you will set all kinds of attributes of the points!

You will continue to work with `mtcars`.

Add a point layer, setting `alpha`, the transparency, to `0.5`.

Add a text layer, setting the `label` to the rownames of the dataset
`mtcars`, and the `color` to `"red"`.

Add a point layer, setting the `shape` to `24` and the `color` to
`"yellow"`.

``` r
ggplot(mtcars, aes(wt, mpg, color = fcyl)) +
  # Add point layer with alpha 0.5
  geom_point(alpha = 0.5)

ggplot(mtcars, aes(wt, mpg, color = fcyl)) +
  # Add text layer with label rownames(mtcars) and color red
  geom_text(label = rownames(mtcars), color = 'red')

ggplot(mtcars, aes(wt, mpg, color = fcyl)) +
  # Add points layer with shape 24 and color yellow
  geom_point(shape = 24, color = 'yellow')
```

### Going all out

In this exercise, you will gradually add more aesthetics layers to the
plot. You’re still working with the `mtcars` dataset, but this time
you’re using more features of the cars. Each of the columns is described
on the
[`mtcars`](https://www.rdocumentation.org/packages/datasets/topics/mtcars)
help page. Columns `fcyl` and `fam` have been added (as before) as
categorical versions of `cyl` and `am` respectively.

Notice that adding more aesthetic mappings to your plot is not always a
good idea! You may just increase complexity and decrease readability.

- Use `mtcars` to draw a plot of `qsec` vs. `mpg`, colored by `fcyl`.
- Add a point layer.

Add another aesthetic: map `fam` onto `shape`.

Add another two aesthetics: map `hp` *divided by* `wt` onto `size`.

``` r
# 3 aesthetics: qsec vs. mpg, colored by fcyl
ggplot(mtcars, aes(mpg, qsec, color = fcyl)) +
  geom_point()

# 4 aesthetics: add a mapping of shape to fam
ggplot(mtcars, aes(mpg, qsec, color = fcyl, shape = fam)) +
  geom_point()

# 5 aesthetics: add a mapping of size to hp / wt
ggplot(mtcars, aes(mpg, qsec, color = fcyl, shape = fam, size = hp / wt)) +
  geom_point()
```

## Modifying aesthetics

### Updating aesthetic labels

In this exercise, you’ll modify some aesthetics to make a bar plot of
the number of cylinders for cars with different types of transmission.

You’ll also make use of some functions for improving the appearance of
the plot.

- [`labs()`](https://www.rdocumentation.org/packages/ggplot2/topics/labs)
  to set the x- and y-axis labels. It takes strings for each argument.
- [`scale_fill_manual()`](https://www.rdocumentation.org/packages/ggplot2/topics/scale_manual)
  defines properties of the color scale (i.e. axis). The first argument
  sets the legend title. `values` is a named vector of colors to use.

Set the x-axis label to `"Number of Cylinders"`, and the y-axis label to
`"Count"` using the `x` and `y` arguments of
[`labs()`](https://www.rdocumentation.org/packages/ggplot2/topics/labs),
respectively.

Implement a custom fill color scale using
[`scale_fill_manual()`](https://www.rdocumentation.org/packages/ggplot2/topics/scale_manual).
Set the first argument to `"Transmission"`, and `values` to `palette`.

Modify the code to set the `position` to `dodge` so that the bars for
transmissions are displayed side by side.

``` r
ggplot(mtcars, aes(fcyl, fill = fam)) +
  geom_bar() +
  # Set the axis labels
  labs(x = "Number of Cylinders", y = "Count")

palette <- c(automatic = "#377EB8", manual = "#E41A1C")

ggplot(mtcars, aes(fcyl, fill = fam)) +
  geom_bar() +
  labs(x = "Number of Cylinders", y = "Count")
  # Set the fill color scale
  scale_fill_manual("Transmission", values = palette)
  
  palette <- c(automatic = "#377EB8", manual = "#E41A1C")

# Set the position
ggplot(mtcars, aes(fcyl, fill = fam)) +
  geom_bar(position = 'dodge') +
  labs(x = "Number of Cylinders", y = "Count")
  scale_fill_manual("Transmission", values = palette)
```

### Setting a dummy aesthetic

In the last chapter you saw that all the visible aesthetics can serve as
attributes and aesthetics, but I very conveniently left out x and y.
That’s because although you can make univariate plots (such as
histograms, which you’ll get to in the next chapter), a y-axis will
always be provided, even if you didn’t ask for it.

You can make univariate plots in `ggplot2`, but you will need to add a
fake y axis by mapping `y` to zero.

When using setting y-axis limits, you can specify the limits as separate
arguments, or as a single numeric vector. That is, `ylim(lo, hi)` or
`ylim(c(lo, hi))`.

- Using `mtcars`, plot `0` vs. `mpg`.
- Make a scatter plot and add `"jitter"` to it.

Use `ylim()` to set the limits on the y-axis from `-2` to `2`.

``` r
# Plot 0 vs. mpg
ggplot(mtcars, aes(mpg, 0)) +
  # Add jitter
  geom_point(position="jitter")

ggplot(mtcars, aes(mpg, 0)) +
  geom_jitter() +
  # Set the y-axis limits from -2 to 2
  ylim(-2, 2)
```

## Aesthetics best practices

### Appropriate mappings

Incorrect aesthetic mapping causes confusion or misleads the audience.

Typically, the **dependent** variable is mapped onto the the **y**-axis
and the **independent** variable is mapped onto the **x**-axis.

In the `ToothGrowth` data set, we have three variables:

| Variable | Description                |
|----------|----------------------------|
| `len`    | Tooth length               |
| `supp`   | Supplement type (VC or OJ) |
| `dose`   | Dose in milligrams/day     |

From the six possible ways to map three variables, one solution is shown
in the viewer. Which of the options below leads to the plot shown?

- [x] `x = supp, y = len, color = dose`
- [ ] `x = dose, y = supp, color = len`
- [ ] `x = len, y = dose, color = supp`
- [ ] `x = len, y = supp, color = dose`
- [ ] `x = supp, y = dose, color = len`

# Geometries

A plot’s geometry dictates what visual elements will be used. In this
chapter, we’ll familiarize you with the geometries used in the three
most common plot types you’ll encounter - scatter plots, bar charts and
line plots. We’ll look at a variety of different ways to construct these
plots.

## Scatter plots

### Overplotting 1: large datasets

Scatter plots (using `geom_point()`) are intuitive, easily understood,
and very common, but we must *always* consider **overplotting**,
particularly in the following four situations:

1.  Large datasets
2.  Aligned values on a single axis
3.  Low-precision data
4.  Integer data

Typically, *alpha* blending (i.e. adding transparency) is recommended
when using solid shapes. Alternatively, you can use opaque, hollow
shapes.

Small points are suitable for large datasets with regions of high
density (lots of overlapping).

Let’s use the `diamonds` dataset to practice dealing with the large
dataset case.

Add a points layer to the base plot.

- Set the point transparency to `0.5`.
- Set `shape = "."`, the point size of 1 pixel.

Update the point shape to remove the line outlines by setting `shape` to
`16`.

``` r
# Plot price vs. carat, colored by clarity
plt_price_vs_carat_by_clarity <- ggplot(diamonds, aes(carat, price, color = clarity))

# Add a point layer with tiny points
plt_price_vs_carat_by_clarity + geom_point(alpha = 0.5, shape = ".")

# Plot price vs. carat, colored by clarity
plt_price_vs_carat_by_clarity <- ggplot(diamonds, aes(carat, price, color = clarity))

# Set transparency to 0.5
plt_price_vs_carat_by_clarity + geom_point(alpha = 0.5, shape = 16)
```

### Overplotting 2: Aligned values

Let’s take a look at another case where we should be aware of
overplotting: Aligning values on a single axis.

This occurs when one axis is continuous and the other is categorical,
which can be overcome with some form of jittering.

In the `mtcars` data set, `fam` and `fcyl` are categorical variants of
`cyl` and `am`.

- Create a base plot `plt_mpg_vs_fcyl_by_fam` of `fcyl` by `mpg`,
  colored by `fam`.
- Add a points layer to the base plot.

Add some jittering by using `position_jitter()`, setting the `width` to
`0.3`.

Alternatively, use `position_jitterdodge()`. Set `jitter.width` and
`dodge.width` to `0.3` to separate subgroups further.

``` r
# Plot base
plt_mpg_vs_fcyl_by_fam <- ggplot(mtcars, aes(fcyl, mpg, color = fam))

# Default points are shown for comparison
plt_mpg_vs_fcyl_by_fam + geom_point()

# Plot base
plt_mpg_vs_fcyl_by_fam <- ggplot(mtcars, aes(fcyl, mpg, color = fam))

# Default points are shown for comparison
plt_mpg_vs_fcyl_by_fam + geom_point()

# Alter the point positions by jittering, width 0.3
plt_mpg_vs_fcyl_by_fam + geom_point(position = position_jitter(width = 0.3))

# Plot base
plt_mpg_vs_fcyl_by_fam <- ggplot(mtcars, aes(fcyl, mpg, color = fam))

# Default points are shown for comparison
plt_mpg_vs_fcyl_by_fam + geom_point()

# Now jitter and dodge the point positions
plt_mpg_vs_fcyl_by_fam + geom_point(position = position_jitterdodge(jitter.width = 0.3, dodge.width = 0.3))
```

### Overplotting 3: Low-precision data

You already saw how to deal with overplotting when using
[`geom_point()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_point)
in two cases:

1.  Large datasets
2.  Aligned values on a single axis

We used `position = 'jitter'` inside
[`geom_point()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_point)
or
[`geom_jitter()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_jitter).

Let’s take a look at another case:

1.  Low-precision data

This results from low-resolution measurements like in the iris dataset,
which is measured to 1mm precision (see viewer). It’s similar to case 2,
but in this case we can jitter on both the x and y axis.

- Change the points layer into a jitter layer.
- Reduce the jitter layer’s width by setting the `width` argument to
  `0.1`.

Let’s use a different approach:

- Within `geom_point()`, set `position` to `"jitter"`.

Provide an alternative specification:

- Have the `position` argument call `position_jitter()` with a `width`
  of `0.1`.

``` r
ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  # Swap for jitter layer with width 0.1
  geom_jitter(alpha = 0.5, width = 0.1)

ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  # Set the position to jitter
  geom_point(alpha = 0.5, position = "jitter")

ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  # Use a jitter position function with width 0.1
  geom_point(alpha = 0.5, position = position_jitter(width = 0.1))
```

### Overplotting 4: Integer data

Let’s take a look at the last case of dealing with overplotting:

1.  Integer data

This can be type `integer` (i.e. 1 ,2, 3…) or categorical (i.e. class
`factor`) variables. `factor` is just a special class of type `integer`.

You’ll typically have a small, defined number of intersections between
two variables, which is similar to case 3, but you may miss it if you
don’t realize that integer and factor data are the same as low precision
data.

The `Vocab` dataset provided contains the years of education and
vocabulary test scores from respondents to US General Social Surveys
from 1972-2004.

- Examine the `Vocab` dataset using `str()`.
- Using `Vocab`, draw a plot of `vocabulary` vs `education`.
- Add a point layer.

<!-- -->

- Replace the point layer with a jitter layer.

<!-- -->

- Set the jitter transparency to `0.2`.

<!-- -->

- Set the shape of the jittered points to hollow circles, (shape `1`).

``` r
# edited/added
library(carData)

# Examine the structure of Vocab
str(Vocab)

# Plot vocabulary vs. education
ggplot(Vocab, aes(education, vocabulary)) +
  # Add a point layer
  geom_point()

ggplot(Vocab, aes(education, vocabulary)) +
  # Change to a jitter layer
  geom_jitter()

ggplot(Vocab, aes(education, vocabulary)) +
  # Set the transparency to 0.2
  geom_jitter(alpha = 0.2)

ggplot(Vocab, aes(education, vocabulary)) +
  # Set the shape to 1
  geom_jitter(alpha = 0.2, shape = 1)
```

## Histograms

### Drawing histograms

Recall that histograms cut up a continuous variable into discrete bins
and, by default, maps the internally calculated `count` variable (the
number of observations in each bin) onto the y aesthetic. An internal
variable called `density` can be accessed by using the `..` notation,
i.e. `..density..`. Plotting this variable will show the relative
frequency, which is the height times the width of each bin.

- Using `mtcars`, map `mpg` onto the x aesthetic.
- Add a histogram layer using `geom_histogram()`.

<!-- -->

- Set the histogram `binwidth` to `1`.

<!-- -->

- Map `y` to the internal variable `..density..` to show frequency
  densities.

<!-- -->

- Set the `fill` color of the histogram bars to `datacamp_light_blue`.

``` r
# Plot mpg
ggplot(mtcars, aes(mpg)) +
  # Add a histogram layer
  geom_histogram()

ggplot(mtcars, aes(mpg)) +
  # Set the binwidth to 1
  geom_histogram(binwidth = 1)

# Map y to ..density..
ggplot(mtcars, aes(mpg, ..density..)) +
  geom_histogram(binwidth = 1)

datacamp_light_blue <- "#51A8C9"

ggplot(mtcars, aes(mpg, ..density..)) +
  # Set the fill color to datacamp_light_blue
  geom_histogram(binwidth = 1, fill = datacamp_light_blue)
```

### Positions in histograms

Here, we’ll examine the various ways of applying positions to
histograms.
[`geom_histogram()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_histogram),
a special case of
[`geom_bar()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_bar),
has a `position` argument that can take on the following values:

- `stack` (the default): Bars for different groups are stacked on top of
  each other.
- `dodge`: Bars for different groups are placed side by side.
- `fill`: Bars for different groups are shown as proportions.
- `identity`: Plot the values as they appear in the dataset.

Update the aesthetics so that the fill color of the bars is determined
by `fam`.

Update the histogram layer to position the bars side-by-side, that is,
`"dodge"`.

Update the histogram layer so the bars’ positions `"fill"` the y-axis.

Update the histogram layer so bars are top of each other, using the
`"identity"` position. So each bar can be seen, set `alpha` to `0.4`.

``` r
# Update the aesthetics so the fill color is by fam
ggplot(mtcars, aes(mpg, fill = fam)) +
  geom_histogram(binwidth = 1)

ggplot(mtcars, aes(mpg, fill = fam)) +
  # Change the position to dodge
  geom_histogram(binwidth = 1, position = "dodge")

ggplot(mtcars, aes(mpg, fill = fam)) +
  # Change the position to fill
  geom_histogram(binwidth = 1, position = "fill")

ggplot(mtcars, aes(mpg, fill = fam)) +
  # Change the position to identity, with transparency 0.4
  geom_histogram(binwidth = 1, position = "identity", alpha = 0.4)
```

## Bar plots

### Position in bar and col plots

Let’s see how the `position` argument changes
[`geom_bar()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_bar).

We have three position options:

- `stack`: The default
- `dodge`: Preferred
- `fill`: To show proportions

While we will be using `geom_bar()` here, note that the function
[`geom_col()`](http://www.rdocumentation.org/packages/ggplot2/functions/geom_col)
is just `geom_bar()` where both the `position` and `stat` arguments are
set to `"identity"`. It is used when we want the heights of the bars to
represent the exact values in the data.

In this exercise, you’ll draw the total count of cars having a given
number of cylinders (`fcyl`), according to manual or automatic
transmission type (`fam`).

- Using `mtcars`, plot `fcyl`, filled by `fam`.
- Add a bar layer using `geom_bar()`.

Set the bar `position` argument to `"fill"`.

Change the bar `position` argument to `"dodge"`.

``` r
# Plot fcyl, filled by fam
ggplot(mtcars, aes(fcyl, fill = fam)) +
  # Add a bar layer
  geom_bar()

ggplot(mtcars, aes(fcyl, fill = fam)) +
  # Set the position to "fill"
  geom_bar(position = "fill")

ggplot(mtcars, aes(fcyl, fill = fam)) +
  # Change the position to "dodge"
  geom_bar(position = "dodge")
```

### Overlapping bar plots

You can customize bar plots further by adjusting the dodging so that
your bars partially overlap each other. Instead of using
`position = "dodge"`, you’re going to use `position_dodge()`, like you
did with `position_jitter()` in the the previous exercises. Here, you’ll
save this as an object, `posn_d`, so that you can easily reuse it.

Remember, the reason you want to use `position_dodge()` (and
`position_jitter()`) is to specify *how much* dodging (or jittering) you
want.

For this example, you’ll use the `mtcars` dataset.

- Use the functional form of the bar position: replace `"dodge"` with a
  call to `position_dodge()`.
- Set its `width` to `0.2`.

<!-- -->

- Set the bar transparency level of the bars to `0.6`.

``` r
ggplot(mtcars, aes(cyl, fill = fam)) +
  # Change position to use the functional form, with width 0.2
  geom_bar(position = position_dodge(width = 0.2))

ggplot(mtcars, aes(cyl, fill = fam)) +
  # Set the transparency to 0.6
  geom_bar(position = position_dodge(width = 0.2), alpha = 0.6)
```

### Bar plots: sequential color palette

In this bar plot, we’ll fill each segment according to an ordinal
variable. The best way to do that is with a sequential color palette.

Here’s an example of using a sequential color palette with the `mtcars`
dataset:

    ggplot(mtcars, aes(fcyl, fill = fam)) +
      geom_bar() +
      scale_fill_brewer(palette = "Set1")

In the exercise, you’ll use similar code on the the `Vocab` dataset.
Both datasets are **ordinal**.

- Plot the `Vocab` dataset, mapping `education` onto `x` and
  `vocabulary` onto `fill`.
- Add a bar layer, setting `position` to `"fill"`.
- Add a brewer fill scale, using the default palette (don’t pass any
  arguments). Notice how this generates a warning message and an
  incomplete plot.

``` r
# Plot education, filled by vocabulary
ggplot(Vocab, aes(education, fill = vocabulary))

# Plot education, filled by vocabulary
ggplot(Vocab, aes(education, fill = vocabulary)) +
  # Add a bar layer with position "fill"
  geom_bar(position = "fill")

# Plot education, filled by vocabulary
ggplot(Vocab, aes(education, fill = vocabulary)) +
  # Add a bar layer with position "fill"
  geom_bar(position = "fill") +
  # Add a brewer fill scale with default palette
  scale_fill_brewer()
```

## Line plots

### Basic line plots

Here, we’ll use the `economics` dataset to make some line plots. The
dataset contains a time series for unemployment and population
statistics from the Federal Reserve Bank of St. Louis in the United
States. The data is contained in the `ggplot2` package.

To begin with, you can look at how the median unemployment time and the
unemployment rate (the number of unemployed people as a proportion of
the population) change over time.

- Print the head of the `economics` dataset.
- Plot `unemploy` vs. `date` as a line plot.

<!-- -->

- Adjust the y-axis aesthetic of the plot so that it represents the
  proportion of the `pop`ulation that is `unemploy`ed.

``` r
# Print the head of economics
head(economics)

# Using economics, plot unemploy vs. date
ggplot(economics, aes(date, unemploy)) +
  # Make it a line plot
  geom_line()

# Change the y-axis to the proportion of the population that is unemployed
ggplot(economics, aes(date, unemploy / pop)) +
  geom_line()
```

### Multiple time series

We already saw how the form of your data affects how you can plot it.
Let’s explore that further with multiple time series. Here, it’s
important that all lines are on the same scale, and if possible, on the
same plot.

`fish.species` contains the global capture rates of seven salmon species
from 1950–2010. Each variable (column) is a Salmon species and each
observation (row) is one year. `fish.tidy` contains the same data, but
in three columns: `Species`, `Year`, and `Capture` (i.e. one variable
per column).

- Use `str()` in the console to examine the structure of both
  `fish.species` and `fish.tidy`.
- Plot only the `Rainbow` salmon time series with `geom_line()`.
- Plot only the `Pink` salmon time series with `geom_line()`.

Now try and plot all time series in a single plot.

- Plot the `fish.tidy` dataset, mapping `Year` to `x` and `Capture` to
  `y`.
- `group` by fish species within the aesthetics of `geom_line()`.

Let’s add color to the previous plot to distinguish between the
different time series.

Plot the `fish.tidy` dataset again, this time making sure to `color` by
`Species`.

``` r
# edited/added
load("fish.RData")
fish.tidy <- gather(fish.species, Species, Capture, -Year)

# Plot the Rainbow Salmon time series
ggplot(fish.species, aes(x = Year, y = Rainbow)) +
  geom_line()

# Plot the Rainbow Salmon time series
ggplot(fish.species, aes(x = Year, y = Rainbow)) +
  geom_line()

# Plot the Pink Salmon time series
ggplot(fish.species, aes(x = Year, y = Pink)) +
  geom_line()

# Plot the Rainbow Salmon time series
ggplot(fish.species, aes(x = Year, y = Rainbow)) +
  geom_line()

# Plot the Pink Salmon time series
ggplot(fish.species, aes(x = Year, y = Pink)) +
  geom_line()

# Plot multiple time-series by grouping by species
ggplot(fish.tidy, aes(Year, Capture)) +
  geom_line(aes(group = Species))

# Plot the Rainbow Salmon time series
ggplot(fish.species, aes(x = Year, y = Rainbow)) +
  geom_line()

# Plot the Pink Salmon time series
ggplot(fish.species, aes(x = Year, y = Pink)) +
  geom_line()

# Plot multiple time-series by grouping by species
ggplot(fish.tidy, aes(Year, Capture)) +
  geom_line(aes(group = Species))

# Plot multiple time-series by coloring by species
ggplot(fish.tidy, aes(Year, Capture, color = Species)) +
  geom_line()
```

# Themes

In this chapter, we’ll explore how understanding the structure of your
data makes data visualization much easier. Plus, it’s time to make our
plots pretty. This is the last step in the data viz process. The Themes
layer will enable you to make publication quality plots directly in R.
In the next course we’ll look at some extra layers to add more variables
to your plots.

## Themes from scratch

### Moving the legend

Let’s wrap up this course by making a publication-ready plot
communicating a clear message.

To change stylistic elements of a plot, call
[`theme()`](http://www.rdocumentation.org/packages/ggplot2/functions/theme)
and set plot properties to a new value. For example, the following
changes the legend position.

    p + theme(legend.position = new_value)

Here, the new value can be

- `"top"`, `"bottom"`, `"left"`, or `"right'"`: place it at that side of
  the plot.
- `"none"`: don’t draw it.
- `c(x, y)`: `c(0, 0)` means the bottom-left and `c(1, 1)` means the
  top-right.

Let’s revisit the recession period line plot (assigned to
`plt_prop_unemployed_over_time`).

- Update the plot to remove the legend.
- *Look at the changes in the plot.*

<!-- -->

- Update the plot to position the legend at the bottom of the plot.
- *Look at the changes in the plot.*

<!-- -->

- Position the legend inside the plot, with x-position `0.6` and
  y-position `0.1`.
- *Look at the changes in the plot.*

``` r
# edited/added
library(lubridate)
recess <- read.csv('recess.csv') %>% 
  mutate(begin = ymd(begin), end = ymd(end))
plt_prop_unemployed_over_time <- ggplot(economics, aes(x = date, y = unemploy/pop)) +
  ggtitle(c("The percentage of unemployed Americans \n increases sharply during recessions")) +
  geom_line() +
  geom_rect(data = recess, 
            aes(xmin = begin, xmax = end, ymin = -Inf, ymax = +Inf, fill = "Recession"), 
            inherit.aes = FALSE, alpha = 0.2) +
  geom_label(data = recess, aes(x = end, y = y, label=event), size = 3) + 
    scale_fill_manual(name = "", values="red", label="Recessions")

# View the default plot
plt_prop_unemployed_over_time

# Remove legend entirely
plt_prop_unemployed_over_time +
  theme(legend.position = "none")

# Position the legend at the bottom of the plot
plt_prop_unemployed_over_time +
  theme(legend.position = "bottom")

# Position the legend inside the plot at (0.6, 0.1)
plt_prop_unemployed_over_time +
  theme(legend.position = c(0.6, 0.1))
```

### Modifying theme elements

Many plot elements have multiple properties that can be set. For
example, line elements in the plot such as axes and gridlines have a
color, a thickness (`size`), and a line type (solid line, dashed, or
dotted). To set the style of a line, you use
[`element_line()`](https://www.rdocumentation.org/packages/ggplot2/topics/margin).
For example, to make the axis lines into red, dashed lines, you would
use the following.

    p + theme(axis.line = element_line(color = "red", linetype = "dashed"))

Similarly, `element_rect()` changes rectangles and `element_text()`
changes text. You can remove a plot element using `element_blank()`.

`plt_prop_unemployed_over_time` is available.

- Give all rectangles in the plot, (the `rect` element) a `fill` color
  of `"grey92"` (very pale grey).
- Remove the `legend.key`’s outline by setting its `color` to be
  missing.
- *Look at the changes in the plot.*

<!-- -->

- Remove the axis ticks, `axis.ticks` by making them a blank element.
- Remove the panel gridlines, `panel.grid` in the same way.
- *Look at the changes in the plot.*

<!-- -->

- Add the major horizontal grid lines back to the plot using
  `panel.grid.major.y`.
  - Set the line `color` to `"white"`, `size` to `0.5`, and `linetype`
    to `"dotted"`.
- *Look at the changes in the plot.*

<!-- -->

- Make the axis tick labels’ text, `axis.text`, less prominent by
  changing the `color` to `"grey25"`.
- Increase the `plot.title`’s, `size` to `16` and change its font `face`
  to `"italic"`.
- *Look at the changes in the plot.*

``` r
plt_prop_unemployed_over_time +
  theme(
    # For all rectangles, set the fill color to grey92
    rect = element_rect(fill = "grey92"),
    # For the legend key, turn off the outline
    legend.key = element_rect(color = NA)
  )

plt_prop_unemployed_over_time +
  theme(
    rect = element_rect(fill = "grey92"),
    legend.key = element_rect(color = NA),
    # Turn off axis ticks
    axis.ticks = element_blank(),
    # Turn off the panel grid
    panel.grid = element_blank()
  )

plt_prop_unemployed_over_time +
  theme(
    rect = element_rect(fill = "grey92"),
    legend.key = element_rect(color = NA),
    axis.ticks = element_blank(),
    panel.grid = element_blank(),
    # Add major y-axis panel grid lines back
    panel.grid.major.y = element_line(
      # Set the color to white
      color = "white",
      # Set the size to 0.5
      size = 0.5,
      # Set the line type to dotted
      linetype = "dotted"
    )
  )

plt_prop_unemployed_over_time +
  theme(
    rect = element_rect(fill = "grey92"),
    legend.key = element_rect(color = NA),
    axis.ticks = element_blank(),
    panel.grid = element_blank(),
    panel.grid.major.y = element_line(
      color = "white",
      size = 0.5,
      linetype = "dotted"
    ),
    # Set the axis text color to grey25
    axis.text = element_text(color = "grey25"),
    # Set the plot title font face to italic and font size to 16
    plot.title = element_text(face = "italic", size = 16)
  )
```

### Modifying whitespace

**Whitespace** means all the non-visible margins and spacing in the
plot.

To set a single whitespace value, use
[`unit(x, unit)`](https://www.rdocumentation.org/packages/grid/topics/unit),
where `x` is the amount and `unit` is the unit of measure.

Borders require you to set 4 positions, so use
[`margin(top, right, bottom, left, unit)`](https://www.rdocumentation.org/packages/ggplot2/topics/margin).
To remember the margin order, think **TRouBLe**.

The default unit is `"pt"` (points), which scales well with text. Other
options include “cm”, “in” (inches) and “lines” (of text).

`plt_mpg_vs_wt_by_cyl` is available. The panel and legend are wrapped in
blue boxes so you can see how they change.

- Give the axis tick length, `axis.ticks.length`, a unit of `2`
  `"lines"`.

<!-- -->

- Give the legend key size, `legend.key.size`, a unit of `3` centimeters
  (`"cm"`).

<!-- -->

- Set the `legend.margin` to `20` points (`"pt"`) on the top, `30` pts
  on the right, `40` pts on the bottom, and `50` pts on the left.

<!-- -->

- Set the plot margin, `plot.margin`, to `10`, `30`, `50`, and `70`
  millimeters (`"mm"`).

``` r
# edited/added
plt_mpg_vs_wt_by_cyl <- ggplot(mtcars, aes(wt, mpg, color = fcyl)) +
  ylab("Miels per gallon") + 
  xlab("weight (1000/lbs)") +
  geom_point()

# View the original plot
plt_mpg_vs_wt_by_cyl

plt_mpg_vs_wt_by_cyl +
  theme(
    # Set the axis tick length to 2 lines
    axis.ticks.length = unit(2, "lines")
  )

plt_mpg_vs_wt_by_cyl +
  theme(
    # Set the legend key size to 3 centimeters
    legend.key.size = unit(3, "cm")
  )

plt_mpg_vs_wt_by_cyl +
  theme(
    # Set the legend margin to (20, 30, 40, 50) points
    legend.margin = margin(20, 30, 40, 50, "pt")
  )

plt_mpg_vs_wt_by_cyl +
  theme(
    # Set the plot margin to (10, 30, 50, 70) millimeters
    plot.margin = margin(10, 30, 50, 70, "mm")
  )
```

## Theme flexibility

### Built-in themes

In addition to making your own themes, there are several [out-of-the-box
solutions](https://ggplot2.tidyverse.org/reference/ggtheme.html) that
may save you lots of time.

- [`theme_gray()`](http://www.rdocumentation.org/packages/ggplot2/functions/ggtheme)
  is the default.
- [`theme_bw()`](http://www.rdocumentation.org/packages/ggplot2/functions/ggtheme)
  is useful when you use transparency.
- [`theme_classic()`](http://www.rdocumentation.org/packages/ggplot2/functions/ggtheme)
  is more traditional.
- [`theme_void()`](http://www.rdocumentation.org/packages/ggplot2/functions/ggtheme)
  removes everything but the data.

`plt_prop_unemployed_over_time` is available.

- Add a black and white theme, `theme_bw()`, to the plot.
- *What changed in the plot?*

<!-- -->

- Add a classic theme, `theme_classic()`, to the plot.
- *What changed in the plot?*

<!-- -->

- Add a void theme, `theme_void()`, to the plot.
- *What changed in the plot?*

``` r
# Add a black and white theme
plt_prop_unemployed_over_time +
  theme_bw()

# Add a classic theme
plt_prop_unemployed_over_time +
  theme_classic()

# Add a void theme
plt_prop_unemployed_over_time +
  theme_void()
```

### Exploring ggthemes

Outside of `ggplot2`, another source of built-in themes is the
`ggthemes` package. The workspace already contains the
`plt_prop_unemployed_over_time`, the line plot from before. Let’s
explore some of the ready-made `ggthemes` themes.

`plt_prop_unemployed_over_time` is available.

- Add a [fivethirtyeight.com](https://fivethirtyeight.com) theme,
  `theme_fivethirtyeight()`, to the plot.
- *What changed in the plot?*

<!-- -->

- Add an [Edward Tufte](https://www.edwardtufte.com/tufte) theme,
  `theme_tufte()`, to the plot.
- *What changed in the plot?*

<!-- -->

- Add a [Wall Street Journal](https://www.wsj.com/) theme,
  `theme_wsj()`, to the plot.
- *What changed in the plot?*

``` r
# edited/added
library(ggthemes)

# Use the fivethirtyeight theme
plt_prop_unemployed_over_time +
  theme_fivethirtyeight()

# Use Tufte's theme
plt_prop_unemployed_over_time +
  theme_tufte()

# Use the Wall Street Journal theme
plt_prop_unemployed_over_time +
  theme_wsj()
```

### Setting themes

Reusing a theme across many plots helps to provide a consistent style.
You have several options for this.

1.  Assign the theme to a variable, and add it to each plot.
2.  Set your theme as the default using
    [`theme_set()`](https://www.rdocumentation.org/packages/ggplot2/topics/theme_get).

A good strategy that you’ll use here is to begin with a built-in theme
then modify it.

`plt_prop_unemployed_over_time` is available. The theme you made earlier
is shown in the sample code.

- Assign the theme to `theme_recession`.
- Add the Tufte theme and `theme_recession` together.
- Use the Tufte recession theme by adding it to the plot.

<!-- -->

- Use `theme_set()` to set `theme_tufte_recession` as the default theme.
- Draw the plot, `plt_prop_unemployed_over_time`, without explicitly
  adding a theme.
- *Look at the plot. Was it styled with the default theme or the new
  theme?*\*

``` r
# Theme layer saved as an object, theme_recession
theme_recession <- theme(
  rect = element_rect(fill = "grey92"),
  legend.key = element_rect(color = NA),
  axis.ticks = element_blank(),
  panel.grid = element_blank(),
  panel.grid.major.y = element_line(color = "white", size = 0.5, linetype = "dotted"),
  axis.text = element_text(color = "grey25"),
  plot.title = element_text(face = "italic", size = 16),
  legend.position = c(0.6, 0.1)
)

# Combine the Tufte theme with theme_recession
theme_tufte_recession <- theme_tufte() + theme_recession

# Add the recession theme to the plot
plt_prop_unemployed_over_time + theme_tufte_recession

theme_recession <- theme(
  rect = element_rect(fill = "grey92"),
  legend.key = element_rect(color = NA),
  axis.ticks = element_blank(),
  panel.grid = element_blank(),
  panel.grid.major.y = element_line(color = "white", size = 0.5, linetype = "dotted"),
  axis.text = element_text(color = "grey25"),
  plot.title = element_text(face = "italic", size = 16),
  legend.position = c(0.6, 0.1)
)
theme_tufte_recession <- theme_tufte() + theme_recession

# Set theme_tufte_recession as the default theme
theme_set(theme_tufte_recession)

# Draw the plot (without explicitly adding a theme)
plt_prop_unemployed_over_time
```

### Publication-quality plots

We’ve seen many examples of beautiful, publication-quality plots. Let’s
take a final look and put all the pieces together.

`plt_prop_unemployed_over_time` is available.

Add Tufte’s theme.

Call the function to add individual theme elements. Turn off the legend
and the axis ticks.

Set the axis title and axis text’s text color to `grey60`.

Set the panel gridlines major y values. Set the color to `grey60`, the
size to `0.25`, and the line type to `dotted`.

``` r
plt_prop_unemployed_over_time +
  # Add Tufte's theme
  theme_tufte()

plt_prop_unemployed_over_time +
  theme_tufte() +
  # Add individual theme elements
  theme(
    # Turn off the legend
    legend.position = "none",
    # Turn off the axis ticks
    axis.ticks = element_blank()
  )

plt_prop_unemployed_over_time +
  theme_tufte() +
  theme(
    legend.position = "none",
    axis.ticks = element_blank(),
    # Set the axis title's text color to grey60
    axis.title = element_text(color = "grey60"),
    # Set the axis text's text color to grey60
    axis.text = element_text(color = "grey60")
  )

plt_prop_unemployed_over_time +
  theme_tufte() +
  theme(
    legend.position = "none",
    axis.ticks = element_blank(),
    axis.title = element_text(color = "grey60"),
    axis.text = element_text(color = "grey60"),
    # Set the panel gridlines major y values
    panel.grid.major.y = element_line(
      # Set the color to grey60
      color = "grey60",
      # Set the size to 0.25
      size = 0.25,
      # Set the linetype to dotted
      linetype = "dotted"
    )
  )
```

## Effective explanatory plots

### Using geoms for explanatory plots

Let’s focus on producing beautiful and effective explanatory plots. In
the next couple of exercises, you’ll create a plot that is similar to
the one shown in the video using `gm2007`, a filtered subset of the
`gapminder` dataset.

This type of plot will be in an info-viz style, meaning that it would be
similar to something you’d see in a magazine or website for a mostly lay
audience.

A scatterplot of `lifeExp` by `country`, colored by `lifeExp`, with
points of size `4`, is provided.

`geom_segment()` adds line segments and requires two additional
aesthetics: `xend` and `yend`. To draw a horizontal line for each point,
map `30` onto `xend` and `country` onto `yend`.

`geom_text` also needs an additional aesthetic: `label`. Map `lifeExp`
onto `label`, and set the attributes `color` to `"white"` and `size` to
`1.5`.

- The color scale has been set for you, but you need to clean up the
  scales. For the x scale:
  - Set `expand` to `c(0, 0)` and `limits` to `c(30, 90)`.
  - Place the axis on the top of the plot with the `position` argument.

Make sure to label the plot appropriately using `labs()`:

- Make the title `"Highest and lowest life expectancies, 2007"`.
- Add a reference by setting `caption` to `"Source: gapminder"`.

``` r
# edited/added
library(gapminder)
library(RColorBrewer)
gm2007 <- gapminder %>% 
  filter(year == 2007) %>% 
  select(country, lifeExp, continent) %>% 
  filter(lifeExp > 80.6 | lifeExp <46) %>% 
  arrange(lifeExp)

# Add a geom_segment() layer
ggplot(gm2007, aes(x = lifeExp, y = country, color = lifeExp)) +
  geom_point(size = 4) +
  geom_segment(aes(xend = 30, yend = country), size = 2)

# Add a geom_text() layer
ggplot(gm2007, aes(x = lifeExp, y = country, color = lifeExp)) +
  geom_point(size = 4) +
  geom_segment(aes(xend = 30, yend = country), size = 2) +
  geom_text(aes(label = lifeExp), color = "white", size = 1.5)

# Set the color scale
palette <- brewer.pal(5, "RdYlBu")[-(2:4)]

# Modify the scales
ggplot(gm2007, aes(x = lifeExp, y = country, color = lifeExp)) +
  geom_point(size = 4) +
  geom_segment(aes(xend = 30, yend = country), size = 2) +
  geom_text(aes(label = round(lifeExp,1)), color = "white", size = 1.5) +
  scale_x_continuous("", expand = c(0,0), limits = c(30,90), position = "top") +
  scale_color_gradientn(colors = palette)

# Set the color scale
palette <- brewer.pal(5, "RdYlBu")[-(2:4)]

# Add a title and caption
ggplot(gm2007, aes(x = lifeExp, y = country, color = lifeExp)) +
  geom_point(size = 4) +
  geom_segment(aes(xend = 30, yend = country), size = 2) +
  geom_text(aes(label = round(lifeExp,1)), color = "white", size = 1.5) +
  scale_x_continuous("", expand = c(0,0), limits = c(30,90), position = "top") +
  scale_color_gradientn(colors = palette) +
  labs(title = "Highest and lowest life expectancies, 2007", caption = "Source: gapminder")
```

### Using annotate() for embellishments

In the previous exercise, we completed our basic plot. Now let’s polish
it by playing with the theme and adding annotations. In this exercise,
you’ll use `annotate()` to add text and a curve to the plot.

The following values have been calculated for you to assist with adding
embellishments to the plot:

    global_mean <- mean(gm2007_full$lifeExp)
    x_start <- global_mean + 4
    y_start <- 5.5
    x_end <- global_mean
    y_end <- 7.5

Our previous plot has been assigned to `plt_country_vs_lifeExp`.

Clean up the theme:

- Add a classic theme to the plot with `theme_classic()`.
- Set `axis.line.y`, `axis.ticks.y`, and `axis.title` to
  `element_blank()`.
- Set the `axis.text` color to `"black"`.
- Remove the legend by setting `legend.position` to `"none"`.

Use `geom_vline()` to add a vertical line. Set `xintercept` to
`global_mean`, specify the color to be `"grey40"`, and set `linetype` to
`3`.

`x_start` and `y_start` will be used as positions to place text and have
been calculated for you.

- Add a `"text"` geom as an annotation.
- For the annotation, set `x` to `x_start`, `y` to `y_start`, and
  `label` to `"The\nglobal\naverage"`.

Annotate the plot with an arrow connecting your text to the line.

- Use a `"curve"` geom.
- Set the arrow ends `xend` to `x_end` and `yend` to `y_end`.
- Set the `length` of the arrowhead to 0.2 cm and the `type` to
  `"closed"`.

``` r
# edited/added
gm2007_full <- gapminder %>% 
  filter(year == 2007) %>% 
  select(country, lifeExp, continent)
global_mean <- mean(gm2007_full$lifeExp)
x_start <- global_mean + 4
y_start <- 5.5
x_end <- global_mean
y_end <- 7.5
plt_country_vs_lifeExp <- ggplot(gm2007, aes(x = lifeExp, y = country, color = lifeExp)) +
  geom_point(size = 4) +
  geom_segment(aes(xend = 30, yend = country), size = 2) +
  geom_text(aes(label = round(lifeExp,1)), color = "white", size = 1.5) +
  scale_x_continuous("", expand = c(0,0), limits = c(30,90), position = "top") +
  scale_color_gradientn(colors = palette) +
  labs(title = "Highest and lowest life expectancies, 2007", caption = "Source: gapminder")

# Define the theme
plt_country_vs_lifeExp +
  theme_classic() +
  theme(axis.line.y = element_blank(),
        axis.ticks.y = element_blank(),
        axis.text = element_text(color = "black"),
        axis.title = element_blank(),
        legend.position = "none")

# Add a vertical line
plt_country_vs_lifeExp +
  theme_classic() +
  theme(axis.line.y = element_blank(),
        axis.ticks.y = element_blank(),
        axis.text = element_text(color = "black"),
        axis.title = element_blank(),
        legend.position = "none") +
  geom_vline(xintercept = global_mean, color = "grey40", linetype = 3)

# Add text
plt_country_vs_lifeExp +
  theme_classic() +
  theme(axis.line.y = element_blank(),
        axis.ticks.y = element_blank(),
        axis.text = element_text(color = "black"),
        axis.title = element_blank(),
        legend.position = "none") +
  geom_vline(xintercept = global_mean, color = "grey40", linetype = 3) +
  annotate(
    "text",
    x = x_start, y = y_start,
    label = "The\nglobal\naverage",
    vjust = 1, size = 3, color = "grey40"
  )

# Add a curve
plt_country_vs_lifeExp +
  theme_classic() +
  theme(axis.line.y = element_blank(),
        axis.ticks.y = element_blank(),
        axis.text = element_text(color = "black"),
        axis.title = element_blank(),
        legend.position = "none") +
  geom_vline(xintercept = global_mean, color = "grey40", linetype = 3) +
  annotate(
    "text",
    x = x_start, y = y_start,
    label = "The\nglobal\naverage",
    vjust = 1, size = 3, color = "grey40"
  ) +
  annotate(
    "curve",
    x = x_start, y = y_start,
    xend = x_end, yend = y_end,
    arrow = arrow(length = unit(0.2, "cm"), type = "closed"),
    color = "grey40"
  )
```
