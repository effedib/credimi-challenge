import psycopg2.extras
from db.config import config_postgres


def query_fc(fiscal_code):

    conn = None
    personal_data = None

    try:
        params = config_postgres()
        with psycopg2.connect(**params) as conn:

            with conn.cursor() as cur:
                select = '''SELECT "Fiscal_code", "ID_Document_Number", "ID_Document_Type", "ID_Document_Issue_Date", "ID_Document_Expiring_Date"
                                from "customers" '''

                if fiscal_code != 'all':
                    where = '''where "Fiscal_code" = \'{}\''''.format(fiscal_code)
                    cur.execute('{}{}'.format(select, where))
                else:
                    cur.execute(select)

                personal_data = cur.fetchall()

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        return personal_data


if __name__ == '__main__':
    print(query_fc('DBLFNC69P52D994G'))
