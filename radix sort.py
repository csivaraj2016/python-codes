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





def countingSort(array, place):             #  used to initialize the places
    size = len(array)
    output = [0] * size
    count = [0] * 10

                                                     # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1


    for i in range(1, 10):
        count[i] += count[i - 1]
        print(count)



                                                            # this fn used for  Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
        print(output)

    for i in range(0, size):
        array[i] = output[i]


                                            #  radix sort main fn
def radixSort(array):
                                                    # Get maximum element
    max_element = max(array)

                                                        # Apply counting sort based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [557, 455]
radixSort(data)
print(data)