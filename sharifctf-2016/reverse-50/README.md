# Reverse 50

Open and read the flag file!

[archived file here] (https://github.com/spyoff/ctf-writeup/raw/master/sharifctf-2016/reverse-50/getit)

# Writeup

There is a flag string on the binary file. Try to run it and nothing happened.

```
root@kali:~/sharifctf7# file getit
getit: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=e389cd7a4b9272ba80f85d7eb604176f6106c61e, not stripped

root@kali:~/sharifctf7# strings getit | grep -i shar
SharifCTF{????????????????????????????????}

root@kali:~/sharifctf7# ./getit 
root@kali:~/sharifctf7#
```

I use edb-debugger as built-in tools from kali linux. Track step-by-step the program with F8 until its repeat something.
Find the string "Sharif" in the memory, and you will see that strings ? mark is being replaced with char. Continue until all character found.

![alt text](https://github.com/spyoff/ctf-writeup/raw/master/sharifctf-2016/reverse-50/string-search.png "Search text")

![alt text](https://github.com/spyoff/ctf-writeup/raw/master/sharifctf-2016/reverse-50/string-dump.png "Run until all text found")


Flag is SharifCTF{b70c59275fcfa8aebf2d5911223c6589}
