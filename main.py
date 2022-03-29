from resources.interface import *


class World:
    def __init__(self, inter):
        self.width, self.height = WORLD_SIZE
        self.space = inter.screen
        self.cells = set()
        self.celling = [[Cell] * self.height for _ in range(self.width)]
        self.base_color = EmptyCell((0, 0)).color
        self.updates = set()
        self.start()

    def start(self):
        self.space.fill(self.base_color)
        for i in range(self.width):
            for j in range(self.height):
                self.celling[i][j] = EmptyCell((i, j))

    def update(self):
        self.updates = set()
        copy = self.cells.copy()
        for cell_pos in copy:
            self.celling[cell_pos[0]][cell_pos[1]].behave(self)
        self.update_cells()

    def update_cells(self):
        cells = set()
        for x, y in self.cells:
            if self.celling[x][y].should_store(self):
                cells.add((x, y))
        cells = set(sorted(cells))
        self.cells = set(sorted(cells, reverse=True))

    def draw(self):
        # self.space.fill(self.base_color)
        for x, y in self.updates:
            rect = self.celling[x][y]
            pygame.draw.rect(self.space, rect.color, rect_convert((x, y)))
            if CELL_SIZE == 1:
                self.space.set_at((x, y), rect.color)

    def in_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        return True

    def swap(self, pos_1, pos_2):
        self.celling[pos_1[0]][pos_1[1]], self.celling[pos_2[0]][pos_2[1]] = self.celling[pos_2[0]][pos_2[1]], \
                                                                             self.celling[pos_1[0]][pos_1[1]]
        self.celling[pos_1[0]][pos_1[1]].update_pos(pos_1)
        self.celling[pos_2[0]][pos_2[1]].update_pos(pos_2)
        self.cells.add(pos_2)
        self.updates.add(pos_1)
        self.updates.add(pos_2)

    def append(self, new_cell):
        if self.in_bounds(new_cell.x, new_cell.y):
            self.celling[new_cell.x][new_cell.y] = new_cell
            self.cells.add((new_cell.x, new_cell.y))
            self.updates.add((new_cell.x, new_cell.y))

    def iterate(self):
        self.draw()
        self.update()


interface = Interface()
world = World(interface)
running = True
# world.append(WaterCell((10, 10)))
while running:
    running = interface.iterate(running, world)
    if interface.clear_button.is_clicked():
        world = World(interface)
    world.iterate()
