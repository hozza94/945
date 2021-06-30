import sqlite3


# DB 생성 (오토 커밋)
conn = sqlite3.connect("member.db", isolation_level=None)
# 커서 획득
c = conn.cursor()

# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
c.execute("CREATE TABLE IF NOT EXISTS table1 \
    (id integer PRIMARY KEY, name text, age integer, sex text, birthday text, contact text,"
          " address text, job text, email text, baptism bool, baptismday text, marriage bool, prev_church text, guider text, guider_p_number text)")

name, age, sex, birthday, contact, address, job, email, baptism, d_of_baptism, marriage,
               prev_church, guider, guider_p_number

name = "구자호"
age = 29
sex = "M"
birthday = "1994.01.05"
contact = ["010-2471-3412", "031-235-8754"]
address = "경기도 수원시 영통구 동수원로 432, 3동 1408호"
job = "취업준비생"
email = "hozza94@gmail.com"
baptism = True
d_of_baptism = "0000.00.00"
marriage = False
prev_church = "수원순복음교회"
guider = "박유여"
guider_p_number = "010-7106-8754"

# class Member:
#
#     def __init__(self):
#         # member count
#         self.count = 0
#
#     def create(self, name, age, sex, d_of_birth, contact, address, job, email, baptism, d_of_baptism, marriage,
#                prev_church, guider, guider_p_number):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.d_of_birth = d_of_birth
#         self.contact = contact
#         self.address = address
#         self.job = job
#         self.email = email
#         self.baptism = baptism
#         self.d_of_baptism = d_of_baptism
#         self.marriage = marriage
#         self.prev_church = prev_church
#         self.guider = guider
#         self.guider_p_number = guider_p_number
#
#
# m = Member.create(name, age, sex, d_of_birth, contact, address, job, email, baptism, d_of_baptism, marriage,
#                   prev_church, guider, guider_p_number)
#
# print(m)
