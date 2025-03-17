from database import get_connection
import pandas as pd

def get_all_characters():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM bonecos", conn)
    conn.close()
    return df

def get_characters_by_attribute(attribute):
    conn = get_connection()
    query = "SELECT * FROM bonecos WHERE characteratribute = ?"
    df = pd.read_sql(query, conn, params=[attribute])
    conn.close()
    return df

