# Create a function with two arguments that will return an array of the first n multiples of x.
#
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
#
# Return the results as an array or list ( depending on language ).

# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]
def count_by_x(x, n):
    num_array = []
    count = 0
    sum1 = 0
    while count < n:
        count = count + 1
        sum1 = sum1 + x
        num_array.append(sum1)
    return num_array

print(count_by_x(3, 10))