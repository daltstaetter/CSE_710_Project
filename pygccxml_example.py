#!/usr/bin/python3


## https://pygccxml.readthedocs.io/en/master/examples/variables/example.html
import os,sys, pathlib
from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser


## Example C file

##namespace ns{
##    int a = 1;
##    int b = 2;
##    double c = 3.0;
##}



##

# Find out the c++ parser
generator_path, generator_name = utils.find_xml_generator()

# Configure the xml generator
xml_generator_config = parser.xml_generator_configuration_t(
    xml_generator_path=generator_path,
    xml_generator=generator_name)

# The c++ file we want to parse
filename = r'/home/daltstaetter/Dropbox/College/Graduate/Fall_2019/CSE_710/Project/example.hpp'

decls = parser.parse([filename], xml_generator_config)
global_namespace = declarations.get_global_namespace(decls)
ns = global_namespace.namespace("ns")

# The variables() method will return a list of variables.
# We know that the c variable is the third one in the list:
c = ns.variables()[2]
print("My name is: " + c.name)
print("My type is: " + str(c.decl_type))
print("My value is: " + c.value)

# Of course you can also loop over the list and look for the right name
for var in ns.variables():
    if var.name == "c":
        print("My name is: " + var.name)
        print("My type is: " + str(var.decl_type))
        print("My value is: " + var.value)

# One way to get a variable is to use the variable() method and
# a lambda function. This is the most flexible way as you can implement
# your own lambda function to filter out variables following your
# specific criteria.
c = ns.variable(lambda v: v.name == "c")
print("My name is: " + c.name)
print("My type is: " + str(c.decl_type))
print("My value is: " + c.value)

##
ns = global_namespace.namespace("bs")

# The variables() method will return a list of variables.
# We know that the c variable is the third one in the list:
c = ns.variables()[2]
print("My name is: " + c.name)
print("My type is: " + str(c.decl_type))
print("My value is: " + c.value)

# Of course you can also loop over the list and look for the right name
for var in ns.variables():
    if var.name == "f":
        print("My name is: " + var.name)
        print("My type is: " + str(var.decl_type))
        print("My value is: " + var.value)

# One way to get a variable is to use the variable() method and
# a lambda function. This is the most flexible way as you can implement
# your own lambda function to filter out variables following your
# specific criteria.
c = ns.variable(lambda v: v.name == "f")
print("My name is: " + c.name)
print("My type is: " + str(c.decl_type))
print("My value is: " + c.value)


