import psycopg2

conn= psycopg2.connect(host = 'localhost',
                       database = 'super hero',
                       user = 'postgres',
                       password = '1234567'
                       )
usernames = [r[0] for r in cur.fetchall()]
def binary_search(username):
    username=input('введите логин')
    cur = conn.cursor()
    cur.execute('SELECT superhero_name FROM superhero.superhero ORDER BY superhero_name ASC LIMIT 15')
    if username == (Tagir)
    return True
    print ('здравствуйте' username)
    else:
    return False
    print('ssory bb2')


conn.commit()
cur.close()
conn.close()