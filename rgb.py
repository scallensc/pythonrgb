import sys
import time
import argparse
import magichue
from magichue import discover_bulbs

from magichue import (
    CustomMode,
    MODE_GRADUALLY,
)

opfade_pat = CustomMode(
    mode=MODE_GRADUALLY,
    speed=0.5,
    colors=[
        (255, 0, 255),
        (255, 35, 0)
    ]
)

gbfade_pat = CustomMode(
    mode=MODE_GRADUALLY,
    speed=0.5,
    colors=[
        (0, 255, 0),
        (0, 0, 255)
    ]
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

def opfade():
    light = magichue.Light('10.0.0.21')
    light.speed = 0.5
    light.mode = opfade_pat


def gbfade():
    light = magichue.Light('10.0.0.21')
    light.speed = 0.5
    light.mode = gbfade_pat

# argparse for command line to trigger function


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_on = subparsers.add_parser('on', help='set light to on')
parser_on.set_defaults(func=seton)

parser_off = subparsers.add_parser('off', help='set light to off')
parser_off.set_defaults(func=setoff)

parser_red = subparsers.add_parser('red', help='set light to red')
parser_red.set_defaults(func=setred)

parser_green = subparsers.add_parser('green', help='set light to green')
parser_green.set_defaults(func=setgreen)

parser_blue = subparsers.add_parser('blue', help='set light to blue')
parser_blue.set_defaults(func=setblue)

parser_orange = subparsers.add_parser('orange', help='set light to orange')
parser_orange.set_defaults(func=setorange)

parser_sloworange = subparsers.add_parser(
    'sloworange', help='set light to slow pulse orange')
parser_sloworange.set_defaults(func=sloworange)

parser_cyan = subparsers.add_parser('cyan', help='set light to cyan')
parser_cyan.set_defaults(func=setcyan)

parser_purple = subparsers.add_parser('purple', help='set light to purple')
parser_purple.set_defaults(func=setpurple)

parser_slowpurple = subparsers.add_parser(
    'slowpurple', help='set light to slow pulse purple')
parser_slowpurple.set_defaults(func=slowpurple)

parser_whitestrobe = subparsers.add_parser(
    'whitestrobe', help='set light to strobe white')
parser_whitestrobe.set_defaults(func=whstrobe)

parser_purplestrobe = subparsers.add_parser(
    'purplestrobe', help='set light to strobe purple')
parser_purplestrobe.set_defaults(func=pustrobe)

parser_gbfade = subparsers.add_parser(
    'gbfade', help='set light to green and blue crossfade')
parser_gbfade.set_defaults(func=gbfade)

parser_opfade = subparsers.add_parser(
    'opfade', help='set light to rainbow crossfade')
parser_opfade.set_defaults(func=opfade)


if len(sys.argv) <= 1:
    sys.argv.append('--help')

options = parser.parse_args()

options.func()
