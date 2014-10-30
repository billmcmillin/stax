#!/usr/bin/python

import csv

#define input file
i_f = open("ranges.csv", "r")
#define output file - script to choose image based on call number input
o_f = open("getMap.php", "w+")

#write the beginning of the php file that gets the call number and outputs html
o_f.write("<?php\n\n")

o_f.write("$callNum = htmlspecialchars($_GET[\"callNum\"]);\n$loc = htmlspecialchars($_GET[\"loc\"]);\n")

o_f.write("//result page that is displayed when user clicks on a link\nprint \"<html>\";\nprint \"<head>\";\n")

o_f.write("print \"<style>\";\nprint \"p {font: 18px/20px verdana, sans-serif;}\";\n")

o_f.write("print \".main {margin-left: auto;\n margin-right:auto;\nwidth: 50%;}\";")
 
o_f.write("print \"</style>\";print \"<body>\";\nprint '<div class=\"main\">';\n")

o_f.write("//begin checking for locations\n")

for line in i_f:
    username = "init uname"
    dep = "init dep"
    uname = line.rsplit(' ',1)[1]

def outputly(uname):
    o_f.write("found faculty name\n")
    o_f.write(uname)
    return

    with open('fac_username_deps_clean.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            colnum = 0
            for col in row:
                if colnum ==0:
                    username = col
                  #  print username
                if colnum ==2:
                    dep = col
                   # print dep
                        
                colnum += 1
            outputly(username);       
        #o_f.write("found faculty name")
        #o_f.write('\n')

i_f.close()
o_f.close()
