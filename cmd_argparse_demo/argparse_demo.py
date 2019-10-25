#!/usr/bin/python3
#导入argparse模块
import argparse

parser= argparse.ArgumentParser(description='''
This script is a demo of argparse module.
''')

#add positonal arguments
parser.add_argument('param1', help='the first param')
parser.add_argument('param2', help='the second param')

#add optional arguments
#you can point certain value or use default value
parser.add_argument('--param3', help='the thrid param(default path)', default='/usr/lib')
parser.add_argument('--param4', help='the forth param(default: 1)', default=1.)
#a param just for certain action
parser.add_argument('--plot', help='plot data')
parser.add_argument('--s', help='save result')
parser.add_argument('--param5', help='print verbose info', action='store_true')	#no value, an action


#parse cmd param
args=parser.parse_args()

#print param info
if args.param5 :
    print(args.param1)	#python3中print为函数，python2中为语句（print args.param1） 
    print(args.param2)
    print(args.param3)
    print(args.param4)
    print(args.param5)
if args.plot :
    print("plot data")
if args.s :
    print("save result")
