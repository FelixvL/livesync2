from dataclasses import dataclass
from flask import request
import mysql.connector


@dataclass
class Auto:
    id: int
    merk: str
    model: str
    bouwjaar: int
    prijs: float
    kenteken: str


def get_connection():
    return mysql.connector.connect(
        host="svbserver.mysql.database.azure.com",
        user="svbadmin",
        password="abcd1234ABCD!@#$",
        database="database1"
    )


def get_all_autos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM autos")
    rows = cursor.fetchall()

    autos = []

    for row in rows:
        auto = Auto(
            id=row["id"],
            merk=row["merk"],
            model=row["model"],
            bouwjaar=row["bouwjaar"],
            prijs=row["prijs"],
            kenteken=row["kenteken"]
        )
        autos.append(auto)

    cursor.close()
    conn.close()

    return autos

def maak_auto():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO autos (merk, model, bouwjaar, prijs, kenteken)
        VALUES (%s, %s, %s, %s, %s)
    """
    data = request.get_json()

    values = (
        data.get("merk"),
        data.get("model"),
        data.get("bouwjaar"),
        data.get("prijs"),
        data.get("kenteken")
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()