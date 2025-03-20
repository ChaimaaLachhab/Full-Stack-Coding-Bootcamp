import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1234'
DATABASE = 'restaurant_db'

def run_query(query):
    conn = psycopg2.connect(
        host=HOSTNAME,
        user=USERNAME,
        password=PASSWORD,
        dbname=DATABASE
    )
    cursor = conn.cursor()
    cursor.execute(query)
    
    results = []
    try:
        results = cursor.fetchall()
    except:
        pass
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return results

query = '''
CREATE TABLE IF NOT EXISTS Menu_Items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL,
    item_price SMALLINT DEFAULT 0
)
'''
run_query(query)
print("Table 'Menu_Items' is ready.")