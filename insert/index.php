<?php
include '../init.php';

if(isset($_POST['me'])) {
    $me = intval($_POST['me']);
    $msg[] = array("class" => "alert-success",
                   "text" => "Successfully submitted. Thank you");

    echo "<br><br><br><br><br><br><br>";
    var_dump($_POST['knows']);

    // Store data in [ME_id].csv
    $myfile = fopen("../data/$me.txt", "w") or die("Unable to open file!");
    foreach ($_POST['knows'] as $key => $other_id) {
        fwrite($myfile, "$other_id,1\n");
    }
    fclose($myfile);
}

$csvFile = file("../people.csv");
$data = [];
$people_index = 0;
foreach ($csvFile as $line) {
    $parsed = str_getcsv($line);
    $courseNr = $parsed[2];
    if(!array_key_exists($courseNr, $data)) {
        $data[$courseNr] = array();
    }
    $data[$courseNr][] = array("name" => $parsed[0],
                               "study" => trim($parsed[1]),
                               "id" => $people_index);
    $people_index += 1;
}

ksort($data);

echo $twig->render('insert.twig', array('heading' => 'Insert connection',
                                        'file'=> "insert",
                                        'msg' => $msg,
                                        'data' => $data,
                                       )
                  );