

class PatensRecord : 
    
    def __ini__(self, ) :
        # self.pationsPasteRecords = {'mohammed': 12}
        pass
        
    def gettingPationsPastRecords(self, **pationsPasteRecords) :
        
        self.pationsPasteRecord = pationsPasteRecords # getting pation's records
    
    def checkPastionRecord(self) :
         
         
        self.pastionName = input('pation\'s name ? ')    # pation's name.
        while self.pastionName not in self.pationsPasteRecord.keys() : 
            print('\n*************************************') 
            print('add the pastion to database recored')
            print('*************************************\n')
            self.addPationToDatabase()
        else :
            print('yes')
            return self.pationsPasteRecord
    
    def addPationToDatabase(self) :
            
            try :
                
                age = int(input('pastion\'s age ? ').strip())
                country = input('pation\s country ? ').strip()
                height = float(input('pation\'s heights ? ').strip()) 
                weight = float(input('pation\'s weights ? ').strip())
                 
                self.pationsPasteRecord.update({self.pastionName : {'name' : self.pastionName, 'age': age, 'country': country, 'height' : height, 'weight': weight}})
                return self.pationsPasteRecord
            except :
                return 'something went wrong.'
pationsPasteRecords = {}
obj = PatensRecord()
print(obj.gettingPationsPastRecords(**pationsPasteRecords))
print(obj.checkPastionRecord())


        
        