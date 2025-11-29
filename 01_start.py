import numpy as np

print(f"line 03: {np.__version__}")

my_list = [1, 2, 3, 4]
print(f"line 06: {my_list}", end="\n\n")
my_list = my_list * 2
print(f"line 08: {my_list}", end="\n\n")

#   numpy arrays are superior to built-in python lists, here's how
array = np.array([1, 2, 3, 4])
print(f"line 12: {array}", end="\n\n")
print(f"line 13: {type(array)}", end="\n\n")

array = array * 2
print(f"line 16: {array}")

#   ------------------------------------------------------------------------------------------------------  #
#                                        multidimensional arays                                             #
#   ------------------------------------------------------------------------------------------------------  #

array = np.array("A")
print(f"line 23: {array.ndim}", end="\n\n")

array = np.array(["a", "b", "c"])
print(f"line 26: {array.ndim}", end="\n\n")

array = np.array([["a", "b", "c"],
                  ["d", "e", "f"],
                  ["g", "h", "i"]])
print(f"line 31: {array.ndim}", end="\n\n")

array = np.array([[["a", "b", "c"],
                   ["d", "e", "f"],
                   ["g", "h", "i"]],

                  [["j", "k", "l"],
                   ["m", "n", "o"],
                   ["p", "q", "r"]],

                  [["s", "t", "u"],
                   ["v", "w", "x"],
                   ["y", "z", "_"]]
                ])
print(f"line 45: {array.ndim}", end="\n\n")
print(f"line 46: {array.shape}", end="\n\n")
print(f"line 47: {array[0][0][0]}", end="\n\n")
print(f"line 48: {array[1][1][2]}", end="\n\n")
print(f"line 49: {array[2][1][1]}", end="\n\n")

word = array[1][1][1] + array[0][0][0] + array[0][2][1] + array[1][0][2] + array[0][0][0]
print(f"line 52: {word}")

#   ------------------------------------------------------------------------------------------------------  #
#                              slicing (array[row_selection, column_selection])                             #
#   ------------------------------------------------------------------------------------------------------  #

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

#   array[start:end:step]
print(f"line 64:\n{array[::-2]}", end="\n\n")

#   select columns
print(f"line 67:\n{array[:, 0:3]}", end="\n\n")
print(f"line 68:\n{array[:, 1:]}", end="\n\n")
print(f"line 69:\n{array[:, ::2]}", end="\n\n")
print(f"line 70:\n{array[:, ::2]}", end="\n\n")
print(f"line 71:\n{array[:, ::-1]}", end="\n\n")
print(f"line 72:\n{array[:, ::-2]}", end="\n\n")

#   combine row and column selection
print(f"line 75:\n{array[0, 0]}", end="\n\n")
print(f"line 76:\n{array[0:2, 0:2]}", end="\n\n")
print(f"line 77:\n{array[0:2, 2:4]}", end="\n\n")
print(f"line 78:\n{array[2:, :2]}", end="\n\n")
print(f"line 49:\n{array[2:, 2:]}", end="\n\n")

#   ------------------------------------------------------------------------------------------------------  #
#                                               arithmetic                                                  #
#   ------------------------------------------------------------------------------------------------------  #

#   scalar arithmetic
array = np.array([1, 2, 3])
print(f"line 87: {array + 1}")
print(f"line 88: {array - 2}")
print(f"line 89: {array * 3}")
print(f"line 90: {array / 4}")
print(f"line 91: {array ** 5}")

# vectorized math functions
array = np.array([1, 2, 3])
print(f"line 95: {np.sqrt(array)}")

array = np.array([1.01, 2.5, 3.99])
print(f"line 98: {np.round(array)}")
print(f"line 99: {np.floor(array)}")
print(f"line 100: {np.ceil(array)}")
print(f"line 101: {np.pi}")

# exercise
radii = np.array([1, 2, 3])
print(f"line 105: {np.pi * radii ** 2}")

# element-wise arithmetic
array_1 = np.array([1, 2, 3])
array_2  = np.array([4, 5, 6])

