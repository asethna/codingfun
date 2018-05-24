import game
import time
from multiprocessing import Process
import pytest

def test_generate_random():
    '''
    Summary:    Generates number between 0-2 using the game.generate_random()
                function. If the values are outside the range, the test will fail.
    Input:      None
    Output:     None
    '''
    flag_0 = False
    flag_1 = False
    flag_2 = False
    for i in range(1000):
        val = game.generate_random()
        if val == 0:
            flag_0 = True
        elif val == 1:
            flag_1 = True
        elif val == 2:
            flag_2 = True
        else:
            print "Found invalid value %d" % val
            assert(False)
    assert(flag_0 and flag_1 and flag_2)

def test_invalid_chars():
    '''
    Summary:    For a defined list of invalid input characters, verifies that
                the output is "Invalid user input:"
    Input:      None
    Output:     None
    '''
    invalid = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
               "j", "k", "l", "m", "n", "o", "q", "t", "u",
               "v", "w", "x", "y", "z", "0", "1", "2", "3",
               "4", "5", "6", "7", "8", "9", "\r", "\n",
               "\s", "~", "!", "@", "#", "$", "%", "^", "&",
               "*", "(", ")", ":", ",", ".", "<", ">", "{",
               "}", "[", "]", "", " "]
    for item in invalid:
        assert "Invalid user input: %s" % item in game.compare(item)


def test_invalid_strings():
    '''
    Summary:    For a defined list of invalid input strings, verifies that
                the output is "Invalid user input:"
    Input:      None
    Output:     None
    '''
    invalid = ["teradici", "race", "cats", "parts", "apple", "space", "now"
               "ssssssss", "rrr", "pp"]
    for item in invalid:
        assert "Invalid user input: %s" % item in game.compare(item)

@pytest.fixture(scope="function", params=[(0,"r"), (1,"p"), (2,"s")])
def draw_cases(request):
    '''
    Summary:    Uses pytest fixtures to define the test cases
    Input:      None
    Output:     Tuplues with input and expected result for each parameter
    '''
    return request.param

def test_draw(monkeypatch, draw_cases):
    '''
    Summary:    Using pytest fixtures to test when result is draw.
                Implemented monkeypatching game.generate_random function.
                Confirms the user_input compared with computer
                output results in "Draw!"
    Input:      None
    Output:     None
    '''
    (input, result) = draw_cases
    def _mocked():
        return input
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "Draw!" in game.compare(result)

@pytest.fixture(scope="function", params=[(0,"s"), (1,"r"), (2,"p")])
def lose_cases(request):
    '''
    Summary:    Uses pytest fixtures to define the test cases
    Input:      None
    Output:     Tuplues with input and expected result for each parameter
    '''
    return request.param

def test_lose(monkeypatch, lose_cases):
    '''
    Summary:    Using pytest fixtures to test when result is draw.
                Implemented monkeypatching for game.generate_random function.
                Confirms the user_input compared with computer
                output results in "Computer Wins!"
    Input:      None
    Output:     None
    '''
    (input, result) = lose_cases
    def _mocked():
        return input
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "Computer Wins!" in game.compare(result)


@pytest.fixture(scope="function", params=[(0,"p"), (1,"s"), (2,"r")])
def win_cases(request):
    '''
    Summary:    Uses pytest fixtures to define the test cases
    Input:      None
    Output:     Tuplues with input and expected result for each parameter
    '''
    return request.param

def test_win(monkeypatch, win_cases):
    '''
    Summary:    Using pytest fixtures to test when result is draw.
                Implemented monkeypatching for game.generate_random function.
                Confirms the user_input compared with computer
                output results in "User Wins!"
    Input:      None
    Output:     None
    '''
    (input, result) = win_cases
    def _mocked():
        return input
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "User Wins!" in game.compare(result)

