import itertools
import math


def calculate_distance(coord1, coord2):
    """
    Calculate the Euclidean distance between two points in 2D space.

    Args:
        coord1 (tuple): The coordinates (x, y) of the first point.
        coord2 (tuple): The coordinates (x, y) of the second point.

    Returns:
        float: The Euclidean distance between the two points.
    """

    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)


def optimize_vrp(depot, customers, vehicle_capacity, num_vehicles):
    """
    Optimize the Vehicle Routing Problem to minimize total travel distance using Brute Force.

    Args:
        depot (tuple): The coordinates (x, y) of the depot, where the vehicles start and end their routes.
        customers (list of tuple): A list of tuples representing the coordinates (x, y) of each customer location.
        vehicle_capacity (int): The maximum capacity of each vehicle.
        num_vehicles (int): The number of vehicles available in the fleet.

    Returns:
        list: A list of routes, where each route represents the sequence of customer locations visited by a single vehicle.
    """
    best_distance = float('inf')
    best_routes = None
    c = len(customers)
    ind_customers = list(range(c))

    for permutation in itertools.permutations(ind_customers):
        routes = []
        route = []
        count = 0
        for idx in permutation:
            if count < vehicle_capacity:
                route.append(idx)
                count += 1
            else:
                routes.append(route)
                route = [idx]
                count = 1
        if route:
            routes.append(route)

        if len(routes) > num_vehicles:
            continue

        total_distance = 0

        for r in routes:
            previous = depot
            for idx in r:
                total_distance += calculate_distance(previous, customers[idx])
                previous = customers[idx]
            # total_distance += calculate_distance(previous, depot)

        if total_distance < best_distance:
            best_distance = total_distance
            best_routes = routes

    result = []

    for route in best_routes:
        converted_route = []
        for i in route:
            converted_route.append(customers[i])
        result.append(converted_route)


    return result

# Example usage:
depot_location = (0, 0)
customer_locations = [(1, 3), (3, 5), (4, 8), (9, 6), (7, 1), (2, 4)]
capacity_per_vehicle = 3
number_of_vehicles = 2

optimized_routes = optimize_vrp(depot_location, customer_locations, capacity_per_vehicle, number_of_vehicles)
print(optimized_routes)
