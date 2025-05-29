import price_info as priceInfo

def test_cost_shopping():
    expectedresult=priceInfo.total_cost_shopping()
    assert (expectedresult==46.75)

def test_cost_of_fruits():
    result=priceInfo.cost_of_fruits('apple',10)
    print(result)
    assert result==12