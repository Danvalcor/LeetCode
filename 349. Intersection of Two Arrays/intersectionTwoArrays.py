import random
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)   # Obtienes los valores unicos de cada arreglo
        sol = nums1 & nums2
        return sol if len(sol) else 0           # Operación bitwise para encontrar la intresección de los valores.
    
    
def randomArray(maxNum=100, maxSize=100):
    startNum = random.randint(1, maxNum)        # Primer digito aleatorio del arreglo
    arrSize = random.randint(1, maxSize)        # Tamaño aleatorio del arreglo, minimo 5
    array = [startNum + i for i in range(arrSize)]
    return array

if __name__ == "__main__":
    solution = Solution()
    nums1 = randomArray(100,10)
    nums2 = randomArray(2,2)
    print(f"nums1:{nums1}")
    print(f"nums2:{nums2}")
    print(f"Repeated numbers: {solution.intersection(nums1, nums2)}")
