<?php

// define a class Foo
class Foo
{
    // variable
    public      $public_var = 'public_var'; // $obj->public_var works
    protected   $protected_var = 'protected_var'; // $obj->protected_var Fatal Error
    private     $private_var = 'private_var'; // $obj->private_var Undefined

    // constant
    const CONSTANT = 'Foo constant_var';

    // static
    public static $static_var = 'static_var';

    // construct method
    function __construct() {
        print get_called_class() . " construct method in Foo\n\n";
    }

    // method
    public function display() {
        $ret = '';
        
        $ret .= $this->public_var . " in public function\n"; // pulibc var
        $ret .= $this->protected_var . " in public function\n"; // protected var
        $ret .= $this->private_var . " in public function\n"; // private var

        $ret .= self::CONSTANT . " in public function\n"; // constant var 

        return $ret;
    }

    protected function protected_method() { // $obj->protected_method Fatal Error
    }

    private function private_method() { // $obj->private_method Fatal Error
    }

    public function static_method() {
        return self::$static_var;
    }
}

class Bar extends Foo
{
    // subclass constant
    const CONSTANT = 'bar constant';

    // construct method call parent construct method
    function __construct() {
        parent::__construct();
        print get_called_class() . " construct method in Bar\n\n";
        print self::CONSTANT . " constant in Bar\n\n";
        print parent::CONSTANT . " constant in Bar\n\n";
    }
}

/******************************************************************************/

// instant a Foo object
$foo = new Foo;

// public var
echo $foo->public_var;
echo "\n\n";

// constant var
echo $foo::CONSTANT;
echo "\n\n";

// call object method
echo $foo->display();
echo "\n\n";

// static variable & function
echo $foo->static_method();
echo "\n\n";

/******************************************************************************/
$bar = new Bar;

/******************************************************************************/

// another solution
echo (new Foo)->display();
echo "\n";

// use string as classname
$className = 'Foo';
echo (new $className)->display();
echo "\n";
