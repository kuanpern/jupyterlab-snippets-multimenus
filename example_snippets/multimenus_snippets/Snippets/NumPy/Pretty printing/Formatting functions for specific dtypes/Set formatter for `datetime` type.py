def format_datetime(date):
    year = date.astype('datetime64[Y]').astype(int) + 1970
    month = date.astype('datetime64[M]').astype(int) % 12 + 1
    day = (date - date.astype('datetime64[M]')).astype(int) + 1
    return 'Y{0}:M{1}:D{2}'.format(year, month, day)
with printoptions(formatter={'datetime': format_datetime}):
    days = np.random.randint(0, 20000, 10)
    dates = np.array([np.datetime64(int(d), 'D') for d in days])
    print(dates)