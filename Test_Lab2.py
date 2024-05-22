import Lab2

def test_min_max():
    result = []
    userinp = [23, 89, 97, 65, 45, 99]

    result = Lab2.find_min_max(userinp)

    assert (result == (23,99))

def test_calc_average():
    result = []
    userinp = [20, 80, 90, 60, 40]

    result = Lab2.calc_average(userinp)

    assert (result == 58)

def test_calc_median_temperature():
    result = []
    userinp = [23, 45, 67, 89, 95]

    result = Lab2.statistics.median(userinp)

    assert (result == 67)