print(f"line 111: {array_1 + array_2}")
print(f"line 112: {array_1 - array_2}")
print(f"line 113: {array_1 * array_2}")
print(f"line 114: {array_1 / array_2}")
print(f"line 115: {array_1 ** array_2}")

#   comparison operators
scores = np.array([91, 55, 100, 73, 82, 64])
print(f"line 119: {scores == 100}")
print(f"line 120: {scores >= 60}")
print(f"line 121: {scores < 60}")

scores[scores < 60] = 0
print(f"line 125: {scores}")

#   broadcasting
#   broadcasting allows NumPy to perform operations on arrays
#   with different shapes by virtually expanding dimensions
#   so they match the larger array's shape

#   the dimensions have the same size
#   or
# one of the dimensions has a size of 1

array_1 = np.array([[1, 2, 3, 4]])
array_2 = np.array([[1], [2], [3], [4]])

print(f"line 138: {array_1.shape}")
print(f"line 139: {array_2.shape}")

#   the dimensions are compatible as one of them in 1 therefore I can broadcast them
print(f"line 142:\n{array_1 * array_2}", end="\n\n")

array_1 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8]])
array_2 = np.array([[1], [2], [3], [4]])

print(f"line 148: {array_1.shape}")
print(f"line 149: {array_2.shape}")

#   the shapes are incompatible => I cannot broadcast them
#print(f"line 152:\n{array_1 * array_2}", end="\n\n")

array_1 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])
array_2 = np.array([[1], [2], [3], [4]])

print(f"line 160: {array_1.shape}")
print(f"line 161: {array_2.shape}")

#   the shapes are incompatible => I cannot broadcast them
print(f"line 164:\n{array_1 * array_2}", end="\n\n")

array_1 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])
array_2 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])

print(f"line 172: {array_1.shape}")
print(f"line 173: {array_2.shape}")

#   the shapes are incompatible => I cannot broadcast them
# print(f"line 176:\n{array_1 * array_2}", end="\n\n")

array_1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array_2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(f"line 181: {array_1.shape}")
print(f"line 182: {array_2.shape}")
print(f"line 183:\n{array_1 * array_2}", end="\n\n")

#   aggregate functions
array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(f"line 189: {np.sum(array)}")
print(f"line 190: {np.mean(array)}")
print(f"line 191: {np.std(array)}")
print(f"line 192: {np.var(array)}") #   var = std ** 2
print(f"line 193: {np.min(array)}")
print(f"line 194: {np.max(array)}")
print(f"line 195: {np.argmin(array)}")
print(f"line 196: {np.argmax(array)}")
print(f"line 197: {np.sum(array, axis=0)}")
print(f"line 198: {np.sum(array, axis=1)}")

#   filtering
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])
teenagers = ages[ages < 18]
print(f"line 204: {teenagers}")
adults = ages[(ages >= 18) & (ages < 65)]
print(f"line 207: {adults}")
seniors = ages[ages >= 65]
print(f"line 209: {seniors}")
evens = ages[ages % 2 == 0]
print(f"line 211: {evens}")
odds = ages[ages % 2 != 0]
print(f"line 213: {odds}")

#   when I use a boolean index, it flattens the data (turn it into a vector)
#   but there is a way to preserve the shape => [2, 8]

adults = np.where(ages >= 18, ages, 0)  #   np.where(condition, array to filter, fill value)
print(f"line 218:\n{adults}")

#   random numbers
rng = np.random.default_rng() # seed=1 check what seed means
print(f"line 222:\n{rng.integers(low=1, high=101, size=(3, 2))}") # rng.integers(low end, high end, number of outputs) => upper interval end is exclusive
print(f"line 223:\n{np.random.uniform(low=-1, high=1, size=(3, 2))}")

#   shuffle an array
array = np.array([1, 2, 3, 4, 5])
print(f"line 227: {array}")
rng = np.random.default_rng()
rng.shuffle(array)
print(f"line 230: {array}")

fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
print(f"line 233: {fruits}")
rng = np.random.default_rng()
rng.shuffle(fruits)
print(f"line 236: {fruits}")
fruit = rng.choice(fruits, size=(3, 3))
print(f"line 238:\n{fruit}")