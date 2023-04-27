from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():
    assert encrypt_message('maceio', 1) == 'm_oieca'
    assert encrypt_message('maceio', 2) == 'oiec_am'
    assert encrypt_message('maceio', 100) == 'oiecam'

    with raises(TypeError):
        encrypt_message('maceio', 'maceio')

    with raises(TypeError):
        encrypt_message(-1, -1)
