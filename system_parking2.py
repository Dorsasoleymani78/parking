#dorsa soleymani

import datetime
import random
from typing import List
class Parking:
    def __init__(self,name,malek,geymatvurud):
     self.name=name
     self.malek=malek
     self.Listtabagat=[]
     self.saatvurud=datetime.datetime.now()
     self.saatKhuruj=datetime.datetime.now()
     self.geymatvurud=geymatvurud

    def addTabage(self,tabage):
        self.Listtabagat.append(tabage)
    
    def EditInformation(self,name,malek):
        self.name=name
        self.malek=malek
    
    def EditgeymatVurud(self,geymatvurud):
        self.geymatvurud=geymatvurud

    def showInformation(self):
     print (f"name is {self.name}\t\t malek is {self.malek}\t\t saatVurud is {self.saatvurud}\t\t geymat vurud is {self.geymatvurud} ")
#-------------------------------------------------------------------
class bakhsh:
    def __init__(self,name,zarfiyat):
        self.name=name
        self.ListJaygah=[]
        self.zarfiyat=zarfiyat
        self.ListJaygahPor=[]
        self.ListJaygahKhali=[]
    
    def __str__(self) -> str:
         return self.ListJaygahPor
    
    def addJaygah(self,Jaygah):
        self.ListJaygah.append(Jaygah)
    
    def showJaygah(self):
       list1=[i for i in self.ListJaygah]
       print(list1)

    def addJaygahpor(self,Jaygah):
         self.ListJaygahPor.append(Jaygah)
    
    def showJaygahPor(self):
        # It_listPor=iter(self.ListJaygahPor)
        # for i in range(len(self.ListJaygahPor)):
        #     print("jaygahpor is",next(It_listPor))
        list1=[ i for i in self.ListJaygahPor]
        print("jaygah por is ",list1)
        
    def  addJaygahKali(self,Jaygah):
        if Jaygah not in self.ListJaygahPor:
         self.ListJaygahKhali.append(Jaygah)
        else:
            print("khali nis babe")
        
    def KhalikardanJagah(self,Jaygah):
        self.ListJaygahPor.remove(Jaygah)
        self.ListJaygahKhali.append(Jaygah)

    def showJaygahKhali(self):
        # It_JagahKhaKhali=iter(self.ListJaygahKhali)
        # for i in range(len(self.ListJaygahKhali)):
        #     print("jaygah khali is",next(It_JagahKhaKhali))
        list1=[i for i in self.ListJaygahKhali]
        print(f"Jaygah khali is {list1}")
    
    
   

    def EditZarfiyat(self,zarfiyat):
        self.zarfiyat=zarfiyat
        return self.zarfiyat
         
    

#-------------------------------------------------------------
class tabage:
    def __init__(self,name) -> None:
         self.name=name
         self.ListBakhsh=[]

    def addBakhsh(self,bakhsh):
        self.ListBakhsh.append(bakhsh)

    def showListBakhsh(self):
        for bakhsh in self.ListBakhsh:
            print(bakhsh) 
    
    def DeleteBakhsh(self,bakhsh):
        self.ListBakhsh.remove(bakhsh)
    
    def EditTabage(self,name):
        self.name=name
        self.addBakhsh(bakhsh)
        self.DeleteBakhsh(bakhsh)
    
#-----------------------------------------------------------------   
class Jaygah:
    def __init__(self ,Code):
        
        self.List1=[]
        self.Code=Code
        self.Type=self.TypeOfJaygah(TypeOfJaygah)
        self.vaziyat= self.ShowVaziyat()
    
    def __str__(self) :

        return f"{self.Type}"

    def getListPor(self,bakhsh):
        for i in bakhsh:
            self.List1.append(i)
            self.ShowVaziyat()
 
    def ShowVaziyat(self ):
        for i in self.List1:
            if  self.Code not in self.List1:
                self.vaziyat="khali"
            else:
                self.vaziyat="por"
  
    def TypeOfJaygah(self,TypeOfJaygah):
         self.Type=TypeOfJaygah
    
    def EditTypeOfJaygah(self,newType ):
        self.Type=newType

    def showInfo(self):
        print(f"vaziyat is {self.vaziyat} \t\ttype of jaygah is {self.Type}")

#------------------------------------------------------------
class  TypeOfJaygah:
    def __init__(self,Name):
        self.Name=Name
        self.gemat=self.calcutegeymat()
    
    def __str__(self) -> str:
        return f"{self.Name}\t\t{self.gemat}"
        
    def calcutegeymat(self):
         
        if self.Name=="personality":
            self.geymat=2000
        elif self.Name=="public":
            self.geymat=5000
        else:
            print("pleaze enter valiable name")
      
    
    def EditTypeOfJaygah(self,NewName):
        self.Name=NewName
    
    def showInfo(self):
        print(f"name is {self.Name}\t\tgemat is{self.gemat}")
         
