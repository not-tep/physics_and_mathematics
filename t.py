class t():
    def from_Celsius_to_Fahrenheit(c: float) -> float:
        return c * 9 / 5 + 32
    def from_Fahrenheit_to_Celsius(f: float) -> float:
        return (f - 32) * 5 / 9
    
if __name__ == '__main__':
    print(t.from_Celsius_to_Fahrenheit(100))