#!/usr/bin/env bash

# Use -e or -o errexit
set -o errexit

function rollback {
    echo "Terminated by $1"
}

trap "rollback 'Ctrl-C'" INT
trap "rollback 'kill'" TERM
trap "rollback 'script error'" EXIT

sleep 6 # wait for Ctrl-C or kill
# make an error
exit 1
