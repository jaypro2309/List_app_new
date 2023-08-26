import pytest

from pages.setup import SetData


@pytest.mark.usefixtures("setup")
class Test_App():
    def test_case(self):
        sp = SetData(self.driver)
        sp.case1()
        sp.case2("apple")
        sp.case4()
        sp.case5()
        sp.case6()
        sp.case7()

    def test_case1(self):
        sp1 = SetData(self.driver)
        sp1.case2("apple")
        sp1.case5()
        sp1.d_case1()
        sp1.case7()

    def test_case2(self):
        sp2 = SetData(self.driver)
        # sp2.case2("apple")
        sp2.check_list()
