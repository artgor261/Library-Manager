import json
from typing import List, Optional, Tuple, TextIO
from book import Book

class Library:
    """
    Perfomance a library which stores books in json file.

    Parameters
    ----------
    path : str
           Relative or absolute path to json file.
    """
    def __init__(self, path:str) -> None: 
        self.__j_file: str = self.__set_file(path)
    
    
    @property
    def j_file(self) -> str:
        """Return path of json file (str)."""
        return self.__j_file

    @j_file.setter
    def j_file(self, path:str) -> None:
        self.__set_file(path)

    def __set_file(self, path:str) -> str:
        """
        Set json file which stores a book items.

        Parameters
        ----------
        path : str
                json file path gotten from __init__ method or setter.

        Returns
        -------
        str
            json file path.

        Raises
        ------
        ValueError
            If file format is not json.
        """
        if path.split(sep='.')[1] == "json":
            return path
        else:
            raise ValueError("Invalid format. Shoud be json")

    def _refresh_id(self, data:List[dict], file:TextIO) -> None:
        """
        Refresh id of each book in json file
        after deleting item. 

        Parameters
        ----------
        data : List[dict]
               A sequence of parsed book items from json.
        file : TextIO
               File object.
        """
        for i in range(len(data)):
            data[i]['id'] = i
        
        with open(file, 'w') as f:
            json.dump(data, f)

    
    def add_book(self, book:Book) -> None:
        """
        Add book item into json file.

        Parameters
        ----------
        book : Book
               A Book object which performs a book.

        Raises
        ------
        TypeError
            If `book` parameter have invalid type.
        """
        if type(book) is Book:
            file = self.__j_file
            data = list()
            rec = {
                'id':book.id,
                'title':book.title,
                'author':book.author,
                'year':book.year,
                'status':book.status
                }
            
            if self.get_count() > 0:
                with open(file, 'r') as f:
                    data = json.load(f)
                    data.append(rec)
                
                with open(file, 'w') as f:
                    json.dump(data, f)
            else:
                with open(file, 'w') as f:
                    data.append(rec)
                    json.dump(data, f)
        else:
            raise TypeError("Invalid type for book parameter")

    def del_book(self, id:int) -> None:
        """
        Delete book item from json file.

        Parameters
        ----------
        id : int
               Book's ID.

        Raises
        ------
        FileNotFoundError
            If json file does not exist.
        """
        file = self.__j_file
        
        try:
            with open(file, 'r') as rf:
                data = json.load(rf)
                for obj in data:
                    if obj['id'] == id:
                        data.remove(obj)
                        break
                    print("This ID does not exist")
            
            self._refresh_id(data, file)
        
        except FileNotFoundError:
            print("File does not exist")

    def search_book(self, attr:Optional[List[str]]) -> List[Book]:
        """
        Return a list of Book objects 
        which corresponds with a search query.

        Parameters
        ----------
        attr : array-like or List[str]
               A sequence of keywords which
                corresponds with relevant Book objects.

        Returns
        -------
        List[Book]
            List of relevant Book objects.

        Raises
        ------
        FileNotFoundError
            If json file does not exist.
        """
        file = self.__j_file
        books = list()
        
        try:
            with open(file, 'r') as rf:
                data = json.load(rf)
                for obj in data:
                    obj_values = list()
                    for i in obj.values():
                        row = ' '.join(str(i).split()).split()
                        for s in row:
                            obj_values.append(s)
                    if set(attr).issubset(obj_values):
                        books.append(Book(**obj))
            return books
        
        except FileNotFoundError:
            print("File does not exist")
    
    def print_all(self) -> List[dict]:
        """
        Print all books from json file.

        Returns
        -------
        List[dict]
            A sequence of Book objects.

        Raises
        ------
        FileNotFoundError
            If file does not exist.
        """
        file = self.__j_file
        
        try:
            with open(file, 'r') as f:
                return json.load(f)
        
        except FileNotFoundError:
            print("File does not exist")
    
    def change_status(self, id:int) -> None:
        """
        Change a book's status. 
        If book is exist set True
        else set False.

        Parameters
        ----------
        id : int
             The book's ID.

        Raises
        ------
        FileNotFoundError
            If file does not exist.
        """
        file = self.__j_file
        
        try:
            with open(file, 'r') as rf:
                data = json.load(rf)
                for i in range(len(data)):
                    obj_id = data[i]['id']
                    obj_status = data[i]['status']
                    if obj_id == id:
                        data[i]['status'] = bool(abs(obj_status - 1))
            
            with open(file, 'w') as wf:
                json.dump(data, wf)
        
        except FileNotFoundError:
            print("File does not exist")
    
    def get_count(self) -> int:
        """
        Get count of books into json file.

        Returns
        -------
        int
            Count of books.
        
        Raises
        ------
        FileNotFoundError
            If file does not exist.
        json.decoder.JSONDecodeError
            If file is not json or contains not valid json-objects.
        """
        file = self.__j_file
        
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                return len(data)
        
        except FileNotFoundError:
            return 0
        
        except json.decoder.JSONDecodeError:
            return 0
