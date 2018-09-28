#피보나치
import time
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return (fibo(n-1)+fibo(n-2))

def iterfibo(n):
    if n<2:
        return n
    else :
        a = 1 #초기값
        b = 1
        c = 0
        for i in range(n-1):
            a = b
            b += c
            c = a
        return b

while True:
    n = int(input("Enter a number: "))
    if n == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(n)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(n, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(n)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(n, fibonumber, ts)
