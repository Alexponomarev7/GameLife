from . import settings


class Block(object):
    def __init__(self, type_id, name):
        self.type_id = type_id
        self.name = name


class Fish(Block):
    rule = [(settings.Fish, settings.BASIC_RADIUS, 2, 3)]
    
    def __init__(self):
        super(Fish, self).__init__(settings.ALIVE, settings.Fish)


class CrayFish(Block):
    rule = [(settings.CrayFish, settings.BASIC_RADIUS, 2, 3)]
    
    def __init__(self):
        super(CrayFish, self).__init__(settings.ALIVE, settings.CrayFish)


class EmptyBlock(Block):
    rule = [(settings.Fish, settings.BASIC_RADIUS, 3, 3),
                                        (settings.CrayFish, settings.BASIC_RADIUS, 3, 3)]
    def __init__(self):
        super(EmptyBlock, self).__init__(settings.LANDSCAPE, settings.EmptyBlock)


class Mountain(Block):
    rule = []
    
    def __init__(self):
        super(Mountain, self).__init__(settings.LANDSCAPE, settings.Mountain)
