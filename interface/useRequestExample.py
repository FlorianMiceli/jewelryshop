from request import *

conn, tunnel = openConn()

result = request(conn, "SELECT * FROM chaines;")
for row in result:
    print(row)

closeConn(conn, tunnel)