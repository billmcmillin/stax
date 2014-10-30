<?php

$callNum = htmlspecialchars($_GET["callNum"]);
$loc = htmlspecialchars($_GET["loc"]);
//result page that is displayed when user clicks on a link
print "<html>";
print "<head>";
print "<style>";
print "p {font: 18px/20px verdana, sans-serif;}";
print ".main {margin-left: auto;
 margin-right:auto;
width: 50%;}";print "</style>";print "<body>";
print '<div class="main">';
//begin checking for locations
