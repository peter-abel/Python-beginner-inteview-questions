 #Rent management
 # Dataclasses is a module that generates special methods e.g(__init__) for classes
from dataclasses import dataclass

@dataclass
class House:
    #attributes
    estate: str
    size: int
    type:str
    
    #methods or functions
    def rent(self) -> float:
        if self.size <= 500:
            return self.size* 10 
        elif self.size <=1000:
            return self.size*20
        elif self.size <=2000:
            return self.size*20         
        return self.size
@dataclass
class flats (House):
    #attributes
    rooms:int
    floors:int

#if __name__=="__main__":
oxford = flats( "lurambi",200,"flat",
1,4)
#oxford.floors= 4
#oxford.size= 200

print(oxford.rent())


