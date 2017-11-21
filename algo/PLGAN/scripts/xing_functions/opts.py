# !/usr/bin/env python
# !encoding:utf-8

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--path", type=str, default='/home/xing/maps-20m', help="Directory to all the maps")

args = parser.parse_args()

# print args.path
