#!/bin/bash

if [ $(id -u) -ne 0 ]; then
    echo "You must be root!"
    exit 1
fi

echo 0 > /proc/sys/kernel/randomize_va_space
