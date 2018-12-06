str = Hello.py
if $# -ge 1
str = $1
echo $str
set FLASK_APP=$str

python $str