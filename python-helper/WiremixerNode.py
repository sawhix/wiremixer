

from asyncio import constants
from Constants import Constants
from MediaTypes import MediaTypes


class WiremixerNode:

    def __init__(self, name, type, numberOfChannels ):
        self.name = name
        self.type = type
        self.numberOfChannels = numberOfChannels

    #get a string for passing to pw-cli in the commandline
    # example: { factory.name=support.null-audio-sink node.name=my-sink media.class=Audio/Sink object.linger=true audio.position=[FL FR FC LFE RL RR] }
    def getCommandString(self):
        return str(f'''{Constants.wrapperCharOpen} {Constants.factoryNameLabel}={Constants.factoryNameValue} {Constants.nodeNameLabel}={self.name} {
        Constants.mediaClassLabel}={str(self.getMediaString())} {Constants.objectLingerLabel}={Constants.objectLingerValue} {
        Constants.audioPositionLabel}={self.getNumberOfChannelsString()} {Constants.wrapperCharClose}
        ''')
        
    #get a string for passing to config file write
    def getConfigString(self):
        pass

    def getNumberOfChannelsString(self):
        match self.numberOfChannels:
            case '1':
                return Constants.audioChannels1
            case '2':
                return Constants.audioChannels2
            case '5':
                return Constants.audioChannels5

    def getMediaString(self):
        match self.type:
            case 'source' | 'Source':
                return MediaTypes.Source
            case 'sink' | 'Sink':
                return MediaTypes.Sink
            case 'duplex' | 'Duplex':
                return MediaTypes.Duplex
            case _:
                return 'Type not found'
