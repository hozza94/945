import sqlite3
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()




# DB 생성 (오토 커밋)
conn = sqlite3.connect("member.db", isolation_level=None)
# 커서 획득
c = conn.cursor()

# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
c.execute("CREATE TABLE IF NOT EXISTS member \
    (id integer PRIMARY KEY, name char(10), age integer, sex char(1), birthDay char(12), contact char(13),"
          "address text, job varchar(50), email varchar(50), baptism bool, baptismDay char(10),"
          "marriage bool, prevChurch varchar(30), guider char(10), guiderContact char(13))")

name = "구자호"
age = 29
sex = "M"
birthDay = "1994.01.05"
contact = "010-2471-3412"
address = "경기도 수원시 영통구 동수원로 432, 3동 1408호"
job = "취업준비생"
email = "hozza94@gmail.com"
baptism = True
baptismDay = "0000.00.00"
marriage = False
prevChurch = "수원순복음교회"
guider = "박유여"
guiderContact = "010-7106-8754"

idCount = 0
idCount += 1
c.execute("INSERT INTO member(id, name, age, sex, birthDay, contact, address, job, email, baptism,"
          " baptismDay, marriage, prevChurch, guider, guiderContact) \
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
          (idCount, name, age, sex, birthDay, contact, address, job,
           email, baptism, baptismDay, marriage, prevChurch, guider,
           guiderContact))

with conn:
    with open('backup.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Completed.')

conn.close()

# m = Member.create(name, age, sex, d_of_birth, contact, address, job, email, baptism, d_of_baptism, marriage,
#                   prev_church, guider, guider_p_number)
#
# print(m)
