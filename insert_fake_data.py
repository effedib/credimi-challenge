import psycopg2
from fake_data import create_fake_data

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'amoidb'
port_id = '5433'
conn = None
cur = None


def insert_fake_SQL(n):
    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id
        ) as conn:

            with conn.cursor() as cur:
                insert_fake_data = ''' INSERT INTO customers
                    ("Fiscal_code", "ID_Document_Number", "ID_Document_Type", "ID_Document_Issue_Date", "ID_Document_Expiring_Date")
                    values (%s, %s, %s, %s, %s)
                '''
                insert_value = create_fake_data(n)

                for record in insert_value:
                    cur.execute(insert_fake_data, record)

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return 0


if __name__ == '__main__':
    insert_fake_SQL(10)