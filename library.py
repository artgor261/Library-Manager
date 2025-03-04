import json
from typing import List
from book import Book
from Levenshtein import distance

class Library:
    """
    Perfomance a library which stores books in json file.

    Parameters
    ----------
    path : str
           Relative or absolute path to json file.
    """
    def __init__(self, path:str) -> None:
        self.__books: dict = {}
        self.__authors: dict = {}
        self.__genres: dict = {}
        self.__j_file: str = self.__set_file(path)
    
    def __load_data(self, path:str) -> None:
        """Filling books, authors and genres dicts by json data."""
        with open(path, 'r') as file:
            data = json.load(file)
            for b in data:
                author = b['author']
                id = b['id']
                genre = b['genre']
                self.__books[id] = Book(**b)
                
                if author not in self.__authors.keys():
                    self.__authors[author] = {id: Book(**b)}
                else:
                    self.__authors[author][id] = Book(**b)
                
                if genre not in self.__genres.keys():
                    self.__genres[genre] = [author]
                else:
                    self.__genres[genre].append(author)
    
    def __dump_data(self, data:List[dict], file) -> None:
        """Dump books from self.__books into json file."""
        if len(data) > 0:
            with open(file, 'w') as f:
                json.dump(data, f)

    @property
    def books(self) -> List[Book]:
        """Return all books"""
        return self.__books
    
    @property
    def authors(self) -> List[str]:
        """Return authors list"""
        return self.__authors.keys()
    
    @property
    def genres(self) -> List[str]:
        """Return genres list"""
        return self.__genres.keys()

    @property
    def j_file(self) -> str:
        """Return path of json file (str)."""
        return self.__j_file

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
        if self.get_count(path) > 0:
            self.__load_data(path)
        
        if path.split(sep='.')[1] == "json":
            return path
        else:
            raise ValueError("Invalid format. Must be json")

    
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
            author = book.author
            id = book.id
            self.__books[id] = book 

            if author in self.__authors.keys():
                self.__authors[author][id] = book
            else:
                self.__authors[author] = {id: book}
            
            file = self.__j_file
            data = list()
            rec = {
                'id':book.id,
                'title':book.title,
                'author':book.author,
                'genre': book.genre,
                'year':book.year,
                'status':book.status
                }
            
            if self.get_count(self.__j_file) > 0:
                with open(file, 'r') as f:
                    data = json.load(f)
                    data.append(rec)                
                self.__dump_data(data, self.__j_file)
            else:
                data.append(rec)
                self.__dump_data(data, self.__j_file)
        else:
            raise TypeError("Invalid type for book parameter")

    def del_book(self, author:str, id:int) -> None:
        """
        Delete book item from json file.

        Parameters
        ----------
        author : str
                    Book's author.
        
        id : int
               Book's ID.

        Raises
        ------
        FileNotFoundError
            If json file does not exist.
        """
        file = self.__j_file
        data = ''
        
        try:
            with open(file, 'r') as rf:
                if id in self.__books.keys():
                    data = json.load(rf)
                    book = self.__books[id]
                    data.remove(book.attrs)
                    self.__books.pop(id)
                    self.__authors[author].pop(id)
                else: return
            self.__dump_data(data, self.__j_file)
        except FileNotFoundError:
            print("File does not exist")

    def search_book(self) -> List[Book]:
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
        genre = input('Print genre: ')
        genres = list(self.__genres.keys())
        result_genre = ''
        result_author = ''
        result_title = ''

        current_min_dist = distance(genre, genres[0])
        current_genre = genres[0]
        
        for i in range(1, len(genres)):
            dist = distance(genre, genres[i])
            if dist < current_min_dist:
                current_min_dist = dist
                current_genre = genres[i]
        result_genre = self.__genres[current_genre]
        
        author = input('Print author: ')
        authors = result_genre
        current_min_dist = distance(author, authors[0])
        current_author = authors[0]
        
        for i in range(1, len(authors)):
            dist = distance(author, authors[i])
            if dist < current_min_dist:
                current_min_dist = dist
                current_author = authors[i]
        result_author = self.__authors[current_author]
        
        title = input('Print book title: ')
        titles = [book.title for id, book in result_author.items()]
        current_min_dist = distance(title, titles[0])
        current_author = titles[0]

        for i in range(1, len(titles)):
            dist = distance(title, titles[i])
            if dist < current_min_dist:
                current_min_dist = dist
                current_title = titles[i]
        result_title = current_title

        for id in result_author:
            book = self.__books[id] 
            if book.title == result_title:
                return book
    
    def change_status(self, id:int) -> None:
        """
        Change book's status. 
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
        book = self.__books[id]
        current_status = book.status
        self.__books[id].status = abs(current_status - 1)
        data = [book.attrs for id, book in self.__books.items()] 
        self.__dump_data(data, self.__j_file)
    
    def get_count(self, path) -> int:
        """
        Get count of self.__books into json file.

        Returns
        -------
        int
            Count of self.__books.
        
        Raises
        ------
        FileNotFoundError
            If file does not exist.
        json.decoder.JSONDecodeError
            If file is not json or contains not valid json-objects.
        """
        file = path
        
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                return len(data)
        except FileNotFoundError:
            return 0
        except json.decoder.JSONDecodeError:
            return 0
