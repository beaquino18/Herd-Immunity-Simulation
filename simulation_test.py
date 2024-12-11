import pytest
from simulation import Simulation
from person import Person
from logger import Logger
from virus import Virus


def test_simulation_init():
    virus = Virus("Ebola", 0.7, 0.2)
    simulation = Simulation(100, 0.5, virus, 10)
    assert simulation.pop_size == 100
    assert simulation.vacc_percentage == 0.5
    assert simulation.virus == virus
    assert simulation.initial_infected == 10
    assert simulation.newly_infected == []
    assert simulation.cumulative_infections == 10
    assert simulation.cumulative_survivor == 0
    assert simulation.cumulative_fatalities == 0
    assert simulation.total_interactions == 0
    assert simulation.current_alive == 0
    assert simulation.current_infected == 0
    assert simulation.time_step_counter == 0
    assert simulation.vaccinated_this_step == 0
    assert simulation.total_vaccinations == 50
    assert simulation.interaction_vaccinations == 0
    assert simulation.interaction_death == 0
    assert simulation.reason == ""
    
def test_create_population():
    virus = Virus("Ebola", 0.7, 0.2)
    simulation = Simulation(100, 0.5, virus, 10)
    population = simulation._create_population()
    
    assert len(population) == 100
    assert len([person for person in population if person.is_vaccinated]) == 50
    assert len([person for person in population if person.infection]) == 10
    assert len([person for person in population if not person.is_vaccinated and not person.infection]) == 40
    
def test_simulation_should_continue():
    virus = Virus("Ebola", 0.7, 0.2)
    simulation = Simulation(100, 0.5, virus, 10)
    assert simulation._simulation_should_continue() == True
    
    for person in simulation.population:
        person.is_alive = False
    assert simulation._simulation_should_continue() == False
    
    for person in simulation.population:
        person.is_alive = True
        person.is_vaccinated = True
    assert simulation._simulation_should_continue() == False

def test_interaction():
    virus = Virus("Ebola", 0.7, 0.2)
    simulation = Simulation(100, 0.5, virus, 10)
    person1 = Person(1, False, virus)
    person2 = Person(2, False, virus)
    simulation.interaction(person1, person2)
    assert person1.is_alive == True
    assert person2.is_alive == True
    assert person1.infection == None
    assert person2.infection == None
    
    person1.is_vaccinated = True
    person2.is_vaccinated = True
    simulation.interaction(person1, person2)
    assert person1.is_alive == True
    assert person2.is_alive == True
    assert person1.infection == None
    assert person2.infection == None
    
    person1.is_vaccinated = False
    person2.is_vaccinated = False
    simulation.interaction(person1, person2)
    assert person1.is_alive == True
    assert person2.is_alive == True
    assert person1.infection == None
    assert person2.infection == None
    
    person1.infection = virus
    person2.infection = virus
    simulation.interaction(person1, person2)
    assert person1.is_alive == False
    assert person2.is_alive == False
    assert person1.infection == None
    assert person2.infection == None
    
    person1.is_alive = True
    person2.is_alive = True
    person1.infection = virus
    person2.infection = None
    simulation.interaction(person1, person2)
    assert person1.is_alive == True
    assert person2.is_alive == True
    assert person1.infection == virus
    assert person2.infection == virus
    
    person1.is_alive = True
    person2.is_alive = True
    person1.infection = None
    person2.infection = virus
    simulation.interaction(person1, person2)
    assert person1.is_alive == True
    assert person2.is_alive == True
    assert person1.infection == virus
    assert person2.infection == virus
