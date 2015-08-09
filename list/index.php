<?php
include '../init.php';

echo $twig->render('list.twig', array('heading' => 'Wer wen kennt',
                                      'file'=> "list",
                                      'msg' => $msg,
                                       )
                  );