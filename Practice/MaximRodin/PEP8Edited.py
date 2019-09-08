import sys
import os
import hashlib
import ast
import argparse
from time import *


class Shuffler:        #название класса с большой буквы

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []  #Тут было 6 пробелов, исправил до 4

    for root, directories, files in os.walk(dirname):
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append([root, file])
    for path, mp3 in mp3s:
        hashname = self.generateName() + '.mp3'
        self.map[hashname] = mp3
        os.rename(path + '/' + mp3, path + '/' + hashname) #тут были лишние скобки
        f = open(output, 'r')   #Эта и строчка ниже относятся к блоку for и должны быть выровнены по одной линии по вертикали
        f.write(str(self.map))

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:   #тут было 5 отступов
            self.map = ast.literal_eval(f.read()) #тут было 3 отступа
        mp3s = []

    for root, directories, files in os.walk(dirname):
        for file in files:
            if file[-3:] == '.mp3':  #тут было 3 отступа
                mp3s.append({root, file})  #тут было 5 отступов
    for path, hashname in mp3s:
        os.rename(path + '/' + hashname, path + '/' + self.map[hashname])
        os.remove(restore_path)  #Данная строчка должна быть на одной линии с верхней тк относятся к блоку for

    def generateName(self, seed=time()):
        return hashlib.md5(str(seed)).hexdigest()  #тут было 5 отступов


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
        if args.output:
            Shuffler.rename(args.dirname, 'restore.info') #тут было 6 отступов
        else:
            Shuffler.rename(args.dirname, args.output) #тут было 6 отступов
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()