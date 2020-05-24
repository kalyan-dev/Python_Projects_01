# - fun(p1,p2,*p3)..can we create such function?


def fun3(a,b,c=10,/):
    pass


def strange(p1,p2, *p3):
    print(p1)
    print(p2)
    for p in p3:
        print(p)


# strange(5,10,1,2,3,4,5,6,6,6)

fun3(10,34,42)