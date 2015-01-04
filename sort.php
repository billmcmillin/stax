<?php

//an adaptation of Koha's Dewey sort routine
//GPL info goes here
		//problem call numbers
		/*
		709.04 M453  
	  704.94978 S727  
		759.06 E96
		759.1H766
		759.1N
		*/

		//759.06 E96 should display as 759_060000000000000_E96
		//$callNum = '759.06 E96';

	function sortNums($callNum){
		//make all characters uppercase
		$init = strtoupper($callNum);
		//get rid of leading whitespace
		$init = preg_replace('/^\s+/', '', $init);
		//get rid of extra whitespace at end of string
		$init = preg_replace('/\s+$/', '', $init);
	  //remove any slashes
		$init = preg_replace('/\//', '', $init);
		//remove any backslashes
		$init = stripslashes($init);
		// replace newline characters
		$init = preg_replace('/\n/','', $init);
		
		//set digit group count
		$digit_group_count = 0;
		//declare first digit group index variable
		$first_digit_group_idx;
		
		//split string into tokens by . or space
		$tokens = preg_split( '/\.|\s+/', $init);
		
		//loop through the tokens
		for($i=0;$i<sizeof($tokens);$i++){
			//if the token begins and ends with digits
			if(preg_match("/^\d+$/", $tokens[$i])){
				//increment the number of digit groups
				$digit_group_count++;
				//if it's the first one, store its index in first_digit_group_idx
				if (1 == $digit_group_count) {
                $first_digit_group_idx = $i;
            }
        //if there is a second group of digits, expand it to 15 places, adding 0s    
        if (2 == $digit_group_count) {
                $tokens[$i] = str_pad($tokens[$i], 15, "0", STR_PAD_RIGHT); 
            }
			}
		
		}
		
		if (1 == $digit_group_count) {
        $tokens[$first_digit_group_idx] .= '_000000000000000';
    }
		
    $key = implode("_", $tokens);
		return $key;
	}
		
		/*
    $init =~ s/\s+$//;
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
                $tokens[$i] = sprintf("%-15.15s", $tokens[$i]);
                $tokens[$i] =~ tr/ /0/;
            }
        }
    }
    # Pad the first digit_group if there was only one
    if (1 == $digit_group_count) {
        $tokens[$first_digit_group_idx] .= '_000000000000000'
    }
    my $key = join("_", @tokens);
    $key =~ s/[^\p{IsAlnum}_]//g;

    return $key;
*/
?>
