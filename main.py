import json
from click import clear
import dataScraper as ds

startYear, endYear = int(input('startYear: ')), int(input('endYear: '))

for i1 in range(startYear, endYear+1):
    for j1 in range(1, ds.raceCount(i1)+1):
    
        rr = ds.raceResult(i1, j1)

        clear()

        print('processing')
        print(f'\nyear: {i1}   grand prix: {j1}\n')
        print(f'{rr["title"]}'.replace(" - Race Result", ""))

        omz = rr['drivers']
        print(f'''P1: {rr['drivers'][1]['driver']}   
P2: {rr['drivers'][2]['driver']}   
P3: {rr['drivers'][3]['driver']}''')

        with open("elo.json", "r") as f: eloData = json.load(f)
        l = []
        for i in eloData.items():
            l.append([
                i[0],
                i[1]['rating']
            ])

        if len(l)>0:
            sl = sorted(l, key=lambda x: x[1])
            print(f'\nhighestElo: {int(sl[::-1][0][1])} - {sl[::-1][0][0]}') 


        # adding new drivers
        with open("elo.json", "r") as f: eloData = json.load(f)
        for i in rr['drivers'].values():
            if i['driver'] not in eloData:
                eloData[i['driver']] = {
                    'rating': 1000,
                    'races': 0, 
                    'avgFinish': 0
                }
        
        for i in rr['drivers'].values():
            
            dr = eloData[i['driver']]
            
            totalPos = int(list(rr['drivers'].keys())[-1])
            if i['position'].isdigit(): 
                pos = int(i['position'])  
            else: 
                pos = totalPos 
            totalRaces = dr['races'] + 1
            actualPos = (totalPos - pos + 1)/totalPos

            actualAvgFinish = (dr['avgFinish']*(totalRaces-1) + actualPos)/totalRaces
            
            delta = 100*(actualPos - dr['avgFinish'])

            eloData[i['driver']] = {
                    'rating': dr['rating'] + delta,
                    'races': totalRaces, 
                    'avgFinish': actualAvgFinish
                }
        
        with open("elo.json", "w") as f: json.dump(eloData, f)
 