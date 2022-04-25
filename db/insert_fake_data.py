import psycopg2
from db.fake_data import create_fake_data
from db.config import config_postgres


def insert_fake_SQL(n, params=None):
    if params is None:
        params = config_postgres()
    conn = None
    try:

        with psycopg2.connect(**params) as conn:

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

    return 1


if __name__ == '__main__':
    insert_fake_SQL(10)
