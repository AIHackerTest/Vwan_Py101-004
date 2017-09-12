class AClass(object):
    """
    doc for AClass
    """
    city_name = "bj"

    def __init__(self):
        self.city = "sh"
    def f(self,city):
        self.city = city

if __name__ == "__main__":
    ac = AClass()
    l = [#__self__,
        ac.f.__func__,
        ac.__doc__,__name__,ac.__module__]
    print(*l)
