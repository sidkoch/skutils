from numpy import asarray
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed

def stochastic_hill_climbing(objective_function, variable_range, total_iterations, step_size):
    """
    ----------
    Functionality
    ----------
    This function implements hill climbing optimization algorithm for function optimization

    ----------
    Todos
    ----------
    Create a line plot of the scores to see the relative change in objective function for each improvement
    Create provision for high dimensional objective functions

    ----------
    Parameters
    ----------
    objective_function : 
    variable_range : 
    total_iterations : 
    step_size : 

    ----------
    Returns
    ----------
    current_point : 
    current_objective : 

    """
    total_updates_required = 0
    total_range = variable_range[:,1] - variable_range[:,0]
    current_point = variable_range[:, 0] + (rand(len(variable_range)) * total_range)
    current_objective = objective_function(current_point)
    print("Started at = ",current_point,current_objective)

    for i in range(total_iterations):
        next_point = current_point + (randn(len(variable_range)) * step_size)
        next_objective = objective_function(next_point)
        if next_objective <= current_objective :
            current_point = next_point
            current_objective = next_objective
            print("Moved to = ",i,current_point,current_objective)
            total_updates_required +=1

    print("total_updates_required = ",total_updates_required, " out of iterations = ",total_iterations)
    return [current_point,current_objective]


def objective_function(x):
	return x[0]**2.0


def runner_function():
    seed(42)
    variable_range = asarray([[-5.0, 5.0]])
    n_iterations = 200
    step_size = 0.1
    optimum_point, optimum_objective = stochastic_hill_climbing(objective_function, variable_range, n_iterations, step_size)
    print("Process done = optimum_point, optimum_objective = ", optimum_point, optimum_objective)


runner_function()