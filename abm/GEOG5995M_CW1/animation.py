import random
from matplotlib import pyplot
from matplotlib import animation
import agent_framework
import csv
import time

n = 100   # number of agents
k = 200 # number of iterations
neighbourhood = 20

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
    pyplot.ylim(0, 300)
    pyplot.xlim(0, 300)
    
    random.shuffle(agents) # shuffles the agents' order; important for share function to ensure that averages are not always calculated in the same order of agent pairs
    agents[0].grass_grow() # has to be outside so that it doesn't grow after each inididual agent moved
    
    for i in range(len(agents)):
        agents[i].eat()
        agents[i].regurgitate()
        agents[i].share(neighbourhood)
        agents[i].moveagent()
        
    for i in range(len(agents)):
        pyplot.scatter(agents[i].x_position, agents[i].y_position, color='white', s=5)

# stops the agents once the grass is eaten up in one spot
def gen_function(b = [0]):
    start = time.time()
    a = 0
    env_list = []
    while True:
        '''
        # adding this bit will save a picture at each iteration
        fname = '_tmp%5d.png' % a
        print('Saving frame', fname)
        pyplot.savefig(fname)
        '''
        for i in range(len(environment)):
            env_list.append(min(environment[i]))
        if min(env_list) > 0:
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
