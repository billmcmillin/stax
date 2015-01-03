#!/usr/bin/python
import re
'''
algorithm adapted from Koha's ClassSortRoutine
Dewey.pm https://github.com/colinsc/koha/blob/master/C4/ClassSortRoutine/Dewey.pm
distributed under GPL 3.0, a copy of which is in this project's root directory
'''

def sortable(inCall):

    #remove spaces
    outCall = re.sub(" ", "", inCall)
    #remove slashes
    outCall = re.sub("/", "", outCall)
    #remove backslashes
    outCall = re.sub("\\\\", "", outCall)
    #strtoupper
    #[A-Za-z]+

    p = re.compile([a-z])
    print(outCall)
    return

callNum = '308.L  \ 49 08// \\41 v.2     '

sortable(callNum)

'''
$init =~ s/^\s+//;
$init =~ s/\s+$//;
$init =~ s/\// /g;
$init =~ s!/!!g;
$init =~ s/^([\p{IsAlpha}]+)/$1 /;
my @tokens = split /\.|\s+/, $init;
my $digit_group_count = 0;
my $first_digit_group_idx;
for (my $i = 0; $i <= $#tokens; $i++) {
if ($tokens[$i] =~ /^\d+$/) {
$digit_group_count++;
if (1 == $digit_group_count) {
$first_digit_group_idx = $i;
}
if (2 == $digit_group_count) {
if ($i - $first_digit_group_idx == 1) {
$tokens[$i] = sprintf("%-15.15s", $tokens[$i]);
$tokens[$i] =~ tr/ /0/;
} else {
$tokens[$first_digit_group_idx] .= '_000000000000000'
}
}
'''
