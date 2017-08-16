<?php

// serialize && unserialize
class MyClass
{
    private $username = 'user';
    private $password = 'passwd';

    // serialize invoking
    public function __sleep() {
        echo "Sleeping\n";
        return array('username', 'password');
    }

    // unserialize invoking
    public function __wakeup() {
        echo "Waking up\n";
    }

    public function show() {
        echo "show: ".$this->username."/".$this->password."\n";
    }

    // echo or print invoking
    public function __toString() {
        echo "toString invoking\n";
        return $this->username.'>>>'.$this->password;
    }

    // obj call as a function
    // $obj('test');
    // is_callable($obj) => true
    public function __invoke($x) {
        echo "invoking invoking\n";
        var_dump($x);
    }

    // var_export invoking
    // $an_array is $var => value of $obj
    public static function __set_state($an_array) {
        echo "set_state invoking\n";
        var_dump($an_array);
    }

    // var_dump invoking
    public function __debuginfo() {
        return [
            'username' => $this->username . ' in debuginfo()'
        ];
    }
}

// TEST __sleep() __wakeup()
$myobj = new MyClass;
$myobj->show();
$storage = serialize($myobj); // serialize -> __sleep()
echo $storage."\n";
$readItem = unserialize($storage); // unserialize -> wakeup()
$readItem->show();
echo "\n";

// TEST __toString()
echo $myobj."\n";

// TEST __invoke()
$myobj('test');
var_dump(is_callable($myobj));
echo "\n";

// TEST __set_state()
var_export($myobj);
echo "\n";

// TEST __debuginfo()
var_dump($myobj);
echo "\n";
