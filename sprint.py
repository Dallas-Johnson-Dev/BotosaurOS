import time
from threading import Thread
import main
#Oh god I can't believe I'm doing this. I'll fix this later on!!

class Sprintmanager:
    activesprints = None
    channelwhitelist = []

    def getactivesprints(self):
        return self.activesprints

    def setactivesprints(self, sprintlist):
        self.activesprints = sprintlist
        return self

    def getchannelwhitelist(self):
        return self.channelwhitelist

    def setchannelwhitelist(self, whitelist):
        self.channelwhitelist = whitelist
        return self

    def whiteListChannel(self, channel):
        self.channelwhitelist.append(channel)

    def startnewsprint(self, length):
        if self.activesprints is not None:
            return "There is already an active sprint! Please wait until it has finished before starting another one!"


class Sprint(Thread):
    length = 0
    highestwordcount = 0

    def __init__(self, *args):
        self._target = main.beginsprint
        self._args = args
        Thread.__init__(self)

    def run(self):
        self._target(*self._args)

    def getlength(self):
        return self.length

    def gethighestwordcount(self):
        return self.highestwordcount

    def setlength(self, length):
        self.length = length
        return self

    def sethighestwordcount(self, count):
        self.highestwordcount = count
        return self

    def startnewsprint(self):
        t1 = Sprint(10)
        t1.start()
        t1.join()