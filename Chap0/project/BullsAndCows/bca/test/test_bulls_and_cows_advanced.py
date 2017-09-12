import pytest
import sys
#sys.path.insert(0,'../.')
print(sys.path)
from bulls_and_cows_advanced import bulls_and_cows_advanced as bca

class TestBCA(object):
    sys_num = 1234
    test_data = [
        [1234,"4A0B"],
        [1000,"1A0B"],
        [4321,'0A4B']
    ]

    def test_check_num(self):
        """
        Test check_num function
        """
        for data in self.test_data:
            result = bca.check_num(self.sys_num,data[0])
            assert result == data[1]

if __name__ == "__main__":
    TestBCA().test_check_num()
