# is-broken-link-github

- Takes file with list of urls input and check the status code 404 and prints if broken or ok.
- Mainly for Github Links.
- Handles all rate limiting of Github


## Setup

```
pip install -r requirements.txt
```

## Usage

```
python process.py {FILE_PATH} {GITHUB_TOKEN (optional)}
```

## Example

```
python process.py github-links.txt
```

## Local Bash Script

```
# $1: File path

cat $1 | awk -F[/] '{print $1"//"$3"/"$4}' | sort | uniq > process.txt

python3 process.py process.txt {GITHUB_TOKEN}
```
