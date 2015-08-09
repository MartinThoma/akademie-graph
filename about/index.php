<?php
include '../init.php';

echo "bla";

echo $twig->render('about.twig', array('heading' => 'About',
                                       'file'=> "about",
                                       'msg' => $msg,
                                       )
                  );