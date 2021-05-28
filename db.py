import psycopg2

# connect to the db
con = psycopg2.connect(
    host="localhost",
    database="template1",
    user="postgres",
    password="test123")

cur = con.cursor()

# cur.execute("insert into users (username, password) values ('orkhan', '1234')")
cur.execute("delete from users where username='isim';")
cur.execute("select username, password from users")
rows = cur.fetchall()

for r in rows:
    print(f"username {r[0]} password {r[1]}")

#commit the transcation 
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()