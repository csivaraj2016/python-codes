
def countsort(A,k=10):
    size=len(A)
    count=[0]*k                 # denote the  len of count
    B=[0]*size                  # denote the output value  array

    for i in range(0,size):                 # count the elements how many time present
        count[A[i]]+=1
        i+=1

    for i in range(1,k):
        count[i]=count[i]+count[i-1]        #  update the count table
        i-=1

    i=size-1
    while i>=0:                     # place the a[i] val in corresponding  b[i] position

        B[count[A[i]]-1]=A[i]
        count[A[i]]-=1
        i-=1

    for i in range(0,size):
        A[i]=B[i]               #  replace with  b[i] value



data=[6,4,2,1,3,1,4,5]
countsort(data)
print(data)