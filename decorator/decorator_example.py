import time


def time_it(func):
    def wrapper():
        START = time.time()
        result = func()
        END = time.time()
        print(f"{func.__name__} took {int((END-START)*1000)}ms")

    return wrapper


@time_it
def some_op():
    print("starting op")
    time.sleep(1)
    print("we are done...")
    return 123


if __name__ == "__main__":
    some_op()
    # time_it(some_op)()
