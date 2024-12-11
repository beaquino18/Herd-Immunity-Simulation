import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        # Clear the simulation log file every run, overwrite with empty string
        with open('simulation_log.txt', 'w') as log:
            log.write("")  
            
        self.logger = Logger('simulation_log.txt')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected = []
        self.cumulative_infections = self.initial_infected 
        self.cumulative_survivor = 0
        self.cumulative_fatalities = 0
        self.total_interactions = 0
        self.current_alive = 0
        self.current_infected = 0
        self.time_step_counter = 0
        self.vaccinated_this_step = 0
        self.total_vaccinations = int(self.pop_size * self.vacc_percentage)
        self.interaction_vaccinations = 0
        self.interaction_death = 0
        self.reason = ""

    def _create_population(self):
        """Creates population (a list of Person objects)"""
        population = []
        
        # Calculation for total number of people who are vaccinated
        total_vaccinated = int(self.pop_size * self.vacc_percentage)
        
        self.initial_infected = min(self.initial_infected, self.pop_size - total_vaccinated)
        
        #Add infected people in the population list
        for i in range(self.initial_infected):
            person = Person(i, False, self.virus)
            population.append(person)
        
        
        #Add vaccinated people in the population list
        for i in range(total_vaccinated):
            person = Person(len(population), True)
            population.append(person)
                
        #Add remaining uninfected, unvaccinated people in the population list
        while len(population) < self.pop_size:
            person = Person(len(population), False)
            population.append(person)
        
        return population
        

    def _simulation_should_continue(self):
        """Determines whether the simulation should continue."""
        living_count = 0
        vaccinated_count = 0
        
        for people in self.population:
            if people.is_alive:
                living_count += 1
                if people.is_vaccinated:
                    vaccinated_count += 1
        
        # If all people in self.pop_size are dead, stop simulation
        if living_count == 0:
            self.reason = "All people are dead"
            return False
        
        # If all people in self.pop_size are vaccincated, stop simulation
        if vaccinated_count == living_count:
            self.reason = "All people are vaccinated"
            return False
        
        # If the conditions aren't met, continue simuation
        return True

    def run(self):
        """Runs the simulation"""
        time_step_counter = 0
        should_continue = True
        
        # Initialize logger
        self.logger.write_metadata(
            self.pop_size,
            self.vacc_percentage,
            self.virus.name,
            self.virus.mortality_rate,
            self.virus.repro_rate,
            self.initial_infected
        )

        # Run simulation steps
        while should_continue:
            self.time_step()
            time_step_counter += 1
            should_continue = self._simulation_should_continue()
                
        #Log final interactions for last step
        self.logger.log_summary(time_step_counter, len(self.population), self.cumulative_infections, 
                                self.cumulative_survivor, self.cumulative_fatalities, 
                                self.total_vaccinations, self.total_interactions,
                                self.interaction_vaccinations, self.interaction_death, self.reason)


    def time_step(self):
        """Simulates one time step in the simulation and logs interaction"""
        interactions = 0
        new_infections = set()
        deaths_this_step = 0
        recovered_this_step = 0
        
        # Get currently infected and alive people
        infected_people = [person for person in self.population if person.infection and person.is_alive]
        
        # Loop through population list, check for interactions
        if infected_people:
            for infected_person in infected_people:
                    for _ in range(100):
                        possible_contacts = [p for p in self.population 
                                                if p._id != infected_person._id 
                                                and p.is_alive]
                        if possible_contacts:
                            random_person = random.choice(possible_contacts)
                            interactions += 1
                            
                            if self.interaction(infected_person, random_person):
                                new_infections.add(random_person._id)
        
        # Process infections
        for person in self.population:
            if person.infection and person.is_alive:
                survival_random = random.random()
                if survival_random < self.virus.mortality_rate:
                    person.is_alive = False
                    deaths_this_step += 1
                    person.infection = None
                    self.interaction_death += 1
                else:
                    person.is_vaccinated = True
                    person.infection = None
                    recovered_this_step += 1
                    self.interaction_vaccinations += 1
                    
        self._infect_newly_infected()
        
        # Update current state
        newly_infected = len(new_infections)
        self.cumulative_infections += newly_infected
        self.total_interactions += interactions
        self.current_alive = sum(1 for person in self.population if person.is_alive)
        self.current_infected = sum(1 for person in self.population if person.infection is not None)
        self.time_step_counter += 1
        self.cumulative_survivor += recovered_this_step
        self.cumulative_fatalities += deaths_this_step
        self.population = [person for person in self.population if person.is_alive]
        self.vaccinated_this_step = sum(1 for person in self.population if person.is_vaccinated)
        self.total_vaccinations += recovered_this_step
        
        # Log the time step results
        self.logger.log_interactions(
            self.time_step_counter,
            self.current_alive,
            self.current_infected,
            newly_infected,
            self.vaccinated_this_step,
            recovered_this_step,
            deaths_this_step,
            interactions
        )
        

    def interaction(self, infected_person, random_person):
        """Handles interactions between two people"""
        assert infected_person.infection is not None
        assert infected_person.is_alive
        assert random_person.is_alive
        
        if not random_person.is_vaccinated and random_person.infection is None:
            random_value = random.uniform(0.0, 1.0)
            if random_value < self.virus.repro_rate:
                self.newly_infected.append(random_person)
                return True
        return False

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    pop_size = int(sys.argv[1])
    vacc_percentage = float(sys.argv[2])
    virus_name = sys.argv[3]
    repro_rate = float(sys.argv[4])
    mortality_rate = float(sys.argv[5])
    initial_infected = int(sys.argv[6])
    
    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)
    sim.run()
