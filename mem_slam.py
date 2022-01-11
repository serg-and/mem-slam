import datetime
l = []
start = datetime.datetime.now()
while True:
    l.append('$' * 10 ** 9)
    if datetime.datetime.now() - start > datetime.timedelta(seconds=5):
        print('slam dunked the memory\ncleaning up now...')
        break
