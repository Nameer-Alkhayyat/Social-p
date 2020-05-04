#This file will be like a thin lyer for our server to interact wiht the database (add or romve things)
import sqlite3 as sql
from os import path
ROOT = path.dirname(path.relpath((__file__)))

#creat a function that creat a post(from the user? im not sure)
def create_post(name, content):
    #create a connection to the db
    con = sql.connect(path.join(ROOT, "nameer.db"))
    # create a cusor: Which allow us to grab only the information we need and not the whole database
    cur = con.cursor()
    cur.execute("insert into posts(name, content) values(?, ?)", (name,content))
    con.commit()
    con.close()

# def a fucntion to pull all the posts from db and disply it back to the forntend/html tamplet

def get_posts():
    con = sql.connect(path.join(ROOT, "nameer.db"))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    con.commit()
    con.close()
    return posts














