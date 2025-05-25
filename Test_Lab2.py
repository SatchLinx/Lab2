import lab2
def test_bubble_min_max():
    temperature = [5,10,15,20,25,30,35,40,45,50]
    result = lab2.find_min_max(temperature)
    assert result == [5,50]
def test_bubble_calc_average():
    temperature = [5,10,15,20,25,30,35,40,45,50]
    result = lab2.calc_average(temperature)
    assert result == 27.5
def test_bubble_median():
    temperature = [5,10,15,20,25,30,35,40,45,50,55]
    result = lab2.Calculate_Median(temperature)
    assert result == 30