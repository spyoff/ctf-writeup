# Task

login.pwn.seccon.jp:10000


# Writeup

Try to connect via netcat :

```
root@spiderman:~# nc login.pwn.seccon.jp 10000
CONNECT 300

Welcome to SECCON server.

The server is connected via slow dial-up connection.
Please be patient, and do not brute-force.
 
login: root
seccon
Sorry, the account is unavailable.

Good bye.

root@spiderman:~#
```

Hmm.. nothing interesting here..

Todo: 
1. Try to open it on a mozilla browser
2. Dump the packet and find something interesting

## Voila

```
CONNECT 300

Welcome to SECCON server.

The server is connected via slow dial-up connection.
Please be patient, and do not brute-force.
S E C C O N { S o m e t i m e s _ w h a t _ y o u _ s e e _ i s _ N O T _ w h a t _ y o u _ g e t } 
login: 

Login timer timed out.
Thank you for your cooperation.

HINT: It is already in your hands.

Good bye.

flag:SECCON{Sometimes_what_you_see_is_NOT_what_you_get}
```

Analysis: those flag is shown since the beginning, but the telnet/nc doesnt show the hidden char.
If you go with tcpdump, you should find it.
