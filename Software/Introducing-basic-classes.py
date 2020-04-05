from abc import ABC, abstractmethod # We will use Abstract Base Classes for some of our classes.
import random #For random actuations 
import math  #For finding distance between robots 

class Robot(ABC):
    """
    Robot is the base class for all robot types. Robot class include the 
    base properties of robots such as name, speed, depth of view and
    view angle of the robots.
    
    At the scenarios every event will affact the properties of the robots. Thus, 
    we will build proper interfaces at robots in order to easy use at events.
    """
    
    def __init__(self,name,speed,depth_of_view,view_angle,position = ""):
        """
        Specify the name, speed and the line of sight for the robots.
        """
        self.name = name
        self.speed = speed # That will the instantenous speed of the robot
        self.depth_of_view = depth_of_view # That will the instantenous depth of view of the robot
        self.view_angle = view_angle # That will the instantenous view angle of the robot
        self.type = "Robot"   #Specift the object type
        self.position = position # store the position of the robot

    @abstractmethod  # Create an abstract method to prevent the creation of objects of ABC
    def abstract_method(self):
        pass

class Lion(Robot):
    """
    Lion is one of the robot types. It's name is Lion. Its base speed
    is 5, base depth of view is 5 and view angle is 40 degrees.
    """
    global lion_base_speed           #When a lion created save its default values as global
    global lion_base_depth_of_view
    global lion_base_view_angle
    
    lion_base_speed = 5              #Define default values of lion
    lion_base_depth_of_view = 5
    lion_base_view_angle = 40

    lion_number = 0
    
    def __init__(self):
        super().__init__("Lion",lion_base_speed,lion_base_depth_of_view,lion_base_view_angle,position = "") 
        # Create instantenous stats for lion
        self.base_speed = lion_base_speed # That will store the base speed of the lion
        self.base_depth_of_view = lion_base_depth_of_view # That will store the base depth of view
        self.base_view_angle = lion_base_view_angle # That will store the base view angle
        Lion.lion_number += 1
        self.name = "Lion{0}".format(self.lion_number)
        print("Total number of Lions is {0}.".format(Lion.lion_number))
        
    def __del__(self):
        Lion.lion_number -=1
        print("Total number of Lions is {0}.".format(Lion.lion_number))
        
    def abstract_method(self): # Override abstractmethod to provide creation of objects
        pass

class Deer(Robot):
    """
    Deer is one of the robot types. It's name is Deer. Its base speed
    is 5, depth of view is 4 and view angle is 60 degrees.
    """
    global deer_base_speed           #When a deer created save its base values as global
    global deer_base_depth_of_view
    global deer_base_view_angle
    
    deer_base_speed = 5              #Define base values of deer
    deer_base_depth_of_view = 4
    deer_base_view_angle = 60
    
    deer_number = 0
     
    def __init__(self):
        super().__init__("Deer",deer_base_speed,deer_base_depth_of_view,deer_base_view_angle,position = "") 
        # Create instantenous stats of deer
        self.base_speed = deer_base_speed # That will store the instantenous speed of the Deer
        self.base_depth_of_view = deer_base_depth_of_view # That will store the instantenous depth of view
        self.base_view_angle = deer_base_view_angle # That will store the instantenous view angle        
        Deer.deer_number += 1
        self.name = "Deer{0}".format(Deer.deer_number)
        print("Total number of Deers is {0}.".format(Deer.deer_number))

    def abstract_method(self): # Override abstractmethod to provide creation of objects
        pass
     
    def __del__(self):
        Deer.deer_number -=1
        print("Total number of Deers is {0}.".format(Deer.deer_number))
        
class Grid(ABC):
    """
    Grid is the base class for all grid types. Grid class includes the main
    properties of grids. Grids only affect the specific robot types' speeds. 
    """ 
    def __init__(self,name,lion_speed = '' ,deer_speed = '' ): # One grid may not affect a certain type of robot. Thus
                                                               # Thus, we will remain optional variable for every robot at ABC class.                                 
        self.name = name
        self.lion_speed = lion_speed 
        self.deer_speed = deer_speed
        self.type = "Grid" # Specify the object type

    @abstractmethod  # Create an abstract method to prevent the creation of objects of ABC
    def abstract_method(self):
        pass
    
class Forest(Grid):
    """
    Forest is a grid type.
    It is a good place to hide and run from the predators.
    """
    def __init__(self): 
        super().__init__("Forest",lion_speed = 3 ,deer_speed = 5 )

    def abstract_method(self): # Override abstractmethod to provide creation of objects
        pass

class Savanna(Grid):
    """
    Savanna is a grid type.
    A good place to hunt for some predators.
    """
    def __init__(self):
        super().__init__("Savanna",lion_speed = 6) # Savanna has no effect on deer speed
                                                   # Thus, it will return a string for deer_speed

    def abstract_method(self): # Override abstractmethod to provide creation of objects
        pass

