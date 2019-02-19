"""
Wind Statistics
----------------

Topics: Using array methods over different axes, fancy indexing.

Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.


See :ref:`wind-statistics-solution`.
"""
import numpy
import pprint

"""
1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'loadtxt' function from numpy to read the data into
   an array.
"""


def read_data(fname):
    array = numpy.array(numpy.loadtxt(fname))
    array.reshape(array.size // 15, 15)
    return array


"""
2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds over all the locations and all the times (a single set of numbers
   for the entire dataset).
"""


def first_exercise(data):
    return data[:, 3:].min(), data[:, 3:].max(), data[:, 3:].mean(), data[:, 3:].std()


"""
3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)
"""


def second_exercise(data):
    return data[:, 3:].min(axis=0), data[:, 3:].max(axis=0), data[:, 3:].mean(axis=0), data[:, 3:].std(axis=0)


"""
4. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)
"""


def third_exercise(data):
    return data[:, 3:].min(axis=1), data[:, 3:].max(axis=1), data[:, 3:].mean(axis=1), data[:, 3:].std(axis=1)


"""
5. Find the location which has the greatest windspeed on each day (an integer
   column number for each day).
"""


def fourth_exercise(data):
    return data[:, 3:].argmax(axis=1)


"""
6. Find the year, month and day on which the greatest windspeed was recorded.
"""


def fifth_exercise(data):
    return data[data[:, 3:].argmax() // (data.shape[1] - 3), :3]

    # where data(data == data.max()) figo
    # numpy.unreavel_index


"""
7. Find the average windspeed in January for each location.
"""

# it is not specified if the exercise is referring to a single January or to all of them


def sixth_exercise(data):
    return numpy.average(data[:32:, 3:], axis=0)


# this is for all januaries
def sixth_exercise_revision(data):
    return numpy.average((data[data[:, 1] == 1])[:, 3:], axis=0)


"""
Bonus 1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)
"""


def seventh_exercise(data, january_column=1, number_of_januaries=18):
    all_january = data[data[:, january_column] == 1, 3:]
    # all_january = numpy.reshape(
    # all_january, (all_january.size // (31 * 12), 31 * 12))
    all_january = numpy.reshape(
        all_january, (-1, 31 * 12))  # -1 lo fa calculare a lui da solo
    return all_january.mean(axis=1)


"""
Bonus 2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.
"""


def eighth_exercise(data):
    first_weeks = numpy.reshape(data[:52 * 7, 3:], (52, 12*7))
    return (first_weeks.min(axis=1), first_weeks.max(axis=1), first_weeks.mean(axis=1), first_weeks.std(axis=1))


"""
Final boss: Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)
"""


def ninth_exercise(data):
    """
    days_data = data[, 2]
    days_data_copy = days_data.copy()
    days_data_copy = numpy.roll(days_data_copy, -1)
    month_indices = numpy.argwhere(days_data > days_data_copy)
    """
    months = ((data[:, 0] - 61) * 12 + data[:, 1] -
              1)  # creo indice unico per ogni mese a partire da 0
    month_indices = numpy.searchsorted(months, numpy.arange(months[-1] + 2))

    monthly_loc_totals = numpy.add.reduceat(data[:, 3:], month_indices[:-1])

    monthly_totals = monthly_loc_totals.sum(axis=1)
    month_days = month_indices[1:] - month_indices[:-1]
    measurement_count = month_days * 12
    mean = monthly_totals / measurement_count
    return mean  # vedere se tutto è esatto


if __name__ == '__main__':
    data = read_data('wind.data')
    print("Data read:")
    pprint.pprint(data)
    print("first_exercise:")
    pprint.pprint(first_exercise(data))
    print("second_exercise:")
    pprint.pprint(second_exercise(data))
    print("third_exercise:")
    pprint.pprint(third_exercise(data))
    print("fourth_exercise:")
    pprint.pprint(fourth_exercise(data))
    print("fifth_exercise:")
    pprint.pprint(fifth_exercise(data))
    print("sixth_exercise:")
    pprint.pprint(sixth_exercise(data))
    print("sixth_exercise_revision:")
    pprint.pprint(sixth_exercise_revision(data))
    print("seventh_exercise:")
    pprint.pprint(seventh_exercise(data))
    print("eighth_exercise:")
    pprint.pprint(eighth_exercise(data))
    print("ninth_exercise:")
    pprint.pprint(ninth_exercise(data))
