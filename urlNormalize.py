#!/usr/bin/env python3

import sys
from urllib.parse import urlparse

if len(sys.argv) > 1:
	if sys.argv[1] ==  "-h":
		print("> Use with URLs in stdin")
		print("> If urls start with http/https and contain :80 or :443 respectively, the port will be removed")
		print("> examples:")
		print("  [+] echo \"http://asdf.qwer.dd:80/\" | urlNormalize.py")
		print("      http://asdf.qwer.dd/")
		print("  [+] echo \"http://asdf.qwer.dd:8080/\" | urlNormalize.py")
		print("      http://asdf.qwer.dd:8080/")
		print("  [+] cat urls.txt | urlNormalize.py")
		exit(0)

for line in sys.stdin:
	inputLine = line.strip("\n")

	if inputLine.startswith("http:") and urlparse(inputLine).netloc.endswith(":80"):
		toOut = inputLine.replace(":80", "")
		sys.stdout.write(f"{toOut}\n")

	elif inputLine.startswith("https:") and urlparse(inputLine).netloc.endswith(":443"):
		toOut = inputLine.replace(":443", "")
		sys.stdout.write(f"{toOut}\n")

	else:
		sys.stdout.write(f"{inputLine}\n")
