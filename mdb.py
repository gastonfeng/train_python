import pypyodbc


def create_mdb(fileName):
    pypyodbc.win_create_mdb(fileName)
    conn = pypyodbc.connect('Driver={Microsoft Access Driver (*.mdb)};DBQ=' + fileName)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE GEOMETRY (SEAT Number PRIMARY KEY,DETECTDATE Date,ST VARCHAR(30),
SETLOC VARCHAR(30),KM Number,SPEED Number,HEIGHT Number,STAGGER Number,HEIGHTDIFF Number,DISTANCE Number);''')
    cur.commit()

    cur.execute('''INSERT INTO GEOMETRY(SEAT,DETECTDATE,ST,SETLOC,KM,SPEED,HEIGHT,STAGGER,HEIGHTDIFF,DISTANCE)
VALUES(?,?,?,?,?,?,?,?,?,?)''', (11, '2015-01-11 15:38:00', 'bj11', 'zt11', 12, 13, 14, 15, 16, 18))
    cur.commit()

    conn.close()


def read_mdb(fileName):
    conn = pypyodbc.connect('Driver={Microsoft Access Driver (*.mdb)};DBQ=' + fileName)
    cur = conn.cursor()

    cur.execute('''SELECT * FROM GEOMETRY''')
    for row in cur.fetchall():
        for field in row:
            print field,
        print ''


if __name__ == '__main__':
    create_mdb('info.mdb')
    read_mdb('info.mdb')
