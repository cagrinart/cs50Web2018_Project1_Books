import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not os.getenv('DATABASE_URL'):
  print('DATABASE_URL is not set as an environmental variable')

# connect to the database
engine = create_engine("postgresql://dzilvjkknagyxb:619dc5a5592521e24fbb9168cef2ea895b60addffc714d9e7c69b11676986c89@ec2-54-216-155-253.eu-west-1.compute.amazonaws.com:5432/d5gleq9s52up17")
db = scoped_session(sessionmaker(bind=engine))

db.execute("DROP TABLE IF EXISTS reviews;")
db.execute("DROP TABLE IF EXISTS books;")
db.execute("DROP TABLE IF EXISTS users")

db.execute("""CREATE TABLE users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR NOT NULL,
                    password VARCHAR NOT NULL
);""")

db.execute("""CREATE TABLE books (
                    id SERIAL PRIMARY KEY,
                    isbn VARCHAR NOT NULL,
                    title VARCHAR NOT NULL,
                    author VARCHAR NOT NULL,
                    year VARCHAR NOT NULL
);""")

db.execute("""CREATE TABLE reviews (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users,
                    book_id INTEGER REFERENCES books,
                    rating INTEGER NOT NULL,
                    review VARCHAR NOT NULL,
                    time TIMESTAMP NOT NULL
);""")
print("Tables are created")

with open("books.csv") as csv_file:
  csv_reader = csv.reader(csv_file)
  headers = next(csv_reader, None)
  for isbn,title,author,year in csv_reader:
    db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
              {'isbn':isbn, 'title':title, 'author':author, 'year':year})
    print(f"Book {title} is added to database")
  db.commit()
