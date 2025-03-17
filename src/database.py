import sqlite3
import pandas as pd
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'bonecos_7ds.db')

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def initialize_database(csv_path):
    conn = get_connection()
    dados = pd.read_csv(csv_path, sep=';')
    dados.to_sql('bonecos', conn, if_exists='replace', index=False)
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'TODOS_OS_BONECO_DO_NNT.csv')
    initialize_database(csv_path)