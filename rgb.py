import sys
import time
import argparse
import magichue
import sys
import socket
import json
from magichue import discover_bulbs

from magichue import (
    CustomMode,
    MODE_GRADUALLY,
)

light = magichue.Light('10.0.0.24')
ip = '10.0.0.24'


def add_checksum(values):
    checksum = int(hex(sum(values) & 0xff), 16)
    values.append(checksum)
    return values


def get_status(ip):
    try:
        data = bytearray(process_raw('81:8a:8b:96'))

        s = socket.socket()
        s.settimeout(5)
        s.connect((ip, 5577))
        s.send(data)
        response = s.recvfrom(1024)
        s.close()
        response = [hex(s).replace('0x', '') for s in response[0]]
        response = ['0'+s if len(s) == 1 else s for s in response]
        return response
    except:
        print_error("Could not get the bulb's status")
        return None


def get_version(ip):
    try:
        data = bytearray(process_raw(
            '48:46:2d:41:31:31:41:53:53:49:53:54:48:52:45:41:44'))  # HF-A11ASSISTHREAD
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        s.sendto(data, (ip, 48899))
        response = s.recvfrom(1024)
        s.close()
        msg = response[0].decode('utf-8')
        version = msg.split(',')

        return version[2]
    except:
        print_error("Could not get the bulb's version")
        return None


def send(ip, values):
    try:
        get_version(ip)

        s = socket.socket()
        s.connect((ip, 5577))
        s.send(bytearray(add_checksum(values)))
        s.close()

        out = {"success": True}
        print(json.dumps(out))
        return
    except:
        print_error("Could not send the message to the bulb")


def process_raw(raw):
    print(raw)
    raw = raw.split(':')
    values = ['0x' + s for s in raw]
    values = [int(v, 16) for v in values]
    return values


def process_rgb(rgb, version):
    rgb = rgb.split(',')
    if len(rgb) < 3:
        print_error('Must have three color values (0-255) for R,G,B')

    values = [int(v) for v in rgb]
    values.insert(0, 49)  # add header

    # this version has an extra zero in the body
    if version == "AK001-ZJ2101":
        values.extend([0])

    values.extend([0, 240, 15])  # add tail
    return values


def process_power(power):
    if power == 'on':
        return process_raw('71:23:0f')
    if power == 'off':
        return process_raw('71:24:0f')


def print_error(message):
    out = {"success": False, "error": message}
    print(json.dumps(out))
    sys.exit()


def seton():
    light.on = True


def setoff():
    light.on = False


def setred():
    light.is_white = False
    light.rgb = (255, 0, 0)
    light.brightness = 255
    light.is_white = False
    print(light._get_status_data())


def setgreen():
    light.is_white = False
    light.rgb = (0, 255, 0)
    light.brightness = 255
    light.is_white = False
    print(light._get_status_data())


def setblue():
    light.is_white = False
    light.rgb = (0, 0, 255)
    light.brightness = 255
    light.is_white = False
    print(light._get_status_data())


def setorange():
    light.is_white = False
    light.rgb = (255, 35, 0)
    light.brightness = 255
    light.is_white = False
    print(light._get_status_data())


def setcyan():
    light.is_white = False
    light.rgb = (0, 255, 255)
    light.brightness = 255
    light.is_white = False
    print(light._get_status_data())


def setpurple():
    light.is_white = False
    light.rgb = (255, 0, 255)
    light.brightness = 255
    light.is_white = False
    print(light._get_status_data())


def setwarm():
    light.cw = 0
    light.w = 255
    light.is_white = True
    print(light._get_status_data())


def setcool():
    cool = hex(int(255)).replace('0x', '')
    print(cool)
    values = process_raw('31:00:00:00:00:'+cool+':0f')
    send(ip, values)

    # light.cw = 255
    # light.w = 0
    # light.is_white = True
    # print(light._get_status_data())


def brightup():
    currentval = light.brightness
    light.brightness = currentval + 25
    print(light._get_status_data())


def brightdown():
    currentval = light.brightness
    light.brightness = currentval - 25
    print(light._get_status_data())


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

parser_cyan = subparsers.add_parser('cyan', help='set light to cyan')
parser_cyan.set_defaults(func=setcyan)

parser_purple = subparsers.add_parser('purple', help='set light to purple')
parser_purple.set_defaults(func=setpurple)

parser_warm = subparsers.add_parser(
    'warm', help='set light to warm white')
parser_warm.set_defaults(func=setwarm)

parser_cool = subparsers.add_parser(
    'cool', help='set light to cool white')
parser_cool.set_defaults(func=setcool)

parser_brightup = subparsers.add_parser(
    'brightup', help='set brightness to +10%')
parser_brightup.set_defaults(func=brightup)

parser_brightdown = subparsers.add_parser(
    'brightdown', help='set brightness to -10%')
parser_brightdown.set_defaults(func=brightdown)

if len(sys.argv) <= 1:
    sys.argv.append('--help')

options = parser.parse_args()

options.func()
