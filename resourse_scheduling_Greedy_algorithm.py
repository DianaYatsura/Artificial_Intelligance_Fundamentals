
def schedule_tasks(tasks, resources, deadline):
    """
    Optimize resource scheduling to complete tasks within the given deadline using Greedy Scheduling.

    Args:
        tasks (list of tuple): A list of tasks, where each tuple contains (task_name, duration, resource_requirements).
        resources (dict): A dictionary representing available resources and their capacities.
                          Keys are resource names, and values are their capacities.
        deadline (float): The maximum time (deadline) within which all tasks must be completed.

    Returns:
        dict: A dictionary representing the optimal assignment of tasks to resources.
              The keys are resource names, and the values are lists of tasks assigned to each resource.
              The dictionary also includes the completion time for each task.
              Example: {'Resource1': ['TaskA', 'TaskB'], 'Resource2': ['TaskC'], 'TaskA': 4.5, 'TaskB': 7.2, 'TaskC': 5.0}
    """
  #initialization
    assigned_tasks = {}
    task_times = {}
    current_time = {}

    for r in resources:
        current_time[r] = 0.0

    for resource in resources.keys():
        assigned_tasks[resource] = []
        print(f'Assigned_tasks', assigned_tasks)

    # Sort tasks in ascending order of their durations
    tasks_sorted = sorted(tasks, key=lambda t: t[1])
    print(f'Tasks_sorted', tasks_sorted)

    # Sort resources in ascending order of their remaining capacities
    resources_sorted = sorted(resources.items(), key=lambda r: r[1])
    print(f'Resources_sorted', resources_sorted)

    for task, duration, requirement in tasks_sorted:
        finish_times = []

    # Assign task to the resource
    # Update resource capacities

        for resource, capacity in resources_sorted:
            if resource in requirement:
                if current_time[resource] + duration > deadline:
                    continue

                assigned_tasks[resource].append(task)
                current_time[resource] += duration
                finish_times.append(current_time[resource])
                print(f'Assigned_tasks', assigned_tasks)

        if not finish_times:
            continue

        task_times[task] = max(finish_times)

    return {**assigned_tasks, **task_times}

# Example usage:
tasks_list = [
    ('TaskA', 4.5, {'Resource1': 2, 'Resource2': 1}),
    ('TaskB', 7.2, {'Resource2': 3}),
    ('TaskC', 5.0, {'Resource1': 1})
]

resources_dict = {'Resource1': 10, 'Resource2': 15}

deadline_time = 12.0

result = schedule_tasks(tasks_list, resources_dict, deadline_time)
print(result)

