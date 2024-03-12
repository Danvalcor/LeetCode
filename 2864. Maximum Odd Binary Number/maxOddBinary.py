class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Con diccionario
        dict = {'0':0, '1':-1}
        for b in s:
            dict[b] = dict.get(b, 0) + 1
        sol = ""+'1'*(dict['1'])+'0'*dict['0']+'1'
        return sol
    
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Con la cantidad de numeros
        ones = sum(int(one) for one in s)-1
        zeros = len(s)-ones-1
        sol = ""+'1'*ones+'0'*zeros+'1'
        return sol
    

if __name__ == "__main__":
    solution = Solution()
    s = "010"
    print(f"Solution:{solution.maximumOddBinaryNumber(s)}")
