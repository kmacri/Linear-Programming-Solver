import numpy as np

#problem: a restaurant produces a dish with three sizes (s, m, l) using three 
#ingridients (a, b, c). How much of each size should they produce to optimize
#their profit.

# s = 1a + 1b + 1c, profit = $1
# m = 3a + 3b + 1c, profit = $4
# L = 5a + 4b + 2c, pfot = $7
#availability of a = 100units
#availability of b = 200units
#availability of c = 100units



def lp_solver():
    #data for the square matrix
    A = np.array([[1, 3, 5], [1, 3, 4], [1, 1, 2]])
    #transpose the array
    inv_A = np.linalg.inv(A)
    #constraint limits
    b = np.array([100, 200, 100])
    x = np.linalg.inv(A).dot(b)

    print(x)

lp_solver()
    
    
