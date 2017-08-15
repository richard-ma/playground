<?php

class PropertyHook
{
    // property hook
    // $obj->a = 1
    public function __set($name, $value) {
        echo "${value} -> ${name}\n";
    }

    // echo $obj->a
    public function __get($name) {
        echo "Getting ${name}\n";
    }

    // isset() empty()
    public function __isset($name) {
        echo "Checking ${name}\n";
    }

    // unset()
    public function __unset($name) {
        echo "Unsetting ${name}\n";
    }

    // method hook
    // $obj->method($args)
    public function __call($name, $arguments) {
        echo "Calling ${name}\n";
    }

    // ClassName::method($args)
    public function __callStatic($name, $arguments) {
        echo "Calling static ${name}\n";
    }
}

$ph = new PropertyHook;
$ph->var = 1;
echo $ph->var;
isset($ph->var);
empty($ph->var);
unset($ph->var);

$ph->method('arg');
PropertyHook::method('arg');
