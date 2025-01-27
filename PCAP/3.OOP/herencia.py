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
    
class Novel(Book):
        def __init__(self, title, quantity, author, price, pages):
            super().__init__(title, quantity, author, price)
            self.pages = pages
            
class Academic(Book):
        def __init__(self, title, quantity, author, price, branch):
            super().__init__(title, quantity, author, price)
            self.branch = branch
        
        def _repr_(self):
            return f"Titulo: '{self.title}', Cantidad: {self.quantity}, Autor: {self.author}, Precio: {round(self.get_price(), 3)}"
        
novela1= Novel('La comunidad de anillo', 30, 'J.R.R Tolkien', 30, 560)
novela1.set_discount(0.20)
    
ensayo1=Academic('Modernida líquida', 12, 'Z. Bauman', 18, 'Sociología')