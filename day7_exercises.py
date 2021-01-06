from datetime import datetime

print('{:%y-%m-%d %H:%M}'.format(datetime(2020,10,3,4,5)))

print('{:%Y-%m-%d}'.format(datetime(2021, 8 , 5)))

print('{:%Y/%m/%d}'.format(datetime(2021, 8 , 5)))

print('{:%Y-%m-%d %H:%M}pm'.format(datetime(2019,8,4,2,5)))

print('{:%D}'.format(datetime(2021, 8 , 5)))

print('{:%Y/%m/%d}'.format(datetime.now()))



