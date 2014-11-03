#!/usr/bin/python

import csv

#define input file
#i_f = open("ranges.csv", "r")
#define output file - script to choose function based on location
o_f = open("getMap.php", "w")
#define output functions file - script to choose image based on call number input
oFunc_f = open("mapFuncs.php", "w")

#write the beginning of the php file that gets the call number and outputs html
o_f.write("<?php\n\n")

o_f.write("require('mapFuncs.php');\n\n")

o_f.write("$callNum = htmlspecialchars($_GET[\"callNum\"]);\n$loc = htmlspecialchars($_GET[\"loc\"]);\n")

o_f.write("//result page that is displayed when user clicks on a link\nprint \"<html>\";\nprint \"<head>\";\n")

o_f.write("print \"<style>\";\nprint \"p {font: 18px/20px verdana, sans-serif;}\";\n")

o_f.write("print \".main {margin-left: auto;\n\t\t margin-right:auto;\n\t\twidth: 50%;}\";")
 
o_f.write("\nprint \"</style>\";\nprint \"<body>\";\nprint '<div class=\"main\">';\n")

o_f.write("//begin checking for locations\n")

o_f.write("//each location will call a function that will display a different set of images\n")
#begin writing the functions php file
oFunc_f.write("<?php\n")

#transform call numbers into sortable values
def sortable(inCall):
    outCall = inCall

    return

def outputly(printVal):
    o_f.write(printVal)
    return

def outputLib(printVal):
    o_f.write(printVal)
    return

def outputFirstLoc(printVal):
    funcVal = printVal.replace(" ", "")
    stringVal = "\nif(strpos($loc,'" + printVal + "') !== false){\n\t" + funcVal + "StacksMap($callNum);\n}\n"
    o_f.write(stringVal)
    return

def outputLoc(printVal):
    funcVal = printVal.replace(" ", "")
    stringVal = "\nelseif(strpos($loc,'" + printVal + "') !== false){\n\t" + funcVal + "StacksMap($callNum);\n}\n"
    o_f.write(stringVal)
    return

def outputLastLoc(printVal):
    funcVal = printVal.replace(" ", "")
    stringVal = "\nelseif(strpos($loc,'" + printVal + "') !== false){\n\t" + funcVal + "StacksMap($callNum);\n}\n"
    termVal = "\nelse{\n}"
    o_f.write(stringVal + termVal)
    return

def outputFirstRange(printVal, imgVal):
    funcVal = printVal.replace(" ", "")
    outFuncVal = "function " + funcVal + "StacksMap($callNum){\n\
    \n\t$location = \"" + printVal + "\";\n\t$callNum = strip_tags($callNum);\
    \n\t$subCall = substr($callNum, 0, 20);\
    \n\tprint \"<p>You searched for $callNum</p>\";"
    oFunc_f.write(outFuncVal)
    stringVal = "if " + printVal + " " + imgVal
    oFunc_f.write(stringVal)
    return

#todo - add correct output vals
def outputRange(firstVal, secondVal, imgVal):
    stringVal = firstVal + " " + secondVal + imgVal
    oFunc_f.write(stringVal)
    return

#todo - add correct output vals
def outputLastRange(firstVal, secondVal, imgVal):
    stringVal = firstVal + " " + secondVal + imgVal
    oFunc_f.write(stringVal)
    return

#in order to write the if, elif, else statements correctly
#we need to count the number of locations
libNum = 0
locNum = 0

with open('ranges.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    
    for row in reader:
        if(row[0] == '!'):
            libNum += 1
        if(row[0] == '!!'):
            locNum += 1
    #print (libNum)
    #print (locNum)

#loop through the csv file and write the locations file
with open('ranges.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    #how many libraries are left to print
    libLeft = libNum
    #how many locations are left to print
    locLeft = locNum
    for row in reader:
        
        #if it's a library and the first one
        if((row[0] == '!') & (libLeft == libNum)):
            #print (row)
            #now there is one less library to print
            libLeft -= 1
            
        #if it's a location and the first one
        elif((row[0] == '!!') & (locLeft == locNum)):
            #print (row)
            outputFirstLoc(row[2])
            #now there is one less location to print
            locLeft -= 1
            
        #if it's a location and not the first or last one
        elif((row[0] == '!!') & (locLeft > 1)):
            #print (row)
            outputLoc(row[2])
            #now there is one less location to print
            locLeft -= 1

        #if it's a location and the last one
        elif((row[0] == '!!') & (locLeft == 1)):
            #print (row)
            outputLastLoc(row[2])
            
        elif(row[0] == '#'):
            #print (row)
            firstCallNum = row[3]
            imgVal = row[5]
            outputFirstRange(firstCallNum, imgVal)
            secondCallNum = row[2]
            outputly(secondCallNum)

#list to hold the lines in the csv    
lines = []

#loop through the csv file and put all lines in a list
with open('ranges.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    x = 0
    for row in reader:
        lines.append(row)
        if(row[0] == '!!'):
            loc = ['empty']
            loc[0] = row[2]
            #print (loc[0])
            x += 1
    print(lines)
    
#loop through the lines list and write the functions file
x = 0
for row in lines:
    if(row[x] == '!!'):
        range = [row[2]]
        range.append(lines[x+1])
        print("location is: " + range[0])
        print(range)
        x += 1
    print (row[x])




o_f.write("\n?>")
oFunc_f.write("\n?>")
#i_f.close()
oFunc_f.close()
o_f.close()
