import enum

class MediaTypes(enum.Enum):
    Sink = 'Audio/Sink'
    Source = 'Audio/Source/Virtual'
    Duplex = 'Audio/Duplex'

    def __str__(self):
        return self.value