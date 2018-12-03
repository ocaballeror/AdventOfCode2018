<?php
$file = fopen("input", "r");
$filesize = filesize("input");
$lines = explode("\n", fread($file, $filesize));
fclose($file);

echo array_sum($lines);
?>

