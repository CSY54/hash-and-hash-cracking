from argparse import ArgumentParser
import hashlib

def md5(text):
    return hashlib.md5(text).hexdigest() 

def sha1(text):
    return hashlib.sha1(text).hexdigest()

def sha224(text):
    return hashlib.sha224(text).hexdigest()

def sha256(text):
    return hashlib.sha256(text).hexdigest()

def sha384(text):
    return hashlib.sha384(text).hexdigest()

def sha512(text):
    return hashlib.sha512(text).hexdigest()

def hash(hash_type, text):
    res = eval(f'{hash_type}("{text}".encode())')
    return f'[RESULT] {hash_type}("{text}") = {res}' 

def crack(f, hash_type, hsh):
    for line in f:
        text = line.strip()
        res = eval(f'{hash_type}("{text}".encode())')
        if res == hsh:
            return f'[FOUND] {hash_type}("{text}") = {hsh}'
        
    return '[ERROR] Could not find such hash'

def main():
    parser = ArgumentParser()
    parser.add_argument('-m', '--method', help='`h` for hash, `c` for crack')
    parser.add_argument('-T', '--type', help='hash method, must be one of md5, sha1, sha224, sha256, sha384, sha512')
    parser.add_argument('-t', '--text', help='text to hash / crack')
    parser.add_argument('-f', '--file', help='path to dictionary file')

    args = parser.parse_args()

    if args.method is None:
        print('[ERROR] Must provide a method to user')
        exit()
    elif args.method != 'h' and args.method != 'c':
        print('[ERROR] Method must be one of h, c')
        exit()

    if args.type is None:
        print('[ERROR] Must provide a hash type')
        exit()
    elif args.type not in ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']:
        print('[ERROR] Invalid hash type')
        exit()

    if args.text is None:
        print('[ERROR] Must provide text to hash / crack')
        exit()
    
    if args.method == 'c':
        if any(i.upper() not in '0123456789ABCDEF' for i in args.text):
            print('[ERROR] Text must be hex string')
            exit()

        try:
            f = open(args.file, 'r')
        except:
            print('[ERROR] Cannot open file')
            exit()

    if args.method == 'h':
        print(hash(args.type, args.text))
    else:
        print(crack(f, args.type, args.text))
        

if __name__ == '__main__':
    main()
