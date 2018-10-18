## CW1 

[Download Animtation Code](original_animation.py)

```
import random
from matplotlib import pyplot
from matplotlib import animation
import agent_framework
import csv
import time


n = 150   # number of agents
neighbourhood = 20
k = 200 # number of iterations

agents = []
environment = []

with open('in_example.txt', newline='\n') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        environment.append(row)
        
# defining the figure

fig = pyplot.figure(figsize=(8, 8))

# creating agents
while len(agents) < n:
    agents.append(agent_framework.Agents(environment, agents))

# update function --> makes agents eat, share, move and animates
def update(frame_number):
    fig.clear()
    pyplot.imshow(environment)
    pyplot.ylim(0, 100)
    pyplot.xlim(0, 100)
    random.shuffle(agents) # shuffles the order in which agents are moved, receive resources, etc. --> important for share function
    agents[0].grass_grow() # has to be outside so that it deons't grow after each inididual agent moved
    for i in range(len(agents)):
        agents[i].eat()
        agents[i].throw_up()
        agents[i].share(neighbourhood)
        agents[i].moveagent()
    for i in range(len(agents)):
        pyplot.scatter(agents[i].x_position, agents[i].y_position, color=['white', 'black', 'brown'], s=5)

# stops the agents once the grass is eaten up in one spot
def gen_function(b = [0]):
    start = time.time()
    a = 0
    list = []
    while True:
        for i in range(len(environment)):
            list.append(min(environment[i]))
        if min(list) > 0:
            a += 1
            yield a
        else:
            end = time.time()
            print('Timer:', end - start, 'seconds')
            break

animation = animation.FuncAnimation(fig, update, frames = gen_function(), repeat=False) # uses gen_function for stopping
```

[Download Agent Class Code](agent_framework.py)

```
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
        a = random.random()
        b = random.random()
        if a < 0.5:
            self.x_position = (self.x_position + 1) % 100
        else:
            self.x_position = (self.x_position - 1) % 100
        if b < 0.5:
            self.y_position = (self.y_position + 1) % 100
        else:
            self.y_position = (self.y_position - 1) % 100            
               
    def eat(self):
        if self.environment[self.y_position][self.x_position] > 10:
            self.environment[self.y_position][self.x_position] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y_position][self.x_position]
            self.environment[self.y_position][self.x_position] = 0
        
    def throw_up(self):
        if self.store > 100:
            self.environment[self.y_position][self.x_position] += 28
            self.environment[self.y_position - 1][self.x_position - 1] += 9
            self.environment[self.y_position - 1][self.x_position + 1] += 9
            self.environment[self.y_position - 1][self.x_position] += 9
            self.environment[self.y_position + 1][self.x_position - 1] += 9
            self.environment[self.y_position + 1][self.x_position + 1] += 9
            self.environment[self.y_position + 1][self.x_position] += 9
            self.environment[self.y_position][self.x_position - 1] += 9
            self.environment[self.y_position][self.x_position + 1] += 9
            self.store -= 100

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
```
