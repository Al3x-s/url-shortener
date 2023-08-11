import random
import string
import sqlite3 

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def check_url(link):
    if "https://" not in link:
        newlink = "https://" + link
        return newlink
    else:
        return link

#returns a true or false value
def check_if_id_exists(id_to_check):
    conn = sqlite3.connect("database.db")      
    cursor = conn.cursor()

    cursor.execute("SELECT link FROM links WHERE link = ?", (id_to_check,))
    result = cursor.fetchone()

    conn.close()
    #print(result)
    return result is not None
#returns id from given link in db
def return_id(check):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM links WHERE link = ?", (check,))

    result = cursor.fetchone()
    conn.close()
    return result

def return_link(check):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT link FROM links WHERE id = ?", (check,))
    result = cursor.fetchone()
    con.close()
    return result





#id_to_add = "your_id_value"
#if not check_if_id_exists(id_to_add):
    #logic
#else:
#already exost
