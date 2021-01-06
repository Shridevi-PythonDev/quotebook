from datetime import datetime

### Day of week

now_date = datetime.now()
##now_date = datetime()

print(now_date.strftime('%A'))

#### Function

def str_sort(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(str_sort('rain', 'ice', 'apple', 'cherry'))

######












