import random
import copy

# Classes

class Agents:
    
    def __init__(self, environment, all_agents):
        # Initiating with random starting point
        self.x_position = random.randint(0, 99)
        self.y_position = random.randint(0, 99)
        self.environment = environment
        self.store = 0
        self.all_agents = all_agents
        
    def __repr__(self):
        # changing print function
        return (f"[{self.x_position}, {self.y_position}]")
        
    def moveagent(self):
        # move agent randomly
        if self.store <= 100:
            a = random.random()
            b = random.random()
            if a <= 0.33:
                self.x_position = (self.x_position + 1) % 101
            elif 0.33 < a and a <= 0.67:
                self.x_position = (self.x_position - 1) % 101
            if b <= 0.33:
                self.y_position = (self.y_position + 1) % 101
            elif 0.33 < b and b <= 0.67:
                self.y_position = (self.y_position - 1) % 101
        else:
            for i in range(2):
                a = random.random()
                b = random.random()
                if a < 0.33:
                    self.x_position = (self.x_position + 1) % 101
                elif a < 0.67:
                    self.x_position = (self.x_position - 1) % 101
                if b < 0.33:
                    self.y_position = (self.y_position + 1) % 101
                elif b < 0.67:
                    self.y_position = (self.y_position - 1) % 101
               
    def eat(self):
        if self.environment[self.y_position][self.x_position] > 10:
            self.environment[self.y_position][self.x_position] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y_position][self.x_position]
            self.environment[self.y_position][self.x_position] = 0
        if self.store >= 100:
            ''' makes them eat it properly, rather than just store --> makes grass disappaear''' 
            self.store -= 5
        
    def throw_up(self):
        if self.store > 150:
            self.environment[self.y_position][self.x_position] += 50
            self.store -= 50

    def grass_grow(self):
        a = random.random()
        if a <= 0.01:
            for i in range(len(self.environment)):
                for j in range(len(self.environment[i])):
                    if self.environment[i][j] < 255:
                        self.environment[i][j] += 1
       
    def distance(self, other_agent):
        # calculate distance between agents
        return ((self.x_position - other_agent.x_position)**2 + 
                (self.y_position - other_agent.y_position)**2)**0.5

    def min_distance(self):
        # calculating the minimum distance between all agents
        return min(self.all_agents[i].distance(self.all_agents[j])
                   for i in range(len(self.all_agents))
                   for j in range(i + 1, len(self.all_agents)))
    
    def max_distance(self):
        # calculating the minimum distance between all agents
        return max(self.all_agents[i].distance(self.all_agents[j])
                   for i in range(len(self.all_agents))
                   for j in range(i + 1, len(self.all_agents)))

       
    def share(self, neighbourhood): 
        # share resources with agents within neighbourhood range
        for agent in self.all_agents:
            distance_btw = self.distance(agent)
            if distance_btw <= neighbourhood:
                self.store = (self.store + agent.store) / 2
                agent.store = copy.copy(self.store)