# Projects

## Agent-based modelling using Python

This model is part of an assessment for GEOG5995. It creates *n* number of agents, which are located randomly on a 100 x 100 grid. In this example the agents represent sheep, which will move around and interact with an imported environment, as well as each other. 

Python and text files are available [here](https://github.com/lena-kilian/lena-kilian.github.io/tree/master/abm/GEOG5995M_CW1)

### Creating the class

First, the `random` and `copy` packages must be imported. 

```
import random
import copy
```

The `class` was defined as Agents. An initiating function was created. 

# NEED TO FINISH THIS!!!
Each agent has an x-coordinate, y-coordinate _________ 

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

Thereafter, `moveagent` was defined to randomly

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
