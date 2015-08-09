<?php
include '../init.php';

function get_people_data_by_id($filename="../people.csv") {
    $csvFile = file($filename);
    $data = [];
    $people_index = 0;
    foreach ($csvFile as $line) {
        $parsed = str_getcsv($line);
        $courseNr = $parsed[2];
        if(!array_key_exists($people_index, $data)) {
            $data[$people_index] = array();
        }
        $data[$people_index][] = array("name" => $parsed[0],
                                       "study" => trim($parsed[1]),
                                       "course_nr" => $courseNr,
                                       "id" => $people_index);
        $people_index += 1;
    }

    ksort($data);
    return $data;
}


function get_people_data_by_course($filename="../people.csv") {
    $csvFile = file($filename);
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
    return $data;
}

function endsWith($haystack, $needle) {
    // search forward starting from end minus needle length characters
    return $needle === "" || (($temp = strlen($haystack) - strlen($needle)) >= 0 && strpos($haystack, $needle, $temp) !== FALSE);
}

function get_adjacency() {
    $adjacency = array();
    for ($i=0; $i < 100; $i++) {
        $adjacency[$i][$j] = 0;
    }

    foreach (scandir('../data/') as $filename) {
        if (endsWith($filename, '.csv')) {
            $my_id = explode('.', $filename)[0];
            $csvFile = file("../data/$filename");
            foreach ($csvFile as $line) {
                $parsed = str_getcsv($line);
                $other_id = $parsed[0];
                $relationship = $parsed[1];
                $adjacency[$my_id][$other_id] = $relationship;
            }
        }
    }

    return $adjacency;
}

if (isset($_GET['me'])) {
    $me_id = intval($_GET['me']);
    $data = get_people_data_by_id();
    $me = $data[$me_id][0];
    $heading = $me['name']." (".$me['study'].") kennt...";
} else {
    $me = false;
    $heading = "Wer bist du?";
}

if(isset($_POST['me'])) {
    $people = get_people_data_by_id();
    $me_id = intval($_POST['me']);
    $msg[] = array("class" => "alert-success",
                   "text" => "Successfully submitted. Thank you");

    // Store data in [ME_id].csv
    $myfile = fopen("../data/$me_id.csv", "w") or die("Unable to open file!");
    foreach ($people as $other_id => $person) {
        if (array_key_exists($other_id, $_POST['knows'])) {
            fwrite($myfile, "$other_id,1\n");
        } else {
            fwrite($myfile, "$other_id,0\n");
        }
    }
    fclose($myfile);
}

$data = get_people_data_by_course();
$adjacency = get_adjacency();

echo $twig->render('insert.twig', array('heading' => $heading,
                                        'file'=> "insert",
                                        'msg' => $msg,
                                        'data' => $data,
                                        'adjacency' => $adjacency,
                                        'me' => $me
                                       )
                  );