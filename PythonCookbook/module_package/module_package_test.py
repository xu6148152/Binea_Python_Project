# -*- encoding: utf-8 -*-
import importlib
importlib.reload()

def test_mymodule():
    from module_package import mymodule
    a = mymodule.A()
    print(a.spam())
    b = mymodule.B()
    print(b.bar())


if __name__ == '__main__':
    test_mymodule()
