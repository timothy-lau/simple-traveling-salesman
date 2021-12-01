# Required Additional Libraries
matplotlib (2.2.2)
pyfiglet (0.8.post1)

# Traveling Salesman

A simplified version of the travelling salesman problem.


## General idea of the project

Suppose there are a number of "cities", as in shown in Figure 1:

![Figure 1, Cities](https://www.dcs.bbk.ac.uk/~vlad/pub/pop1/proj/Figure1.png)



The distance between any two cities with the coordinates (x1, y1) and (x2,y2) is
 the standard Euclidean distance, that is, 

sqrt((x1-x2)^2 + (y1-y2)^2)

Thus, we assume that the Earth is "flat" for the purposes of this assignment.
A traveling salesman wishes to visit every city exactly once, 
then return to their starting point. (It doesn't matter what city is 
the starting point.) Such a path is called a *circuit*, 
as in Figure 2:

![Figure 2. A circuit](https://www.dcs.bbk.ac.uk/~vlad/pub/pop1/proj/Figure2.png)

However, the salesman also wishes to minimise the total distance that 
must be travelled.

This is a classic computer science problem, known as the 
**Traveling Salesman problem**. You can find algorithms for 
finding reasonably good solutions on the web, and you are welcome to look 
at those algorithms. However, we want you use a *hill climbing& approach, 
where you start with "any" solution, and try to progressively improve 
it until you can't improve it any more.

## Specific requirements

### Data representation

`city-data.txt` contains the 
latitudes and longitudes of the fifty state capitals of the U.S.A. 
Each line contains:
- the name of the state, 
- the name of the city, 
- the latitude, and 
- the longitude. 

These four items are separated by **tabs** (\t symbol). 
Read this file in as a list of four-tuples.
The list tuples will be referred to as a *"road map"*. 
It represents the path the salesman follows, starting with the 
first city in the list and ending back at the first city in the list.
You can assume that the format of the input file as above. 

Note however that the file name as well as its contents can be arbitrary (e.g., 
it can be a file `Brazil.txt` with the info on Brazilian states/cities).

While we will require these particular data representations as 
function parameters and function results, this does not imply that 
you have to work with these representations as you solve the problems.
What you do inside the functions is up to you, as long as they work as expected.
