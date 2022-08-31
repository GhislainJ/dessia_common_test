"""
Tests for dessia_common.HeterogeneousList class (loadings, check_platform and plots)
"""
import json
import random
import numpy as npy
from matplotlib.pyplot import close as closefig
from dessia_common.models import all_cars_wi_feat
from dessia_common.datatools import HeterogeneousList, CategorizedList

# =============================================================================
# TEST PARETO FRONT
# =============================================================================
# Uniform
coord_1 = [random.uniform(0, 0.1) for i in range(1000)]
coord_2 = [random.uniform(0.9e6, 1e6) for i in range(1000)]
costs = npy.array([coord_1, coord_2]).T

pareto_points = HeterogeneousList.pareto_indexes(costs)
pareto_frontiers = HeterogeneousList.pareto_frontiers(len(costs), costs)
closefig()

# Uniform
coord_1 = [random.uniform(0, 0.001) for i in range(1000)]
coord_2 = [random.uniform(0, 1e6) for i in range(1000)]
costs = npy.array([coord_1, coord_2]).T

pareto_points = HeterogeneousList.pareto_indexes(costs)
pareto_frontiers = HeterogeneousList.pareto_frontiers(len(costs), costs)
closefig()

# Gaussan
coord_1 = [random.gauss(50000, 1) for i in range(1000)]
coord_2 = [random.gauss(10, 1) for i in range(1000)]
costs = npy.array([coord_1, coord_2]).T

pareto_points = HeterogeneousList.pareto_indexes(costs)
pareto_frontiers = HeterogeneousList.pareto_frontiers(len(costs), costs)
closefig()

# Cars
all_cars_with_features = HeterogeneousList(all_cars_wi_feat)
costs = [all_cars_with_features.get_attribute_values('weight'), all_cars_with_features.get_attribute_values('mpg')]
costs = list(zip(*costs))

pareto_points = all_cars_with_features.pareto_points(costs)
pareto_frontiers = HeterogeneousList.pareto_frontiers(len(all_cars_wi_feat), costs)
closefig()

# With transposed costs
transposed_costs = list(zip(*costs))
pareto_frontiers = HeterogeneousList.pareto_frontiers(len(all_cars_wi_feat), transposed_costs)
closefig()

categorized_pareto = CategorizedList.from_pareto_sheets(all_cars_with_features, costs, 7)
pareto_plot_data = categorized_pareto.plot_data()
assert(json.dumps(pareto_plot_data[0].to_dict())[150:200] == ', "Cluster Label": 0}, {"mpg": 0.0, "displacement"')
assert(json.dumps(pareto_plot_data[1].to_dict())[10500:10550] == 't": 2901.0, "acceleration": 16.0, "Cluster Label":')
assert(json.dumps(pareto_plot_data[2].to_dict())[50:100] == 'te_names": ["Index of reduced basis vector", "Sing')

costs = all_cars_with_features.matrix
categorized_pareto = CategorizedList.from_pareto_sheets(all_cars_with_features, costs, 1)
pareto_plot_data = categorized_pareto.plot_data()
assert(json.dumps(pareto_plot_data[0].to_dict())[150:200] == ' "Cluster Label": 0}, {"mpg": 14.0, "displacement"')
assert(json.dumps(pareto_plot_data[1].to_dict())[10500:10550] == 'acceleration": 8.5, "Cluster Label": 1}, {"mpg": 0')
assert(json.dumps(pareto_plot_data[2].to_dict())[50:100] == 'te_names": ["Index of reduced basis vector", "Sing')
