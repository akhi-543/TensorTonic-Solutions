import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    res = np.asarray(x,dtype = float)
    sigg = np.exp(-res)
    return 1 / (1 + sigg)

    pass