import pymysql
import json

def con_db():
    return pymysql.connect(host="db-mysql-nyc3-04073-do-user-6764381-0.b.db.ondigitalocean.com", user="doadmin",
                           passwd="e5n939mgoytcp3yo", db="meli", port=25060)


def select_stats():
    conn = con_db()
    cursor = conn.cursor()
    sql = """SELECT SUM(mutant) mutant_count, SUM(human) human_count FROM meli.stats"""
    cursor.execute(sql)
    stats = cursor.fetchone()
    conn.commit()
    _mutant = int(stats[0])
    human = int(stats[1])
    ratio = round((_mutant / human), 2)
    conn.close()
    return _mutant, human, ratio


def insert_stats(dna, mutant, human):
    conn = con_db()
    cursor = conn.cursor()
    _dna = str(dna)
    sql = "INSERT INTO meli.stats (dna, mutant, human) VALUES  (%s, %s, %s);"
    print(sql, (_dna, mutant, human))
    cursor.execute(sql, (_dna, mutant, human))
    conn.commit()
    conn.close()
