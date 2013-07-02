<?php

$content = file_get_contents("http://iframe.ip138.com/ic.asp");

preg_match_all("/([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})/",$content, $ip);
var_dump($ip);
