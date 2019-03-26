# Empty-space-finder
Find the space where distances to all employees is minimal.
The distance from an empty space to an employee is the shortest path from the employee to the empty space.
Employees can only walk in x,y (no diagonals).
Employees can't walk through wall or other employees.

Given a building floor map like:

    WWWWWWWWWWWWW
    W E   W E   W
    W     W     W
    W           W
    W     W     W
    W E   W E   W
    WWWWWWWWWWWWW

 __Properties__
* W - wall
* E - employee
* [SPACE] - empty space

The place needs to be located in the empty space for which the sum of distances to all employees is minimal.

Usage
=====

Run `layoutmapping.py` or `kitchenmapping.py`

## Notes
This was my first time writing a python program so it's not an optimal solution to the problem.


I think `layoutmapping.py` is the more efficent solution but it will fail to find the best spot in certain maps such as:

    WWW
    WEW
    W W
    W W
    W WWWWWWWWWW
    W         EW
    WWWWWWWWWWWW

`kitchenmapping.py` should find the correct spot in such maps but I didn't validate the path as much as I wrote it quikcly only to see if I can find the solution that 'layoutmapping.py' didn't:
* Employees can walk through each other
* Not all employees must reach the spot
* Spot validation can be off as I check for employees x,y instead of distance

Python 3.7.2
