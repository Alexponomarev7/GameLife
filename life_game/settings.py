BASIC_RADIUS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]
ALIVE = True
LANDSCAPE = False

ADDS = ["EmptyBlock", "Fish", "CrayFish", "Mountain"]

EmptyBlock = 0
Fish = 1
CrayFish = 2
Mountain = 3

ROW_COORDINATE = 0
COLUMN_COORDINATE = 1

TYPE = 0
POSITIONS = 1
MIN_VALUE = 2
MAX_VALUE = 3

UPLOADED_BLOCKS = {"f" : Fish,
                   "s" : CrayFish,
                   "n" : EmptyBlock,
                   "r" : Mountain}

UPLOADED_BLOCKS_REV = dict([(UPLOADED_BLOCKS[x], x) for x in UPLOADED_BLOCKS])
