#Author: Esteban Acosta
# Write a function that accepts two square (NxN) matrices (two dimensional arrays), and returns the product of the two. Only square matrices will be given.

# How to multiply two square matrices:

# We are given two matrices, A and B, of size 2x2 (note: tests are not limited to 2x2). Matrix C, the solution, will be equal to the product of A and B. 
# To fill in cell [0][0] of matrix C, you need to compute: A[0][0] * B[0][0] + A[0][1] * B[1][0].

# More general: To fill in cell [n][m] of matrix C, you need to first multiply the elements in the nth row of matrix A by the elements in the mth column of matrix B, then take the sum of all those products.
# This will give you the value for cell [m][n] in matrix C.

# Example
#   A         B          C
# |1 2|  x  |3 2|  =  | 5 4|
# |3 2|     |1 1|     |11 8|
# Detailed calculation:

# C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0] = 1*3 + 2*1 =  5
# C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1] = 1*2 + 2*1 =  4
# C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0] = 3*3 + 2*1 = 11
# C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1] = 3*2 + 2*1 =  8
# Link to Wikipedia explaining matrix multiplication (look at the square matrix example): http://en.wikipedia.org/wiki/Matrix_multiplication

# A more visual explanation of matrix multiplication: http://matrixmultiplication.xyz

def matrix_mult(a, b):
    bcols = []
    ans = []
    c= []
    #loop through the columns of the second matrix
    for col in range(len(b[0])):
        cols = []
        #loop through the rows of the second matrix
        for row in range(len(b)):
            #add all the values in that specific column to the list
            cols.append(b[row][col])
        #add this column to the list of columns in matrix b
        bcols.append(cols)
    
    #loop through each column of the second matrix
    for cols in range(len(bcols)):
        cCol = []
        #loop through each row of the first matrix
        for row in range(len(a)):
            #multiply the column values of the second matrix with the row values of the first matrix
            #Zip takes the values in the second matrix's column and takes the values in the first matrix's row
            #And combine them together in one list. Then we multiply the zipped values and sum them up
            #We append the values to a list of all of the product matrix's columns
            cCol.append(sum([a * b for a, b in zip(a[row], bcols[cols])]))
        #add this column to matrix c
        c.append(cCol)
    
    #Loop through each columns of the product matrix
    for col in range(len(c[0])):
        cols = []
        #Loop through each rows of the product matrix
        for row in range(len(c)):
            cols.append(c[row][col])
        #Switch the rows in the matrix with the columns in order to get the right answer
        ans.append(cols)
    
    return ans
