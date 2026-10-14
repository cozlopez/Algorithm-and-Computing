from typing import Callable, TypeVar, List, Tuple, Dict

from path_finding import dijkstra, a_star

# These constants are used to represent the different types of robots and resources
# You can use these constants to index into the lists that represent the state of the factory
# Ex: state.robots[IRON] or self.robots[IRON] would give you the number of iron robots in the factory
# Ex: state.resources[IRON] or self.resources[IRON] would give you the number of iron resources in the factory
IRON: int = 0
COPPER: int = 1
SILICON: int = 2
URANIUM: int = 3

# This is a dictionary that maps the names of the robots to the index of the robot in the list
# Ex: ROBOT_NAMES_TO_INDICES['ironRobot'] would give you 0
# By using this dictionary, you can refer to the robots by name instead of by index
ROBOTS_NAME_TO_INDICES: Dict[str, int] = {
    'ironRobot': IRON,
    'copperRobot': COPPER,
    'siliconRobot': SILICON,
    'uraniumRobot': URANIUM
}


class Factory:
    # add your constructor and the other methods here
    def __init__(self,blueprint:(Dict[str, List[int]]),robots :(List[int]),resources:(List[int]),step:(int)=0) -> None:
        self.robots=robots
        self.blueprint=blueprint
        self.resources=resources
        self.step=step
        
        
    def __lt__(self, other) -> bool:
        return True

    def __eq__(self, other) -> bool:
        return True

    def __hash__(self) -> int:
        h = hash(str(self.resources) + str(self.robots) + str(self.step))
        return h

    def __repr__(self):
        return f'Factory(robots={self.robots}, resources={self.resources}, step={self.step})'
    
    def can_build_robot(self,bottype:str):
        
        if bottype in self.blueprint:
            bluelist=self.blueprint[bottype]
            print(bluelist)
            print(self.resources)
            count=0
            for i in range(len(self.resources)):
                if not(self.resources[i]>=bluelist[i]):
                    count+=1
                    break
                
            if count==0:
                return True
            
            else:
                return False
    
    def produce_robot(self,robot:str):
        
        if robot in self.blueprint:
            bluelist=self.blueprint[robot]
            count=0
            for i in range(len(self.resources)):
                if not(self.resources[i]>=bluelist[i]):
                    count+=1
                    break
            newresource=[]
            newrobot=[]
            if count==0:
    
                for i in range(len(self.resources)):
                    newresource.append(self.resources[i]-bluelist[i])
                if robot=='ironRobot':
                    for i in range(len(self.robots)):
                        x=[1,0,0,0]
                        newrobot.append(self.robots[i]+x[i])
                elif robot=='copperRobot':
                    for i in range(len(self.robots)):
                        x=[0,1,0,0]
                        newrobot.append(self.robots[i]+x[i])
                elif robot=='siliconRobot':
                    for i in range(len(self.robots)):
                        x=[0,0,1,0]
                        newrobot.append(self.robots[i]+x[i])
                elif robot=='uraniumRobot':
                    for i in range(len(self.robots)):
                        x=[0,0,0,1]
                        newrobot.append(self.robots[i]+x[i])
                        
                blueprint=self.blueprint
                newfac=Factory(blueprint,newresource,newrobot,1)
                    
                return newfac
            else:
                return None
            


def get_neighbors(state: Factory) -> List[Tuple[Factory, float]]:
    return [(state, 1.0)]


if __name__ == "__main__":
    # You can test your implementation here
    blueprint1 = {
    'ironRobot': [2, 0, 0, 0],
    'copperRobot': [4, 0, 0, 0],
    'siliconRobot': [2, 2, 0, 0],
    'uraniumRobot': [3, 2, 2, 0]}

    robots = [1, 0, 0, 0]
    resources = [2, 0, 0, 0]

    my_factory = Factory(blueprint1, robots, resources)
    print(my_factory.can_build_robot('ironRobot'))
    print(my_factory.produce_robot('ironRobot'))
    
    

