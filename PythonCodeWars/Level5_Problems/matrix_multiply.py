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