"""Given a signed 32-bit integer x,
return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Time Complexity-O(log n), Space Complexity-O(1)"""


class ReverseInteger:
    def reverseInt(self, x:int)->int:
        rev=0
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        while x!=0:
            digit=x%10
            x=x//10
            rev=rev*10+digit
        rev=rev*sign
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev
ri=ReverseInteger()
print(ri.reverseInt(123))
print(ri.reverseInt(-123))
print(ri.reverseInt(120))


