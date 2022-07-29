import pandas as pd
pd.DataFrame()

class RailwayForm: 
    formType = "RailwayForm"
    def printData(self):
        print(f'Name is {self.name}')
        print(f'Train is {self.train}')

harrysApplication = RailwayForm()
harrysApplication.name = "Harry"    
harrysApplication.train = "London to Paris"
harrysApplication.printData()