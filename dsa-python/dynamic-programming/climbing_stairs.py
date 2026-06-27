# climbing stairs is a variation of Fibonacci series where we consider the n=0 way as 1 

class ClimbingStairs:

    def ways(self, n:int) -> int:

        if n<=1:
            return 1
        
        a = 1
        b = 1

        for i in range(2, n+1):
            temp = a
            a = b
            b = temp + a

        return b
    
   
