'''
LeetCode: X to the power of N

Implement pow(x, n).


Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100

Solution: O(logN)
Algorithm:
    0) Preprocessing:
    a) Convert the negative powers to positive by reciprocal-ing the number
    b) Take care of special case of N=0
    1) We can decompose the power N into binary components. We take advantage of
    the fact that any number can be expressed as a combination of powers of 2
    i.e X^N = X^(2^a) * X^(2^b) * .. X^(2^n)
    2) Maintain 2 lines, the answer line and the power line
    3) The power line indicates the power of the number when only 1 bit of the
    power is active i.e 1 (X^1), 10 (X^2), 100 (X^4), 1000 (X^8), etc
    e.g) N= 5 = 101 (base 2),
    Power Lines: 1, 10, 100
    4) The answer line is initialized to 1 (to indicate X to the power 0)
    5) The answer line draws from the power line when the actual power bit is 1
    i.e answer line = answer line * power line when the current power bit is 1
    
e.g) X=3, N =5 (base 10) =101 (base 2)

A = 1
P = 3
**************
N   1  0  1
          ^
A         3*1
P         3
**************
N   1  0  1
       ^ 
A      3
P      9
**************
N   1  0  1
    ^ 
A   81*3
P   81
**************
'''

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        answer_line = 1
        power_line = x
        while n>0:
            if n&1:
                answer_line *= power_line
            power_line *= power_line
            n>>=1
        return answer_line