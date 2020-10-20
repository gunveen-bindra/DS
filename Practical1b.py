# Write a program to perform the Matrix addition, Multiplication and Transpose
# Operation.


X = [[1,8,5],  
       [2,4,6],  
       [3,7,9]]  
 
Y = [[10,12,14],  
      [11,13,15],  
      [16,17,18]]  
#addition of a matrix 
def add_matrix():
    
    result = [[0,0,0], [0,0,0], [0,0,0]]
    
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    for r in result:
        print(r)

#Multiplication of a matrix         
def mul_matrix():
    
    result = [[0,0,0], [0,0,0], [0,0,0]]
    
    for i in range(len(X)):  
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    for r in result:
        print(r)

#transpose of a matrix        
def transpose_matrix():
    
    result = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(len(X)): 
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
    for r in result:
        print(r)
        
print("X = ",X)
print("Y = ",Y)
print("Addition of two matrix is")       
add_matrix()
print("Multiplication of two matrix is")
mul_matrix()
print("Transpose of a matrix is")
transpose_matrix()
