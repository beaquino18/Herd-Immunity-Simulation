class Virus(object):
    """roperties and attributes of the virus used in Simulation"""
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate
        

# Test this class
if __name__ == "__main__":
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
    
    print(f"Virus name: {virus.name}\nReproduction Rate: {virus.repro_rate * 100}%\nMortality Rate: {virus.mortality_rate * 100}%\n")
    
    virus = Virus("COVID", 0.5, 0.1)
    assert virus.name == "COVID"
    assert virus.repro_rate == 0.5
    assert virus.mortality_rate == 0.1
    
    print(f"Virus name: {virus.name}\nReproduction Rate: {virus.repro_rate * 100}%\nMortality Rate: {virus.mortality_rate * 100}%\n")
    
    virus = Virus("FLU", 0.9, 0.0)
    assert virus.name == "FLU"
    assert virus.repro_rate == 0.9
    assert virus.mortality_rate == 0.0
    
    print(f"Virus name: {virus.name}\nReproduction Rate: {virus.repro_rate * 100}%\nMortality Rate: {virus.mortality_rate * 100}%\n")
    