import numpy as np

def calculate(list):
    # Input Validation
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")

    # Convert list into Numpy array 3x3
    a = np.array(list, dtype='float')
    a.shape = (3,3)
    
    # Axis1 = Columns; Axis = Rows; Flattened = General
    # Mean
    ax1 = [a[:,value].mean() for value in range(0,a.shape[0])]
    ax2 = [a[value,:].mean() for value in range(0,a.shape[1])]
    flt = a.mean()
    meanval = [ax1, ax2, flt]
    
    # Variance
    ax1 = [a[:,value].var() for value in range(0,a.shape[0])]
    ax2 = [a[value,:].var() for value in range(0,a.shape[1])]
    flt = a.var()
    varval = [ax1, ax2, flt]
    
    # SD
    ax1 = [a[:,value].std() for value in range(0,a.shape[0])]
    ax2 = [a[value,:].std() for value in range(0,a.shape[1])]
    flt = a.std()
    sdval = [ax1, ax2, flt]
    
    # Max
    ax1 = [a[:,value].max() for value in range(0,a.shape[0])]
    ax2 = [a[value,:].max() for value in range(0,a.shape[1])]
    flt = a.max()
    maxval = [ax1, ax2, flt]

    # Min
    ax1 = [a[:,value].min() for value in range(0,a.shape[0])]
    ax2 = [a[value,:].min() for value in range(0,a.shape[1])]
    flt = a.min()
    minval = [ax1, ax2, flt]
    
    # Sum
    ax1 = [a[:,value].sum() for value in range(0,a.shape[0])]
    ax2 = [a[value,:].sum() for value in range(0,a.shape[1])]
    flt = a.sum()
    sumval = [ax1, ax2, flt]
    
    calculations = {'mean': meanval, 'variance': varval, 'standard deviation': sdval, 'max': maxval, 'min': minval, 'sum': sumval}

    return calculations