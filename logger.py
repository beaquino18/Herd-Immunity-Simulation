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

    def log_interactions(self, time_step, population_alive, current_infected, 
                            new_infections, vaccinated_people, recoveries, deaths_this_step, 
                            total_interactions):
        """Writes information about the interactions in the simulation."""
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"Time Step: {time_step}\n"
                f"Population Status:\n"
                f"- Currently Alive: {population_alive}\n"
                f"- Currently Infected: {current_infected}\n"
                f"- New Infections: {new_infections}\n"
                f"- Recoveries This Step: {recoveries}\n"
                f"- Number of Vaccinated People This Step (Initially Vaccinated + Recoveries): {vaccinated_people}\n"
                f"- Deaths This Step: {deaths_this_step}\n"
                f"- Total Interactions: {total_interactions}\n\n"
            )
            
            
    def log_summary(self, total_steps, population, cumulative_infections, 
                    cumulative_survivor, cumulative_fatalities, total_vaccinations, 
                    total_interactions, interaction_vaccinations, interaction_death, reason):
        """Writes a summary of the simulation."""
        with open('simulation_log.txt', 'a') as log:
            log.write(
                f"\n----------------------------------------------------\n\n"
                f"=== Simulation Summary ===\n"
                f"Total Steps: {total_steps}\n"
                f"Final Population alive: {population}\n"
                f"Total Infections: {cumulative_infections}\n"
                f"Cummulative Survivors: {cumulative_survivor}\n"
                f"Cumulative Fatalities: {cumulative_fatalities}\n"
                f"Total Number of Vaccinations: {total_vaccinations}\n"
                f"Total Number of Interactions: {total_interactions}\n"
                f"Number of interactions resulted in vaccination: {interaction_vaccinations}\n"
                f"Number of interactions resulted in death: {interaction_death}\n"
                f"Why the simulation ended: {reason}\n"   
            )
