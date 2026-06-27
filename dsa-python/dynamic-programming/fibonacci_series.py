class FibonacciSeries:

    def fib_meomization(self, n: int, memo = None) -> int:

        if memo is None:
            memo = {}

        if memo[n]:
            return memo[n]
        
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = self.fib_meomization(n-1, memo) + self.fib_meomization(n-2, memo)

    
        
    def fibonacci_dp(self, n:int) -> int:

        if n <= 1:
            return n
        
        a = 0
        b = 1

        for i in range(2, n+1):
            temp = a
            a = b
            b = temp + a

        return b