import pytest
from television import Television
tv = Television()
tv_2 = Television(True, False, 1, 1)
def test_init():
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    assert tv_2.__str__() == "Power = True, Channel = 1, Volume = 1"

def test_power():
    tv.power()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
def test_channel_up():
    tv.channel_up()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_up()
    assert tv.__str__() == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    assert tv.__str__() == "Power = True, Channel = 2, Volume = 0"
    tv.channel_up()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    tv.channel_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
def test_channel_down():
    tv.channel_down()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    tv.channel_down()
    assert tv.__str__() == "Power = True, Channel = 2, Volume = 0"
    tv.channel_down()
    assert tv.__str__() == "Power = True, Channel = 1, Volume = 0"
    tv.channel_down()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.channel_down()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    tv.power()
    tv.channel_down()
    assert tv.__str__() == "Power = False, Channel = 3, Volume = 0"
def test_volume_up():
    tv.volume_up()
    assert tv.__str__() == "Power = False, Channel = 3, Volume = 0"
    tv.power()
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 1"
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 2"
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 2"
def test_volume_down():
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 1"
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    tv.power()
    tv.volume_down()
    assert tv.__str__() == "Power = False, Channel = 3, Volume = 0"
def test_mute():
    tv.power()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    tv.volume_up()
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 2"
    tv.mute()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    tv.power()
    tv.mute()
    assert tv.__str__() == "Power = False, Channel = 3, Volume = 0"
    tv.power()
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 1"
    tv.mute()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 2"



