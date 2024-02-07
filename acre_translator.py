class Translator():
    @staticmethod
    def from_km_to_mi(km: float) -> float:
        return km * 0.621371
    
    @staticmethod   
    def from_mi_to_km(mi: float) -> float:
        return mi * 1.60934
    
    @staticmethod
    def from_liters_to_gallons(li: float) -> float:
        return li * 0.264172
    
    @staticmethod
    def from_gallons_to_liters(ga: float) -> float:
        return ga * 3.78541