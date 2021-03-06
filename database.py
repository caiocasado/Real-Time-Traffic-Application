# coding: utf-8

# In[ ]:

import sqlite3

class database(object):

    def createDatabase(self, name='busLocationDatabase'):

        self.databaseName = name

        self.conn = sqlite3.connect(name + '.sqlite')
        self.cur = self.conn.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Locations (Bus_ID TEXT, location_X TEXT, location_Y TEXT)''')

        return print ('You just created a database named: ' + self.databaseName + '.sqlite')

    def saveBusLocation(self, js):

        busLocation = js['vs']

        for bus in busLocation:

            busID = (bus['p'])

            locationX = (bus['px'])
            locationY = (bus['py'])

            self.cur.execute('''INSERT INTO Locations (Bus_ID,  location_X, location_Y)
            VALUES ( ?, ?, ? )''', (busID, locationX, locationY) )

            self.conn.commit()

        return print ('You just saved {0} in {0} database'.format(str(len(busLocation)), self.databaseName))
    
    def exportDataToJavaScript(self):

        self.cur.execute('SELECT * FROM Locations')

        datajs = open('busData.js','w')
        datajs.write("data = ")

        data = []
        
        for line in self.cur:

            (busID, longitude, latitude) = (line[0], float(line[1]), float(line[2]))

            bus = {'id': busID,
            'longitude': longitude,
            'latitude': latitude
            }

            data.append(bus)

        datajs.write(str(data))

        self.cur.close()
        datajs.close()

        return print ('You just exported all data in {0} database'.format(self.databaseName))
