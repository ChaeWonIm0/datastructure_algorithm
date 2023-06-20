memo = {}
def fibo(n):
    # 가장 아래쪽까지 내려가서 n이 3일때 1+2부터 시작
    if n == 1 or n ==2:
        return 1
    # n이 4일 경우 3+2부터 시작
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

fibo(7)