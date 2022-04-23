from flask import Flask
import json
from query_fake_data import query_fc
from check_status_doc import check_status_doc

app = Flask('app')


@app.route('/')
def hello_world():
    return '<h1>Hello, this is my challenge for Credimi!</h1>'


@app.route('/<fiscal_code>')
def check_docs(fiscal_code):
    doc_list = query_fc(fiscal_code)
    output = []
    for row in doc_list:
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


app.run(host='0.0.0.0', port=8080)
