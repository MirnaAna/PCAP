class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        #encapsulamos: private atributes
        self.prince = price
        self.discount = None

    #setter method
    def set_discount(self, discount):
        self.discount = discount
    #getter function
    def get_prince(self):
        if self._discount:
            return self._price * (1-self._discount)
        return self._price
    #return 
    def __repr__(self):
       return f"Titulo: '{self.title}', Cantidad: {self.quantity}, Autor: {self.author}, Precio: {round(self.get_price(), 3)}"

book1= Book('El señor de los anillos', 30, 'J.R.R',22)
book2= Book('El cuento de la criada', 20, 'J.i.o',67)
book3= Book('mi dorama', 30, 'J.R.R',8)

print(book1)
print(book2)
print(book3)

print(book1.title)
print(book1.quantity)
print(book1.author)
print(book1.get_price)








