import simple_calc

def test_add():
    assert simple_calc.add(0, 0) == 0
    assert simple_calc.add(-1, -1) == -2
    assert simple_calc.add(4, 5) == 9
    assert simple_calc.add(1, 2, 3, 4) == 10

    print(simple_calc.add(0, 0))
    print(simple_calc.add(-1, -1))
    print(simple_calc.add(4, 5))
    print(simple_calc.add(1, 2, 3, 4))


def test_multiply():
    assert simple_calc.multiply(1, 2) == 2
    assert simple_calc.multiply(-1, -1) == 1
    assert simple_calc.multiply(4, 5) == 20
    assert simple_calc.multiply(1, 2, 3, 4) == 24

    print(simple_calc.multiply(0, 0))
    print(simple_calc.multiply(-1, -1))
    print(simple_calc.multiply(4, 5))
    print(simple_calc.multiply(1, 2, 3, 4))




    




    
