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
    array.reshape(len(array) // 15, 15)
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
    return data[data[:, 3:].argmax() // (data.shape[1] - 3),:3]
"""
7. Find the average windspeed in January for each location.
"""


def sixth_exercise(data):
    return data[:32:,3:].average(axis=0)

"""
Bonus 1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)
"""


def seventh_exercise(data):
    
"""
Bonus 2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.
"""


def eighth_exercise(data):

"""
Final boss: Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)
"""


def ninth_exercise(data):


if __name__ == '__main__':
    data = read_data('wind.data')
    pprint.pprint(data)
    pprint.pprint(first_exercise(data))
    pprint.pprint(second_exercise(data))
    pprint.pprint(third_exercise(data))
    pprint.pprint(fourth_exercise(data))
    pprint.pprint(fifth_exercise(data))
    pprint.pprint(sixth_exercise(data))
    pprint.pprint(seventh_exercise(data))
    pprint.pprint(eighth_exercise(data))
    pprint.pprint(ninth_exercise(data))
