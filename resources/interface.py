from Python.resources.cells import *


class Button:
    icon = pygame.Surface
    pos = ()
    size = ()

    def __init__(self):
        pass

    def in_bounds(self, x, y):
        if self.pos[0] <= x < self.pos[0] + self.size[0]:
            if self.pos[1] <= y < self.pos[1] + self.size[1]:
                return True
        return False

    def is_clicked(self):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 1 and self.in_bounds(mouse_pos_x, mouse_pos_y):
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, EMPTY_COLOR, (self.pos, self.size))
        screen.blit(self.icon, self.pos)


class PlusButton(Button):

    def __init__(self):
        super().__init__()
        self.icon = plus_icon
        self.pos = plus_icon_pos
        self.size = self.icon.get_size()

    @staticmethod
    def action(size):
        if size + 1 < MAX_INS_SIZE:
            return size + 1
        return size


class MinusButton(Button):
    def __init__(self):
        super().__init__()
        self.icon = minus_icon
        self.pos = minus_icon_pos
        self.size = self.icon.get_size()

    @staticmethod
    def action(size):
        if size - 1 > 1:
            return size - 1
        return size


class SandButton(Button):
    def __init__(self):
        super().__init__()
        self.icon = sand_icon
        self.pos = sand_icon_pos
        self.size = self.icon.get_size()


class WaterButton(Button):
    def __init__(self):
        super().__init__()
        self.icon = water_icon
        self.pos = water_icon_pos
        self.size = self.icon.get_size()


class ClearButton(Button):
    def __init__(self):
        super().__init__()
        self.icon = clear_icon
        self.pos = clear_icon_pos
        self.size = self.icon.get_size()


class Instrument(ABC):
    button = Button
    size = 1
    type = None
    image = None

    @abstractmethod
    def __init__(self):
        pass

    def update_size(self, new_size):
        self.size = new_size

    @abstractmethod
    def get_cell(self, cell_pos):
        pass

    def draw(self, screen, render_text=False):
        self.button.draw(screen)
        text = FONT.render(str(self.type), True, FONT_COLOR)
        pygame.draw.rect(screen, EMPTY_COLOR, ((self.button.pos[0], self.button.pos[1] + self.button.size[1]), text.get_size()))
        if render_text:
            screen.blit(text, (self.button.pos[0], self.button.pos[1] + self.button.size[1]))

    def is_chosen(self):
        return self.button.is_clicked()

    def action(self, world):
        if pygame.mouse.get_pressed()[0] == 1:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(self.size):
                for j in range(self.size):
                    world.append(self.get_cell((grid_convert(mouse_pos)[0] + i, grid_convert(mouse_pos)[1] + j)))


class SandInstrument(Instrument):
    def __init__(self):
        self.image = sand_icon
        self.type = "Sand"
        self.size = 1
        self.button = SandButton()

    def get_cell(self, cell_pos):
        return SandCell(cell_pos)


class WaterInstrument(Instrument):
    def __init__(self):
        self.image = water_icon
        self.type = "Water"
        self.size = 1
        self.button = WaterButton()

    def get_cell(self, cell_pos):
        return WaterCell(cell_pos)


class SizeInstrument:
    def __init__(self):
        self.plus_button = PlusButton()
        self.minus_button = MinusButton()
        self.size = 1

    def draw(self, screen):
        text = FONT.render(str(self.size), True, FONT_COLOR)
        text_attribute = FONT.render("SIZE", True, FONT_COLOR)
        text_width = text.get_width()
        text_pos_x = (plus_icon_pos[0] + plus_icon_width + minus_icon_pos[0] - text_width) // 2
        text_pos_y = plus_icon_pos[1]
        self.plus_button.draw(screen)
        self.minus_button.draw(screen)
        pygame.draw.rect(screen, EMPTY_COLOR, (size_attr_pos, text_attribute.get_size()))
        pygame.draw.rect(screen, EMPTY_COLOR, ((text_pos_x, text_pos_y), text.get_size()))
        screen.blit(text_attribute, size_attr_pos)
        screen.blit(text, (text_pos_x, text_pos_y))

    def action(self):
        if self.plus_button.is_clicked():
            self.size = self.plus_button.action(self.size)
            return True
        if self.minus_button.is_clicked():
            self.size = self.minus_button.action(self.size)
            return True
        return False


class Interface:
    size = sc_width, sc_height = WINDOW_WIDTH, WINDOW_HEIGHT
    screen = pygame.display.set_mode(size, pygame.SCALED)
    screen.set_alpha(None)
    instruments = [SandInstrument(), WaterInstrument()]
    instrument_in_use = instruments[0]
    ins_size = SizeInstrument()
    clear_button = ClearButton()
    set_clicked = False

    def __init__(self):
        pass

    def iterate(self, running, world):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for ins in self.instruments:
            if ins.is_chosen():
                self.instrument_in_use = ins
                self.set_clicked = True
            else:
                ins.draw(self.screen)
        self.instrument_in_use.draw(self.screen, True)
        self.ins_size.draw(self.screen)
        self.clear_button.draw(self.screen)

        if self.ins_size.action():
            self.set_clicked = True
        if self.clear_button.is_clicked():
            self.set_clicked = True
        if not self.set_clicked:
            self.instrument_in_use.action(world)
        self.instrument_in_use.update_size(self.ins_size.size)
        set_fps()
        pygame.display.flip()
        self.set_clicked = False
        return running
