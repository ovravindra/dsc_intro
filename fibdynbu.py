# my aim is to store the values of the fibonacci series in a matrix and return the value of the Nth term in the matrix

caches = {} # defining Null matrix

def fibdynbu(n):
    caches[1] = 1
    caches[2] = 1 # defining the initial values for the Matrix

    if n > 2:
        for i in range(3, n+1):
            caches[i] = caches[i-1] + caches[i-2]
    return caches[n]


n = int(input("enter value for fibonacci: "))

for i in range(1, n+1):
    print(i, ":", fibdynbu(i))