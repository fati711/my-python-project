library=[]
wishlist=[]
#Adding books
book_own=input("Enter the name of a book you own: ")
library.append(book_own)
another_book=input("Enter the name of another book you own(or press 'Enter' to skip): ")
if another_book:
  library.append(another_book)
  
print(f"\nYour Library: {library}")

#Managing the wishlist
book_wish=input("\nEnter the name of a book you wish to have in the future: ")
wishlist.append(book_wish)

another_book_wish=input("Enter the name of another book you wish to have ( or press 'Enter' to skip): ")
if another_book_wish:
  wishlist.append(another_book_wish)
  
print(f"\nYour Wishlist: {wishlist}")

#Merging wishlist into library
book_acquired=input("Enter the name of a book from your wishlist that you've acquired ( or press 'Enter' to skip): ")

if book_acquired in wishlist:
  wishlist.remove(book_acquired)
  library.append(book_acquired)
    
    
print(f"Updated library: {library}")
print(f"Updated wishlist: {wishlist}")


#Donating books
book_done=input("Enter the name of a book from your library wish to donate ( or press'Enter' to skip) : ")

if book_done in library:
  library.remove(book_done)
    
print(f"Final library after Donations: {library}")
 

