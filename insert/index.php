<?php
include '../init.php';

function get_people_data_by_id($filename="../people.csv") {
    $csvFile = file($filename);
    $data = [];
    $people_index = 0;
    $adjacency = get_adjacency();

    foreach ($csvFile as $line) {
        $parsed = str_getcsv($line);
        $courseNr = $parsed[2];
        if(!array_key_exists($people_index, $data)) {
            $data[$people_index] = array();
        }
        $knows_nr = 0;
        foreach ($adjacency[$people_index] as $key => $value) {
            if ($value == 1) {
                $knows_nr += 1;
            }
        }
        $data[$people_index][] = array("name" => $parsed[0],
                                       "study" => trim($parsed[1]),
                                       "course_nr" => $courseNr,
                                       "id" => $people_index,
                                       "knows" => $knows_nr);
        $people_index += 1;
    }

    ksort($data);
    return $data;
}


function get_people_data_by_course($filename="../people.csv") {
    $csvFile = file($filename);
    $data = [];
    $people_index = 0;

    $people_id = get_people_data_by_id();

    foreach ($csvFile as $line) {
        $parsed = str_getcsv($line);
        $courseNr = $parsed[2];
        if(!array_key_exists($courseNr, $data)) {
            $data[$courseNr] = array();
        }
        $data[$courseNr][] = array("name" => $parsed[0],
                                   "study" => trim($parsed[1]),
                                   "id" => $people_index,
                                   "knows" => $people_id[$people_index][0]['knows']);
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
$course_names = array("1" => "Kausalität, Exoplaneten und Black Jack: Wie man aus Daten lernt",
                      "3" => "Britische Ideengeschichte und deutsche Begriffsgeschichte im Vergleich und in der Anwendung",
                      "4" => "Bin ich zu komplex? Systemtheoretische Ansätze in Forschung und Praxis der Psychologie",
                      "5" => "Personalized Medicine, Big Data, and the Future of Health Care",
                      "6" => "Regulierung und Überwachung des Internets – Ende der Kommunikationsfreiheiten?",
                      "7" => "TTIP – Transatlantic Trade and Investment Partnership");

echo $twig->render('insert.twig', array('heading' => $heading,
                                        'file'=> "insert",
                                        'msg' => $msg,
                                        'data' => $data,
                                        'adjacency' => $adjacency,
                                        'me' => $me,
                                        'course_names' => '$course_names
                                       )
                  );