#--------------------------------------------------------------------------
class car:
    def __init__(self,pelak,TypeOfCar):
         self.pelak=pelak
         self.TypeOfCar=TypeOfCar
    
    def __str__(self) :
         return f"{self.pelak}\t\t{self.TypeOfCar}"
#----------------------------------------------------------------------------
class paziresh:
    def __init__(self ):
        self.shomareyPaziresh=self.addshomareyPaziresh()
        self.pelakMashin=self.addpelakMashin(car)
        self.CodeJaygah=self.addCodeJaygah(Jaygah)
        self.startDate=datetime.datetime.now()
        self.endDate=datetime.datetime.now()
        self.ListCodeEshterak=[]
    
    def addCodeEshterak(self,eshterak):
        self.ListCodeEshterak.append(eshterak)
    
    def showCodeEshterak(self):
        list1=[i for i in self.ListCodeEshterak]
        print(f"code eshterak is{list1}")
    
    def checkEshterak(self,codeEshterak):
        if codeEshterak in self.ListCodeEshterak:
            print("ok")
        else:
            print("no")
        
    def searchJayeKhali(self,bakhsh):
        list1=[i for i in bakhsh]
        print("jahaye khali is ",list1)

             


    def addshomareyPaziresh(self):
        return random.randint(1,10000)
    
    def addpelakMashin(self,car):
         self.pelakMashin=car
        
    def addCodeJaygah(self,Jaygah):
        self.CodeJaygah=Jaygah
    
    def calcutTimeHozur(self):
        return self.startDate-self.endDate
        
    def mablagevurudi(self,parking):
        return parking






#-------------------------------------------------------------------------------
class eshterak:
    def __init__(self,CodeEshterak):
        self.CodeEshterak=CodeEshterak
        # self.Type=Type
        self.startDate=datetime.date.today()
        self.endDate=datetime.date.today()
    
    def expireCodeEshterak(self):
        if self.endDate==2021:
            print("expire")
         
#--------------------------------------------------------------------
class TypeOfEshterak:
    def __init__(self,name) -> None:
         self.name=name
        #  self.geymat=self.getGaymat()
        
    def __str__(self) -> str:

        return f"{self.name}\t\t " 
     
    



#--------------------------------------------------------------
Parking1=Parking("saba","soleymani",1000)
Parking1.addTabage(1)
Parking1.addTabage(2)
Parking1.addTabage(3)
Parking1.showInformation()
Parking1.EditInformation("dorsa","asadi")
Parking1.EditgeymatVurud(2000)
 
Parking1.showInformation()
Jaygah1=Jaygah(12)
Jaygah2=Jaygah(6)
Jaygah3=Jaygah(3)

bakhsh1=bakhsh("A",7)
bakhsh1.addJaygah(Jaygah1.Code)
bakhsh1.addJaygah(Jaygah2.Code)
bakhsh1.showJaygah()
 
bakhsh1.addJaygahpor(Jaygah1.Code)
bakhsh1.addJaygahpor(Jaygah2.Code)
bakhsh1.showJaygahPor()
 
bakhsh1.addJaygahKali(Jaygah3.Code)
 
bakhsh1.showJaygahKhali()

 
eshterak1=eshterak(1)
eshterak2=eshterak(2)
eshterak3=eshterak(3)

paziresh1=paziresh()
paziresh1.addCodeEshterak(eshterak1.CodeEshterak)
paziresh1.addCodeEshterak(eshterak2.CodeEshterak)
paziresh1.addCodeEshterak(eshterak3.CodeEshterak)
paziresh1.showCodeEshterak()
paziresh1.checkEshterak(2)

paziresh1.searchJayeKhali(bakhsh1.ListJaygahKhali)
 

Jaygah1.getListPor(bakhsh1.ListJaygahPor)
bakhsh1.showJaygahPor()
TypeOfJaygah1=TypeOfJaygah("personality")
Jaygah1.TypeOfJaygah(TypeOfJaygah1.Name)
Jaygah1.showInfo()
Jaygah2.getListPor(bakhsh1.ListJaygahPor)
TypeOfJaygah2=TypeOfJaygah("public")
Jaygah2.TypeOfJaygah(TypeOfJaygah2.Name)
Jaygah2.showInfo()
 
 

 
