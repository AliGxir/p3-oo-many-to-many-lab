class Author:
    
    all = []
    
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties) 
        return new_contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
class Book:
    
    all = []
    
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)
        
    # this is part of the pytest, but not in the readme
    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    
    # this is part of the pytest, but not in the readme
    def authors(self):
        return [contract.author for contract in self.contracts()]
    
class Contract:
    
    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if type(author) is not Author:
            raise TypeError("author must be of Author object")
        self._author = author
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if type(book) is not Book:
            raise TypeError("book must be in Book object")
        self._book = book
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if type(date) is not str:
            raise TypeError("date must be in string format")
        self._date = date
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not type(royalties) is int:
            raise TypeError("royalties must be an integer")
        self._royalties = royalties
         
    # pytest doesn't expect cls as an argument, but the readme provides it
    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date is date]