class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                sum_ = mul + result[i + j + 1]
                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10
        return ''.join(map(str, result)).lstrip('0')

# num1 = 123
# num2 = 456
# m,n = 3,3
# result = [0,0,0,0,0,0]
# for i in range(2,-1,-1) =>2,1,0 => 3 2 1
# for j in range(2,-1,-1) =>2,1,0 => 6 5 4
# ord(num1[i])= ascii value of num1[i] ord(num[i])-48) (ord(0)=48) so that converst '3' to 3 and so on and same for j as well
# in the ned of the loop we will have result = 56088 as integer
# return ''. join ()=> joins all separated  strs , map()=> converts all ints to strs and as we all know lstrip('0') removes all leading 0's



# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         n1 = int(num1)
#         n2 = int(num2)
#         mu = n1 * n2
#         mus = str(mu)
#         return mus
# i mean this works as well and this is the first soln i wrote but ik the problem wasn;t lookin for this answer but it;s practical so why not... right
