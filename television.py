class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self, status=False, muted=False, volume=0, channel=0):
        self.__status = status
        self.__volume = volume
        self.__channel = channel
        self.__muted = muted
    def power(self):
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def mute (self):
        if self.__status == False:
            return  
        if self.__muted == False:
            self.__muted = True
        else:
            self.__muted = False
    def channel_up(self):
        if self.__status == False:
            return
        if self.__channel < self.MAX_CHANNEL:
            self.__channel += 1
        else:
            self.__channel = self.MIN_CHANNEL
    def channel_down(self):
        if self.__status == False:
            return
        if self.__channel > self.MIN_CHANNEL:
            self.__channel -= 1
        else:
            self.__channel = self.MAX_CHANNEL
    def volume_up(self):
        if self.__status == False:
            return
        if self.__volume < self.MAX_VOLUME:
            self.__volume += 1
        if self.__muted == True:
            self.__muted = False
    def volume_down(self):
        if self.__status == False:
            return
        if self.__volume > self.MIN_VOLUME:
            self.__volume -= 1
        if self.__muted == True:
            self.__muted = False
    def __str__(self):
        if self.__muted == True:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
    
        
