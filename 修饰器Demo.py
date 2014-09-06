#! python3
def deco(func):
    def _ede():
        print("before myfunc() called.")
        aa = func()
        print("after myfunc() called.")
        return aa

    return _ede


@deco
def myfunc():
    print("myfunc() called.")
    return 'ok'

myfunc()
