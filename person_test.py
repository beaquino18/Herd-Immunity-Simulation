import pytest
from virus import Virus
from person import Person


def test_vaccinated_person():
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None
    
def test_unvaccinated_person():
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

def test_infected_person():
    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

def test_survival_person():  
    virus = Virus("Covid", 0.7, 0.2)
    people = []
    for i in range(0, 100):
        infected_person = Person(4, False, virus)
        people.append(infected_person)
        
    did_survived = 0
    did_not_survive = 0
    
    for person in people:
        survived = person.did_survive_infection()
        if survived == True:
            did_survived += 1
        else:
            did_not_survive += 1
            
    print(f"Number of people survived: {did_survived}\nNumber of people died: {did_not_survive}")
    
    assert did_survived + did_not_survive == 100
    