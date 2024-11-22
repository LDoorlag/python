from xmlrpc.client import Boolean, boolean


class Television():
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL:int = 3
    def __init__(self, status=False, muted=False, volume=0, channel=0):
        self.__status: bool = status
        self.__volume: int = volume
        self.__channel: int = channel
        self.__muted: bool = muted
    def power(self):
        '''
        This method will turn the television on or off by switching status to True or False.
        no function if power off
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def mute (self):
        '''
        This method will mute the television if it is not muted, and unmute the television if it is muted.
        It switches the muted var to True or False.
        no function if power off
        '''
        if self.__status == False:
            return  
        if self.__muted == False:
            self.__muted = True
        else:
            self.__muted = False
    def channel_up(self):
        '''
        increased channel by 1 or if at max channel, reset to min channel
        no function if power off
        '''
        if self.__status == False:
            return
        if self.__channel < self.MAX_CHANNEL:
            self.__channel += 1
        else:
            self.__channel = self.MIN_CHANNEL
    def channel_down(self):
        '''
        decreased channel by 1 or if at min channel, reset to max channel
        no function if power off
        '''
        if self.__status == False:
            return
        if self.__channel > self.MIN_CHANNEL:
            self.__channel -= 1
        else:
            self.__channel = self.MAX_CHANNEL
    def volume_up(self):
        '''
        increases volume by 1. If at max volume, does nothing.
        no function if power off
        '''
        if self.__status == False:
            return
        if self.__volume < self.MAX_VOLUME:
            self.__volume += 1
        if self.__muted == True:
            self.__muted = False
    def volume_down(self):
        '''
        decreses volume by 1. If at min volume, does nothing.
        no function if power off
        '''
        if self.__status == False:
            return
        if self.__volume > self.MIN_VOLUME:
            self.__volume -= 1
        if self.__muted == True:
            self.__muted = False
    def __str__(self):
        '''
        This method will return a string representation of the Television object.
        If the television is muted, the volume will be 0.
        does function if power off
        '''
        if self.__muted == True:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
    
        
