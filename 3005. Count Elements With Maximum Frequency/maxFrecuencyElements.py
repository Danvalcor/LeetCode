class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        dict = {}                           # Se crea una hashtable para guardar las frecuencias
        for i in nums:                      
            dict[i] = dict.get(i, 0) + 1    # Se actualiza la frecuencia con la cual aparece cada numero.
        maxFreq = max(dict.values())        # Se obtiene la frecuencia más alta.
        return sum(maxFreq == n for n in dict.values())*maxFreq # Se cuentan los numeros con la misma frecuencia y se multiplican.



test = [1,2,2,3,1,4]


print(Solution.maxFrequencyElements(Solution, test))



