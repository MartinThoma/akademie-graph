<?php
include '../init.php';

echo $twig->render('insert.twig', array('heading' => 'Insert connection',
                                        'file'=> "insert",
                                        'msg' => $msg,
                                       )
                  );