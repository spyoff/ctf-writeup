# Task

What is this file?

[archived file here] (https://github.com/spyoff/ctf-writeup/blob/master/sharifctf-2016/forensic-150-pretty-raw/pretty_raw?raw=true)

# Writeup

Checking the file, it shows nothing (data only). Checking with binwalk, looks like we got some png image there.
But exiftool doesnt sees anything, so it must be broken png, or there is other data in it.

```
root@kali:~/sharifctf7# file pretty_raw
pretty_raw: data
root@kali:~/sharifctf7# binwalk pretty_raw

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
116254        0x1C61E         PNG image, 1434 x 1060, 8-bit colormap, non-interlaced

root@kali:~/sharifctf7#
root@kali:~/sharifctf7# exiftool pretty_raw
ExifTool Version Number         : 9.74
File Name                       : pretty_raw
Directory                       : .
File Size                       : 166 kB
File Modification Date/Time     : 2016:12:17 03:13:57-05:00
File Access Date/Time           : 2016:12:18 13:48:33-05:00
File Inode Change Date/Time     : 2016:12:17 03:13:57-05:00
File Permissions                : rw-r--r--
Error                           : Unknown file type

```

Extract the png files with binwalk, might be something there

```
root@kali:~/sharifctf7# binwalk --dd='.*' pretty_raw

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
116254        0x1C61E         PNG image, 1434 x 1060, 8-bit colormap, non-interlaced
root@kali:~/sharifctf7# cd _pretty_raw.extracted/
root@kali:~/sharifctf7/_pretty_raw.extracted# ls
1C61E
```

Show it on a file editor. It shows nothing but information of another file, probable the flag. It shows 1570 x 74 in the dimension, which is interesting. 

![alt text](https://github.com/spyoff/ctf-writeup/raw/master/sharifctf-2016/forensic-150-pretty-raw/png-extract.png "Look at the file dimension")

1570 x 74 x 8 bit = 116,180 bytes, Size of extracted png files is 53,833 bytes and size of pretty_raw files is 170,087 bytes, which left 116,254 on something. Cut the data in front of PNG header in a hex editor, and save it as other files. I use HxD for windows to simplify but you can use other tools such as xxd though.

![alt text](https://github.com/spyoff/ctf-writeup/raw/master/sharifctf-2016/forensic-150-pretty-raw/hexeditor-cut-file.png "Cutting the file through hex editor")

After that, we need to plot it into bitmap or png files. Google helps : 

http://superuser.com/questions/294270/how-to-view-raw-binary-data-as-an-image-with-given-width-and-height

```
root@kali:~/sharifctf7# convert -depth 8 -size 1571x74+0 gray:pretty_raw_cutted prett_raw_out.png
```

Voila, The Flag is :

![alt text](https://github.com/spyoff/ctf-writeup/raw/master/sharifctf-2016/forensic-150-pretty-raw/flag.png "Flag")
