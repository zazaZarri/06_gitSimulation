from sensore import Sensore

class Satellite:
    def __init__ (self, name: str)
        self.name = name
        self.sensori = sensori{}
        self.letture = letture[]
    
    
    def aggiungi_sensore(self, sensore: Sensore)->None:
        if sensore.codice in self.sensori
            raise ValueError("Erorr")
        self.sensori[sensore.codice] = sensore
        
        
        
    def registra_lettura(self,codiceSensore: str, valore: float)->None:
        if codiceSensore not in self.sensori
            raise ValueError("erorr")
        sensore = self.sensori[codiceSensore]
        self.letture.append({
            "sensore" = codiceSensore
            "grandezza" = sensore.grandezza
            "unita" = sensore.unita
            "valore" = valore
            "allarme" = valore > sensore.soglia_massima
            })
        
    def lettura_in_allarme(self) ->list:
        allarmi: list= []
        
        for lettura in letture
            if lettura[allarme]
                allarmi.appen(lettura)
                
                
        return allarmi
    
    
    
    def riepilogo(self) ->None:
        
        print("Telemetria satellite:", self.name)
        
        for lettura in self.letture:
            stato = "ALLARME" if lettura["allarme"] else "OK"
            print(lettura["sensore"], lettura["valore"], lettura["unita"], stato)
            
            
            
            

        