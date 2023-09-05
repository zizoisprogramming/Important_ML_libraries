import numpy as np
"""

    np.array() -> takes list or tuple and make a ndarray
    
    
"""


array_fro_list = np.array([1,2,3,4,5])
array_from_tupl = np.array((1,2,3,4,5))
print(array_fro_list, type(array_fro_list))
print(array_from_tupl, type(array_from_tupl))


"""

    np.arrange() ndarray with a sequence of evenly spaced values
    
    
"""
n = int(5)
array_from_arrange = np.arange(n) # from 0 -> n - 1 values, required n as stop value
print(array_from_arrange)


"""

    np.linspace() ndarray with floating values
    

"""
array_from_linspace = np.linspace(start=10,stop=50) # from start to stop floating values
print(array_from_linspace)

"""

    np.eye() create I matrix
    

"""
identity_matrix = np.eye(3) # takes n as argument which is size of the matrix
print(identity_matrix)

"""

    np.random.rand() generates random number between 0 and 1
    

"""
random = np.array([np.random.rand() for i in range(5)]) # generates array of random numbers between 0 -> 1
print(random)

"""

    np.reshape(matrix)


"""
matrix_1 = [[1,2,3],[3,1,2]]
matrix_2 = np.reshape(matrix_1,(3,2)) # takes ndarrayto reshape and the new shape to go to
print(matrix_1, "\n", matrix_2)

"""

    np.mean() 


"""

new_array = array_fro_list - np.mean(array_fro_list) # passes over every element in the array or list and subtract scalar
list_1 = [1,2,3,4,5]
new_list = list_1 - np.mean(list_1)
print(new_list)
print(new_array)