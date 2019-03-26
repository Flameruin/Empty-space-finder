# Finds if a path is possible  from end to start.
def init_kitchen_path(graph, start, end, visited=[]):
    visited += [start]
    if start == end:
        return True
    for node in graph[start]:
        if node not in visited:
            init_kitchen_path(graph, node, end, visited)
    if end in visited:
        return True
    else:
        return False


# After initial path found it's enough to reach the old path.
def kitchen_path(start, end, oldvisited, visited=[]):
    visited += [start]
    oldvisited += [start]
    if start == end:
        return True
    for node in graph[start]:
        if node not in oldvisited:
            kitchen_path(node, end, oldvisited, visited)
        else:
            return True
    if end in visited:
        return True
    else:
        return False


def check_kitchen_placement(graph, placement, spacechar):
    visited = []
    for e in employees_coordinates:
        # First path init is from employee to placement.
        if len(visited) == 0:
            if(not init_kitchen_path(graph, e, placement, visited)):
                return False
        # In case employee was visited no need to check him again.
        elif e not in visited:
            newvisited = []
            # After initial path was made it's enough to connect to it.
            # Checking path form employee to placement or previous path.
            if(not kitchen_path(e, placement, visited, newvisited)):
                return False
    return True


# Convert map to movement graph.
def map_to_graph(map):
    graph = {}
    x, y = 0, 0
    for key, val in mapping.items():
        if val != 'W':
            graph.setdefault(key, [])
            x, y = key[0], key[1]
            if (x, y-1) in map and map[(x, y-1)] == ' ':
                graph[key].append((x, y-1))
            if (x, y+1) in map and map[(x, y+1)] == ' ':
                graph[key].append((x, y+1))
            if (x-1, y) in map and map[(x-1, y)] == ' ':
                graph[key].append((x-1, y))
            if (x+1, y) in map and map[(x+1, y)] == ' ':
                graph[key].append((x+1, y))
    return graph


# Maps the floorplan.
def layout(floorplan):
    mapped = {}
    x, y = 0, 0

    for i in floorplan:
        if i != '\n':
            mapped[(x, y)] = i
            y += 1

        elif i == '\n':
            y = 0
            x += 1

    return mapped


# Custom exception class.
class ZeroEmployees(Exception):
    """Raised when employees are found."""
    pass


# Floor layout depiction in rows and columns.
# k = average 'E' coordinante (3, 5).
"""
  0123456789101112
0 WWWWWWWWWWWWW
1 W E   W E   W
2 W     W     W
3 W    K      W
4 W     W     W
5 W E   W E   W
6 WWWWWWWWWWWWW

WWWWWWWWWWWWW
W E  W
W     W
W                     KW
W WWW
W                                         E   W
WWWWWWWWWWWWW

Best placement isn't valid
WWWWWWWWWWWWW
W E  W
W     W
W                     KW
W WWW
W            E                             E   W
WWWWWWWWWWWWW

WWWWWWWWWWWWW
W E  W
W     W
W                     KW
WWWWWWWWWWWWWW
W     E   W
WWWWWWWWWWWWW
"""

# Opens and captures the files content in a variable.
with open('wall_space_employee.txt', 'r') as floormap:
    a = floormap.read()


# Captures the function's return value in a variable.
mapping = layout(a)
# for i in mapping:
#     print(i, mapping[i])
nx, ny = [], []


try:
    employees_coordinates = [i for i in mapping if mapping[i] == 'E']

    if len(employees_coordinates) > 0:
        for i in employees_coordinates:
            nx.append(i[0])
            ny.append(i[1])

        print(f'Employee Coordinates: {[i for i in employees_coordinates]}')
        # Average between all employees is the place where kitchen should be.
        avg = (sum(nx) // len(nx), sum(ny) // len(ny))
        print(f'Average Coordinate: {avg}')

        can_place_kitchen = False
        # Checks if the placement is an open space.
        if avg in mapping and mapping[avg] == ' ':
            # Creates a graph for legal moves of employees
            graph = map_to_graph(mapping)
            # Checks if employees can reach kitchen placement.
            # Captures the function's return value in a variable.
            can_place_kitchen = check_kitchen_placement(graph, avg, ' ')
        # Prints if the kitchen can be placed at best coordinantes
        if(can_place_kitchen):
            print(f'kitchen can be placed at: {avg}')
        else:
            print(f"kitchen can't be placed at: {avg}")
    # Raised exception if there are no employees
    elif len(employees_coordinates) == 0:
        raise ZeroEmployees

except ZeroEmployees:
    print('No Employees Found. No kitchen needed.')
