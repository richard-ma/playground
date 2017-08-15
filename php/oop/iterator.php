<?php

/* 
 * rewind() reset pointer to start of data
 * current() get current item value
 * key() get current item key
 * next() get next item
 * valid() check the key in the array or not
 */
class MyIterator implements Iterator
{
    private $var = array();

    public function __construct($array) {
        if (is_array($array)) {
            $this->var = $array;
        }
    }

    // foreach start invoking
    // only once for one foreach
    public function rewind() {
        echo "Rewinding\n";
        reset($this->var);
    }

    // current value
    public function current() {
        $var = current($this->var);
        echo "Current: ${var}\n";
        return $var;
    }

    // current key
    public function key() {
        $var = key($this->var);
        echo "Key: ${var}\n";
        return $var;
    }

    // get next one -> every loop step end invoking
    public function next() {
        $var = next($this->var);
        echo "Next: ${var}\n";
        return $var;
    }

    // valid key -> every loop step start invoking
    public function valid() {
        $key = key($this->var);
        $var = ($key !== NULL && $key !== FALSE);
        echo "Valid: ${var}\n";
        return $var;
    }
}

$values = array(1, 2, 3);
$obj = new MyIterator($values);

foreach ($obj as $key => $value) {
    print "${key} => ${value}\n";
}

// IteratorAggregate must have an Iterator
class MyCollectoin implements IteratorAggregate
{
    private $items = array();
    private $count = 0;

    public function getIterator() {
        return new MyIterator($this->items);
    }

    public function add($value) {
        $this->items[$this->count++] = $value;
    }
}

$coll = new MyCollectoin();
$coll->add('value1');
$coll->add('value1');
$coll->add('value1');

foreach($coll as $key => $value) {
    echo "key/value => ${key}/${value}\n";
}
