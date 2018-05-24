#Function: InitializeMatrix
#Input: Number of  rows, number of columns, int value to init InitializeMatrix
#Output : Initialized matrix
#e.g
# >>> InitializeMatrix(3,4,0)
# >>> [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def InitializeMatrix(rows, columns, value):
    return [[value for eachColumns in range(columns)] for eachRow  in range(rows)]
    
################ InitializeMatrix##################
