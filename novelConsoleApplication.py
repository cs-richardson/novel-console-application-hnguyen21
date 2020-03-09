'''
This is console based application allows you to see the Novel table
in the Novel database, and also add a new novel. Should the added novel's
produce an error, a message will be sent and no novel will be added.
Also, there is an option to add an author because only certain authors are
in the database, so to add a novel that doesn't have the author's name in the
database, you'll have to add that author first.

By Ben
'''
import sqlite3 as sq

con = sq.connect("novel.db")
c = con.cursor()

#Query Functions
def get_authors():
    res = c.execute("SELECT * FROM Author")
    data = c.fetchall()
    return data

def add_author(name, nationality, sex):
    ins_str = "INSERT INTO Author (AuthorName, AuthorNationality, AuthorSex) VALUES ('" + str(name) + "', '" + str(nationality) + "', '" + str(sex) + "');"
    res = c.execute(ins_str)
    con.commit()

def get_novels():
    res = c.execute("SELECT NovelID, ISBN, Title, Price, AuthorName FROM Novel JOIN Author WHERE Novel.AuthorID = Author.AuthorID")
    data = c.fetchall()
    return data

def add_novel(isbn, title, price, authorid):
    ins_str = "INSERT INTO Novel (ISBN, Title, Price, AuthorID) VALUES (" + str(isbn) + ", '" + str(title) + "', " + str(price) + ", " + str(authorid) + ");"
    res = c.execute(ins_str)
    con.commit()

#Database Selections
def author_lb(authors):
    print("\n\nAuthor\n")
    for row in authors:
        print(row)
    author = input("\nChoose an author by AuthorID:\t")
    return author

#Menu Functions
def render_menu():
    print("1. Novel Report")
    print("2. Enter Novel")
    print("3. Author Report")
    print("4. Enter Author")
    print("5. Exit")
    choice = int(input("Choose an option:\t"))

    if choice == 1:
        render_novel_report()
    elif choice == 2:
        render_novel_request()
    elif choice == 3:
        render_author_report()
    elif choice == 4:
        render_author_request()
    elif choice == 5:
        end_program()
        return False

    return True

def end_program():
    con.close()

#Novel Report and Request
def render_novel_report():
    novels = get_novels()
    tbl = "|---------------------------------------------------------------------------------|\n| "
    for row in novels:
        for field in row:
            tbl += str(field)
            tbl += " | "
        tbl += "\n| "
    tbl += "---------------------------------------------------------------------------------|"

    print("Report results\n\n" + tbl)

def render_novel_request():
    isbn = input("Input an ISBN:\t")
    title = input("Input a title:\t")
    price = input("Input a price:\t")
    authors = get_authors()
    authorchoice = author_lb(authors)

    check_and_enter_selection_novel(isbn, title, price, authorchoice)

#Author Report and Request
def render_author_report():
    authors = get_authors()
    tbl = "|---------------------------------------------------------------------------------|\n| "
    for row in authors:
        for field in row:
            tbl += str(field)
            tbl += " | "
        tbl += "\n| "
    tbl += "---------------------------------------------------------------------------------|"

    print("Report results\n\n" + tbl)

def render_author_request():
    name = input("Input a full name:\t")
    nationality = input("Input a nationality:\t")
    sex = input("Input a sex (M or F):\t")

    if sex != "M" or sex != "F":
        print("Error- Try again", "\nPossible errors:  \nThere is already an author with that combination\nThe name, nationality or sex is in an invalid format, \nSomeone else is entering an author at the same time.")
        return
    
    check_and_enter_selection_author(name, nationality, sex)

#Final Addition Check
def check_and_enter_selection_novel(i, t, p, a):
    try:
        add_novel(i, t, p, a)
        print("Success!", "Your novel had been added.")

    except:
        print("Error- Try again", "\nPossible errors:  \nThere is already a novel with that combination, you chose an invalid author\nThe price, title or isbn is in an invalid format, \nSomeone else is entering a novel at the same time.")
        return
    
def check_and_enter_selection_author(nam, nat, s):
    try:
        add_author(nam, nat, s)
        print("Success!", "Your author had been added.")

    except:
        print("Error- Try again", "\nPossible errors:  \nThere is already an author with that combination\nThe name, nationality or sex is in an invalid format, \nSomeone else is entering an author at the same time.")
        return

#Main Program
while(render_menu()):
    print("\n\nWelcome to our library")



