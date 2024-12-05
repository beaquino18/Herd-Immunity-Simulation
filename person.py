import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id: int, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    # Checks if a person survived an infection
    def did_survive_infection(self):
        if self.infection != None:
            random_value = random.uniform(0.0, 1.0)
            if random_value <= self.infection.mortality_rate:
                self.is_alive = False
                return False
            else:
                self.is_alive = True
                self.is_vaccinated = True
                self.infection = None
                return True
    

    

if __name__ == "__main__":
    # Test for a vaccinated person
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Test an infected person. An infected person has an infection/virus
    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus
    

    # Test for did_survive_infection method
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
    
    # Test for valid attributes of a person
    person = Person(10, False, None)
    assert person._id == 10
    assert person.is_vaccinated is False
    assert person.infection is None
    assert person.is_alive is True
    
    # Test when mortality rate is 100%
    virus = Virus("Zombie Virus", 0.8, 1.0)
    person = Person(1, False, virus)
    
    assert person.did_survive_infection() is False
    assert person.is_alive is False
    assert person.is_vaccinated is False
    assert person.infection is virus
    
    # Test when person is infected twice
    virus = Virus("Mild", 0.8, 0.2)
    person = Person(3, False, virus)
    
    assert person.did_survive_infection() is True
    assert person.is_vaccinated is True
    assert person.infection is None
    
    new_virus = Virus("Deadly", 0.8, 0.8)
    person.infection = new_virus
    assert person.is_vaccinated is True
    assert person.infection is new_virus
    assert person.is_alive is True
    

    # Stretch Challenge - test for knowing the infected and uninfected count of a certain group of people
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
    
    print(f"Number of people infected: {infected_count}\nNumber of people uninfected: {uninfected_count}")
    
