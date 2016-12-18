# Task

http://ctf.sharif.edu:8087/

![alt text](https://github.com/spyoff/ctf-writeup/blob/master/sharifctf-2016/misc-150-lesula-isola/lesula-isola.png?raw=true "Lesula Isola")

# Writeup

Try to play it, and found that we play insult vs bot from Curse of the monkey island game.
[game wiki](https://en.wikipedia.org/wiki/The_Curse_of_Monkey_Island)

We ask or answer question to the bot, that we can check on walkthrough.

http://www.ladyofthecake.com/monkeys3/html/insults.html

http://www.the-spoiler.com/ADVENTURE/Lucas.Arts/monkey3.5/insults.html

However, we only got 1 question/answer on the beginning. Overtime, the question/answer list is increasing, if our answer is correct.

The task runs mainly using websocket on ctf.sharif.edu:4010

![alt text](https://github.com/spyoff/ctf-writeup/blob/master/sharifctf-2016/misc-150-lesula-isola/ws-lesula-isola.png?raw=true "Lesula Isola WS")

Flow found:
00 : we lose, we answer the question from bot
01 : we win, we ask question to bot
Question / answer list separated by #, and placement is random.

Write a python script to automate learning, until eventually we win.

https://github.com/spyoff/ctf-writeup/blob/master/sharifctf-2016/misc-150-lesula-isola/lesula-isola.py


```
=====win, now our turn=====
UPDATE: You'll find I'm dogged and relentless to my prey. : Then be a good dog.  Sit!  Stay!
Send question 0 : Flag is: SharifCTF{2f7a87d9afd14d7f6de27546e8084168}
Monkey answer: 
root@kali:~/sharifctf7#
```

The flag is Flag is: SharifCTF{2f7a87d9afd14d7f6de27546e8084168}
