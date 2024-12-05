import datetime
from person import Person


class Logger(object):
    def __init__(self, simulation_log):
        self.simulation_log = simulation_log
        with open('simulation_log.txt', 'w') as log:
            log.write("=== Simulation Log ===\n")
            log.write("Created at: "+ str(datetime.datetime.now()) + "\n\n")

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        with open('simulation_log.txt', 'a') as log:
            log.write(f"""Population size: {pop_size}\n
                        % of Vaccinated: {vacc_percentage}\n
                        Virus: {virus_name}\n
                        Mortality Rate: {mortality_rate}\n
                        Reproduction Rate: {basic_repro_num}\n
                        """)

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        if number_of_interactions > 0:
            infection_rate = (number_of_new_infections / number_of_interactions) * 100
        else:
            infection_rate = 0
            
        with open('sumulation_log.txt', 'a') as log:
            log.write(f"""=== Interaction Time Step {step_number} ===\n
                        Total Interactions: {number_of_interactions}\n
                        New Infections: {number_of_new_infections}\n
                        Infection Rate: {infection_rate:.2f}%\n
                        """)
            

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        fatalities = 0
        for person in population_count:
            if person.did_survive_infection() == False:
                fatalities += 1
                
        number_of_new_fatalities = fatalities
        with open('simulation.txt', 'a') as log:
            log.write(f"""=== Time Step {step_number} ===\n
                        Population size: {population_count}\n
                        Number of Fatalities: {number_of_new_fatalities}""")

    def log_time_step(self, time_step_number):
        time_step_number = 0
        
        for time in time_step_number:
            time_step_number += 1
            
        with open('simulation_log.txt', 'a') as log:
            log.write(f"Time Step: {time_step_number}\n")
