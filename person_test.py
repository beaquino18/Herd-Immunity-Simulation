import random
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


def test_person_valid_attributes():
    person = Person(10, False, None)
    assert person._id == 10
    assert person.is_vaccinated is False
    assert person.infection is None
    assert person.is_alive is True

def test_person_always_dies_with_100_mortality():
    virus = Virus("Zombie Virus", 0.8, 1.0)
    person = Person(1, False, virus)
    
    assert person.did_survive_infection() is False
    assert person.is_alive is False
    assert person.is_vaccinated is False
    assert person.infection is virus

def test_vaccinated_person_infected_twice():
    virus = Virus("Mild", 0.8, 0.2)
    person = Person(3, False, virus)
    
    #Person survives the infection and becomes vaccinated
    assert person.did_survive_infection() is True
    assert person.is_vaccinated is True
    assert person.infection is None
    
    #Try to infect the person again
    new_virus = Virus("Deadly", 0.8, 0.8)
    person.infection = new_virus
    assert person.is_vaccinated is True
    assert person.infection is new_virus
    assert person.is_alive is True
    
#Stretch challenge - test for infected and uninfected group
def test_infected_uninfected_group():
    virus = Virus("Wild", 0.7, 0.5)
    
    uninfected_group = []
    
    for i in range(0, 100):
        uninfected_person = Person(5, False)
        uninfected_group.append(uninfected_person)
    
    infected_count = 0
    uninfected_count = 0
    
    for people in uninfected_group:
        random_infection_rate = random.uniform(0.0, 1.0)
        if random_infection_rate < virus.repro_rate:
            people.infection = virus
            infected_count += 1
        else:
            uninfected_count += 1
