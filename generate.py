#!/usr/bin/python

import csv

#define input file
#i_f = open("ranges.csv", "r")
#define output file - script to choose function based on location
o_f = open("getMap.php", "w")


#write the beginning of the php file that gets the call number and outputs html
o_f.write("<?php\n\n")
#include the php sort file
o_f.write('  include("../include/sort.php");')

o_f.write("$callNum = htmlspecialchars($_GET[\"callNum\"]);\n$loc = htmlspecialchars($_GET[\"loc\"]);\n")

o_f.write("//result page that is displayed when user clicks on a link\nprint \"<html>\";\nprint \"<head>\";\n")

o_f.write("print \"<style>\";\nprint \"p {font: 18px/20px verdana, sans-serif;}\";\n")

o_f.write("print \".main {margin-left: auto;\n\t\t margin-right:auto;\n\t\twidth: 50%;}\";")
 
o_f.write("\nprint \"</style>\";\nprint \"<body>\";\nprint '<div class=\"main\">';\n")

o_f.write("//define locations array\n")


#loop through the csv file and write the locations file
with open('ranges.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')

    for row in reader:
        #print (row[0])
        
        #if it's a library
        if(row[0] == '!'):
            #print (row[1])
            libName = row[1]
            
        #if it's a location
        elif(row[0] == '!!'):
            #print (row[2])
            loc = row[2]

        #if it's a range
        elif(row[0] == '#'):
            print (libName + ' ' + loc + ' ' + row[3] + ' ' + row[4] + ' ' + row[5])
            beginCallNum = row[3]
            endCallNum = row[4]
            imageFile = row[5]
            

            


o_f.write("\n?>")
#i_f.close()
o_f.close()
