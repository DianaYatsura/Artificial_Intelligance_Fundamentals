import pulp


def optimize_inventory_management(demand, holding_cost, ordering_cost, initial_inventory, reorder_point):
    """
    Optimize inventory levels using Linear Programming.

    This function uses Linear Programming to determine the optimal inventory levels for each period in the planning
    horizon. The goal is to minimize the total cost of inventory while meeting the demand and inventory requirements.

    Args:
        demand (list): A list representing the demand for each period.
        holding_cost (float): The cost of holding one unit of inventory for one period.
        ordering_cost (float): The cost of placing an order for a fixed quantity of inventory.
        initial_inventory (int): The initial inventory level at the beginning of the planning horizon.
        reorder_point (int): The inventory level at which a new order should be placed to avoid stockouts.

    Returns:
        list: A list representing the optimal inventory levels for each period.
    """
    periods = len(demand)

    optimization = pulp.LpProblem("Inventory_Management_Optimization", pulp.LpMinimize)

    inventory = pulp.LpVariable.dicts("Inventory", range(periods), lowBound=0)
    order_quantity = pulp.LpVariable.dicts("OrderQty", range(periods), lowBound=0)


    cost_terms = []
    for t in range(periods):
        term = holding_cost * inventory[t] + ordering_cost * order_quantity[t]
        cost_terms.append(term)

    total_cost = 0
    for term in cost_terms:
        total_cost += term

    optimization += total_cost

    optimization += inventory[0] == initial_inventory

    for t in range(1, periods):
        optimization += inventory[t] >= demand[t] + order_quantity[t] - inventory[t - 1]

    optimization.solve()

    result = []
    for t in range(periods):
        value = pulp.value(inventory[t])
        result.append(int(value))

    return result

# Example usage:
demand_forecast = [10, 20, 15, 25, 30]
holding_cost_per_period = 1.5
ordering_cost_per_order = 25.0
initial_inventory_level = 50
reorder_point_level = 50

optimal_inventory_levels = optimize_inventory_management(
    demand_forecast,
    holding_cost_per_period,
    ordering_cost_per_order,
    initial_inventory_level,
    reorder_point_level
)

print("Optimal Inventory Levels:", optimal_inventory_levels)
