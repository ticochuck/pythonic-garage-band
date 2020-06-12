from pythonic_garage_band import __version__
from pythonic_garage_band.garage_band import (
    Musician, 
    Band, 
    Guitarist, 
    Bassist,
    Drummer
)

def test_version():
    assert __version__ == '0.1.0'

def test_Musician_exists():
    assert Musician

def test_Band_exists():
    assert Band

def test_Guitarist_exists():
    assert Guitarist

def test_Bassist_exists():
    assert Bassist

def test_Drummer_exists():
    assert Drummer


def test_Musician_pass():
    musician1 = Guitarist('guitar', 'We are the champions')
    actual = musician1.play_solo()
    expected = 'We are the champions'
    assert actual == expected

def test_Drummer_pass():
    musician2 = Drummer('Drum', 'Somebody to love')
    actual = musician2.play_solo()
    expected = 'Somebody to love'
    assert actual == expected

def test_Bassist_pass():
    musician6 = Bassist('Bass', 'Paradise City')
    actual = musician6.play_solo()
    expected = 'Paradise City'
    assert actual == expected

def test_Bassist_fail():
    musician6 = Bassist('Bass', 'Paradise City')
    actual = musician6.play_solo()
    expected = 'City'
    assert actual != expected
