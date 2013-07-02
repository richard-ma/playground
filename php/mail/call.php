<?php
require_once "./smtp.class.php";

$mailcfg['server'] = 'smtp.qq.com'; 

$mailcfg['port'] = '25'; 

$mailcfg['auth'] = 1; 
$mailcfg['from'] = '178613284 <178613284@qq.com>'; 

$mailcfg['auth_username'] = '178613284'; 

$mailcfg['auth_password'] = 'ML19850509'; 

$stmp=new stmp($mailcfg); 
$mail=array('to'=>'richard.ma.19850509@gmail.com','subject'=>'测试标题','content'=>'邮件内容<a href="http://www.phpobject.net">PHP面向对象</a>'); 
if(!$stmp->send($mail)){ 
    echo $stmp->get_error(); 
}else{ 
    echo 'mail succ!'; 
} 
