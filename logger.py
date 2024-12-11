import datetime
from person import Person
from virus import Virus


class Logger(object):
    #Define logger class
    def __init__(self, simulation_log):
        self.simulation_log = simulation_log


    # Metadata information
    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate, initial_infected):
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"------- HERD IMMUNITY SIMULATION -------\n"
                f"Created at: {datetime.datetime.now()}\n\n"
                f"Population size: {pop_size}\n"
                f"% of Initially Vaccinated: {vacc_percentage * 100}%\n"
                f"Initially Infected: {initial_infected}%\n"
                f"Virus: {virus_name}\n"
                f"Mortality Rate: {mortality_rate * 100}%\n"
                f"Reproduction Rate: {repro_rate * 100}%\n\n"
                f"----------------------------------------------------\n\n"
            )

    # Log interactions
    def log_interactions(self, time_step, population_alive, current_infected, new_infections, deaths, recoveries, total_interactions):
            
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"Time Step: {time_step}\n"
                f"Population Status:\n"
                f"- Currently Alive: {population_alive}\n"
                f"- Currently Infected: {current_infected}\n"
                f"- New Infections: {new_infections}\n"
                f"- Deaths This Step: {deaths}\n"
                f"- Recoveries This Step: {recoveries}\n"
                f"- Total Interactions: {total_interactions}\n"
            )
            
    # Logs number of people survived with infection
    def log_infection_survival(self, step_number, population_count):
        survivors_count = 0
        fatalities_count = 0
        
        # Check survival for infected people
        for person in population_count:
            if person.infection is not None:
                if person.did_survive_infection():
                    survivors_count += 1
                else:
                    fatalities_count += 1
                    
        living_count = sum(1 for person in population_count if person.is_alive)
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"Step {step_number} - Survival Outcomes:\n"
                f"Population alive: {living_count}\n"
                f"Survivors: {survivors_count}\n"
                f"Fatalities: {fatalities_count}\n\n"
            )

    # Logs time step
    def log_time_step(self, time_step_number):
        with open('simulation_log.txt', 'a') as log:
            log.write(f"Time Step: {time_step_number}\n")
            
    def log_summary(self, total_steps, population, total_infections):
        total_survivors = sum(1 for person in population if person.did_survive_infection())
        total_fatalities = sum(1 for person in population if not person.is_alive)
        
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"\n----------------------------------------------------\n"
                f"=== Simulation Summary ===\n"
                f"Total Steps: {total_steps}\n"
                f"Final Population alive: {sum(1 for p in population if p.is_alive)}\n"
                f"Total Infections: {total_infections}\n"
                f"Cumulative Survivors: {total_survivors}\n"
                f"Cumulative Fatalities: {total_fatalities}\n"
            )
