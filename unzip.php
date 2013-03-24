<?php
$zip = new ZipArchive;
$res = $zip->open('file_up.zip');
if ($res === TRUE) {
  $zip->extractTo('/home/smscr4mp/public_html/demos/upload/');
  $zip->close();
  echo 'Extraction complete';
} else {
  echo 'Error!';
}

echo getcwd() . "\n";

unlink('file_up.zip');

?>