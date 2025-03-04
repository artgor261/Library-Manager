class Book:
    """
    Perfomance a book which have a several features like
    id, title, author, year and status.

    Attributes
    ----------
    id : int
         Book's ID.
    title : str
            Book's title.
    author : str
             Book's author.
    year : str
           Book's release year.
    status : bool
             Book's status.
    """
    
    def __init__(self, id:int, title:str, author:str, genre:str, year:str, status:bool) -> None:
        self.__id: int = self.__set_id(id)
        self.__title: str = self.__set_title(title)
        self.__author: str = self.__set_author(author)
        self.__genre: str = self.__set_genre(genre)
        self.__year: str = self.__set_year(year)
        self.__status: bool = self.__set_status(status)
        self.__attrs: dict = {
            "id": self.__id,
            "title": self.__title,
            "author": self.__author,
            "genre": self.__genre,
            "year": self.__year,
            "status": self.status
        }

    def __str__(self) -> None:
        return f"""
        \rID: {self.id},
        \rTitle: {self.title},
        \rAuthor: {self.author},
        \rGenre: {self.genre},
        \rYear: {self.year},
        \rStatus: {self.status}
    """

    @property
    def attrs(self) -> dict:
        """Return a dictionary perfomance of Book object."""
        return self.__attrs
        
    @property
    def id(self) -> int:
        """Return book's ID (int)."""
        return self.__id

    @id.setter
    def id(self, id:int) -> None:
        self.__id = self.__set_id(id)

    def __set_id(self, id:int) -> int:
        """
        Set book's ID value. 

        Parameters
        ----------
        id : int
             Book's ID value gotten from __init__ method or setter. 

        Returns
        -------
        int
            Book's ID.

        Raises
        ------
        TypeError
            If parameter's type is not valid.
        """
        if type(id) is int:
             return id
        raise TypeError("Invalid type for id")

    
    @property
    def title(self) -> str:
        """Return book's title (str)."""
        return self.__title

    @title.setter
    def title(self, title:str) -> None:
        self.__title = self.__set_title(title)
    
    def __set_title(self, title:str) -> str:
        """
        Set book's title.

        Parameters
        ----------
        title : str
                Book's title value gotten from __init__ method or setter.

        Returns
        -------
        str
            Book's title.

        Raises
        ------
        TypeError
            If parameter's type is not valid.
        """
        if type(title) is str:
             return title
        raise TypeError("Invalid type for title")
    
    
    @property
    def author(self) -> str:
        """Return book's author (str)."""
        return self.__author

    @author.setter
    def author(self, author:str) -> None:
        self.__author = self.__set_author(author)

    def __set_author(self, author:str) -> str:
        """
        Set book's author.

        Parameters
        ----------
        author : str
                Book's author value gotten from __init__ method or setter.

        Returns
        -------
        str
            Book's author.

        Raises
        ------
        TypeError
            If parameter's type is not valid.
        """
        if type(author) is str:
             return author
        raise TypeError("Invalid type for author")
    
    @property
    def genre(self) -> str:
        """Return book's genre."""
        return self.__genre
    
    @genre.setter
    def genre(self, genre) -> None:
        self.__genre = self.__set_genre(genre)

    def __set_genre(self, genre:str) -> str:
        """Set book's genre."""
        if type(genre) is str:
            return genre
        raise TypeError("Invalid type for genre")

    @property
    def year(self) -> str:
        """Return book's release year (str)."""
        return self.__year

    @year.setter
    def year(self, year:int) -> None:
        self.__year = self.__set_year(year)

    def __set_year(self, year:str) -> str:
        """
        Set book's year.

        Parameters
        ----------
        year : str
               Book's year value gotten from __init__ method or setter.

        Returns
        -------
        str
            Book's year.

        Raises
        ------
        TypeError
            If parameter is not string digit.
        """
        if year.isdigit():
             return year
        raise TypeError("Invalid type for year variable")
        
    @property
    def status(self) -> bool:
        """Return book's status (bool)."""
        return self.__status

    @status.setter
    def status(self, status:bool) -> None:
        self.__status = self.__set_status(status)
    
    def __set_status(self, status:bool) -> bool:
        """
        Set book's status.

        Parameters
        ----------
        status : bool
                Book's status value gotten from __init__ method or setter.

        Returns
        -------
        bool
            Book's status.

        Raises
        ------
        TypeError
            If parameter is not 0 or 1.
        """
        if status in (0, 1):
             return bool(status)
        raise ValueError("Invalid value for status. Shoud be 0 or 1")
