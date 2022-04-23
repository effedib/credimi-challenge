import psycopg2.extras


def query_fc(fiscal_code):
    hostname = 'localhost'
    database = 'postgres'
    username = 'postgres'
    pwd = 'amoidb'
    port_id = '5433'
    conn = None
    personal_data = None
    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id) as conn:

            with conn.cursor() as cur:
                cur.execute('''SELECT "Fiscal_code", "ID_Document_Number", "ID_Document_Type", "ID_Document_Issue_Date", "ID_Document_Expiring_Date"
                                from "customers" where "Fiscal_code" = \'{}\''''.format(fiscal_code))

                personal_data = cur.fetchall()

    except Exception as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        return personal_data


if __name__ == '__main__':
    print(query_fc('DBLFNC69P52D994G'))
