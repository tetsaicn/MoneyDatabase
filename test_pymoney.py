
import pymoney
import os
def test_pymoney():
    try:
        os.remove(test.db)
    except:
        pass
    data = pymoney.connect("sqlite","test.db")
    data.init_database()
    data.new("tetsai")
    assert str(data.income("tetsai", 99.99)) == "99.99"
    assert str(data.expenditure("tetsai", 99.99)) == "0.0"
    assert str(data.income("tetsai", 134.52)) == "134.52"
    assert str(data.expenditure("tetsai", 34.51)) == "100.01"
    assert str(data.get("tetsai")) == "100.01"
    data.close()
    os.remove("test.db")