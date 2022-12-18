import csv

c = csv.DictReader(open('../data/DLC2_Complete.csv'))
f = open('../data/chests.csv', 'w')
item = {'type':'coin','icon':'chest_coin','id':'','x':0,'y':0,'z':0,'item':1,'price':1,'comment':'','image':'','ytVideo':'','ytStart':'','ytEnd':''}
w = csv.DictWriter(f,item.keys())
w.writeheader()

for o in c:
    if o['object_class'].endswith('Chest_C'):
        d = item.copy()
        d['x'] = o['location_x']
        d['y'] = o['location_y']
        d['z'] = o['location_z']
        d['price'] = o['spawncount']
        d['id'] = o['object_name']
        d['comment'] = o['object_name']
        w.writerow(d)
