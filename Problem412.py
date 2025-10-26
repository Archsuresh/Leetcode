class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out_list=[]
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0 :
                out_list.append("FizzBuzz")
            elif i % 3 == 0:
                out_list.append("Fizz")
            elif i % 5 == 0:
                out_list.append("Buzz")
            else:
                out_list.append(str(i)) 
        return out_list
