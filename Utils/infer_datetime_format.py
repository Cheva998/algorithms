from datetime import datetime

def infer_datetime_format(date_str: str) -> datetime:
    """Try different datetime formats and returns a datetime"""
    formats = [
        '%Y-%m-%d %H:%M:%S',
        '%Y/%m/%d %H:%M:%S',

        '%Y-%m-%d %H:%M:%S.%f',
        '%Y/%m/%d %H:%M:%S.%f',
        
        '%Y-%m-%d %H:%M:%S.%f %z',
        '%Y/%m/%d %H:%M:%S.%f %z'
    ]
    for format_i in formats:
        try:
            date_format = datetime.strptime(date_str, format_i)
            return date_format
        except ValueError:
            pass
    return None

test_date1 = '2024/01/11 08:05:09'
test_date2 = '2024/01/11 08:05:09.025'
test_date3 = '2024/01/11 08:05:09.025 -0500'

test_date4 = '2024-01-11 08:05:09'
test_date5 = '2024-01-11 08:05:09.025'
test_date6 = '2024-01-11 08:05:09.025 -0500'

print(infer_datetime_format(test_date1))
print(infer_datetime_format(test_date2))
print(infer_datetime_format(test_date3))
print(infer_datetime_format(test_date4))
print(infer_datetime_format(test_date5))
print(infer_datetime_format(test_date6))

