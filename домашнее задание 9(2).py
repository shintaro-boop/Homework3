from datetime import datetime
def func_log(func) :
    def wrapper(*args, **kwargs):
        start = f'{func.__name__}, {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} \n'
        return_value = func(*args, **kwargs)
        timestart = open('log.txt', 'a+', encoding='utf-8')
        timestart.write(start)
        timestart.close()
        timestart1 =open(func.__name__, 'a+', encoding='utf-8')
        timestart1.write(start)
        timestart1.close()
        return return_value
    return wrapper


@func_log
def func123342435() :
    x1 = 'Исходнеая функция'
    print (x1)

func123342435()
