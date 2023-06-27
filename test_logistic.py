import pytest
from math import isclose
import logistic
import numpy as np

SEED = np.random.randint(0,2**31)
@pytest.fixture
def random_state():
    print(f"Using SEED {SEED}")
    rs = np.random.RandomState(SEED)
    return rs

@pytest.mark.parametrize(("r", "x", "f" ), [(2.2, 0.1, .198), (3.4, 0.2, .544), (1.7, 0.75, .31875)])

def test_logistic(r, x, f):
    isclose(logistic.logistic(x,r), f)

#def test_iterate_f(r,x,)

#def test_random():
 #   for n in range(1,10000):
  #      x=np.random.uniform(-100,100)
   #     #print(x)
    #    if isclose(logistic.logistic(x,1.5), 1/3) == True:
     #       print(x,logistic.logistic(x,1.5))
      #      assert True

def test_random(random_state):
    random_state.rand()
    for _ in range(100):
        x = np.random.uniform(0,1)
        result = logistic.iterate_f(100, x, 1.5)
        print(result[-1])
        assert isclose(result[-1], 1 / 3)