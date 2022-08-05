#storage class for constants as pipewire config values and labels, etc
class Constants:
    factoryNameValue = 'support.null-audio-sink'
    factoryNameLabel = 'factory.name'
    factoryValue = 'adapter'
    factoryLabel = 'factory'
    objectLingerValue = 'true'
    objectLingerLabel = 'object.linger'
    nodeNameLabel = 'node.name'
    mediaClassLabel = 'media.class'
    audioPositionLabel = 'audio.position'
    audioPositionsCharOpen = '['
    audioPositionsCharClose = ']'
    wrapperCharOpen = '{'
    wrapperCharClose = '}'
    audioChannels1 = "MONO"
    audioChannels2 = "[FL FR]"
    audioChannels5 = "[FL FR FC RL RR]"

    def __init__(self):
        pass