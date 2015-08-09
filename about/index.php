<?php
include '../init.php';

echo $twig->render('about.twig', array('heading' => 'About',
                                       'file'=> "about",
                                       'msg' => $msg,
                                       )
                  );