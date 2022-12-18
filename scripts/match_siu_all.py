import csv

# this script overwrites all the chest data (youtube, etc. is nullified)

f = open('../data/chests.csv', 'w')

item = {'type':'coin','icon':'chest_coin','id':'','x':0,'y':0,'z':0,'item':1,'price':1,'comment':'','image':'','ytVideo':'','ytStart':'','ytEnd':''}
w = csv.DictWriter(f,item.keys())
w.writeheader()


import glob
chests = 0

for filename in glob.glob('data_sets/DLC2_*.csv'):
    c = csv.DictReader(open(filename))
    for o in c:
        if 'chest' in o['object_class'].lower() or 'chest' in o['object_name'].lower():
            chests += 1
            d = item.copy()
            d['x'] = o['location_x']
            d['y'] = o['location_y']
            d['z'] = o['location_z']
            d['item'] = '%s (%s pcs)' % (o['spawns'], o['spawncount'])
            d['id'] = o['object_name']
            d['comment'] = o['object_name']
            w.writerow(d)


print('chests found', chests)
