# game settings

# imports
import pygame

# Game Settings
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 720
CLOCK = pygame.time.Clock()
CELL_SIZE = 10
WORLD_SIZE = WORLD_WIDTH, WORLD_HEIGHT = WINDOW_WIDTH // CELL_SIZE, WINDOW_HEIGHT // CELL_SIZE
FPS = 120
MAX_INS_SIZE = 20
pygame.init()

# UI settings
FONT = pygame.font.SysFont('pixel', 20)
FONT_COLOR = pygame.Color((255, 255, 255))
UI_COL_SIZE = (WINDOW_WIDTH * .05)
UI_BORDERLINE = (WINDOW_WIDTH * .01)

# sand button
sand_icon_ref = pygame.image.load("resources/sand_icon.png")
sand_icon_ref_width, sand_icon_ref_height = sand_icon_ref.get_size()
sand_icon_scale = (UI_COL_SIZE - UI_BORDERLINE) / sand_icon_ref_width
sand_icon_width, sand_icon_height = int(sand_icon_ref_width * sand_icon_scale), \
                                    int(sand_icon_ref_height * sand_icon_scale)
sand_icon = pygame.transform.scale(sand_icon_ref,
                                   (sand_icon_width, sand_icon_height))
sand_icon_pos = sand_icon_pos_x, sand_icon_pos_y = \
    int(WINDOW_WIDTH - UI_COL_SIZE), int(WINDOW_HEIGHT * .2)

# water icon
water_icon_ref = pygame.image.load("resources/water_icon.png")
water_icon_ref_width, water_icon_ref_height = water_icon_ref.get_size()
water_icon_scale = (UI_COL_SIZE - UI_BORDERLINE) / water_icon_ref_width
water_icon_size = water_icon_width, water_icon_height = int(water_icon_ref_width * water_icon_scale), \
                                                        int(water_icon_ref_height * water_icon_scale)
water_icon = pygame.transform.scale(water_icon_ref, water_icon_size)
water_icon_pos = water_icon_pos_x, water_icon_pos_y = \
    int(WINDOW_WIDTH - UI_COL_SIZE), int(WINDOW_HEIGHT * .01 + sand_icon_pos_y + sand_icon_height)
# plus button
plus_icon_size = 60, 60
plus_icon_ref_pos = 270, 140
plus_icon_ref = pygame.image.load("resources/icons.png").subsurface((plus_icon_ref_pos, plus_icon_size))
plus_icon_width, plus_icon_height = plus_icon_size
plus_icon_scale = (UI_COL_SIZE / 3) / plus_icon_width
plus_icon_size = plus_icon_width, plus_icon_height = int(plus_icon_width * plus_icon_scale), \
                                                     int(plus_icon_height * plus_icon_scale)
plus_icon = pygame.transform.scale(plus_icon_ref,
                                   (plus_icon_width, plus_icon_height))
plus_icon_pos = WINDOW_WIDTH - 3 / 2 * UI_COL_SIZE - UI_BORDERLINE, int(WINDOW_HEIGHT * .1)

# minus button
minus_icon_size = 60, 60
minus_icon_ref_pos = 360, 140
minus_icon_ref = pygame.image.load("resources/icons.png").subsurface((minus_icon_ref_pos, minus_icon_size))
minus_icon_ref_width, minus_icon_ref_height = minus_icon_size
minus_icon_scale = (UI_COL_SIZE / 3) / minus_icon_ref_width
minus_icon_size = minus_icon_width, minus_icon_height = int(minus_icon_ref_width * minus_icon_scale), \
                                                        int(minus_icon_ref_height * minus_icon_scale)
minus_icon = pygame.transform.scale(minus_icon_ref,
                                    (minus_icon_width, minus_icon_height))
minus_icon_pos = WINDOW_WIDTH - int(minus_icon_width) - UI_BORDERLINE, int(WINDOW_HEIGHT * .1)

# clear button
clear_icon_ref = pygame.image.load("resources/reset_icon.png")
clear_icon_ref_width, clear_icon_ref_height = clear_icon_ref.get_size()
clear_icon_scale = (2*UI_COL_SIZE - UI_BORDERLINE) / clear_icon_ref_width
clear_icon_size = clear_icon_width, clear_icon_height = int(clear_icon_ref_width * clear_icon_scale), \
                                                        int(clear_icon_ref_height * clear_icon_scale)
clear_icon = pygame.transform.scale(clear_icon_ref,
                                    (clear_icon_width, clear_icon_height))
clear_icon_pos = WINDOW_WIDTH - 2 * UI_COL_SIZE - UI_BORDERLINE, 0

# Size Text
size_attr_pos = (plus_icon_pos[0] + minus_icon_pos[0]) // 2, int(plus_icon_pos[1] + plus_icon_height)

# colors
EMPTY_COLOR = pygame.Color((58, 56, 69))
SAND_COLOR = pygame.Color((198, 155, 123))
FONT_COLOR = pygame.Color((255, 255, 255))
WATER_COLOR = pygame.Color((108, 150, 220))


# game functions
def grid_convert(pos):
    return pos[0] // CELL_SIZE, pos[1] // CELL_SIZE


def surf_convert(pos):
    return pos[0] * CELL_SIZE, pos[1] * CELL_SIZE


def rect_convert(pos):
    return (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE), (CELL_SIZE, CELL_SIZE)


# Show FPS
def set_fps():
    CLOCK.tick(120)
    pygame.display.set_caption(f'FPS: {CLOCK.get_fps()}')
