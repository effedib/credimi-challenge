import psycopg2
from config import config_postgres


def create_table():
    conn = None

    try:
        params = config_postgres()
        with psycopg2.connect(**params) as conn:

            with conn.cursor() as cur:
                create_table_customers = ''' CREATE TABLE IF NOT EXISTS customers(
                                            "id"                            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
                                            "Fiscal_code"                   char(16) NOT NULL,
                                            "ID_Document_Number"            varchar(150) NOT NULL UNIQUE,
                                            "ID_Document_Type"              varchar(10) NOT NULL,
                                            "ID_Document_Issue_Date"        date NOT NULL,
                                            "ID_Document_Expiring_Date"     date NOT NULL,
                                            "ID_Document_URL"               text,
                                            "Creation_date"                 date NOT NULL DEFAULT CURRENT_DATE,
                                            "Last_modified_date"            date NOT NULL DEFAULT CURRENT_DATE)'''

                cur.execute(create_table_customers)

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return 0


if __name__ == '__main__':
    create_table()
