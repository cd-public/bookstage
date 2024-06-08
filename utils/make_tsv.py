#!/bin/python3

import sys, os, hashlib, base64

PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/' # DONT scrape Gutenberg
MAX_FS = 10 if len(sys.argv) == 1 else int(sys.argv[1])
BK_DIR = '../books/'

open("books.tsv",'w').writelines(['TsvHttpData-1.0\n'] + ['%s%s\t%s\t%s\n' % (PREFIX, f, os.path.getsize(BK_DIR + f), base64.b64encode(hashlib.md5(open(BK_DIR + f,'rb').read()).digest()).decode("utf-8")) for f in os.listdir(BK_DIR)[:MAX_FS] if '.txt' in f])
