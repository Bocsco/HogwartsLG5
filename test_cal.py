import pytest
from pythoncode.calculator import calculator

class TestCal:
    def setup_class(self):
        self.cals = calculator()
    @pytest.mark.parametrize("a,b,expect",[(100,100,200),(20,20,40),(3,5,8)])
    def test_add(self,a,b,expect):
        result1 = self.cals.add(a,b)
        assert result1 == expect

    @pytest.mark.parametrize("a,b,expect",[(200,100,100),(60,30,30),(400,300,100)])
    def test_sub(self,a,b,expect):
        result2 =self.cals.sub(a,b)
        assert result2 == expect

    @pytest.mark.parametrize("a,b,expect",[(2,4,8),(3,6,18),(7,2,14)])
    def test_mul(self,a,b,expect):
        result3 = self.cals.mul(a,b)
        assert result3 == expect

    def test_div(self,a,b,expect):
        result4 = self.cals.div(a,b)
        assert result4 == expect


