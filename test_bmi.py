import Lab2.bmi as bmi


def test_bmi_normal_weight():


    result = bmi.calculate_bmi(height=1.73, weight=57)

    assert (result == 0)

def test_bmi_over_weight():
  
   
    result = bmi.calculate_bmi(height=1.6, weight=70)

    assert (result == 1)

def test_bmi_under_weight():
  
   
    result = bmi.calculate_bmi(height=1.6, weight=40)

    assert (result == -1)