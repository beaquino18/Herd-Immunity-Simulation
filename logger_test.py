import pytest
from logger import Logger
from person import Person
from virus import Virus


def test_write_metadata():
    logger = Logger("simulation_log.txt")
    logger.write_metadata(
        pop_size=100,
        vacc_percentage=0.5,
        virus_name="Ebola",
        mortality_rate=0.7,
        repro_rate=0.2,
        initial_infected=10
    )
    
    with open("simulation_log.txt", "r") as log:
        content = log.read()
        assert "------- HERD IMMUNITY SIMULATION -------" in content
        assert "Created at:" in content
        assert "Population size: 100" in content
        assert "% of Initially Vaccinated: 50.0% or 50 people" in content
        assert "# of People Initially Infected: 10" in content
        assert "Virus: Ebola" in content
        assert "Mortality Rate: 70.0%" in content
        assert "Reproduction Rate: 20.0%" in content
    
def test_log_interaction():
    logger = Logger("simulation_log.txt")
    logger.log_interactions(
        time_step=1,
        population_alive=95,
        current_infected=10,
        new_infections=5,
        vaccinated_people=50,
        recoveries=2,
        deaths_this_step=3,
        total_interactions=1000
    )
    
    with open("simulation_log.txt", "r") as log:
        content = log.read()
        assert "Time Step: 1" in content
        assert "Currently Alive: 95" in content
        assert "Currently Infected: 10" in content
        assert "New Infections: 5" in content
        assert "Recoveries This Step: 2" in content
        assert "Number of Vaccinated People This Step (Initially Vaccinated + Recoveries): 50" in content
        assert "Deaths This Step: 3" in content
        assert "Total Interactions: 1000" in content
        

def test_log_summary():
    logger = Logger("simulation_log.txt")
    population = [
        Person(1, False, None),  # Alive
        Person(2, False, None),  # Alive
        Person(3, False, None)   # Alive
    ]
    
    logger.log_summary(
        total_steps=2,
        population=len(population),
        cumulative_infections=10,
        cumulative_survivor=7,
        cumulative_fatalities=3,
        total_vaccinations=5,
        total_interactions=100,
        interaction_vaccinations=4,
        interaction_death=3,
        reason="All people are vaccinated"
    )
    
    with open("simulation_log.txt", "r") as log:
        content = log.read()
        assert "=== Simulation Summary ===" in content
        assert "Total Steps: 2" in content
        assert "Final Population alive: 3" in content
        assert "Total Infections: 10" in content
        assert "Cummulative Survivors: 7" in content
        assert "Cumulative Fatalities: 3" in content
        assert "Total Number of Vaccinations: 5" in content
        assert "Total Number of Interactions: 100" in content
        assert "Number of interactions resulted in vaccination: 4" in content
        assert "Number of interactions resulted in death: 3" in content
        assert "Why the simulation ended: All people are vaccinated" in content
