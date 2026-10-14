from robots import Factory, get_neighbors
from path_finding import a_star, dijkstra

BLUEPRINT = {
    'ironRobot': [2, 0, 0, 0],
    'copperRobot': [4, 0, 0, 0],
    'siliconRobot': [3, 3, 0, 0],
    'uraniumRobot': [2, 4, 3, 0]
}
ROBOTS = [1, 0, 0, 0]
RESOURCES = [2, 0, 0, 0]


def test_factory_constructor():
    factory = Factory(BLUEPRINT, ROBOTS, RESOURCES)
    assert factory.robots == ROBOTS
    assert factory.resources == RESOURCES
    assert factory.blueprint == BLUEPRINT
    assert factory.step == 0


def test_factory_copy_list():
    robots = ROBOTS.copy()
    factory = Factory(BLUEPRINT, robots, RESOURCES)
    robots[0] = 10
    assert factory.robots == [1, 0, 0, 0]


def test_factory_comparison():
    factory1 = Factory(BLUEPRINT, ROBOTS, RESOURCES)
    factory2 = Factory(BLUEPRINT, ROBOTS, RESOURCES)
    factory3 = Factory(BLUEPRINT, ROBOTS, [0, 0, 0, 1])
    assert factory1 == factory2
    assert factory1 != factory3
    assert factory1 < factory3
    assert hash(factory1) == hash(factory2)


def test_factory_can_build_robot():
    factory = Factory(BLUEPRINT, ROBOTS, [0, 0, 0, 0])
    assert not factory.can_build_robot('ironRobot')
    assert not factory.can_build_robot('copperRobot')
    assert not factory.can_build_robot('siliconRobot')
    assert not factory.can_build_robot('uraniumRobot')
    factory.resources = [2, 1, 1, 1]
    assert factory.can_build_robot('ironRobot')
    assert not factory.can_build_robot('copperRobot')
    assert not factory.can_build_robot('siliconRobot')
    assert not factory.can_build_robot('uraniumRobot')
    factory.resources = [4, 3, 3, 3]
    assert factory.can_build_robot('ironRobot')
    assert factory.can_build_robot('copperRobot')
    assert factory.can_build_robot('siliconRobot')
    assert not factory.can_build_robot('uraniumRobot')
    factory.resources = [2, 4, 3, 3]
    assert factory.can_build_robot('ironRobot')
    assert not factory.can_build_robot('copperRobot')
    assert not factory.can_build_robot('siliconRobot')
    assert factory.can_build_robot('uraniumRobot')


def test_factory_produce_robot():
    factory = Factory(BLUEPRINT, ROBOTS, [2, 0, 0, 0])
    f2 = factory.produce_robot('ironRobot')
    assert f2.robots == [2, 0, 0, 0]
    assert f2.resources == [0, 0, 0, 0]
    assert f2.step == 1
    f3 = f2.produce_robot('ironRobot')
    assert f3 is None

    factory = Factory(BLUEPRINT, [2, 1, 1, 1], [2, 4, 3, 0], 8)
    f2 = factory.produce_robot('uraniumRobot')
    assert f2.robots == [2, 1, 1, 2]
    assert f2.resources == [0, 0, 0, 0]
    assert f2.step == 9


def test_factory_gather_resources():
    factory = Factory(BLUEPRINT, [2, 1, 1, 1], [2, 4, 3, 0], 8)
    f2 = factory.gather_resources()
    assert f2.resources == [4, 5, 4, 1]
    assert f2.robots == [2, 1, 1, 1]
    assert f2.step == 9

    factory = Factory(BLUEPRINT, [0, 0, 0, 0], [2, 4, 3, 0], 8)
    f2 = factory.gather_resources()
    assert f2.robots == [0, 0, 0, 0]
    assert f2.resources == [2, 4, 3, 0]
    assert f2.step == 9


def test_get_neighbors():
    blueprint = {
        'ironRobot': [2, 0, 0, 0],
        'copperRobot': [4, 0, 0, 0],
        'siliconRobot': [2, 2, 0, 0],
        'uraniumRobot': [3, 2, 2, 0]
    }
    robots = [2, 0, 0, 0]
    resources = [3, 3, 3, 0]
    my_factory = Factory(blueprint, robots, resources, 15)  # 15 minutes spent
    neighbors = list(sorted(get_neighbors(my_factory), key=lambda x: x[0].robots + x[0].resources))

    assert len(neighbors) == 4
    assert neighbors == [
        (Factory(blueprint, [3, 0, 0, 0], [1, 3, 3, 0], 16), 1),  # create an iron robot
        (Factory(blueprint, [2, 0, 1, 0], [1, 1, 3, 0], 16), 1),  # create a copper robot
        (Factory(blueprint, [2, 0, 0, 1], [0, 1, 1, 0], 16), 1),  # create a uranium robot
        (Factory(blueprint, [2, 0, 0, 0], [5, 3, 3, 0], 16), 1),  # gather resources
    ]


def test_compare_factories():
    f1 = Factory(BLUEPRINT, [1, 0, 0, 0], [0, 0, 0, 0], 1)
    f2 = Factory(BLUEPRINT, [0, 0, 0, 0], [0, 0, 0, 5], 8)
    assert f1 < f2
    assert f1 != f2
    assert f1 == f1
    assert not f2 < f1


def test_heuristic():
    from robots import heuristic

    f1 = Factory(BLUEPRINT, [1, 0, 0, 0], [0, 0, 0, 0], 1)
    f2 = Factory(BLUEPRINT, [0, 0, 0, 0], [0, 0, 0, 5], 8)

    assert heuristic(f1, f2) == 5
    assert heuristic(f2, f1) == 5
    assert heuristic(f1, f1) == 0
    assert heuristic(f2, f2) == 0


def test_dijkstra():
    factory = Factory(BLUEPRINT, ROBOTS, RESOURCES)
    goal = Factory(BLUEPRINT, [0, 0, 0, 0], [0, 0, 0, 3])
    path = dijkstra(get_neighbors, factory, goal)
    assert path is not None
    assert path[-1] == goal
    assert len(path) == 16


def test_a_star():
    from src.robots import heuristic
    factory = Factory(BLUEPRINT, ROBOTS, RESOURCES)
    goal = Factory(BLUEPRINT, [0, 0, 0, 0], [0, 0, 0, 3])
    path = a_star(get_neighbors, factory, goal, heuristic)
    assert path is not None
    assert path[-1] == goal
    assert len(path) == 16
