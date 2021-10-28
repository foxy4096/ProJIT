def avg(*nums):
    result = 0
    count = 0
    for num in nums:
        result = result + num
        count = count + 1
    return result/count


print(avg(1,2,3,45,5))