from typing import Optional
import random
import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        current = self
        result = []
        while current:
            result.append(str(current.val))
            current = current.next
        return ' -> '.join(result)

class Solution:    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Crear un nodo ficticio para manejar el caso especial de eliminar el primer nodo
        dummy = ListNode(0)
        dummy.next = head  # Enlaza el nodo ficticio al inicio de la lista
        fast = slow = dummy  # Inicializa los punteros fast y slow al nodo ficticio

        # Avanza el puntero rápido n+1 pasos hacia adelante
        for _ in range(n + 1):
            fast = fast.next
        
        # Avanza ambos punteros hasta que el puntero rápido llegue al final de la lista
        while fast:
            fast = fast.next  # Avanza el puntero rápido
            slow = slow.next  # Avanza el puntero lento

        # El puntero lento está ahora en el nodo justo antes del que queremos eliminar
        # Elimina el nodo deseado enlazando el siguiente nodo al siguiente del nodo lento
        slow.next = slow.next.next
        
        return dummy.next  # Devuelve la cabeza de la lista original (sin el nodo eliminado)

def generate_list(n, random=False):
    if n <= 0:
        return None
    if random:
        # Genera valores aleatorios para los nodos
        values = [random.randint(1, 100) for _ in range(n)]
        # Crea los nodos y enlázalos
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    else:
        # Crea el primer nodo de la lista
        head = ListNode(1)
        current = head

        # Agrega los nodos restantes de 2 a n
        for i in range(2, n+1):  
            current.next = ListNode(i)
            current = current.next
        return head
    
    



# Ejecutar la prueba
if __name__ == "__main__":
    solution = Solution()
        
    numPruebas = 100
    pruebasTime = {}
    #head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    #n = 2
    for n in range(1,numPruebas-1):
        num = random.randint(1,1000)
        head = generate_list(num)
        n = random.randint(1,num)
        #print(f"Caso {n}:{head}\nNode:{n}")
        print(f"Caso {n}: Elements:{num} Node:{n}")
        iniTime = time.time_ns()
        result = solution.removeNthFromEnd(head, n)
        totalTime = time.time_ns()-iniTime
        print(f"Result:{result}\nTime:{totalTime}ns")
        pruebasTime[n]=totalTime

