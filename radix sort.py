# radixSort Algorithm
#   d <- maximum number of digits in the largest element
#   create d buckets of size 0-9
#   for i <- 0 to d
#     sort the elements according to ith place digits using countingSort
#
# countingSort(array, d)
#   max <- find largest element among dth place elements
#   initialize count array with all zeros
#   for j <- 0 to size
#     find the total count of each unique digit in dth place of elements and
#     store the count at jth index in count array
#   for i <- 1 to max
#     find the cumulative sum and store it in count array itself
#   for j <- size down to 1
#     restore the elements to array
#     decrease count of each element restored by 1





def countingSort(A, position,k=10):             #  used to initialize the places
    n = len(A)          # cal the number of elts in A
    B = [0] * n
    count = [0] * k

                                                     # Calculate count of elements
    for i in range(0, n):
        index = A[i] // position
        count[index % 10] += 1

        # because values  only  range from 0-9
    for i in range(1, k):
        count[i] =count[i]+ count[i - 1]



                                                            # this fn used for  Place the elements in sorted order
    i = n - 1
    while i >= 0:
        index = A[i] // position
        B[count[index % 10] - 1] = A[i]
        count[index % 10] -= 1              # every time count val decresed
        i -= 1


    for i in range(0, n):           # restoring the value
        A[i] = B[i]


                                            #  radix sort main fn
def radixSort(A):
                                                    # Get maximum element
    max_element = max(A)

                                                        # Apply counting sort based on place value.
    position = 1
    while (max_element//position>0):
        countingSort(A, position)
        position *= 10


data = [557, 455,234,12,567,23555,67,45]
radixSort(data)
print(data)
