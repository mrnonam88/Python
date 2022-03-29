from Python.resources.settings import *


class Solid(enum.Enum):
    sand = "SAND"


class Liquid(enum.Enum):
    water = "WATER"


class CellType(enum.Enum):
    solid = Solid
    liquid = Liquid
    empty = "EMPTY"


class Cell(ABC):
    color = None
    pos = x, y = None, None
    type = None

    @abstractmethod
    def __init__(self):
        pass

    def update_pos(self, new_pos):
        self.pos = self.x, self.y = new_pos[0], new_pos[1]

    @abstractmethod
    def try_move(self, x, y, bounds):
        pass

    @abstractmethod
    def behave(self, bounds):
        pass

    @abstractmethod
    def should_store(self, bounds):
        pass


class EmptyCell(Cell):
    def __init__(self, p):
        self.color = EMPTY_COLOR
        self.type = CellType.empty
        self.pos = self.x, self.y = p

    def try_move(self, x, y, bounds):
        pass

    def behave(self, bounds):
        pass

    def should_store(self, bounds):
        return False


class SandCell(Cell):
    def __init__(self, p):
        super().__init__()
        self.color = SAND_COLOR
        self.type = CellType.solid.value.sand
        self.pos = self.x, self.y = p
        self.moved = False

    def try_move(self, x, y, bounds):
        if bounds.in_bounds(x, y):
            if bounds.celling[x][y].type != CellType.solid.value.sand:
                return True
        return False

    def behave(self, bounds):
        if self.try_move(self.x, self.y + 1, bounds):
            bounds.swap(self.pos, (self.x, self.y + 1))
        else:
            if self.try_move(self.x + 1, self.y + 1, bounds) and self.try_move(self.x - 1, self.y + 1, bounds):
                bounds.swap(self.pos, (self.x + randint(-1, 1), self.y + 1))
            else:
                if self.try_move(self.x + 1, self.y + 1, bounds):
                    bounds.swap(self.pos, (self.x + 1, self.y + 1))
                if self.try_move(self.x - 1, self.y + 1, bounds):
                    bounds.swap(self.pos, (self.x - 1, self.y + 1))

    def should_store(self, bounds):
        return True


class WaterCell(Cell):
    def __init__(self, p):
        super().__init__()
        self.color = WATER_COLOR
        self.type = CellType.liquid.value.water
        self.pos = self.x, self.y = p

    def try_move(self, x, y, bounds):
        if bounds.in_bounds(x, y):
            if bounds.celling[x][y].type != CellType.solid.value.sand \
                    and bounds.celling[x][y].type != CellType.liquid.value.water:
                return True
        return False

    def behave(self, bounds):
        if self.try_move(self.x, self.y + 1, bounds):
            bounds.swap(self.pos, (self.x, self.y + 1))
        else:
            if self.try_move(self.x + 1, self.y + 1, bounds) and self.try_move(self.x - 1, self.y + 1, bounds):
                bounds.swap(self.pos, (self.x + randint(-1, 1), self.y + 1))
            else:
                if self.try_move(self.x + 1, self.y + 1, bounds):
                    bounds.swap(self.pos, (self.x + 1, self.y + 1))
                elif self.try_move(self.x - 1, self.y + 1, bounds):
                    bounds.swap(self.pos, (self.x - 1, self.y + 1))
                else:
                    if self.try_move(self.x - 1, self.y, bounds) and self.try_move(self.x + 1, self.y, bounds):
                        bounds.swap(self.pos, (self.x + randint(-1, 1), self.y))
                    else:
                        if self.try_move(self.x + 1, self.y, bounds):
                            bounds.swap(self.pos, (self.x + 1, self.y))
                        elif self.try_move(self.x - 1, self.y, bounds):
                            bounds.swap(self.pos, (self.x - 1, self.y))

    def should_store(self, bounds):
        return True
