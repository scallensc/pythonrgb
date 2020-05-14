import sys
import time
import argparse
import magichue
from magichue import discover_bulbs

from magichue import (
    CustomMode,
    MODE_GRADUALLY,
)

sloworange_pat = CustomMode(
    mode=MODE_GRADUALLY,
    speed=0.5,
    colors=[
        (255, 35, 0),
        (128, 16, 0)
    ]
)

slowpurple_pat = CustomMode(
    mode=MODE_GRADUALLY,
    speed=0.5,
    colors=[
        (255, 0, 255),
        (128, 0, 72)
    ]
)


def seton():
    light = magichue.Light('10.0.0.21')
    light.on = True


def setoff():
    light = magichue.Light('10.0.0.21')
    light.on = False

# RGB basic colours


def setred():
    light = magichue.Light('10.0.0.21')
    light.mode = magichue.NORMAL
    light.rgb = (255, 0, 0)
    light.brightness = 255


def setblue():
    light = magichue.Light('10.0.0.21')
    light.mode = magichue.NORMAL
    light.rgb = (0, 0, 255)
    light.brightness = 255


def setgreen():
    light = magichue.Light('10.0.0.21')
    light.mode = magichue.NORMAL
    light.rgb = (0, 255, 0)
    light.brightness = 255

# Blends


def setorange():
    light = magichue.Light('10.0.0.21')
    light.mode = magichue.NORMAL
    light.rgb = (255, 35, 0)
    light.brightness = 255


def setcyan():
    light = magichue.Light('10.0.0.21')
    light.mode = magichue.NORMAL
    light.rgb = (0, 255, 255)
    light.brightness = 255


def setpurple():
    light = magichue.Light('10.0.0.21')
    light.mode = magichue.NORMAL
    light.rgb = (255, 0, 255)
    light.brightness = 255


def whstrobe():
    light = magichue.Light('10.0.0.21')
    revertm = light.mode
    revertc = light.rgb

    light.speed = 1
    light.mode = magichue.WHITE_STROBE

    time.sleep(3)
    light.rgb = revertc
    light.mode = revertm
    light.brightness = 255


def pustrobe():
    light = magichue.Light('10.0.0.21')
    revertm = light.mode
    revertc = light.rgb

    light.speed = 1
    light.mode = magichue.PURPLE_STROBE

    time.sleep(3)
    light.rgb = revertc
    light.mode = revertm
    light.brightness = 255


def slowpurple():
    light = magichue.Light('10.0.0.21')
    light.speed = 0.5
    light.mode = slowpurple_pat


def sloworange():
    light = magichue.Light('10.0.0.21')
    light.speed = 0.5
    light.mode = sloworange_pat


def gbcrossfade():
    light = magichue.Light('10.0.0.21')
    light.speed = 0.5
    light.mode = magichue.GREEN_BLUE_CROSSFADE


def rbcrossfade():
    light = magichue.Light('10.0.0.21')
    light.speed = 0.5
    light.mode = magichue.RAINBOW_CROSSFADE


if __name__ == "__main__":
    print('RGB Control online!')
