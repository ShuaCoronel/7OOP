import mysql.connector

conn = mysql.connector.connect(host="localhost", user="shua_coronel",password="",database="moviedb_oop")
cursor = conn.cursor()

def menu():
    while True:
        print("OOP MENU\n"
          "1. ADD MOVIE\n"
          "2. VIEW MOVIE\n"
          "3. UPDATE MOVIE\n"
          "4. DELETE MOVIE\n"
          "5. SEARCH MOVIE\n"
          "6. DISPLAY TOTAL RECORDS\n"
          "7. EXIT\n ")

        choice = int(input("Enter Choice: "))

        if (choice == 1):
            add_movie()
        elif(choice == 2):
            view_movie()
        elif(choice==3):
            update_movie()
        elif(choice==4):
            delete_movie()
        elif(choice==5):
            search_movie()
        elif(choice==6):
            display_record()
        elif(choice==7):
            conn.close()
            break


def add_movie():
    title = input("Enter Movie: ")
    main_act= input("Enter Actor: ")
    director=input("Enter Director: ")
    genre = input("Enter Genre: ")
    grossSales=float(input("Enter Gross: "))
    rating=input("Rating(G,PG, R13, R16, X: )").upper()
    cursor.execute("INSERT INTO movies (title, main_actor, director,genre,gross_sales,ratings) VALUES(%s,%s,%s,%s,%s,%s)", (title,main_act, director,genre,grossSales,rating))
    conn.commit()
    print("Movie added successfully!\n")
    view_movie()

def view_movie():
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    if rows:
        print("\nMovie List:")
        for row in rows:
            print(row)
    else:
        print("\nNo Movies found.")

def update_movie():
    view_movie()
    movie_id = input("Enter Movie number to update: ").strip()
    title = input("Enter New Title: ")
    main_act = input("Enter New Actor: ")
    director = input("Enter New Director: ")
    genre = input("Enter New Genre: ")
    grossSales = input("Enter New Gross: ")
    rating = input("Enter New Rating: ")
    cursor.execute("UPDATE movies SET title=%s, main_actor=%s,director=%s,genre=%s,gross_sales=%s,ratings=%s WHERE movie_id=%s", (title, main_act,director,genre,grossSales,rating, movie_id))
    conn.commit()
    print("Movie updated successfully!\n")



def delete_movie():
    view_movie()
    movie_id = input("Enter Movie ID to delete: ").strip()
    cursor.execute("DELETE FROM movies WHERE movie_id=%s", (movie_id,))
    conn.commit()
    print("Movie deleted successfully!\n")


def search_movie():
    movie_Search = input("Enter Movie to search: ").strip()
    cursor.execute("SELECT * FROM movies WHERE title=%s", (movie_Search,))
    result = cursor.fetchall()
    if result:
        print("RESULT\n")
        for row in result:
            print(row)
    else:
        print("Movie not found!")

def display_record():
    cursor.execute("SELECT * FROM movies")
    result = cursor.fetchall()
    record=0
    for row in result:
        record+=1
    print(f"RECORD OF MOVIES: {record}")


if __name__ == '__main__':
    menu()

