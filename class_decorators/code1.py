def func(f):
    def wrapper(*args, **kwargs):
        print("Starting the process")
        result = f(*args, **kwargs)
        print("Ended the process")
        return result
    return wrapper

@func
def func1(*args):
    res = sum(args)
    print(res)

@func
def func2():
    print("Olive")

func1(2,5,10)
func2()
