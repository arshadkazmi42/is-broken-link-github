# $1: File path

cat $1 | grep github.com | awk -F[/] '{print $1"//"$3"/"$4}' | sort | uniq > process.txt

python3 -u process.py process.txt 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

cat $1 | grep bitbucket.org | awk -F[/] '{print $1"//"$3"/"$4}' | sort | uniq > process.txt

python3 -u process.py process.txt

