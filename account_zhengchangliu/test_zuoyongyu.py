import pytest


@pytest.fixture(scope="function")
def aa():
    print("fixture函数被运行了")
    return (11)
class Test1():
    def test_er(self,aa):
        print(aa)
    def test_kl(self,aa):
        print(aa)


class Test2():
    def test_er(self,aa):
        print(aa)
    def test_kl(self,aa):
        print(aa)


