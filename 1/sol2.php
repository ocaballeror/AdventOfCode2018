<?php
$file = fopen("input", "r");
$filesize = filesize("input");
$lines = explode("\n", fread($file, $filesize));
fclose($file);

$acc = 0;
$seen = array();
$seen[$acc] = true;
while(true) {
	foreach($lines as $num) {
		if(empty($num))
			continue;
		$acc += $num;
		if(array_key_exists($acc, $seen)){
			die("$acc is repeated\n");
		}
		$seen[$acc] = true;
	}
}
?>

