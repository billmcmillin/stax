#!/usr/bin/python

import csv

#define input file
#i_f = open("ranges.csv", "r")
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


def outputly(printVal):
    o_f.write(printVal)
    return

with open('ranges.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        colnum = 0
        rownum = 0
        for row in reader:
            if(row[0] == '!'):
                print (row)
                outputly(row[0])
            if(row[0] == '!!'):
                print (row)
                outputly(row[0])
            if(row[0] == '#'):
                print (row)
                firstCallNum = row[1]
                outputly(firstCallNum)
                secondCallNum = row[2]
                outputly(secondCallNum)
                    
        
      
#i_f.close()
o_f.close()
