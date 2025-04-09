import time
import pytest
class All_division :
    def all_division(self, *arg1):
        division = arg1[0]
        for i in arg1[1:]:
            division /= i
        return division


class TestAllDivisionCalculator :
    @classmethod
    def setup_class(cls):
        cls.start_time = time.time()
        print(f'Начало выполнения тестов класса : {cls.start_time}')

    @classmethod
    def teardown_class(cls):
        end_time = time.time()
        duration = end_time - cls.start_time
        print ('\n' f'Завершение выполнения тестов класса : {end_time}')
        print (f'Общее время выполнения : {duration : .2f} секунд')

    @pytest.fixture
    def time_tracker(self):
        start_time = time.time()
        yield
        end_time = time.time()
        execution_time = end_time - start_time
        print (f'\nВремя выполнения теста : {execution_time: .6f} секунд')

    def setup_method(self):
        self.calculator = All_division()

    @pytest.mark.smoke
    def test_01(self) :
        with pytest.raises(ZeroDivisionError):
            self.calculator.all_division( 10, 0)
        time.sleep(1)

    @pytest.mark.smoke
    def test_02(self) :
        with pytest.raises(IndexError):
            self.calculator.all_division()
        time.sleep(2)

    @pytest.mark.smoke
    def test_03(self) :
        result = self.calculator.all_division(2,-2)
        assert result == -1
        time.sleep(3)

    @pytest.mark.hihi
    def test_04 (self, time_tracker):
        result = self.calculator.all_division(1000000, 1000, 10)
        assert result == 100.0
        time.sleep(4)

    @pytest.mark.hihi
    def test_05 (self) :
        result = self.calculator.all_division(0.001, 0.01)
        assert  0.1 ==pytest.approx(result)
        time.sleep(5)
