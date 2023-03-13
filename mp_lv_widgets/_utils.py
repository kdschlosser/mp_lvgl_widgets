import micropython
import math


@micropython.viper
def remap(value: int,old_min: int,old_max: int, new_min: int, new_max: int) -> int:
    return int((((value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min)


@micropython.viper
def point_on_circle(degree: int,center_x: int,center_y: int,radius: int) -> tuple:
    radians = float(math.radians(degree / 1000.0))
    cos = float(math.cos(radians))
    sin = float(math.sin(radians))

    x = int(round(center_x + (radius * cos)))
    y = int(round(center_y + (radius * sin)))
    return x, y

