import os 
from pyairtable import Api



api = Api('patuiuU1ZvSWdG4bx.c5a1c135917606bc3170b19200f9e7b5899e2ea6165e9210fd8f601eddb6124e')
table = api.table('appsc0X3pVmjyOey9', 'tbl0CJXV7WCVwI7WR')


class BookReview:
    def __init__(self,):
        self.api = api
        self.table = table
        
        
    def get_book_rating(self, book_name):
        records = self.table.all()
        
        for record in records:
            if record['fields']['Book'] == book_name:
                return record['fields']['rating']
        return None
    
    def add_book_rating(self, book_name, rating, notes=None):
        records = self.table.all()
        
        for record in records:
            if record['fields']['Book'] == book_name:
                return False
        
        self.table.create({'Book': book_name, 'rating': rating, 'Notes': notes})
        return True
    



if __name__ == '__main__':
    br = BookReview()
    print(br.get_book_rating('Otaraki Book'))
    print(br.add_book_rating('AOT', 5, 'This is a great book'))