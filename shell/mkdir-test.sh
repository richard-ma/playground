#!/usr/bin/env bash

# Usage
# mkdir-test.sh
# Or
# mkdir-test.sh hello

dir_name=$1
# dir_name length == 0 then got a default value
[ -z "$1" ] && echo "DirName Please!" && exit 1

# traditional way
mkdir "$dir_name"

# robust way
# $dir_name may be a path name
# /path/to/dir
#mkdir -p "$dir_name"

# rm dir
rmdir "$dir_name"

# dir has been deleted

# warning: traditional way
rmdir "$dir_name"
# Or
# no warning: robust way
#rm -f "$dir_name"

exit
