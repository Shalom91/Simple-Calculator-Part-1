import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../simple_calculator/')))
import simple_calculator

def test_add():
    assert simple_calculator.add(0, 0) == 0
    assert simple_calculator.add(-1, -1) == -2
    assert simple_calculator.add(4, 5) == 9
    assert simple_calculator.add(1, 2, 3, 4) == 10

test_add()

def test_multiply():
    assert simple_calculator.multiply(1, 2) == 2
    assert simple_calculator.multiply(-1, -1) == 1
    assert simple_calculator.multiply(4, 5) == 20
    assert simple_calculator.multiply(1, 2, 3, 4) == 24

test_multiply()



    




    
