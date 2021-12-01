import csv
import math
import random
import os
import matplotlib.pyplot as plt
import pyfiglet


class TSP:

    def __init__(self, n=10000, init_input=True):
        print(pyfiglet.figlet_format('POP TSP', font="slant"))

        # Prompt user input when set to True, False for pytest to be able to run
        if init_input:
            # Initiate user input for the file
            self.file_path = str(
                input('Please enter the file name to read in. (Defaulted to city-data.txt, Press enter '
                      'to continue.)'))
            if self.file_path == '':
                self.file_path = 'city-data.txt'

            while not os.path.exists(self.file_path):
                self.file_path = str(input('The file name ' + self.file_path + ' was not found in the same directory. '
                                                                               'Please check the file name and try '
                                                                               'again.'))

        self.total_distance = 0
        self.iterations_n = n

    def read_cities(self, file_name):
        """
        Read in the cities from the given `file_name`, and return
        them as a list of four-tuples:

          [(state, city, latitude, longitude), ...]

        Use this as your initial `road_map`, that is, the cycle

          Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.

        Args:
            file_name (text file): File name to read in

        Return:
            List : Contains a list of tuples in the following format of eg. [(state, city, latitude, longitude), ...]
        """
        # Read in text file
        print('Reading in ' + file_name + '...')
        with open(file_name, 'r') as f:
            raw = csv.reader(f, delimiter='\t')
            # Mapping data into list of 4-tuples
            data_list = [tuple([row[0], row[1], float(row[2]), float(row[3])]) for row in raw]
        return data_list

    def print_cities(self, road_map):
        """
        Prints a list of cities, along with their locations.
        Print only one or two digits after the decimal point.

        Args:
            road_map (List): List of tuples each with city names and their attributes

        Return:
            List: Prints a list of cities, along with their locations. Print only one or two digits after the decimal point.
        """
        print('State City Latitude Longitude')
        for city in road_map:
            print(' '.join([city[0],
                            city[1],
                            str(round(city[2], 2)),
                            str(round(city[3], 2))
                            ]))
        print('\n')

    def calc_distance(self, x1, y1, x2, y2):
        """
        Method to calculate 2d distance

        Args:
            x1 (Float): Longitude of city 1
            y1 (Float): Longitude of city 1
            x2 (Float): Longitude of city 2
            y2 (Float): Longitude of city 2

        Return:
            Float: The distance between the two cities
        """
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def compute_city_distance(self, road_map):
        """
        Method to compute the distance between each of the cities and return as a list.

        Args:
            road_map (List): List of tuples each with city names and their attributes

        Return:
            List: Distances of floats between each of the cities in the road map
        """
        # Initialise list variable and previous_city variable
        distance_list = []
        prev_city = ['', '', 0.0, 0.0]
        for city in road_map:
            # calculate the distance between each cities and append into the list above
            distance_list.append(self.calc_distance(city[3], city[2], prev_city[3], prev_city[2]))
            prev_city = city
        # Removing first element as first element is variable prev_city with empty values
        distance_list.pop(0)
        # Calculating distance from the last city back to the starting city
        first_elem, last_elem = road_map[0], road_map[-1]
        distance_list.append(self.calc_distance(last_elem[2], last_elem[3], first_elem[2], first_elem[3]))
        return distance_list

    def compute_total_distance(self, road_map):
        """
        Returns, as a floating point number, the sum of the distances of all
        the connections in the `road_map`. Remember that it's a cycle, so that
        (for example) in the initial `road_map`, Wyoming connects to Alabama...

        Args:
            road_map (List): List of tuples each with city names and their attributes

        Return:
            Float: the sum of the distances of all the connections in the `road_map`
        """
        distance_list = self.compute_city_distance(road_map)
        return sum(distance_list)

    def swap_cities(self, road_map, index1, index2):
        """
        Take the city at location `index` in the `road_map`, and the
        city at location `index2`, swap their positions in the `road_map`,
        compute the new total distance, and return the tuple

            (new_road_map, new_total_distance)

        Allow for the possibility that `index1=index2`,
        and handle this case correctly.

        Args:
            road_map (List): List of tuples each with city names and their attributes
            index1 (Int): Index in the list to swap with index2
            index2 (Int): Index in the list to sawp with index1

        Returns:
            Tuple: List of tuples each with city names and their attributes after the index change,
            and a total distance
        """
        road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
        return tuple([road_map, self.compute_total_distance(road_map)])

    def shift_cities(self, road_map):
        """
        For every index i in the `road_map`, the city at the position i moves
        to the position i+1. The city at the last position moves to the position
        0. Return the new road map.

        Args:
            road_map (List): List of tuples each with city names and their attributes

        Returns:
            List: List of tuples each with city names and their attributes after the index change
        """
        # Creating a copy of the variable without modifying the original
        temp_road_map = road_map.copy()

        # Removing the last element of the list and put it at the start of the list
        shifted_road_map = [tuple(temp_road_map.pop())] + temp_road_map
        return shifted_road_map

    def find_best_cycle(self, road_map):
        """
        Using a combination of `swap_cities` and `shift_cities`,
        try `10000` swaps/shifts, and each time keep the best cycle found so far.
        After `10000` swaps/shifts, return the best cycle found so far.
        Use randomly generated indices for swapping.

        Args:
            road_map (List): List of tuples each with city names and their attributes

        Return:
            List: List of tuples each with city names and their attributes after optimising routes
        """
        n = 0
        max_len = len(road_map) - 1
        while n < self.iterations_n:

            # Shift road map
            shifted_road_map = self.shift_cities(road_map)

            # Initiate index variables for while statement
            rand_index1 = 0
            rand_index2 = 0

            # To avoid situation where index1 = index2
            while rand_index1 == rand_index2:
                rand_index1 = random.randint(0, max_len)
                rand_index2 = random.randint(0, max_len)

            # Swap cities randomly
            road_map_dist_tup = self.swap_cities(shifted_road_map, rand_index1, rand_index2)

            # If distance after swapping is less than original, replace original route
            if road_map_dist_tup[1] < self.total_distance:
                self.total_distance = road_map_dist_tup[1]
                road_map = road_map_dist_tup[0]

            n += 1
        return road_map

    def print_map(self, road_map):
        """
        Prints, in an easily understandable format, the cities and
        their connections, along with the cost for each connection
        and the total cost.

        Args:
            road_map (List): List of tuples each with city names and their attributes
        """
        # Returning a list of distances
        dist_list = self.compute_city_distance(road_map)

        # Combining list of distances and the road map and map it into a printable format
        # eg. 1) city_1 (2.1) ->  2) city_2 (2.44)
        city_dist = [str(n) + ') ' + city[0] + ' (' + str(round(distance, 2)) + ') -> '
                     for city, distance, n in zip(road_map, dist_list, range(1, len(road_map) + 1))]

        print('Road Map After Optimising (City and cost between each connection)')
        print(' '.join(city_dist), '1) ', road_map[0][0])
        print('\n')

    def visualise(self, road_map, total_distance):
        """
        Plots the road map visualising the route for travelling between the cities.
        City highlighted in dark blue indicating the first stop and
        dark purple indicating the last stop

        Args:
            road_map (List): List of tuples each with city names and their attributes
            total_distance (Float): Current total cost of the route
        """
        # Appending Longitude and Latitude for each city in the road map
        x = []
        y = []
        for i in road_map:
            x.append(i[3])
            y.append(i[2])

        # Connecting the last city back to the first city
        x.append(road_map[0][3])
        y.append(road_map[0][2])

        plt.figure(figsize=(13, 7))
        plt.plot(x, y, '-ok', alpha=0.4, color='lightskyblue')
        plt.xlabel(('Longitude'))
        plt.ylabel(('Latitude'))
        plt.title('Travelling Salesman Optimised Road-map with Total Distance of {}'.format(total_distance))

        n = 1
        for i in road_map:
            city_label = ''.join([str(n), '). ', i[0]])
            # Adjusting different font properties for start and end city
            if i == road_map[0]:
                plt.text(i[3], i[2], city_label, fontdict={'color': 'darkblue',
                                                           'size': 8, 'alpha': 0.8,
                                                           'weight': 'bold'})
            elif i == road_map[-1]:
                plt.text(i[3], i[2], city_label, fontdict={'color': 'darkviolet',
                                                           'size': 8, 'alpha': 0.8,
                                                           'weight': 'bold'})
            else:
                plt.text(i[3], i[2], city_label, fontdict={'color': 'indigo',
                                                           'size': 8,
                                                           'alpha': 0.7})
            n += 1
        plt.show()

    def main(self):
        """
        Reads in, and prints out, the city data, then creates the "best"
        cycle and prints it out.
        """
        # Read in text file
        road_map = self.read_cities(self.file_path)
        # Print original road map
        self.print_cities(road_map)

        # Compute initial distance
        self.total_distance = self.compute_total_distance(road_map)
        # Prints initial distance
        print('Initial distance is {}\n'.format(str(round(self.total_distance, 2))))

        # Run find best cycle
        print('Proceeding with {} iterations.'.format(self.iterations_n))
        print('Optimising best cycle...')
        road_map = self.find_best_cycle(road_map)

        # Prints final
        self.print_map(road_map)
        print('Final distance is {}'.format(str(round(self.total_distance, 2))))

        # Visualise final road map
        self.visualise(road_map, str(round(self.total_distance, 2)))


if __name__ == "__main__":  # keep this in
    tsp = TSP()
    TSP.main(tsp)
