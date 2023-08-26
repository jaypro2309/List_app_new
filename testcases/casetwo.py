import time

import pytest

from testcases.caseone import Test_App


@pytest.mark.usefixtures("setup")
class Test_App2():

    def test_list2(self):
        tc = Test_App()
        tc.test_case()
        tc.test_case1()
        tc.test_case2()
