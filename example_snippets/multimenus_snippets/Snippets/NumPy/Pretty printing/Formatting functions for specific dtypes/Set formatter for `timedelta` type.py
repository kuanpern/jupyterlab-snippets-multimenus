def format_timedelta(delta):
    days = delta.astype('timedelta64[D]').astype(int)
    hours = delta.astype('timedelta64[h]').astype(int) - 24*days
    minutes = delta.astype('timedelta64[m]').astype(int) - 60*(24*days+hours)
    seconds = delta.astype('timedelta64[s]').astype(int) - 60*(60*(24*days+hours)+minutes)
    return '{0}days,{1}hours,{2}minutes,{3}seconds'.format(days, hours, minutes, seconds)
with printoptions(formatter={'timedelta': format_timedelta}):
    print(np.array([np.timedelta64(int(sec), 's') for sec in np.random.randint(0, 1000000, 10)]))