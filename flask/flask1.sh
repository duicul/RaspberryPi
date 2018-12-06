#!/bin/bash
echo $#
str=Hello.py
if test $# -ge 1
then str=$1
fi
echo  $str
set FLASK_APP=$str
python $str
