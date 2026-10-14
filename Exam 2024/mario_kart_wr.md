# Mario Kart 8 World Records

In this exercise, you will be working with a dataset of _Mario Kart 8 Deluxe_
world records (WRs). The dataset contains the following columns and everything
is a string:
- `Track`: the name of the track
- `Time`: the total time of the WR, measured by running 3 laps on the track
- `Hybrid Controls Used`: whether or not _hybrid controls_ have been used or
  not, either `"true"` or `"false"`
- `Player`: the name of the player who owns the WR
- `Nation`: the nation where the player owning the WR comes from
- `Date`: the date at which the WR was recorded
- `Duration`: an unused column
- `Character`: the name of the character used in game for the WR
- `Vehicle`: the name of the vehicle used in game for the WR
- `Tires`: the name of the tires used in game for the WR
- `Glider`: the name of the glider used in game for the WR

The dataset is stored in the `MARIO_KART_WORLD_RECORDS_DATASET` constant in
[`src/datasets.py`](src/datasets.py).

> :exclamation: **Important**
>
> All the questions can be done independently from each other. You can fill them in any order you want.
>
> This part of the exam has been designed to be done in 45 minutes.
>
> If you get stuck on a question, you might want to consider skipping it and try doing the next ones.

---
> You can go to
> - [Part 2: _Solving an optimization problem with path-finding algorithms_](robots.md)
> - the [main page](README.md)
---

![mk8dx](assets/mk8dx.png)

The objective of this exercise is to analyze the dataset and answer the following
questions.

To do that, complete the functions in the file `src/mario_kart_wr.py`.

## 1. Get the number of records

:pencil: Fill the function `get_number_of_records` and return the number of records in the dataset.

The function must return an integer.

## 2. Get the name of the tracks

:pencil: Fill the function `get_tracks` and return the names of the tracks in the dataset.

The function must return a list of strings.

> :bulb: **Note**
>
> be careful, there might be multiple people with the same world record!
>
> you must count each track only once.

## 3. Get the name of the fastest track

:pencil: Fill the function `get_fastest_track` and return the name of the track with the fastest
record.

The function must return a string (not a dictionary !).

> :bulb: **Note**
>
> The time is in the format `minutes'seconds"milliseconds`. You can use the `helpers.time_to_ms`
> function to convert the time to milliseconds:
> ```python
> from helpers import time_to_ms
>
> record_time = "1'23\"456"
> time_in_ms = time_to_ms(record_time)
> print(time_in_ms)
> ```

## 4. Get the number of world records by player

:pencil: Fill the function `get_number_of_records_by_player` and return the number of records by
player in the dataset.

The function must return a dictionary where the keys are the players and the values are the
number of records (as integer).

## 5. Get the Player with the most records

:pencil: Fill the function `get_player_with_most_records` and return the player with the most
records in the dataset.

The function must return a string.

## 6. Get the most common characters without the _Hybrid controls_

:pencil: fill the function `get_most_common_characters_without_hc`.

This function must filter the records that have `Hybrid Controls Used` set to `false` and
return the list of the most common `Characters` associated with the number of records.
The list must be sorted by the number of records in descending order, from the most common to the
least common.

If two characters have the same number of records, the order in which they appear in the result does
not matter.

This list must contain the `Character` and the number of records as a tuple.

> :bulb: **Note**
>
> be careful with the type of the `Hybrid Controls Used` column.

## 7. Analyzis of the world records of _Mario Kart 8 Deluxe_

> :bulb: **Note**
>
> there are no tests for this part, only the final figure will be evaluated.

### 7.1 Computing some statistics

:pencil: Write a function `mean` that computes the mean $\mu$ of a list of numbers.

This function should return a float.

The variance of a list of numbers, denoted as $\sigma^2$ is defined as the
_mean of the squared deviations to the mean_ and is given by
$$\sigma^2 = \frac{1}{n}\sum\limits_{i=1}^{n} (\overline{X} - x_i)^2$$

where the input values are the $(x_i)_{1 \leq i \leq n}$ and $\overline{X}$ is their mean.

:pencil: Write a function `stddev` that computes the standard deviation $\sigma$ of a list of numbers.

This function should return a float.

### 7.2 Plotting the results

We will now assume that the WRs times follow a _normal distribution_ and thus can be simplified to
their mean and standard deviation.

A _normal distribution_ with a mean $\mu$ and a standard deviation $\sigma$ will be denoted as
$N(\mu, \sigma)$ is given by
$$N(\mu, \sigma)(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x - \mu}{\sigma})^2}$$

:pencil: Write a function `normal_dist` that computes $N(\mu, \sigma)(x)$ for any input $x$.

It should take a three `float` arguments, namely $x$, $\mu$ and $\sigma$, and return a `float`.
> :bulb: **Note**
>
> To compute the exponential, you can use the `math.exp` function from the `math` module (it is already imported).
> You can also use the `math.sqrt` function to compute the square root, and the `math.pi` constant:
> ```python
> result = math.sqrt(4 * math.exp(2)) * math.pi
> ```
> would compute $\pi \sqrt{4e^{2}}$

:pencil: Using `matplotlib`, plot the following elements:
- the raw times of the world records as a scatter plot on the X axis
- the mean and standard deviation as straight vertical lines, you can use the `helpers.mu_vline`
  and `helpers.sigma_vlines` helper functions for this
- the plot of a _bell curve_ with the same mean and standard deviation as the data

You must ensure the following
- running `python src/mario_kart_wr.py` shows the figure
- everything is on the same figure
- there is a legend
- the data is clear and easy to read, e.g. no weird limit values on the axis, no
  need to zoom in, ...

---
> This part is now over, you can go to
> - [Part 2: _Solving an optimization problem with path-finding algorithms_](robots.md)
> - the [main page](README.md) to zip everything and submit your work
