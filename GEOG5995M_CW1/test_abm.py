"""
tests for abm: agents_framework.py
"""
import pytest
import agent_framework


# none of this is working yet!!!!

agents = []

def test_moveagent():
    agent_A = agent_framework.Agents(environment, agents)
#    agent_B = agent_framework.Agents(environment, agents)
#    agent_C = agent_framework.Agents(environment, agents)
    assert agent_A.moveagent() == (49, 49) or agent_A.moveagent() == (49, 51) or agent_A.moveagent() == (51, 49) or agent_A.moveagent() == (51, 51)  
# ^ this test will fail because agent A is not at [50, 50] but generally this is how it would be done


pytest.main()  
    
  
    
'''
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
        if random.random() < 0.5:
            self.x_position = (self.x_position + 1) % 100
        else:
            self.x_position = (self.x_position - 1) % 100
        if random.random() < 0.5:
            self.y_position = (self.y_position + 1) % 100
        else:
            self.y_position = (self.y_position - 1) % 100
        if self.x_position == 0:
            self.x_position = 1
        if self.y_position == 0:
            self.y_position = 1
               
    def eat(self):
        if self.environment[self.y_position][self.x_position] > 10:
            self.environment[self.y_position][self.x_position] -= 10
            self.store += 10
        else:
            self.environment[self.y_position][self.x_position] = 0
            self.store += self.environment[self.y_position][self.x_position]
            
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
                agent.store = (self.store + agent.store) / 2

'''
