import pytest
from logger import Logger
from person import Person
from virus import Virus

def test_logger_initialization():
  logger = Logger("simulation_log.txt")
  with open("simulation_log.txt", "r") as log:
    content = log.readlines()
    assert content[0] == "=== Simulation Log ===\n"
    assert "Created at: " in content[1]

def test_write_metadata():
  logger = Logger("simulation_log.txt")
  logger.write_metadata(100, 0.5, "Ebola", 0.7, 0.2, 10)
  with open("simulation_log.txt", "r") as log:
    content = log.read()
    assert "--- HERD IMMUNITY SIMULATION ---" in content
    assert "Population size: 100" in content
    assert "% of Initially Vaccinated: 50.0%" in content
    assert "Initially Infected: 10" in content
    assert "Virus: Ebola" in content
    assert "Mortality Rate: 70.0%" in content
    assert "Reproduction Rate: 20.0%" in content

def test_log_interactions_with_infections():
  logger = Logger("simulation_log.txt")
  logger.log_interactions(1, 100, 50)
  with open("simulation_log.txt", "r") as log:
    content = log.read()
    assert "Step 1 - Interactions:" in content
    assert "Total Interactions: 100" in content
    assert "New Infections: 50" in content
    assert "Infection Rate: 50.00%" in content

def test_log_infection_survival():
  logger = Logger("simulation_log.txt")
  virus = Virus("Ebola", 0.7, 0.2)
  population = [
    Person(1, False, virus),
    Person(2, False, virus),
    Person(3, True),
  ]
  logger.log_infection_survival(1, population)
  
  with open("simulation_log.txt", "r") as log:
    content = log.read()
    assert "Step 1 - Survival Outcomes:" in content
    assert "Population alive:" in content
    assert "Survivors:" in content
    assert "Fatalities:" in content
    