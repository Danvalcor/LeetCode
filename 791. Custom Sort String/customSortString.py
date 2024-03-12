import random
import string

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sol = ""
        for letter in order:            # buscar cada letra que debe ser ordenada
            while letter in s:          # mientras haya en el arreglo se agrega a la solucion y elimina del arrelo
                sol =sol+letter  
                s = s.replace(letter, "",1)
        return sol+s
                
def randomString(length):
    # Generar un arreglo de caracteres aleatorios utilizando letras minúsculas
    arreglo = ''.join(random.choices(string.ascii_lowercase, k=length))
    return arreglo

def randomOrder(string):
    order = ""
    while len(order) < (int(len(string)/2)+1):
        letra = random.choice(string)
        if letra not in order:
            order += letra
    return order
        
        
if __name__ == "__main__":
    solution = Solution()
    s = randomString(random.randint(5,26))
    order = randomOrder(s)
    print(f"String: {s}")
    print(f"Order: {order}")
    print(solution.customSortString(order, s))
    