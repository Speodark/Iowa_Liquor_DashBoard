import psycopg2

conn = None

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="LowaLiquorSales",
        user="postgres",
        password="1234"
    )
except:
    print("DB NOT WORKING")


def getConnection():
    return conn


cur = getConnection().cursor()


def getCursor():
    global cur
    if not cur:
        cur = getConnection().cursor()
        return cur
    return cur
