"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.functions import *


def test_set_target_number():
    """Tests set_target_number function in few cases"""
    assert set_target_number(3, 50) >=3
    assert set_target_number(3, 50) <=50
    assert isinstance(set_target_number(40, 100), int )
    assert callable(set_target_number)
    
    
def test_quit_game():
    """Tests quit_game function in few cases"""
    assert quit_game('hahaha') == False
    assert quit_game('quit game') == True
    assert isinstance(quit_game('???'), bool )
    assert callable(quit_game)
    
    
def test_check_min():
    """Tests check_min function in one case"""
    assert callable(check_min)

    
def test_check_max():
    """Tests check_max function in one case"""
    assert callable(check_max)
    
    
def test_guessing_game():
    """Tests guessing_game function in one case"""
    assert callable(guessing_game)
                 
    
def test_all():
    """Tests all tests"""
    test_set_target_number()
    test_quit_game()
    test_check_min()
    test_check_max()
    test_guessing_game()