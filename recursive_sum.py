def recursive_sum(n):

    """Function to return the sum of recursive numbers"""
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n-1)

# change this value for a different result
number = 69

if number < 0:
    print("Enter a positive number")
else:
    print("The sum is", recursive_sum(number))
