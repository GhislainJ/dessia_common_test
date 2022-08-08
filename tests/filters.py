"""
Tests for dessia_common.DessiaFilters/FiltersList class
"""
import itertools
from dessia_common.models import all_cars_no_feat, all_cars_wi_feat, rand_data_large
from dessia_common.core import HeterogeneousList, DessiaFilter, FiltersList

# When attribute _features is not specified in class Car
all_cars_without_features = HeterogeneousList(all_cars_no_feat)
# When attribute _features is specified in class CarWithFeatures
all_cars_with_features = HeterogeneousList(all_cars_wi_feat)
# Auto-generated heterogeneous dataset with nb_clusters clusters of points in nb_dims dimensions
RandData_heterogeneous = HeterogeneousList(rand_data_large)

# Filters creation
weight_val = 2000.
mpg_big_val = 100.
mpg_low_val = 40.
filter_1 = DessiaFilter('weight', 'le', weight_val)
filter_2 = DessiaFilter('mpg', 'ge', mpg_big_val)
filter_3 = DessiaFilter('mpg', 'ge', mpg_low_val)
filters_list = [filter_1, filter_3]
print(FiltersList(filters_list, logical_operator="or"))

# Or testing
filters_list_fun = lambda x: ((getattr(value, 'weight') <= weight_val or
                               getattr(value, 'mpg') >= mpg_big_val or
                               getattr(value, 'mpg') >= mpg_low_val)
                              for value in all_cars_no_feat)

assert(all(item in all_cars_without_features.filtering(filters_list, logical_operator="or")
           for item in list(itertools.compress(all_cars_no_feat, filters_list_fun(all_cars_no_feat)))))

# And with non empty result
filters_list = [filter_1, filter_3]
filters_list_fun = lambda x: ((getattr(value, 'weight') <= weight_val and getattr(value, 'mpg') >= mpg_low_val)
                              for value in all_cars_no_feat)
assert(all(item in all_cars_without_features.filtering(filters_list, logical_operator="and")
           for item in list(itertools.compress(all_cars_no_feat, filters_list_fun(all_cars_no_feat)))))

# And with empty result
filters_list = [filter_1, filter_2]
assert(all_cars_without_features.filtering(filters_list, "and") == HeterogeneousList())

# Xor
filter_1 = DessiaFilter('weight', 'le', weight_val)
filter_3 = DessiaFilter('mpg', 'ge', mpg_low_val)
filters_list = [filter_1, filter_2, filter_3]
filters_list_fun = lambda x: ((getattr(value, 'weight') <= weight_val
                               and not getattr(value, 'mpg') >= mpg_big_val
                               and not getattr(value, 'mpg') >= mpg_low_val) or
                              (not getattr(value, 'weight') <= weight_val
                               and getattr(value, 'mpg') >= mpg_big_val
                               and not getattr(value, 'mpg') >= mpg_low_val) or
                              (not getattr(value, 'weight') <= weight_val
                               and not getattr(value, 'mpg') >= mpg_big_val
                               and getattr(value, 'mpg') >= mpg_low_val)
                          for value in all_cars_no_feat)
assert(all(item in all_cars_without_features.filtering(filters_list, logical_operator="xor")
           for item in list(itertools.compress(all_cars_no_feat, filters_list_fun(all_cars_no_feat)))))

try:
    all_cars_without_features.filtering(filters_list, logical_operator="blurps")
    raise ValueError("'blurps' should not work for logical_operator attribute in FiltersList")
except Exception as e:
    assert(e.args[0] == "'blurps' str for 'logical_operator' attribute is not a use case")

