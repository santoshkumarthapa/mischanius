# input
#       1 2 3
#       4 5 6
#       7 8 9
#       10 11 12
# output 
#        1 4 7
#        2 5 8
#        3 6 9

# Algo
#     Run a nested loop using two integer pointers i and j for 0 <= i < N and 0 <= j < M
#     Swap A[i][j] with A[j][i]      
# matrix 

mat = [[1,2,3],[4,5,6],[7,8,9], [10,11,12]]
#4*3
#3*4
tr_mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i  in range(len(mat)):
    for j in range(len(mat[0])):
        #print((i,j))
        tr_mat[j][i] = mat[i][j]
print(tr_mat) 


# initializing a (3 x 2) matrix.
matrix = [[1, 2], [2, 3], [3, 4]]

# initializing another (2 x 3) matrix to store the result.
transpose = [[0, 0, 0], [0, 0, 0]]

# iterating the rows and then columns of each row
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]