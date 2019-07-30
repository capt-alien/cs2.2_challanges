#!python3
import sys

def fib(n):
    """Fibonacci method without Memoization"""
    if n == 0: return 0
    elif n == 1: return 1
    elif  n>1:
        return fib(n-1)+fib(n-2)



fib_cash = {0:0, 1:1}
def fib_memo(n):
    """Add Memoizationto Fibonacci"""
    pass





# Run
if __name__ == '__main__':
    print(fib(sys.argv[1]))
