# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)
# factorial(4)

def fibo(n):
    if n==1 or 2:
        return 1
    return fibo(n-2) + fibo(n-1)
fibo(5)