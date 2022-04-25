"""
Check the document status.
If the 'expire date' is past, the status will be 'Expired'.
If the 'expire date' is between today and (today + 30 days) the status will be 'Expiring'.
If the 'expire date' is > (today + 30 days), the status will be 'Valid'.
"""


def check_status_doc(expire_date):
    from datetime import date, timedelta

    if (expire_date - date.today()) > timedelta(days=30):
        status = 'Valid'
    elif timedelta(days=1) <= (expire_date - date.today()) <= timedelta(days=30):
        status = 'Expiring'
    else:
        status = 'Expired'

    return status


# Check if the fiscal code has a correct format.
def is_valid_fiscal_code(fiscal_code):
    pass


if __name__ == '__main__':
    print(is_valid_fiscal_code('DBLFNC69P52D994G'))
    print(is_valid_fiscal_code('1BLFNC69P52D994G'))
    print(is_valid_fiscal_code('BLFNC69P52994'))
