import sys
import copy


def fill_grid(a, count, i, j):
    try:
        if a[i][j-1] != 'W':
            # Left
            if a[i][j-1] == 'E':
                visited_set.add((i, j-1))
            elif (i, j-1) not in visited_set:
                a[i][j-1] += count/2
                visited_set.add((i, j-1))
                fill_grid(a, count+1, i, j-1)
            elif a[i][j-1] > count + gridmap[i][j-1]:
                a[i][j-1] = count + gridmap[i][j-1]/2
                fill_grid(a, count+1, i, j-1)
    except IndexError:
        return None

    try:
        if a[i][j+1] != 'W':
            # Right
            if a[i][j+1] == 'E':
                visited_set.add((i, j+1))
            elif (i, j+1) not in visited_set:
                a[i][j+1] += count/2
                visited_set.add((i, j+1))
                fill_grid(a, count+1, i, j+1)
            elif a[i][j+1] > count + gridmap[i][j+1]:
                a[i][j+1] = count + gridmap[i][j+1]/2
                fill_grid(a, count+1, i, j+1)
    except IndexError:
        return None

    try:
        if a[i-1][j] != 'W':
            # Up
            if a[i-1][j] == 'E':
                visited_set.add((i-1, j))
            elif (i-1, j) not in visited_set:
                a[i-1][j] += count/2
                visited_set.add((i-1, j))
                fill_grid(a, count+1, i-1, j)
            elif a[i-1][j] > count + gridmap[i-1][j]:
                a[i-1][j] = count + gridmap[i-1][j]/2
                fill_grid(a, count+1, i-1, j)
    except IndexError:
        return None

    try:
        if a[i+1][j] != 'W':
            # Down
            if a[i+1][j] == 'E':
                visited_set.add((i+1, j))
            elif (i+1, j) not in visited_set:

                a[i+1][j] += count/2
                visited_set.add((i+1, j))
                fill_grid(a, count+1, i+1, j)
            elif a[i+1][j] > count + gridmap[i+1][j]:
                a[i+1][j] = count + gridmap[i+1][j]/2
                fill_grid(a, count+1, i+1, j)
    except IndexError:
        return None


# Maps the floorplan.
def layout(floorplan, employees_set):
    x, y = 0, 0
    mapped = [[]]
    temporaryLine = []
    for i in floorplan:
        if i != '\n':
            if i == 'E':
                employees_set.add((x, y))
            if i == ' ':
                temporaryLine.append(0)  # float("inf"))'
            else:
                temporaryLine.append(i)
            y += 1
        elif i == '\n':
            mapped.insert(x, temporaryLine)
            temporaryLine = []
            y = 0
            x += 1
    if(len(temporaryLine) > 0):
        mapped.insert(x, temporaryLine)
    return mapped, employees_set


# Custom exception class.
class ZeroEmployees(Exception):
    """Raised when employees are found."""
    pass


def place_kitchen():
    # Finds optimal place to place a kitchen
    try:
        with open("wall_space_employee.txt", "r") as floormap:
            a = floormap.read()

    except Exception as e:
        print(f"{repr(e)}")
        sys.exit(3)

    employees_coordinates = set()
    try:

        global gridmap
        gridmap, employees_coordinates = layout(a, employees_coordinates)
        if len(employees_coordinates) > 0:
            helpermap = [[]]
            for e in employees_coordinates:
                visited_set.clear()
                helpermap = copy.deepcopy(gridmap)
                fill_grid(helpermap, 1, e[0], e[1])
                gridmap = copy.deepcopy(helpermap)

            if len(employees_coordinates - visited_set) == 0:
                nx, ny = [], []
                for i in employees_coordinates:
                    nx.append(i[0])
                    ny.append(i[1])

                # Trying to find median average
                avg = (sum(nx) // len(nx) + sum(ny) // len(ny))/2
                m = float("inf")
                x, y = 0, 0
                for i in gridmap:
                    for cell in i:
                        if not isinstance(cell, str) and avg < cell < m:
                            m = cell
                            kitchen_placement = (x, y)
                        y += 1
                    y = 0
                    x += 1

                print(f'kitchen should be placed at: {kitchen_placement}')
            else:
                print(f'kitchen should be placed at')
        # Raised exception if there are no employees
        elif len(employees_coordinates) == 0:
            raise ZeroEmployees

    except ZeroEmployees:
        print('No Employees Found. No kitchen needed.')


visited_set = set()
gridmap = [[]]
# Main program
place_kitchen()
