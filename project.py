"""
Created on Tue May 26 18:32:57 2020
"""

# MAIN MENU
def main_func():
    menuSelect = 0
    print("\n\t !!WELCOME TO LIBRARY!!")
    print("********** Main Menu **********")
    print("\n\t1. Books List")
    print("\t2. History")
    print("\t3. Search")
    print("\t4. Quit")
    print("\n*******************************")
    menuSelect = int(input("Please select the menu: "))

    while menuSelect < 1 or menuSelect > 4:
        print("The selection provided is invalid.")
        menuSelect = int(input("\nPlease select one of the four options "))

    if menuSelect == 1:
        bklist_func()
    elif menuSelect == 2:
        history_func()
    elif menuSelect == 3:
        search_func()
    elif menuSelect == 4:
        end()

# BACK TO MAIN MENU CODE
def back_main():
    again = input("Enter 'Yes'or'y' to go back to Main menu\nEnter any key to close program\nPlease enter your choice: ")
    again = again.lower()
    if again=="yes" or again=="y":
        print("\n")
        main_func()
    else:
        end()

#Function books
def bk1():
    book1= open("All the fish.txt",)
    history = open("history.txt",'a+')
    history.write("All the fish\n")
    print("\n")
    print(book1.read())
    history.close()
def bk2():
    book2= open("Drama at my drama class.txt")
    history = open("history.txt",'a+')
    history.write("Drama at my drama class\n")
    print("\n")
    print(book2.read())
    history.close()
def bk3():
    book3= open("I hate it when my brother Charlie has to go away.txt")
    history = open("history.txt",'a+')
    history.write("I hate it when my brother Charlie has to go awa\n")
    print("\n")
    print(book3.read())
    history.close()
def bk4():
    book4= open("Love girlfriend.txt")
    history = open("history.txt",'a+')
    history.write("Love girlfriend\n")
    print("\n")
    print(book4.read())
    history.close()
def bk5():
    book5= open("My love of father and mother.txt")
    history = open("history.txt",'a+')
    history.write("My love of father and mother\n")
    print("\n")
    print(book5.read())
    history.close()
def bk6():
    book6= open("One True Love.txt")
    history = open("history.txt",'a+')
    history.write("One True Love\n")
    print("\n")
    print(book6.read())
    history.close()
def bk7():
    book7= open("The Snow Train.txt")
    history = open("history.txt",'a+')
    history.write("The Snow Train\n")
    print("\n")
    print(book7.read())
    history.close()
def bk8():
    book8= open("They got the definition wrong.txt")
    history = open("history.txt",'a+')
    history.write("They got the definition wrong\n")
    print("\n")
    print(book8.read())
    history.close()
    
# BOOKS LIST
def bklist_func():
    booklist = open("booklist.txt")
    print(booklist.read())
    booklist.close()
    book_choose = int(input("Select the number of book that you want to read: "))
    if book_choose==1:
        bk1()
    elif book_choose==2:
        bk2()
    elif book_choose==3:
        bk3()
    elif book_choose==4:
        bk4()
    elif book_choose==5:
        bk5()
    elif book_choose==6:
        bk6()
    elif book_choose==7:
        bk7()
    elif book_choose==8:
        bk8()
    back_main() # Back to main menu

# HISTORY    
def history_func():
    history = open("history.txt")
    print("********** HISTORY **********")
    print(history.read())
    print("*****************************")
    history.close()
    
    
    back_main() # Back to main menu
    
# SEARCH        
def search_func():
    Genre = open("genre.txt")
    bkgenre = Genre.read()
    bkgenreList = bkgenre.split()
    print(bkgenreList)
    find_bk = input("[c=Comedy, r=Romance, h=Horror, f=Fantasy]\nWhat genre do you want to see: ")
    find_bk = find_bk.lower()
    if find_bk == 'c':
        comedy = open("Comedylist.txt")
        print(comedy.read())
        bk_c = int(input("Select the book that you want to read by enter the number: "))
        if bk_c == 1:
            bk1()
        if bk_c == 2:
            bk2()
    elif find_bk =='r':
        romance = open("Romancelist.txt")
        print(romance.read())
        bk_c = int(input("Select the book that you want to read by enter the number: "))
        if bk_c == 1:
            bk5()
        if bk_c == 2:
            bk4()
    elif find_bk =='h':
        horror = open("Horrorlist.txt")
        print(horror.read())
        bk_c = int(input("Select the book that you want to read by enter the number: "))
        if bk_c == 1:
            bk3()
        if bk_c == 2:
            bk8()
    elif find_bk =='f':
        fantasy = open("Fantasylist.txt")
        print(fantasy.read())
        bk_c = int(input("Select the book that you want to read by enter the number: "))
        if bk_c == 1:
            bk6()
        if bk_c == 2:
            bk7()
        
    back_main() # Back to main menu

# CLOSE PROGRAME
def end():
   print("Thanks for using our application!")
        
       
# DISPLAY MAIN MENU     
main_func()