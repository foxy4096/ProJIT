# n = int(input("n: "))
# s = sum(range(0, n+1, 2))
# print(s)

# print(sum(range(0, int(input("n="))+1, 2)))

# n = int(input("n: "))
# i = 10
# s = 0
# while n > 0:
#     s = s + (n % i) * (n % i)
#     n = n // i
# print(s)


# n = int(input("n: "))
# def fac(n):
#     x=1
#     for i in range(1,n+1):
#         x = i*x
#     print(x)
# fac(n)


# n = int(input("n: "))
# i = 10
# temp = n
# s = 0
# while n > 0:
#     s = s + (n % i) * (n % i) * (n % i)
#     n = n // i

# if s == temp:
#     print("it's an Armstrong number")
# else:
#     ("nope")


# s = input("sentence:")
# count = 0
# vowels = "aeiou"
# for i in s:
#     if i.lower() in vowels:
#         count += 1

# print(count)

# n = int(input("n:"))
# r = 0
# i = n
# while i > 0:
#     r = (r * 10) + (i % 10)
#     i = i // 10

# if r == n:
#     print("palindrome")

# else:
# print("not palindrome")

# n = int(input("n:"))
# c = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         c += 1
# if c == 2:
#     print("it's a prime number")
# else:
#     print("it's not a prime number")

# n = int(input("n:"))
# fac = 1
# for i in range(1, n + 1):
#     fac = fac * i
# print(fac)

# n = int(input("n:"))
# a = 0
# b = 1
# c = 0
# while c < n:
#     print(c, end=" ")
#     a = b
#     b = c
#     c = a + b

