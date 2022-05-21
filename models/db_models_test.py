from sqlalchemy import text

from db_models import BinType, BinInfo, Sensor, WeightSensor, FullnessSensor, UsageSensor
from db_models import WeightMetric, FullnessMetric, UsageMetric
from dummy_test_script import session


def adding_new_bin_tests():
    previous_number_of_bins = len(session.query(BinInfo).all())
    new_bin = BinInfo(id=-1, uuid=-1, lat=-1, lon=-1, bin_type="T")

    session.add(new_bin)

    new_number_of_bins = len(session.query(BinInfo).all())
    assert previous_number_of_bins == new_number_of_bins - 1

    print(session.query(BinInfo).all())




if __name__ == '__main__':
    adding_new_bin_tests()
