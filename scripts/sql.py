import sqlite3

conn = sqlite3.connect('/data/lewzylu/CDM/db.sqlite3')
c = conn.cursor()
c.execute("select name from sqlite_master where type='table' order by name")
print c.fetchall()
c.execute("select username,password,email from auth_user")
print c.fetchall()
