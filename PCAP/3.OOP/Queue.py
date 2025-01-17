class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, valor):
        self.queue.append(valor)
        print(f"Se agrego el valor {valor} a la cola")
    
    def dequeue(self):
        if len(self.queue) > 0:
            print("La cola esta vacia")
            return 
        else:
            valor = self.queue.pop()
            print(f"Se canbio el valor {valor} de la cola")
            return valor
  
cola = Queue()
cola.enqueue(1)
cola.enqueue(9)

    