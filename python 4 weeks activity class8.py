#5 5 5 5 5
#5 4 4 4 5
#5 4 3 4 5
#5 4 4 4 5
#5 5 5 5 5

n = 5
for i in range(n):
    for j in range(n):
        print(i,end = " ")
    print()
    
n = 5
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j), end = " ")
    print( )  
    
n = 5
for i in range(n):
    for j in range(n):
        print((i,j), end = " ")
    print( )  
    
for i in range(n):
    for j in range(n):
        print(max(i,j), end = " ")
    print( )  
    
for i in range(n):
    for j in range(n):
        print(
            max(max(i+1,j+1),max(n-j,n-i)
                ), end = " ")
    print( )  
    
#sum takes in array
