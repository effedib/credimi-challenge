# credimi-challenge

Requirments
-------------

Given the client's Fiscal Code, returns a list of ID documents uploaded by that person, with the following information:

-  `Fiscal Code`
-  `ID Document Number`
-  `ID Document Type`
-  `ID Document Issuing Date`
-  `Status: Valid/Expiring/Expired`

You can assume that the architecture is the one you have designed and that you have full control of the database with the input data.

----


Basic Usage
-----------

Install dependencies:

.. code:: bash

    pip install -r requirements.txt

Create a `postgreSQL`instance in localhost.
Create `config.ini` in the project directory with the following information:

-  `host`
-  `dbname`
-  `user`
-  `password`
-  `port`


Run `main.py`


.. code:: bash

    python3 main.py

The development server is running on:
 * http://127.0.0.1:8080
 * http://192.168.178.40:8080

Percival, to test the API, we have to put some fake data in the db using the following routes:

- `/create_table_customers`

and only after the table creation

- `/insert_fakes/<num_customers_you_want_create>`


Now we can query all the inserted data:

- `/all`

or a single fiscal code:

- `/<fiscal_code>`
