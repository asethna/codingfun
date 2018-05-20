import game
import time
from multiprocessing import Process

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

def test_draw_rock(monkeypatch):
    '''
    Summary:    Using monkeypatching for game.generate_random function.
                Confirms the user_input matches computer and output is a draw
                when rock is picked.
    Input:      None
    Output:     None
    '''
    def _mocked():
        return 0
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "Draw!" in game.compare('r')
    
def test_draw_paper(monkeypatch):
    '''
    Summary:    Using monkeypatching for game.generate_random function.
                Confirms the user_input matches computer and output is a draw
                when paper is picked.
    Input:      None
    Output:     None
    '''
    def _mocked():
        return 1
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "Draw!" in game.compare('p')
    
def test_draw_scissors(monkeypatch):
    '''
    Summary:    Using monkeypatching for game.generate_random function.
                Confirms the user_input matches computer and output is a draw
                when scissors is picked.
    Input:      None
    Output:     None
    '''
    def _mocked():
        return 2
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "Draw!" in game.compare('s')

def test_lose_rock(monkeypatch):
    '''
    Summary:    Using monkeypatching for game.generate_random function.
                Confirms the user_input loses against computer when
                rock is picked.
    Input:      None
    Output:     None
    '''
    def _mocked():
        return 0
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "Computer Wins!" in game.compare('s')
    
def test_lose_paper(monkeypatch):
    '''
    Summary:    Using monkeypatching for game.generate_random function.
                Confirms the user_input loses against computer when
                paper is picked.
    Input:      None
    Output:     None
    '''
    def _mocked():
        return 1
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "Computer Wins!" in game.compare('r')
    
def test_lose_scissors(monkeypatch):
    '''
    Summary:    Using monkeypatching for game.generate_random function.
                Confirms the user_input loses against computer when
                scissors is picked.
    Input:      None
    Output:     None
    '''
    def _mocked():
        return 2
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "Computer Wins!" in game.compare('p')

def test_win_rock(monkeypatch):
    '''
    Summary:    Using monkeypatching for game.generate_random function.
                Confirms the user_input wins against computer when
                rock is picked.
    Input:      None
    Output:     None
    '''
    def _mocked():
        return 0
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "User Wins!" in game.compare('p')
    
def test_win_paper(monkeypatch):
    '''
    Summary:    Using monkeypatching for game.generate_random function.
                Confirms the user_input wins against computer when
                paper is picked.
    Input:      None
    Output:     None
    '''
    def _mocked():
        return 1
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "User Wins!" in game.compare('s')
    
def test_win_scissors(monkeypatch):
    '''
    Summary:    Using monkeypatching for game.generate_random function.
                Confirms the user_input wins against computer when
                scissors is picked.
    Input:      None
    Output:     None
    '''
    def _mocked():
        return 2
    monkeypatch.setattr("game.generate_random", _mocked)
    assert "User Wins!" in game.compare('r')
