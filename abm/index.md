# Projects

## Agent-based modelling using Python

This model is part of an assessment for GEOG5995. It creates n number of agents, which are located randomly on a 100 x 100 grid. In this example the agents represent sheep, which will move around an imported environment. 

Python and text files are available [here](https://github.com/lena-kilian/lena-kilian.github.io/tree/master/abm/GEOG5995M_CW1)

### Creating the class

First, the `random` and `copy` packages must be imported. 

```
import random
import copy
```

The `class` was defined as Agents.  

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
