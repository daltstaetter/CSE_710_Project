#!/usr/bin/env python3

from platform import python_version
ver = python_version()

if ver.startswith('2'):
    sys.exit('Run with python3')

import os,sys, pathlib, re, scanf




def get_variable(input_line):
    var_dict = {}
    var_re = re.compile("fix_t \w[,\s\w]*") # gets all var declarations
    #Qformat = re.compile("fix_t\s+\w[,\s\w]*[\s=]*[x\d\sa-fA-F]*;\s*/[\*/]+\s*[Qq][\d]+\.[\d]+[\s\*]*[/]*") # fix_t a[,b,c,d][ = 0x123]; // Q3.28 
    match = var_re.match(input_line)
    if match:
        match_str = match.group()
        in_vars = match_str.split('fix_t')[1].strip() # removes 'fix_t'

        for i in in_vars.split(','):
            var_dict[i.strip()] = None

    print(var_dict)

    # get q_format
    if '//' in input_line:
        var_qformat_str = input_line.split('//')[1].strip()
        print(var_qformat_str)
        while var_qformat_str[0] is not ('q' or 'Q') and ('q' or 'Q') in var_qformat_str[1:]:
            var_qformat_str = var_qformat_str[1:].strip()
        
    elif '/*' in input_line:
        var_qformat_str = input_line.split('/*')[1].strip()
        print(var_qformat_str)
        while var_qformat_str[0] is not ('q' or 'Q') and ('q' or 'Q') in var_qformat_str[1:]:
            var_qformat_str = var_qformat_str[1:].strip()
    else:
        var_qformat_str = None;


    qformat_re = re.compile("[Qq][\d]+\.[\d]+")
    qformat = qformat_re.match(var_qformat_str)
    if qformat:
        (_,nInt,nFraction) = scanf.scanf("%c%d.%d",qformat.group())    
    print(nInt,nFraction)


##






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
            get_variable(line.strip())
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
