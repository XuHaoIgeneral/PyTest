

def Test(func):
    num = 3
    def wrapper(*args, **kwargs):
        print(*args)
        nonlocal num
        if num == 0:
            print("a")
            return "PASS"
        a = func(*args, **kwargs)
        if a is False:
            num-=1
            return "No"
    return wrapper


@Test
def aa(num):
    if num==1:
        print("T")
        return True
    else:
        print("F")
        return False

aa(0)
aa(0)
aa(0)
aa(0)
aa(0)
