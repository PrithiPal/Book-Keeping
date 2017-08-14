import sqlite3

def main() :

    DATABASE_NAME = "db.sqlite3.db"
    connection = sqlite3.connect(DATABASE_NAME)


    FILENAME = "genre_list.txt"
    process_file(FILENAME,connection)


def process_file(filename,connection) :
    genre_list = []

    for genre in open(str(filename),'r') :
        genre_list.append(genre[:-1]) ## skip the line feed character
        INSERT_QUERY = "INSERT INTO book_keeping_genre(id,name) VALUES(1," + genre[:-1] + ");"
        c = connection.cursor()
        c.execute(INSERT_QUERY)
        print("INSERTED ",str(genre))

    connection.commit()
    connection.close()

if __name__ == "__main__" :
    main()
