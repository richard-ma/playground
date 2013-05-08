<?php 

class Renren
{
    var $_cookiefile;
    var $_email;
    var $_password;
    
    function __construct($email, $password)
    {
        $this->_cookiefile = 'renren.cookie';
        $this->_email = $email;
        $this->_password = $password;
    }

    function login()
    {
        $login_url = 'http://passport.renren.com/PLogin.do';

        $post_fields['email'] = $this->_email;
        $post_fields['password'] = $this->_password;
        $post_fields['origURL'] = 'http://www.renren.com/home';
        $post_fields['domain'] = 'renren.com';

        $ch = curl_init($login_url);
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5');
        curl_setopt($ch, CURLOPT_HEADER, 1);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_MAXREDIRS, 1);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt($ch, CURLOPT_AUTOREFERER, 1);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $post_fields);
        curl_setopt($ch, CURLOPT_COOKIEJAR, $this->_cookiefile);
        $contents = curl_exec($ch);
        curl_close($ch);

        var_dump($contents);
    }

    function getHomePage()
    {
        $send_url='http://www.renren.com/home';
        $ch = curl_init($send_url);
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $this->_cookiefile);
        $contents = curl_exec($ch);
        curl_close($ch);

        //print_r($contents);
    }

    function setStatus($status)
    {
        $post_fields['content'] = $status;
        $post_fields['hostid'] = '222785680';
        $post_fields['channel'] = 'renren';

        $send_url='http://shell.renren.com/222785680/status';
        $ch = curl_init($send_url);
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5');
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt($ch, CURLOPT_REFERER,'http://shell.renren.com/ajaxproxy.htm');
        curl_setopt($ch, CURLOPT_POSTFIELDS, $post_fields);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $this->_cookiefile);
        $contents = curl_exec($ch);
        curl_close($ch);

        //$contents = json_decode($contents,TRUE);
        //print_r($contents);
    }
}

$renrenapi = new Renren('', '');
$renrenapi->login();
$renrenapi->getHomePage();
$renrenapi->setStatus('这是个测试');
