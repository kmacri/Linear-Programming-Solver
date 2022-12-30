import numpy as np

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
    
    
