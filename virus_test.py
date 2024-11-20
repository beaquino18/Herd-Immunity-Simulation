import pytest
from virus import Virus

def test_virus():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
    
def test_virus_covid():
    virus = Virus("COVID", 0.5, 0.1)
    assert virus.name == "COVID"
    assert virus.repro_rate == 0.5
    assert virus.mortality_rate == 0.1

def test_virus_flu():
    virus = Virus("FLU", 0.9, 0.0)
    assert virus.name == "FLU"
    assert virus.repro_rate == 0.9
    assert virus.mortality_rate == 0.0
