# Hash and Hash Cracking

A hash and hash cracking task from Fedora Project @ GCI 2019

## Screenshot

![[asciicast](https://asciinema.org/a/EOIOf3qPZeOFieHZSOtD8mivt.png)](https://asciinema.org/a/EOIOf3qPZeOFieHZSOtD8mivt)

## Usage

```shell
usage: hash.py [-h] [-m METHOD] [-T TYPE] [-t TEXT] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
                        `h` for hash, `c` for crack
  -T TYPE, --type TYPE  hash method, must be one of md5, sha1, sha224, sha256,
                        sha384, sha512
  -t TEXT, --text TEXT  text to hash / crack
  -f FILE, --file FILE  path to dictionary file
```
