"""
Check the document status.
If the expire date is past, the status will be 'Expired'.
If the expire date is between today and (today + 30 days) the status will be 'Expiring'.
If the expire date is > (today + 30 days), the status will be 'Valid'.
"""


from datetime import date, timedelta


def check_status_doc(expire_date):
    if (expire_date - date.today()) > timedelta(days=30):
        status = 'Valid'
    elif timedelta(days=1) <= (expire_date - date.today()) <= timedelta(days=30):
        status = 'Expiring'
    else:
        status = 'Expired'

    return status
