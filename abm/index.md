# Agent-based modelling using Python

This model is part of an [assessment](http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/assessment1/index.html) for [GEOG5995](http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/index.html). It creates *n* number of agents, which are located randomly on a 100 x 100 grid. In this example the agents represent sheep, which will move around and interact with an imported environment, as well as each other. 

The final model will create an animation as depicted in *Figure 1*

![Figure 1](animation3.gif)

*Figure 1: Animated illustration of the final model.*

_*Notes: This figure contains some snapshots of the model at different times and not the whole sequence._ 

Python and text files with the full code can be downloaded [here](https://github.com/lena-kilian/lena-kilian.github.io/tree/master/abm/GEOG5995M_CW1).

**Sections:**
[1 The Agent Framework](#1)
- [1.1 Creating the class](#1.1)
- [1.2 Moving around the environment](#1.2)
- [1.3 Interacting with the environment](#1.3)
- [1.4 Interacting with other agents](#1.4)
[2 Testing](#2)
- [2.1 Creating a mock framework](#2.1)
- [2.2 Creating test functions](#2.2)
[3 Building the animation](#3)


## <a name="1"></a>1 The Agent Framework
### <a name="1.1"></a>1.1 Creating the class

First, the `random` and `copy` packages must be imported. 

```
import random
import copy
```

The `class` was defined as Agents. An initiating function was created. 

```
class Agents:
    
    def __init__(self, environment, all_agents):
        # Initiating with random starting point
        self.x_position = random.randint(0, 99)
        self.y_position = random.randint(0, 99)
        self.environment = environment
        self.store = 0
        self.all_agents = all_agents
```

Each agent has an x-coordinate, y-coordinate, access to the environment, a store, and access to other agents' positions. Definitions for these variables are in table 1. 


*Table 1: Variable definitions from the `__init__` function.*

| Variable || Definition |
| - | - | - |
| `x_position` || An agent's x-coordinate |
| `y-position` || An agent's y-coordinate |
| `environment` || The environment: It is saved as a list containing lists of values, where the position of each list indicates the y-co-ordinate of said value, while the position of a value within each sub-list denotes the value's x-coordinate. Values here refer to how much grass is on a point in the environment. Visually, values respond to different colours. |
| `store` || The amount of grass an agent has gathered |
| `all_agents` || A list of all agents' positions |


Moreover, the `print` was overwritten, such that it would print the x- and y-coordinates of the printed agent.

```
    def __repr__(self):
        # changing print function
        return (f"[{self.x_position}, {self.y_position}]")
```

### <a name="1.2"></a>1.2 Moving around the environment

Thereafter, `moveagent` was defined to randomly move the agent around the environment. An agent's move along the x- and y-directions were separated, and there was an equal chance that the agents position is a given direction would increase, decrease or remain the same. If an agent had a store higher than or equal to 100, they were coded to move twice in a given round. The direction of the first move would not impact the direction of the second move. 

To prevent agents from leaving the grid, a torus was installed. This was done using a remainder function. In this way, agents exiting the grid on one side, will re-enter it on the opposite side.

```
   def moveagent(self):
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



### <a name="1.3"></a>1.3 Interacting with the environment

In addition to being able to move around the environment, agents are able to interact with it by eating it or regurgitating some grass they had previously eaten onto it. With each `eat` iteration, 10 units are removed from the point the agent stands on in the environment and added to the agent's store. If less than 10 units are available in an agent's environemnt, the agent will eat the remaining value and the environemnt will drop to 0 at that point. If an agent's store is equal to or higher than 100, they will remove 10 units from the point in the environment they stand on, but only move 5 units to their store. The remaining five units will be fully eaten, so that they are unavailble to `share` (see below) and to slow down the storage accumulation. 

In a similar manner, using `regurgitate` once an agent has stored more than 150 units, the their store will decrease by 50 units. The point in they environment they stand on will then increase by 26 units, while the surrounding 8 points will each gain 3 units. These units will become available for other agents to `eat` if they land on said points in the environment. 

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

    def regurgitate(self):
        if self.store > 150:
            self.environment[self.y_position][self.x_position] += 26
            self.environment[self.y_position - 1][self.x_position - 1] += 3
            self.environment[self.y_position - 1][self.x_position + 1] += 3
            self.environment[self.y_position - 1][self.x_position] += 3
            self.environment[self.y_position + 1][self.x_position - 1] += 3
            self.environment[self.y_position + 1][self.x_position + 1] += 3
            self.environment[self.y_position + 1][self.x_position] += 3
            self.environment[self.y_position][self.x_position - 1] += 3
            self.environment[self.y_position][self.x_position + 1] += 3
            self.store -= 50
```

`grass_grow` is slightly different in that the environment is accessed through an agent, but the agent is not actually manipulated.

```
    def grass_grow(self):
        a = random.random()
        if a <= 0.01:
            for i in range(len(self.environment)):
                for j in range(len(self.environment[i])):
                    if self.environment[i][j] < 255:
                        self.environment[i][j] += 1
```

### <a name="1.4"></a>1.4 Interacting with other agents

sharing stock! --> so needs access to other agents' stock information

```
    def share(self, neighbourhood): 
        # share resources with agents within neighbourhood range
        for agent in self.all_agents:
            distance_btw = self.distance(agent)
            if distance_btw <= neighbourhood:
                self.store = (self.store + agent.store) / 2
                agent.store = copy.copy(self.store)
```

needs access to other agents' spatial information!!
```
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

       

```


## <a name="2"></a>2 Testing 
### <a name="2.1"></a>2.1 Creating a mock framework

### <a name="2.2"></a>2.2 Creating test functions

## <a name="3"></a>3 Building the animation
