import os
import json

path = 'A:\\Games\\World_of_Tanks_RU\\replays\\'      #get sure folder contains only replays

def get_replays():                #parse all replays in folder. 
    w_path = os.listdir(path)
    for n in range(0, len(w_path)):
        replay_read(w_path[n])
        print(f"{n} \ {len(w_path)}   {w_path[n]}")

def replay_read(replay):
    file = open(path + replay, 'rb')
    dest = open("path_to_destination.txt", 'a', encoding='utf-8')
    skip = file.read(8)                               #skip 8 non-informative bytes
    byteslen = file.read(4)
    length = int.from_bytes(byteslen, 'little')    #very cool func, love it. gets decimal without extra convertations
    print(length)
    info = file.read(length).decode()                  
    infojson = json.loads(info)
    players = infojson['vehicles'].values()        #data processing example
    for player in players:                      
        name = player['name']
        dest.write("'" + name + "', ")
    dest.close()
    file.close()

def main():
    get_replays()

if __name__ == "__main__":
    main()