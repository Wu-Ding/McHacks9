# Testing our created functions

import pytest
from railvision import *

passengers = ((25,50,75,100,125,150,125,100,75,50,45,40,35,30,25,20,15,10,5),
              (50,75,100,125,150,175,150,125,100,100,75,75,50,45,35,25,20,15,10),
              (50,100,150,200,250,200,175,150,150,125,100,75,50,50,45,40,35,30,25))

tentative_schedule = (0,8,18,27,35,38,48,57,67,78,88,98,108,128,155,178)
tentative_capacities = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 200, 400, 200, 200)

def test_one_train():
    assert one_train(0, 400, [(0,25),(10,50),(20,75)], [(0,50),(10,75),(20,100)], [(0,50),(10,100),(20,150)]) == 3375
    
def test_all_trains():
    assert all_trains(tentative_schedule, tentative_capacities, passengers) == 11685
    
def test_all_trains_left_behind():
    assert all_trains([0], [0], [[1],[1],[1]]) == 100000000
    
def test_avg_waittime():
    assert avg_waittime(tentative_schedule, tentative_capacities, passengers) == '2:32'
    
def test_format():
    assert format_t(0) == '7:00'
    
def test_format2():
    assert format_t(178) == '9:58'
    
def test_get_info():
    assert get_info(0, 400, [(0,25),(10,50),(20,75)], [(0,50),(10,75),(20,100)], [(0,50),(10,100),(20,150)]) == ['L8', '7:00', '400', '25', '7:11', '375', '125', '7:23', '250', '250', '7:37', '0', 400]
    