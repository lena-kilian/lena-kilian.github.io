# Projects

# Agent-based modelling using Python

This model is part of an [assessment](http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/assessment1/index.html) for [GEOG5995](http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/index.html). It creates *n* number of agents, which are located randomly on a 100 x 100 grid. In this example the agents represent sheep, which will move around and interact with an imported environment, as well as each other. 

Python and text files can be downloaded [here](https://github.com/lena-kilian/lena-kilian.github.io/tree/master/abm/GEOG5995M_CW1).

## 1 The Agent Framework
### 1.1 Creating the Class

First, the `random` and `copy` packages must be imported. 

```
import random
import copy
```

The `class` was defined as Agents. An initiating function was created. 

# NEED TO FINISH THIS!!!
### NEED TO FINISH THIS!!!
Each agent has an x-coordinate, y-coordinate _________ 
### NEED TO FINISH THIS!!!
# NEED TO FINISH THIS!!!

Moreover, the `print` was overwritten, such that it would print the x- and y-coordinates of the printed agent. 

```
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
```

### 1.2 Building Functions for the Class

Thereafter, `moveagent` was defined to randomly move the agent around the environment. An agent's move along the x- and y-directions were separated, and there was an equal chance that the agents position is a given direction would increase, decrease or remain the same. If an agent had a store higher than or equal to 100, they were coded to move twice in a given round. The direction of the first move would not impact the direction of the second move. 


```
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
```

In addition to being able to move around the environment, agents are able to interact with it by eating it or regurgitating some grass they had previously eaten onto it. With each eating iteration, 10 units are removed from the point the agent stands on in the environment and added to the agent's store. If less than 10 units are available in an agent's environemnt, the agent will eat the remaining value and the environemnt will drop to 0 at that point. If an agent's store is equal to or higher than 100, they will remove 10 units from the point in the environment they stand on, but only move 5 units to their store. The remaining five units will be fully eaten, so that they are unavailble to `share` (see below) and to slow down the storage accumulation. 

In a similar manner, once an agent has stored 150 units, the they will regurtitate 50 units onto the point in they environment they stand on. These units will become available for other agents to `eat` if they land on said point in the environment. 


# NEED TO CHANGE FUNCTION NAME!!!
### NEED TO CHANGE FUNCTION NAME!!!
```
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
```
### NEED TO CHANGE FUNCTION NAME!!!
# NEED TO CHANGE FUNCTION NAME!!!

## 2 Testing 
### 2.1 Creating a Mock Framework

### 2.2 Creating Test Functions

## 3 Building the Animation
