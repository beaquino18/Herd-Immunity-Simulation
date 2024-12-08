import datetime
from person import Person
from virus import Virus


class Logger(object):
    """Defines a logger class to log the simulation."""
    def __init__(self, simulation_log):
        self.simulation_log = simulation_log
    
    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate, initial_infected):
        """Writes the initial metadata for the simulation."""
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"------- HERD IMMUNITY SIMULATION -------\n"
                f"Created at: {datetime.datetime.now()}\n\n"
                f"Population size: {pop_size}\n"
                f"% of Initially Vaccinated: {vacc_percentage * 100}% or {int(pop_size * vacc_percentage)} people\n"
                f"# of People Initially Infected: {initial_infected}\n"
                f"Virus: {virus_name}\n"
                f"Mortality Rate: {mortality_rate * 100}%\n"
                f"Reproduction Rate: {repro_rate * 100}%\n\n"
                f"----------------------------------------------------\n\n"
            )

    def log_interactions(self, time_step, population_alive, current_infected, new_infections, deaths, recoveries, total_interactions):
        """Writes information about the interactions in the simulation."""
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"Time Step: {time_step}\n"
                f"Population Status:\n"
                f"- Currently Alive: {population_alive}\n"
                f"- Currently Infected: {current_infected}\n"
                f"- New Infections: {new_infections}\n"
                f"- Recoveries This Step: {recoveries}\n"
                f"- Deaths This Step: {deaths}\n"
                f"- Total Interactions: {total_interactions}\n\n"
            )
            
            
    def log_summary(self, total_steps, population, total_infections, total_survivors, total_fatalities):
        """Writes a summary of the simulation."""
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"\n----------------------------------------------------\n\n"
                f"=== Simulation Summary ===\n"
                f"Total Steps: {total_steps}\n"
                f"Final Population alive: {sum(1 for p in population if p.is_alive)}\n"
                f"Total Infections: {total_infections}\n"
                f"Cummulative Survivors: {total_survivors}\n"
                f"Cumulative Fatalities: {total_fatalities}\n"
            )
