class Sensore:
    def __init__ (self, codice: str, grandezza: str, unita: str, soglia_massima: float)->None:
        
        self.codice = codice
        self.grandezza = grandezza
        self.unita = unita
        self.soglia_massima = soglia_massima
        
    
    @property
    def codice(self) -> str:
        return._codice
    
    