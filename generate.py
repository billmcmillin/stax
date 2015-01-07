#!/usr/bin/python

import csv

#define input file
#i_f = open("ranges.csv", "r")
#define output file - script to choose function based on location
o_f = open("getMap.php", "w")


#write the beginning of the php file that gets the call number and outputs html
o_f.write("<?php\n\n")
#include the php sort file
o_f.write('  include("sortLCC.php");\n')

o_f.write('class stdObject {\n    public function __construct(array $arguments = array()) {\n')

o_f.write('        if (!empty($arguments)) {\n            foreach ($arguments as $property => $argument) {\n')

o_f.write('                $this->{$property} = $argument;\n}\n}\n}\n\n')

o_f.write('    public function __call($method, $arguments) {\n        $arguments = array_merge(array("stdObject" => $this), $arguments); // Note: method argument 0 will always referred to the main class ($this).\n')

o_f.write('        if (isset($this->{$method}) && is_callable($this->{$method})) {\n')

o_f.write('            return call_user_func_array($this->{$method}, $arguments);\n        } else {\n')

o_f.write('            throw new Exception("Fatal error: Call to undefined method stdObject::{$method}()");\n}\n}\n}\n')

o_f.write("$callNum = htmlspecialchars($_GET[\"callNum\"]);\n$loc = htmlspecialchars($_GET[\"loc\"]);\n$x = 0;\n\n")

o_f.write("$subCall = NormalizeLC($callNum);\n")

o_f.write("//result page that is displayed when user clicks on a link\nprint \"<html>\";\nprint \"<head>\";\n")

o_f.write("print \"<style>\";\nprint \"p {font: 18px/20px verdana, sans-serif;}\";\n")

o_f.write("print \".main {margin-left: auto;\n\t\t margin-right:auto;\n\t\twidth: 50%;}\";")
 
o_f.write("\nprint \"</style>\";\nprint \"<body>\";\nprint '<div class=\"main\">';\n")

o_f.write("//declare an object for each location and populate it\n")


#loop through the csv file and write the locations file
with open('ranges.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    x = 0
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
            o_f.write('  $locObj' + str(x) + '= new stdObject();\n  $locObj' + str(x) + '->libName = "' + libName + '";\n')
            o_f.write('  $locObj' + str(x) + '->location = "' + loc + '";\n  $locObj' + str(x) + '->callNumBegin = NormalizeLC("' + beginCallNum + '");\n')
            o_f.write('  $locObj' + str(x) + '->callNumEnd = NormalizeLC("' + endCallNum + '");\n  $locObj' + str(x) + '->imageFile = "' + imageFile + '";\n\n')

            x = x + 1
            

    o_f.write('//put all the objects in an array\n\n')
    o_f.write('	$locArray = array(\n')
    q = 0
    with open('ranges.txt', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:            
            #if it's a range
            if(row[0] == '#'):
                o_f.write('	  ' + str(q) + ' => $locObj' + str(q) + ',\n')
                q = q + 1
    o_f.write(');\n\n')

    o_f.write('//begin checking for locations\n\n')
    o_f.write('  foreach ($locArray as $locValue => $cur){\n\n')
    o_f.write('  //iterate through each location object and if a match is found, display the map\n')
    o_f.write('  if (($cur->location === $loc)&& ($subCall >= $cur->callNumBegin) && ($subCall <= $cur->callNumEnd)) {\n')
    o_f.write('    print "<p>Call number " . $subCall . " is in location: " . $cur->location . ".";\n')
    o_f.write('    print "<img src=\\"../img/" . $cur->imageFile . "\\"/><br />";\n    $x = 1;\n\n}}')
    
    


o_f.write("\n?>")
#i_f.close()
o_f.close()
