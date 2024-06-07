#!/bin/python3

import sys, os, hashlib, base64

PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/' # DONT scrap Gutenberg
MAX_FS = 10 if len(sys.argv) == 1 else int(sys.argv[1])

tsv = open("books.tsv",'w')

os.chdir("../books")
tsv.writelines(['TsvHttpData-1.0\n'] + ['%s%s\t%s\t%s\n' % (PREFIX, f, os.path.getsize(f), base64.b64encode(hashlib.md5(open(f,'rb').read()).digest()).decode("utf-8")) for f in os.listdir()[:MAX_FS] if '.txt' in f])
