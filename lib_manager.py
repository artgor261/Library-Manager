from library import Library
from book import Book


def main() -> None:
    file = input('Print relative or absolute path to json file: ')
    lib = Library(file)
    
    attr = {
        'id':None,
        'title':None, 
        'author':None, 
        'genre': None,
        'year':None, 
        'status':None
    }
    
    commands = ('add', 'del', 'search', 'all', 'status', 'end')
    query = None

    while query != 'end':
        print("\n1. add\n2. del\n3. search\n4. all\n5. status\n6. end")
        query = input('Print command: ')
        
        if query in commands:
            if query == 'add':
                attr['id'] = lib.get_count(lib.j_file) + 1
                attr['title'] = input('Title: ')
                attr['author'] = input('Author: ')
                attr['genre'] = input('Genre: ')
                attr['year'] = input('Year: ')
                attr['status'] = True
                lib.add_book(Book(**attr))
            
            elif query == 'del':
                author = input("Print book's author: ")
                id = int(input("Print book's ID: "))
                lib.del_book(author, id)
            
            elif query == 'search':
                print(lib.search_book())
            
            elif query == 'all':
                for key, value in lib.books.items():
                    print('\n', value)
            
            elif query == 'status':
                id = int(input("Print book's ID: "))
                lib.change_status(id)
        
            else:
                break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
