import csv

# this script overwrites all the chest data (youtube, etc. is nullified)

f = open('../data/chests.csv', 'w')

item = {'type':'coin','icon':'chest_coin','x':0,'y':0,'z':0,'item':1,'price':1,'comment':'','image':'','ytVideo':'','ytStart':'','ytEnd':'', 'id':''}
w = csv.DictWriter(f,item.keys())
w.writeheader()


import glob
chests = 0

for filename in glob.glob('data_sets/DLC2_*.csv'):
    c = csv.DictReader(open(filename))
    area = filename.split('\\').pop().split('.')[0]
    for o in c:
        #if 'chest' in o['object_class'].lower(): # only 146 Chest_C, let's use name
        if 'chest' in o['object_name'].lower():
            chests += 1
            d = item.copy()

            id = area +':'+o['object_name']

            x,y,z = o['location_x'],o['location_y'],o['location_z']

            d['x'] = x
            d['y'] = y
            d['z'] = z

            d['item'] = '%s (%s pcs)' % (o['spawns'], o['spawncount'])
            d['id'] = id
            d['comment'] = '%s (%s,%s,%s)' % (id, x,y,z)
            w.writerow(d)


print('chests found', chests)