class Random_Actuation(ABC):
    
    """
    Random Actuion is the base class for all actuation types. 
    Actuations may affect the every properties of the Robots.
    They even may change the name of the robot. Actuations basicly depends on possbility if 
    the victim is lucky they shall pass.
    """
    def __init__(self,name,speed_multiplier = '',depth_of_view_multiplier = '', view_angle_multiplier = '' ):
        self.name = name
        self.speed_multiplier = speed_multiplier
        self.depth_of_view_multiplier = depth_of_view_multiplier
        self.view_angle_multiplier = view_angle_multiplier
        self.type = "Random Actuation"
        
    def myopic(actuation_name,robot,depth_of_view_multiplier,possibility):
        """
        For the actuations that will affect the depth of view.
        """
        goodluck = random.randint(0,100)
        
        if goodluck < possibility:
            robot.depth_of_view = robot.depth_of_view * depth_of_view_multiplier
            print("{0} is affected by {2}. Its depth of view multiplied by {1}!".format(robot.name,depth_of_view_multiplier,actuation_name))
            return robot
        else:
            print("{1} effect is not succesful on {0}!".format(robot.name,actuation_name))
            return robot
    
    def hobbler(actuation_name,robot,speed_multiplier,possibility): 
        """
        For the actuations that will affect the speed.
        """
        goodluck = random.randint(0,100)
        
        if goodluck < possibility:
            robot.speed = robot.speed * speed_multiplier
            print("{0} is affected by {2}. Its speed multiplied by {1}!".format(robot.name,speed_multiplier,actuation_name))
            return robot
        else:
            print("{1} effect is not succesful on {0}!".format(robot.name,actuation_name))
            return robot

    def surgery(actuation_name,exposed_robot,transform_robot,possibility):
        """
        For the actuations that will affact the name of the robot.
        A change in the name will also affect all other properties.
        """
        goodluck = random.randint(0,100)
        
        if goodluck < possibility: # Surgery will transform exposed_robot to transform_robot with base stats of transform_robot.
            old_name = exposed_robot.name #Store the old name of exposed_robot
            exposed_robot = transform_robot.__class__() 
            print("{0} is affected by {2}. It's name is now {1}!".format(old_name,exposed_robot.name,actuation_name))
            return exposed_robot
        else:
            print("{1} is not succesful on {0}!".format(exposed_robot.name,actuation_name))
            return exposed_robot
     
    @abstractmethod  # Create an abstract method to prevent the creation of objects of ABC
    def abstract_method(self):
        pass
    
def Thunder(robot):
    """
    Basic Random Actuation method that affects the speed and the depth of view.
    
    Ex: 
        a = Deer()
        a = Thunder(a)
    """
    robot_return = Random_Actuation.myopic("Thunder",robot,0.5,20)  # with a %20 chance myopic will be triggered
    robot_return = Random_Actuation.hobbler("Thunder",robot,0.5,20) # with a %20 change hobbler will be triggered
    return robot_return

def Transformer(robot1,robot2):
    """
    Basic Random Actuation method that affects the name of the robot.
    
    Ex:
        a = Deer()
        b = Lion()
        a = Rainbow(a,b)
    """ 
    #with a 50% change surgery will be triggered
    return Random_Actuation.surgery("Transformer",robot1,robot2,50)
  
class Sensors(ABC):
    """
    This is the main class for the holding values that will be obtained from
    simulations.
    """
    def __init__(self,name):
        self.name = name
        self.type = "Sensor" # Specify the object type

    @abstractmethod  # Create an abstract method to prevent the creation of objects of ABC
    def abstract_method(self):
        pass

class Distance_sensor(Sensors):
    """
    Distance sensor.
    """
    def _init(self):
        super().__init__("DistanceSensor")

    def GetValue(self):
        pass

    def abstract_method(self): # Override abstractmethod to provide creation of objects
        pass    

class Scenario(ABC):
    """
    Main class for the scenarios
    """
    def __init__(self,name,threshold):
        self.name = name
        self.type = "Scenario" # Specify the object type
        self.threshold = threshold # Define specific threshold value for scenarios

    def win_condition(self, target, robot):
        dist = math.sqrt((target.position[0]-robot.position[0])**2
                         + (target.position[1]-robot.position[1])**2)
        
        # Calculate distance and compare it with specified threshold
        if dist < self.threshold:
            global Robot_win
            Robot_win = True #Define a flag to figure out if prey has won or not
            print("{0} has won!".format(robot.name))
        else:
            Robot_win = False #If flag still 'False' after specified time 
                                 #Prey will lost.
            
    @abstractmethod  # Create an abstract method to prevent the creation of objects of ABC
    def abstract_method(self):
        pass

class Prey_Predator(Scenario):
    """
    Prey & Predator game scenario.  If one of the Predator got its Prey then
    it wins the game.
    """        
    def __init__(self,prey,predator,threshold):
        super().__init__("Prey&Predator", threshold)
        self.win_condition(prey,predator)
        
    def abstract_method(self): # Override abstractmethod to provide creation of objects
        pass   

class Search_Rescue(Scenario):
    """
    Search & Rescue game scenario. All robots in the arena should find disabled robots
    in the arena. If one robot find a disabled robot, that disabled robot will join its team.
    At the end of the specified time. Largest group will win.
    """
    def __init__(self,searcher,disabled_robot,threshold):
        super().__init__("Search & Rescue", threshold)
        self.win_condition(searcher,disabled_robot)
        
        if Robot_win:
            disabled_robot.name = searcher.name
        else:
            pass
