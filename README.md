# SandBox Project

To run my project in terminal run this commands:
det-apt install pipx
(or brew install pipx if you use MacOS)
- pipx install pygame
- pipx install enum
- pipx install random
Then in terminal try "python3 main.py"

To have fun:
- in file resources/settings.py, there are WINDOW size, such as:
        "WINDOW_WIDTH = 1024 WINDOW_HEIGHT = 720"
    you can change them yourself if you want to
- in file resources/settings.py, there are CELL size, such as:
        "CELL_SIZE = 5"
        "MAX_INS_SIZE = 10"
    this sets up the minimum cell_size that can be in my game
    I highly do not recommend set it very low(like from 1 to 4) due to bad performance
