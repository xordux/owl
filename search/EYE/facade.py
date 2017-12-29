import mysql.connector


def find(query):
    cnx = mysql.connector.connect(user='search',password='search@123',database='searchEngine')
    cursor = cnx.cursor()
    
    cursor.execute("select * from info")
    for (ID, main, additional, url) in cursor:
        print(ID, main, additional, url)
    return "Good morning"+query


