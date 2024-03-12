import random

class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        # Delcara los atributos para usar los metodos internos
        self.nums1 = nums1
        self.nums2 = nums2
        return self
    
        # Método interno que implementa el enfoque de dos punteros
    def twoPointers(self) -> list[int]:
            # Inicialización de punteros
            i = 0
            j = 0

            # Recorrido de las dos listas simultáneamente
            while i < len(nums1) and j < len(nums2):
                # Si encuentra un valor común, lo devuelve
                if nums1[i] == nums2[j]:
                    return nums1[i]
                # Incrementa el puntero i si el elemento en nums1 es menor
                elif nums1[i] < nums2[j]:
                    i += 1
                # Incrementa el puntero j si el elemento en nums2 es menor
                else:
                    j += 1
        
            # Si no se encuentra ningún valor común, devuelve -1
            return -1
    
        # Método interno que implementa el enfoque de lista fusionada
    def mergedNumbers(self) -> list[int]:
            # Obtiene la intersección de los conjuntos nums1 y nums2
            nums = set(nums1) & set(nums2)
            # Devuelve el valor mínimo común si existe, de lo contrario, devuelve -1
            return min(nums) if len(nums) else -1
        

def randomArray(maxNum=100, maxSize=100):
    startNum = random.randint(1, maxNum)        # Primer digito aleatorio del arreglo
    arrSize = random.randint(5, maxSize)        # Tamaño aleatorio del arreglo, minimo 5
    array = [startNum + i for i in range(arrSize)]
    return array


if __name__ == "__main__":
    solution = Solution()
    
    nums1 = randomArray(100,100)
    nums2 = randomArray(100,100)
    print(f"nums1:{nums1}")
    print(f"nums2:{nums2}")
    print(f"Two Pointers: {solution.getCommon(nums1, nums2).twoPointers()}")
    print(f"Merged Set:{solution.getCommon(nums1, nums2).mergedNumbers()}")