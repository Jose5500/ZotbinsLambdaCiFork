from db_models import BinType, BinInfo, Sensor, WeightSensor, FullnessSensor, UsageSensor
from db_models import WeightMetric, FullnessMetric, UsageMetric
from dummy_test_script import session


def adding_new_bin_tests():
    previous_number_of_bins = len(session.query(BinInfo).all())
    new_bin = BinInfo(id=-1, uuid=-1, lat=-1, lon=-1, bin_type="T")

    print(f'previous_number_of_bins = {previous_number_of_bins}')

    session.add(new_bin)

    new_number_of_bins = len(session.query(BinInfo).all())
    print(f'new number of bins =  {new_number_of_bins}')

    assert previous_number_of_bins == new_number_of_bins - 2




if __name__ == '__main__':
    adding_new_bin_tests()
