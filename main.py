"""
Use Flask to run a simple server with only 3 routes.
A GET request containing the fiscal code as parameter (retrieve_docs function).
The response will show the detailed documents stored for that fiscal code, using the following schema:

{
  Fiscal Code
  ID Document Number
  ID Document Type
  ID Document Issuing Date
  Status
}

Two POST requests (create_table_customers and insert_fake_customers) to create the fake data to test the server
"""

from flask import Flask
import json
from db.create_table_customers import create_table
from db.insert_fake_data import insert_fake_SQL
from db.query_fake_data import query_fc
from utils.utils import check_status_doc, is_valid_fiscal_code

app = Flask('app')


@app.route('/')
def hello_world():
    return '<h1>Hello, this is my challenge for credimi.com</h1>'


@app.route('/<fiscal_code>')
def retrieve_docs(fiscal_code):
    # if is an invalid fiscal code, give an invalid input response
    if not is_valid_fiscal_code(fiscal_code):
        return '<h1>Invalid Fiscal Code, please retry using a valid Italian format</h1>'
    # store the query results in a list of lists
    doc_list = query_fc(fiscal_code)
    output = []
    for row in doc_list:
        # check the status controlling the expire date
        expire_date = row[4]
        status = check_status_doc(expire_date)
        output.append({
            'Fiscal Code': fiscal_code,
            'ID Document Number': row[1],
            'ID Document Type': row[2],
            'ID Document Issuing Date': row[3],
            'Status': status
        })

    return json.dumps(output, indent=4, default=str)


@app.route('/create_table_customers')
def create_table_customers():
    created = create_table()
    if created:
        return '<h1>Table customers created</h1>'
    else:
        return '<h1>An error occurred, table not created</h1>'


@app.route('/insert_fakes/<num_customers>')
def insert_fake_customers(num_customers):
    try:
        num_customers = int(num_customers)
        inserted = insert_fake_SQL(num_customers)
        if inserted:
            return '<h1>Created {0} customers</h1>'.format(num_customers)
        else:
            return '<h1>An error occurred, fake data not inserted</h1>'
    except:
        return '<h1>An error occurred, fake data not inserted</h1>'


app.run(host='0.0.0.0', port=8080)
