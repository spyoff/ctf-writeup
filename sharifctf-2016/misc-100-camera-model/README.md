# Task

Find the camera model.
Flag = SharifCTF{md5(Camera_Model)}

[archived file] (https://github.com/spyoff/ctf-writeup/raw/master/sharifctf-2016/misc-100-camera-model/Image_Viewer.tar.xz)

# Writeup

Extract the file, it is an executable.

```
root@kali:~/sharifctf7# file Image_Viewer 
Image_Viewer: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=c3aaafe49fbcc6a7a2adbcdf4f3c2dd125a3dd32, not stripped

root@kali:~/sharifctf7# binwalk Image_Viewer 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             ELF 64-bit LSB executable, AMD x86-64, version 1 (SYSV)
5432          0x1538          Zlib compressed data, best compression, uncompressed size >= 65536
142856        0x22E08         LZMA compressed data, properties: 0x89, dictionary size: 16777216 bytes, uncompressed size: 100663296 bytes
142984        0x22E88         LZMA compressed data, properties: 0x9A, dictionary size: 16777216 bytes, uncompressed size: 100663296 bytes
```

![alt text](https://github.com/spyoff/ctf-writeup/blob/master/sharifctf-2016/misc-100-camera-model/run-image-viewer.png?raw=true "Run image viewer")

So, basically the executables load the images file from itself. Binwalk shows some data, but unsure what it is.
Try to search some image strings (due to camera model is stored in exif information), return nothings. But looks like our images is on jpeg format.

```
root@kali:~/sharifctf7# strings Image_Viewer | egrep -i "jp|PN"
/org/CTF/pic1.jpg
pic1.jpg
IIKJp
-aJpH
 JPXpM2
%s*jp
```

It might possible to reverse and extract the jpeg images, but i'm too lazy for that. Googling for dumping memory of a process: 

http://serverfault.com/questions/173999/dump-a-linux-processs-memory-to-file

```
root@kali:~/sharifctf7# ps -aef | grep Image
root      3377     1  0 14:43 ?        00:00:00 /root/sharifctf7/Image_Viewer
root      3498  2862  0 14:58 pts/2    00:00:00 grep Image

root@kali:~/sharifctf7# gcore 3377
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
0x00007fb1234ff4f0 in __poll_nocancel () at ../sysdeps/unix/syscall-template.S:81
81	../sysdeps/unix/syscall-template.S: No such file or directory.
warning: Memory read failed for corefile section, 8192 bytes at 0x7fffbb3d5000.
Saved corefile core.3377

```

I open it with hexeditor and try to look some jpeg header/information by searching JFIF text.

```
File: core.3377                   ASCII Offset: 0x000BCA4E / 0x005524D7 (%14)  
000BCA40  00 00 00 00  00 00 00 00   FF D8 FF E0  00 10 4A 46   ..............JF
000BCA50  49 46 00 01  01 01 00 48   00 48 00 00  FF E1 26 60   IF.....H.H....&`
000BCA60  45 78 69 66  00 00 4D 4D   00 2A 00 00  00 08 00 08   Exif..MM.*......
000BCA70  01 10 00 02  00 00 00 09   00 00 00 6E  01 12 00 03   ...........n....
000BCA80  00 00 00 01  00 01 00 00   01 1A 00 05  00 00 00 01   ................
000BCA90  00 00 00 78  01 1B 00 05   00 00 00 01  00 00 00 80   ...x............
000BCAA0  01 28 00 03  00 00 00 01   00 02 00 00  01 31 00 02   .(...........1..
000BCAB0  00 00 00 0C  00 00 00 88   01 32 00 02  00 00 00 14   .........2......
000BCAC0  00 00 00 94  87 69 00 04   00 00 00 01  00 00 00 A8   .....i..........
000BCAD0  00 00 00 EA  44 53 4C 52   34 37 38 31  00 00 00 00   ....DSLR4781....
000BCAE0  00 48 00 00  00 01 00 00   00 48 00 00  00 01 47 49   .H.......H....GI
000BCAF0  4D 50 20 32  2E 38 2E 31   36 00 32 30  31 36 3A 31   MP 2.8.16.2016:1
000BCB00  32 3A 30 32  20 31 31 3A   33 38 3A 30  34 00 00 05   2:02 11:38:04...
000BCB10  90 00 00 07  00 00 00 04   30 32 32 31  A0 00 00 07   ........0221....
000BCB20  00 00 00 04  30 31 30 30   A0 01 00 03  00 00 00 01   ....0100........
000BCB30  FF FF 00 00  A0 02 00 04   00 00 00 01  00 00 01 63   ...............c
000BCB40  A0 03 00 04  00 00 00 01   00 00 01 7E  00 00 00 00   ...........~....
000BCB50  00 06 01 03  00 03 00 00   00 01 00 06  00 00 01 1A   ................
000BCB60  00 05 00 00  00 01 00 00   01 38 01 1B  00 05 00 00   .........8......
000BCB70  00 01 00 00  01 40 01 28   00 03 00 00  00 01 00 02   .....@.(........
^G Help   ^C Exit (No Save)   ^T goTo Offset   ^X Exit and Save   ^W Search
```

DSLR4781 looks like a name for a camera. Try md5 it and submit.
The flag is SharifCTF{md5(DSLR4781)} = SharifCTF{ccb7ed56eea6576263abeca4cdb03f62}
