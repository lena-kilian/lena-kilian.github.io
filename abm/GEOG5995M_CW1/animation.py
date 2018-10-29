import random
from matplotlib import pyplot
from matplotlib import animation
import agent_framework
import csv
import time

n = 100   # number of agents
k = 200 # number of iterations
neighbourhood = 20

environment = []
with open('in_example.txt', newline='\n') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        environment.append(row)

agents = []
while len(agents) < n:
    agents.append(agent_framework.Agents(environment, agents))
    
# defining the figure
fig = pyplot.figure(figsize=(8, 8))

# defining the functions
def update(frame_number):
    # makes agents eat, share, move and displays the chart
    fig.clear()
    pyplot.imshow(environment)
    pyplot.ylim(0, 100)
    pyplot.xlim(0, 100)
    random.shuffle(agents) # shuffles the order in which agents are moved, receive resources, etc. --> important for share function
    agents[0].grass_grow() # has to be outside so that it doesn't grow after each inididual agent moved
    for i in range(len(agents)):
        agents[i].eat()
        agents[i].regurgitate()
        agents[i].share(neighbourhood)
        agents[i].moveagent()
    for i in range(len(agents)):
        pyplot.scatter(agents[i].x_position, agents[i].y_position, color='white', s=10)

def gen_function(b = [0]):
    # stops the agents once the grass is eaten up in one spot
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
'''
animation = animation.FuncAnimation(fig, update, frames = k, repeat=False) # uses number of iterations (k) for stoping 
'''
