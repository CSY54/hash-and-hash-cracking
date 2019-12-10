#!/bin/bash

test="rockyou"

hash() {
  py=`python3 hash.py -m h -T $1 -t $2 | awk '{ print $4 }'`
  op=`printf $2 | openssl $1`
  echo "- $1 hash"
  echo "hash.py: $py"
  echo "openssl: $op"
  echo ""
}

crack() {
  hsh=`printf $2 | openssl $1`
  res=`python3 hash.py -m c -T $1 -t $hsh -f ~/CTF/Tools/rockyou.txt | awk -F'"' '{ print $2 }'`
  echo "- $1 crack"
  echo $res
  echo ""
}

hash md5 $test
hash sha1 $test
hash sha224 $test
hash sha256 $test
hash sha384 $test
hash sha512 $test

crack md5 $test
crack sha1 $test
crack sha224 $test
crack sha256 $test
crack sha384 $test
crack sha512 $test



