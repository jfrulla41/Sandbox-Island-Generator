class Tile(object):

    def __init__(self, elevation=0):
        self.elevation=elevation
        self.populated=False
        self.type=""
        self.subtype=""
        self.humidity=0.0
        self.biome=""
        self.tree_cluster=False
        self.tree_tile=False
        self.additional_humidity=0
        self.humidity_adjusted=False
