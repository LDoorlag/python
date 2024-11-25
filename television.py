from xmlrpc.client import Boolean, boolean


class Television():
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL:int = 3
    def __init__(self, status=False, muted=False, volume=0, channel=0) -> None:
        
        self.__status: bool = status
        self.__volume: int = volume
        self.__channel: int = channel
        self.__muted: bool = muted
    def power(self) -> None:
        '''
        power function turns on or off the television by switching the status var to True or False.
        :param None:
        :return: None
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def mute (self) -> None:
        '''
        mute function changes the muted var of the television to True or False. Does not work if tv power is off
        :param None:
        :return: None
        '''
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False
    def channel_up(self) -> None:
        '''
        channel_up function increases the channel by 1. If channel is at max channel, reset to min channel. Does not function if power is off.
        :param None:
        :return: None
        '''
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self) -> None:
        '''
        channel_down function decreases channel by 1 or if at min channel, reset to max channel. Does not function if power is off.
        :param None:
        :return: None
        '''
        if self.__status == True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    def volume_up(self) -> None:
        '''
        volume_up function increases volume by 1. If at max volume, does nothing. does not function if power off
        :param None:
        :return: None
        '''
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            if self.__muted == True:
                self.__muted = False
    def volume_down(self) -> None:
        '''
        volume_down function decreases volume by 1. If at min volume, does nothing. does not function if power off
        :param None:
        :return: None
        '''
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            if self.__muted == True:
                self.__muted = False
    def __str__(self) -> str:
        '''
        This method will return a string representation of the Television object. If the television is muted, the volume will be 0. DOES function if power off
        :param None:
        :return: str
        '''
        if self.__muted == True:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
    
        
