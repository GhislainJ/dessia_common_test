"""
Cluster.py package testing.
"""
import json
import pkg_resources
from dessia_common import tests, cluster
from dessia_common.core import HeterogeneousList
import dessia_common.workflow as wf

# Standard cars homogeneous dataset from the Internet
csv_cars = pkg_resources.resource_stream('dessia_common', 'models/data/cars.csv')
all_cars_homomgeneous = HeterogeneousList(tests.Car.from_csv(csv_cars))

# Auto-generated heterogeneous small dataset with nb_clusters clusters of points in nb_dims dimensions
mean_borns = [-50, 50]
std_borns = [-2, 2]
small_clustesters_heterogeneous = HeterogeneousList(
    tests.ClusTester_d5.create_dataset(nb_clusters = 10, nb_points = 250, mean_borns = mean_borns, std_borns = std_borns) +
    tests.ClusTester_d4.create_dataset(nb_clusters = 10, nb_points = 250, mean_borns = mean_borns, std_borns = std_borns) +
    tests.ClusTester_d3.create_dataset(nb_clusters = 10, nb_points = 250, mean_borns = mean_borns, std_borns = std_borns))

# Auto-generated heterogeneous large dataset with nb_clusters clusters of points in nb_dims dimensions
mean_borns = [-50, 50]
std_borns = [-2, 2]
big_clustesters_heterogeneous = HeterogeneousList(
    tests.ClusTester_d9.create_dataset(nb_clusters = 10, nb_points = 500, mean_borns = mean_borns, std_borns = std_borns) +
    tests.ClusTester_d7.create_dataset(nb_clusters = 10, nb_points = 500, mean_borns = mean_borns, std_borns = std_borns) +
    tests.ClusTester_d8.create_dataset(nb_clusters = 10, nb_points = 500, mean_borns = mean_borns, std_borns = std_borns))

# Generate ClusterResults from HeterogeneousLists
dbtest = cluster.ClusterResult.from_dbscan(all_cars_homomgeneous, eps=50)
aggclustest = cluster.ClusterResult.from_agglomerative_clustering(big_clustesters_heterogeneous, n_clusters=10)
kmeanstest = cluster.ClusterResult.from_kmeans(small_clustesters_heterogeneous, n_clusters=10, scaling=False)

# Test ClusterResults instances on platform
dbtest._check_platform()
aggclustest._check_platform()
kmeanstest._check_platform()

# Test plots outside platform
dbtest.plot(attributes=all_cars_homomgeneous.common_attributes)
aggclustest.plot(attributes=big_clustesters_heterogeneous.common_attributes)
kmeanstest.plot()


# =============================================================================
# TO CHANGE IN VERY SOON COMMITS
# =============================================================================
# dbtest.check_dimensionality()
# aggclustest.check_dimensionality()
# kmeanstest.check_dimensionality()

# dict_ = dbtest.to_dict(use_pointers=True)

# json_dict = json.dumps(dict_)
# decoded_json = json.loads(json_dict)
# deserialized_object = dbtest.dict_to_object(decoded_json)

# dbtest._check_platform()
# aggclustest._check_platform()
# kmeanstest._check_platform()

# data_method = wf.MethodType(class_=tests.Car, name='from_csv')
# block_data = wf.ClassMethod(method_type=data_method, name='data load')

# cluster_method = wf.MethodType(class_=cluster.ClusterResult, name='from_agglomerative_clustering')
# block_cluster = wf.ClassMethod(method_type=cluster_method, name='clustering')

# display_cluster = wf.Display(name='Display Cluster')

# block_workflow = [block_cluster, display_cluster]
# pipe_worflow = [wf.Pipe(block_cluster.outputs[0], display_cluster.inputs[0])]
# workflow = wf.Workflow(block_workflow, pipe_worflow, block_cluster.outputs[0])

# workflow_run = workflow.run({workflow.index(block_cluster.inputs[0]): all_cars})
# cresult = workflow_run.output_value._display_from_selector('plot_data')

# # ff=workflow_run.output_value.display_settings()[1]
# # ff.selector

# workflow.plot()
# workflow.display_settings()
# workflow_run.output_value.plot()

# gg = workflow_run._display_from_selector('plot_data')
# json.dumps(gg.to_dict())
# workflow_run._displays
