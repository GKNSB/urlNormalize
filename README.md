## urlNormalize

Receives URLs as stdin. If the urls start with http/https and contain :80 or :443 respectively, the port will be cleaned.

Examples:
```
$ cat test.txt
http://qqq.aaa.zz:80/
http://qqq.aaa.zz/
http://qqq.aaa.zz:443/
https://qqq.aaa.zz:80/
https://qqq.aaa.zz/
https://qqq.aaa.zz:443/

$ cat test.txt | urlNormalize.py | sort -u
http://qqq.aaa.zz/
http://qqq.aaa.zz:443/
https://qqq.aaa.zz/
https://qqq.aaa.zz:80/
```

Help:
```
$ urlNormalize.py -h
> Use with URLs in stdin
> If urls start with http/https and contain :80 or :443 respectively, the port will be removed
> examples:
  [+] echo "http://asdf.qwer.dd:80/" | urlNormalize.py
      http://asdf.qwer.dd/
  [+] echo "http://asdf.qwer.dd:8080/" | urlNormalize.py
      http://asdf.qwer.dd:8080/
  [+] cat urls.txt | urlNormalize.py
```