# We used https://pypi.python.org/pypi/websocket-client/0.7.0
from websocket import create_connection
import pprint
from random import randint


pp = pprint.PrettyPrinter(indent=4)
question = {}
tmp = []

ws = create_connection("ws://ctf.sharif.edu:4010")
prvstate = 0
prvanswer = ''
prvquestion = ''

try:    
    while True:        
        o = ws.recv()
        print "Received: "+o
        if o == "00":            
            print "===lose==="
            #if previously we ask question, save answer 
            if prvstate == 1:
                question[prvquestion] = prvanswer
                print('UPDATE: '+prvquestion+' : '+prvanswer)
                #pp.pprint(question)
            
            #read question
            o = ws.recv()
            print "Monkey ask: "+o
            ask = o[1:]
            #read available answer
            o = ws.recv()
            ans = o[1:].split("#")
            #answer
            if ask in question:
                if question[ask] in ans:
                    ws.send(str(ans.index(question[ask])))
                    print "Send: "+str(ans.index(question[ask]))+" : "+question[ask]
                    prvanswer = question[ask]
                else:
                    ws.send('0')
                    print "Send: 0" + ans[0]
                    prvanswer = ans[0]
            else:                
                ws.send('0')
                print "Send: 0" + ans[0]
                prvanswer = ans[0]
            prvstate = 0
            
            prvquestion = ask
            
        elif o == "01":
            print "=====win, now our turn====="
            #if previously we correct, save answer 
            if prvstate == 0:
                question[prvquestion] = prvanswer
                print('UPDATE: '+prvquestion+' : '+prvanswer)
                #pp.pprint(question)
            
            #read available question
            o = ws.recv()
            s = o[1:]
            qlist = s.split("#")
            for item in qlist:
                #print item                
                if item not in question:
                    question[item] = ''
            #print "Available question: "+o
            
            #ask question that doesnt have answer
            foundquestiontoask = 0
            for item in qlist:
                #print item
                #print question[item]
                if question[item] == '':
                    ws.send(str(qlist.index(item)))
                    print "Send question "+str(qlist.index(item))+" : "+item
                    prvquestion = item
                    foundquestiontoask = 1
                    break
            if foundquestiontoask == 0:
                randindex = randint(0,len(qlist)-1)
                ws.send(str(randindex))
                print "Send question "+str(randindex)+" : "+qlist[randindex]
                prvquestion = qlist[randindex]
            #read answer
            o = ws.recv()
            prvanswer = o[1:]
            prvstate = 1            
            print "Monkey answer: "+o
except:
    ws.close()
