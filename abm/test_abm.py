"""
tests for abm: agents_framework.py
"""
import pytest
import mock_framework

   
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


def test_throw_up():
    environment = []
    list = []
    while len(list) < 100:
        list.append(100)
    while len(environment) < 100:
        environment.append(list.copy())
    
    agents = []
    agents.append(mock_framework.Agents(environment, agents))
    
    agents[0].store = 100
    agents[0].throw_up()
    assert agents[0].store == 100 and agents[0].environment[agents[0].y_position][agents[0].x_position] == 100
 
    agents[0].store = 300
    agents[0].throw_up()
    assert agents[0].store == 250 and agents[0].environment[agents[0].y_position][agents[0].x_position] == 150

    
def test_grass_grow():
    environment = []
    list = []
    while len(list) < 100:
        list.append(100)
    while len(environment) < 100:
        environment.append(list.copy())
    environment[5][5] = 600
    environment[2][5] = 254
    
    agents = []
    agents.append(mock_framework.Agents(environment, agents))
    
    agents[0].grass_grow()
    agents[0].grass_grow()
    
    assert environment[1][1] == 102 and environment[5][5] == 600 and environment[2][5] == 255
 
    
def test_distance():
    environment = []
    agents = []
    while len(agents) < 2:
         agents.append(mock_framework.Agents(environment, agents))
    
    agents[0].x_position = 4
    agents[0].y_position = 0
    agents[1].x_position = 0
    agents[1].y_position = 3
    
    dist = agents[0].distance(agents[1])
      
    assert dist == 5


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


def test_max_distance():
    environment = []
    agents = []
    while len(agents) < 3:
         agents.append(mock_framework.Agents(environment, agents))
    
    agents[0].x_position = 37
    agents[0].y_position = 45
    agents[1].x_position = 50
    agents[1].y_position = 0
    
    assert agents[0].max_distance() == 50
      
    agents[2].x_position = 50
    agents[2].y_position = 100
    
    assert agents[0].max_distance() == 100

def test_share():
    environment = []
    agents = []
    while len(agents) < 3:
         agents.append(mock_framework.Agents(environment, agents))
    
    agents[2].x_position = 90
    agents[2].y_position = 90
    
    agents[0].store = 10
    agents[1].store = 0
    
    agents[0].share(10)
    
    assert agents[0].store == 5 #and agents[1].store == 5

pytest.main()  
    
  
  