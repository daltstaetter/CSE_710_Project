#!/usr/bin/env python3

from platform import python_version
ver = python_version()

if ver.startswith('2'):
    sys.exit('Run with python3')

import os,sys, pathlib

#sys.argv[0] = 'fixpoint_parser.py'
#sys.argv.append('filename.c')
#sys.argv.append('/home/daltstaetter/eclipse_workspace/Fixed_Point_program/main.c')
#sys.argv.append('/home/daltstaetter/Fall_2019/CSE_710/Project/meeting.txt')

if len(sys.argv) is not 2:
    print("usage: python3 fixpoint_parser.py filename.c")
    sys.exit()
    

f_path1 = pathlib.Path(os.getcwd() + os.sep + sys.argv[1])
f_path2 = pathlib.Path(sys.argv[1])

if f_path1.exists():
    path = f_path1
elif f_path2.exists():
    path = f_path2
else:
    print("invalid path to {0} or {0} does not exist".format(sys.argv[1]))
    sys.exit()

lvars = dict()
found_fmul3 = 0
cnt = 0
line_num = 0
with path.open() as in_file:
    program = in_file.readlines()
    for line in program:
        line_num = line_num + 1
        if line.strip().startswith(r'//'):
            continue
        elif line.strip().startswith(r'fix_t'):
            pass # identify variables & assign format
        elif 'FMUL3' in line.strip():
            found_fmul3 = True;#print(line + " found FMUL",end='')
            cnt = cnt + 1
            
                           
        print(line.rstrip('\n'), end=' ')
        if found_fmul3 is True:
            print("Found FMUL3_{}".format(cnt), end='')
            found_fmul3 = False

        print("")
##        
