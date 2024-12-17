def arrays(arr):
    # complete this function
    # use numpy.array
    # list_arr = list(arr)
    reverse_arr = arr[::-1]
    numpy_arr = numpy.array(reverse_arr, float)
    return numpy_arr
