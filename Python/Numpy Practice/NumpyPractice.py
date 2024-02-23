import numpy as np

one_dimensional_array = np.array([1,2,3,4,5,6,7,8,9])

two_dimensional_array = np.array([[1,2],[3,4],[5,6]])   #creates array in matrix form

zeros = np.zeros(22)                                    #numpy.zeros((row,column),dtype = )

sequence_of_integers = np.arange(5,12)                  #creates integer array in order excluding upper bound

random_integers_between_l_and_h = np.random.randint(low=50,high=101,size=6)  #high excluded

random_floats_between_0_and_1 = np.random.random((6,2)) #generates floats between 0 and 1

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0  #value is added to each item
#same goes for multiplication

'''------------------------------------------------------------------------------'''

a = np.arange(1,11)
print(a[2])
