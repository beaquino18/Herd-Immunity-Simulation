import datetime
from person import Person
from virus import Virus


class Logger(object):
    
    #Define logger class
    def __init__(self, simulation_log):
        self.simulation_log = simulation_log
        with open('simulation_log.txt', 'w') as log:
            log.write("=== Simulation Log ===\n")
            log.write(f"Created at: {datetime.datetime.now()}\n\n")

    # Metadata information
    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"Population size: {pop_size}\n"
                f"% of Vaccinated: {vacc_percentage}\n"
                f"Virus: {virus_name}\n"
                f"Mortality Rate: {mortality_rate * 100}%\n"
                f"Reproduction Rate: {basic_repro_num * 100}%\n\n"
            )

    # Log interactions
    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        if number_of_interactions > 0:
            infection_rate = (number_of_new_infections / number_of_interactions) * 100
        else:
            infection_rate = 0
            
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"Step {step_number} - Interactions:\n"
                f"Total Interactions: {number_of_interactions}\n"
                f"New Infections: {number_of_new_infections}\n"
                f"Infection Rate: {infection_rate:.2f}%\n\n"
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
                f"Survivors: {survivors_count}\n\n"
                f"Fatalities: {fatalities_count}\n\n"
            )

    # Logs time step
    def log_time_step(self, time_step_number):
        with open('simulation_log.txt', 'a') as log:
            log.write(f"Time Step: {time_step_number}\n")
