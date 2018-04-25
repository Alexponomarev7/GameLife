#! /usr/bin/env python3

from life_game.utility import Game


import argparse


parser = argparse.ArgumentParser(prog='Game "Life"',
                                 description='''Life simulator in ocean.''',
                                 epilog='''
                                 Alex Ponomarev DIHT 796''')

parser.add_argument("-fin", "--filein", type=str, help="Read given desk from the file. Default is stdin.", metavar='INPUT')
parser.add_argument("-fout", "--fileout", type=str, help="Write current desk to the file. Default is stdout.", metavar='OUTPUT')
parser.add_argument("-t", "--test", type=str, help="Test current directory.")

args = parser.parse_args()

source_in = None
source_out = None

if args.filein:
    source_in = args.filein 

if args.fileout:
    source_out = args.fileout

g = Game()

g.upload(source_in)
g.make_generation(g.generations)
g.download(source_out)
