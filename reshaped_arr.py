import numpy

user_input = list(map(int, input().split()))
numpy_arr = numpy.array(user_input)
reshaped_array = numpy_arr.reshape(3,3)
print(reshaped_array)
