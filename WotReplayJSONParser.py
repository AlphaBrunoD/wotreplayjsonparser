import os
import json
import codecs


path='to %replays% folder'      #get sure folder contains only replays


def get_replays():         #parse all replays in folder. 
    n=0
    for replay in os.listdir(path):
        relpay_read(replay)
        print(str(n)+' \ '+str(len(os.listdir(path)))+'   '+replay) #show progress
        n=n+1

def relpay_read(replay):
    f = open(path+replay, 'rb')
    d = open("path to destination.txt", 'a', encoding='utf-8')
    skip= f.read(8)                               #skip 8 non-informative bytes
    byteslen= f.read(4)
    length = int.from_bytes(byteslen, 'little')   #very cool func, love it. gets decimal without extra convertations
    print(length)
    info=f.read(length).decode()                  
    infojson=json.loads(info)
    players= infojson['vehicles'].values()
    for player in players:                      #data processing example
        name=player['name']
        d.write("'"+name+"', ")
        # print(name)

    f.close()

def main():
    get_replays()

if __name__ == "__main__":
    main()