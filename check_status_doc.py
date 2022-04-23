from datetime import date, timedelta


def check_status_doc(expire_date):
    if (expire_date - date.today()) > timedelta(days=30):
        status = 'Valid'
    elif timedelta(days=1) <= (expire_date - date.today()) <= timedelta(days=30):
        status = 'Expiring'
    else:
        status = 'Expired'

    return status
