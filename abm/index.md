# <a name="pagetop"></a>Agent-based modelling using Python

This model is part of an [assessment](http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/assessment1/index.html) for [GEOG5995](http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/index.html). It creates *n* agents, which are located randomly on a 100 x 100 grid. In this example the agents represent sheep, which will move around and interact with an imported environment, as well as each other. 

The final model will create an animation as depicted in *Figure 1*

![Figure 1](animation3.gif)<br/>
*Figure 1: Animated illustration of the final model.*<br/>
_*Notes: This figure contains some snapshots of the model at different times and not the whole sequence._


Python and text files with the full code can be downloaded [here](https://github.com/lena-kilian/lena-kilian.github.io/tree/master/abm/GEOG5995M_CW1). Please note that all indentations within this online representation of the code are intentional. In other words, the functions in sections 1 and 2 are defined *within* a class and are therefore indented. 

### Sections:

[1 The Agent Framework](#1)
- [1.1 Creating the class](#1.1)
- [1.2 Moving around the environment](#1.2)
- [1.3 Interacting with the environment](#1.3)
- [1.4 Interacting with other agents](#1.4)

[2 Testing](#2)
- [2.1 Creating a mock framework](#2.1)
- [2.2 Creating test functions](#2.2)

[3 Building the animation](#3)
- [3.1 Basic animation stopping after *k* iterations](#3.1)
- [3.2 Alternative endings: Stopping the animation using a generator function](#3.2)


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
        self.x_position = random.randint(0, 99)
        self.y_position = random.randint(0, 99)
        self.environment = environment
        self.store = 0
        self.all_agents = all_agents
```

Each agent has an x-coordinate, y-coordinate, access to the environment, a store, and access to other agents' positions. Definitions for these variables are in table 1. 


*<a name="T1"></a>Table 1: Variable definitions from the `__init__` function.*  

| Variable || Definition |
| - | - | - |
| `x_position` || An agent's x-coordinate |
| `y-position` || An agent's y-coordinate |
| `environment` || Raster data saved as a list containing lists of values, where the position of each list indicates the y-co-ordinate of said value, while the position of a value within each sub-list denotes the value's x-coordinate. Values here refer to how much grass is on a point in the environment. Visually, values respond to different colours. |
| `store` || The amount of grass an agent has gathered |
| `all_agents` || A list of all agents' positions |


Moreover, the `print` was overwritten, such that it would print the x- and y-coordinates of the printed agent.

```
    def __repr__(self):
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

In addition to being able to move around the environment, agents are able to interact with it by eating it or regurgitating some grass they had previously eaten onto it. With each `eat` iteration, 10 units are removed from the point the agent stands on in the environment and added to the agent's store. If less than 10 units are available in an agent's environment, the agent will eat the remaining value and the environment will drop to 0 at that point. If an agent's store is equal to or higher than 100, they will remove 10 units from the point in the environment they stand on, but only move 5 units to their store. The remaining five units will be fully eaten, so that they are unavailable to `share` (see below) and to slow down the storage accumulation. 

In a similar manner, using `regurgitate` once an agent has stored more than 150 units, their store will decrease by 50 units. The raster in the environment they stand on will then increase by 26 units, while the surrounding 8 rasters will each gain 3 units. These units will become available for other agents to `eat` if they land on said raster in the environment. 

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

Similarly, `grass_grow` is an environmental manipulations. However, it differs from `eat` and `regurgitate` in that the environment is accessed through an agent, but the agent is not actually manipulated. To avoid the grass growing excessively, and because its values have to be integers, the occurrence of this function was randomised. In other words, with each iteration of this function, the probability that the values within the lists within the environment will increase by 1 unit is 0.01. Moreover, is a value within the environment was over 255 units, `grass_grow` would not impact the environment. This value was chosen as it is the highest value in the environment at the start.

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

Just as the agents are able to interact with the environment, they are able to interact with other agents. By providing agents with other agents' spatial location data (see `all_agents` in [table 1](#T1)) we are able to automate distance calculations (using Pythagoras' theorem) between each agent pair.

```
    def distance(self, other_agent):
        return ((self.x_position - other_agent.x_position)**2 + 
                (self.y_position - other_agent.y_position)**2)**0.5
```
Calculating the distances between agents can be useful for a variety of things. Here, they were used to indicate whether an agent would `share` their stock with another agent. If agent A in within a certain range of agent B (range is defined by the variable `neighbourhood`), their stocks will average to their mean stock. 

```
    def share(self, neighbourhood): 
        for agent in self.all_agents:
            distance_btw = self.distance(agent)
            if distance_btw <= neighbourhood:
                self.store = (self.store + agent.store) / 2
                agent.store = copy.copy(self.store)
```
Moreover, the distance function can be used to calculate minimum and maximum distances between all agents. Particularly for the minimum distance it is important to ensure that an agent is not calculating their distance to themselves. Therefore, two `for` loops were used, where the first one ran through all agents, *i* through *n*, while the second one only started at *i + 1*.

```
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

In order to test functions, an expected output needs to be provided. For instance, as agents' starting points were randomised in the original model, a mock framework was created in which this randomisation was removed. Although all functions from [section 1](#1) were tested, this section will only go through the functions which had to be altered for testing. The full mock framework can be found [here](https://github.com/lena-kilian/lena-kilian.github.io/tree/master/abm/GEOG5995M_CW1). The packages used in the mock framework were identical with those used in the actual framework.

As already mentioned, starting points were de-randomised. For this, `__init__` was altered to provide non-random x- and y-coordinates. 

```
class Agents:
    
    def __init__(self, environment, all_agents):
        self.x_position = 50
        self.y_position = 50
        self.environment = environment
        self.store = 0
        self.all_agents = all_agents
```

Moreover, the `moveagent` function was changed, to force the agent to move in each iteration. Earlier, there was a 0.33 chance that the agent would not move on a given axis. To test with certainty that agents can actually move, this was removed in the mock framework. Moreover, the ability of agents with a store of 100 units or more to move twice was altered. While they are still able to move twice, the direction of their movement was changed to be identical for both iterations. 

```
    def moveagent(self):
        a = random.random()
        b = random.random()
        if self.store <= 100:
            if a <= 0.33:
                self.x_position = (self.x_position + 1) % 101
            else:
                self.x_position = (self.x_position - 1) % 101
            if b <= 0.33:
                self.y_position = (self.y_position + 1) % 101
            else:
                self.y_position = (self.y_position - 1) % 101
        else:
            for i in range(2):
                if a < 0.33:
                    self.x_position = (self.x_position + 1) % 101
                else:
                    self.x_position = (self.x_position - 1) % 101
                if b < 0.33:
                    self.y_position = (self.y_position + 1) % 101
                else:
                    self.y_position = (self.y_position - 1) % 101
```

Lastly, randomisation was removed from `grass_grow`, to test if this function is actually able to manipulate the environment as wanted. 

```
    def grass_grow(self):
        for i in range(len(self.environment)):
            for j in range(len(self.environment[i])):
                if self.environment[i][j] < 255:
                    self.environment[i][j] += 1
```

### <a name="2.2"></a>2.2 Creating test functions

To test the mock framework, a testing file was created. In addition to importing `mock_framework`, `pytest` will be needed to run the actual test function. 

```
import pytest
import mock_framework
```

Again, although all functions were tested, I will only present a few examples on this page. Please refer to [test_abm.py](https://github.com/lena-kilian/lena-kilian.github.io/tree/master/abm/GEOG5995M_CW1) for the full code. 

Because the mock framework defined agents to start at (50, 50) and because `moveagent` would force the agent to move, `test_moveagent` should check if an agent with a store below 100 units should be at (50 +/- 1, 50 +/- 1) after one iteration, while an agent with a higher store should be at (50 +/- 2, 50 +/- 2). 

```
def test_moveagent():
    agents = []
    environment = []
    while len(agents) < 2:
        agents.append(mock_framework.Agents(environment, agents))
    
    agents[0].store = 0
    agents[0].moveagent()
    assert agents[0].y_position == 49 or agents[0].y_position == 51
    assert agents[0].x_position == 49 or agents[0].x_position == 51
    
    agents[1].store = 200
    agents[1].moveagent()
    assert agents[1].y_position == 48 or agents[1].y_position == 52
    assert agents[1].x_position == 48 or agents[1].x_position == 52
```

In testing, it is important to test for various scenarios. In this case, I therefore tested that both cases (store >= 100 and store < 100) were functioning properly. This was also done for the other functions. For instance, `test_eat` tested for the reduction of units from the environment and the addition of units to the stock for cases of an environmental raster containing 10+ units and having less than 10 units. Moreover, the aspect of the function in which an agent's stock only increases by 5 units if their (post-eating) store was 100 units or more was tested. 

```
def test_eat():
    environment = []
    list = []
    while len(list) < 100:
        list.append(100)
    while len(environment) < 100:
        environment.append(list.copy())
    
    agents = []
    while len(agents) < 2:
        agents.append(mock_framework.Agents(environment, agents))
    
    agents[0].eat()
    assert agents[0].environment[agents[0].y_position][agents[0].x_position] == 90 and agents[0].store == 10
    
    agents[0].store = 90
    agents[0].eat()
    assert agents[0].environment[agents[0].y_position][agents[0].x_position] == 80 and agents[0].store == 95
    
    agents[0].environment[agents[0].y_position][agents[0].x_position] = 3
    agents[0].eat()
    assert agents[0].environment[agents[0].y_position][agents[0].x_position] == 0 and agents[0].store == 98
```

A final example I would like to highlight here is `test_min_distance`. Here it was particularly important to test that agents do not calculate their distance from themselves. Additionally I checked that value provided as the minimum distance between all agents was not impacted by the agents' order. Thus, I manipulated the agents' positions and varied the agent pair with the minimum distance. 

```
def test_min_distance():
    environment = []
    agents = []
    while len(agents) < 3:
         agents.append(mock_framework.Agents(environment, agents))
    
    agents[0].x_position = 4
    agents[0].y_position = 0
    agents[1].x_position = 0
    agents[1].y_position = 3
    
    assert agents[0].min_distance() == 5
    
    agents[2].x_position = 0
    agents[2].y_position = 3
    
    assert agents[0].min_distance() == 0
```

## <a name="3"></a>3 Building the animation

### <a name="3.1"></a>3.1 Basic animation stopping after *k* iterations

First, all relevant packages were loaded, and relevant variables and lists were created. 

*<a name="T2"></a>Table 2: Variables and lists needed for the animation.*  

| Variable / List || Definition |
| - | - | - |
| `n` || The number of agents |
| `k` || The number of iterations |
| `neighbourhood` || The maximum distance 2 agents can have to `share` their stock |
| `agents` || A list containing all agents |
| `environment` || Same as in [table 1](#T1) |
| `fig` || A (currently empty) graph, in which the agents and environment will be displayed |

```
import random
from matplotlib import pyplot
from matplotlib import animation
import agent_framework
import csv

n = 100
k = 200
neighbourhood = 20

environment = []
with open('in_example.txt', newline='\n') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        environment.append(row)

agents = []
while len(agents) < n:
    agents.append(agent_framework.Agents(environment, agents))
    
fig = pyplot.figure(figsize=(8, 8))
```

Second, an `update` function needs to be defined. This contains all functions we want to occur in the final animation (`move_agent`, `eat`, `regurgitate`, `grass_grow`, `share`). Thus, `update` can be used as a replacement for using the other functions individually. Moreover, `update` scatters each iteration onto `fig`. In order to only display agents' most recent positions, `fig` is also cleared in each iteration of `update`. 

```
def update(frame_number):
    fig.clear()
    pyplot.imshow(environment)
    pyplot.ylim(0, 100)
    pyplot.xlim(0, 100)
    random.shuffle(agents) # shuffles the order in which agents are manipulated, so that the sharing order shuffles
    agents[0].grass_grow() # has to be outside so that it doesn't grow after each inidividual agent moved
    for i in range(len(agents)):
        agents[i].eat()
        agents[i].regurgitate()
        agents[i].share(neighbourhood)
        agents[i].moveagent()
    for i in range(len(agents)):
        pyplot.scatter(agents[i].x_position, agents[i].y_position, color='white', s=10)
```

The animation can now be run, using the number of iterations (*k*) as a stopping point.

```
animation = animation.FuncAnimation(fig, update, frames = k, repeat=False)
```


### <a name="3.2"></a>3.2 Alternative endings: Stopping the animation using a generator function

As an add-on the animation stopping with a function was timed. Thus `time` had to be imported in addition to the packages from [section 3.1](#3.1).

```
import time
```

Thereafter, a generator function was defined, in which the agents, environment and visualisation are updated until there is a raster in the environment which contains 0 units of grass. Once this happens, `gen_function` will break the `update` loop. This function was then added to the animation as a measure of length (`frames`) of the animation. As the value assigned to `frames` must be numerical, the generator function was built in a way in which it adds one to variable `a` (here the number of frames), each time the smallest value within the environment is still greater than 0. 

```
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

animation = animation.FuncAnimation(fig, update, frames = gen_function(), repeat=False)
```

[Go back to top](#pagetop)
