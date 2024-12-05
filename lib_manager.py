from library import Library
from book import Book


def main() -> None:
    file = input('Print relative or absolute path to json file: ')
    lib = Library(file)
    
    attr = {
        'id':None,
        'title':None, 
        'author':None, 
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
                attr['id'] = lib.get_count()
                attr['title'] = input('Title: ')
                attr['author'] = input('Author: ')
                attr['year'] = input('Year: ')
                attr['status'] = True
                lib.add_book(Book(**attr))
            
            elif query == 'del':
                id = int(input("Print book's ID: "))
                lib.del_book(id)
            
            elif query == 'search':
                s = input('Search: ').split()
                for b in lib.search_book(s): 
                    print(b)
            
            elif query == 'all':
                for obj in lib.print_all():
                    print("\n")
                    for key, value in obj.items():
                        print(f"{key}: {value}")
            
            elif query == 'status':
                id = int(input("Print book's ID: "))
                lib.change_status(id)
            
            else:
                break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()







                    
                









    

        





    


