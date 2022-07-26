"""
Tests for workflow.filter and HeterogeneousList.filtering
"""
import os
import json
from dessia_common import tests
from dessia_common.core import HeterogeneousList, DessiaFilter
import dessia_common.workflow as wf

# =============================================================================
# HETEROGENEOUSLIST.FILTERING
# =============================================================================
file_path = '/'.join(os.getcwd().split('/')[:-2]) + '/dessia_common/models/data/cars.csv'

data_method = wf.MethodType(class_=tests.CarWithFeatures, name='from_csv')
block_data = wf.ClassMethod(method_type=data_method, name='data load')

block_heterogeneous_list = wf.InstantiateModel(model_class=HeterogeneousList, name='heterogeneous list of data')

filters_list = [DessiaFilter('weight', "<=", 1800), DessiaFilter('mpg', ">=", 40)]

apply_method = wf.MethodType(class_=HeterogeneousList, name='filtering')
block_apply = wf.ModelMethod(method_type=apply_method, name='apply filter')

block_workflow = [block_data, block_heterogeneous_list, block_apply]
pipe_worflow = [wf.Pipe(block_data.outputs[0], block_heterogeneous_list.inputs[0]),
                wf.Pipe(block_heterogeneous_list.outputs[0], block_apply.inputs[0])
                ]
workflow = wf.Workflow(block_workflow, pipe_worflow, block_apply.outputs[0])

workflow_run = workflow.run({
    workflow.index(block_data.inputs[0]): file_path,
    workflow.index(block_apply.inputs[1]): filters_list,
    workflow.index(block_apply.inputs[2]): "or"})

# Workflow tests
# workflow._check_platform()
# workflow.plot()
# workflow.display_settings()
workflow_run.output_value.plot()

# JSON TESTS
dict_workflow = workflow.to_dict(use_pointers=True)
json_dict = json.dumps(dict_workflow)
decoded_json = json.loads(json_dict)
deserialized_object = workflow.dict_to_object(decoded_json)

# JSON Workflow_run tests
dict_workflow_run = workflow_run.to_dict(use_pointers=True)
json_dict = json.dumps(dict_workflow_run)
decoded_json = json.loads(json_dict)
deserialized_object = workflow_run.dict_to_object(decoded_json)

# Debug of block display, kept for now, will be removed soon
gg = workflow_run._display_from_selector('plot_data')
json.dumps(workflow_run.to_dict())
workflow_run._displays

# =============================================================================
# BLOCK FILTER
# =============================================================================

data_method = wf.MethodType(class_=tests.CarWithFeatures, name='from_csv')
block_data = wf.ClassMethod(method_type=data_method, name='data load')

filters_list = [DessiaFilter('weight', "<=", 1800), DessiaFilter('mpg', ">=", 40)]

block_filter = wf.Filter(filters=filters_list, logical_operand="or")

block_workflow = [block_data, block_filter]
pipe_worflow = [wf.Pipe(block_data.outputs[0], block_filter.inputs[0])]

workflow = wf.Workflow(block_workflow, pipe_worflow, block_filter.outputs[0])

workflow_run = workflow.run({workflow.index(block_data.inputs[0]): file_path})


# Workflow tests
workflow._check_platform()
workflow.plot()
workflow.display_settings()
print(workflow_run.output_value)

# JSON TESTS
dict_workflow = workflow.to_dict(use_pointers=True)
json_dict = json.dumps(dict_workflow)
decoded_json = json.loads(json_dict)
deserialized_object = workflow.dict_to_object(decoded_json)

# JSON Workflow_run tests
dict_workflow_run = workflow_run.to_dict(use_pointers=True)
json_dict = json.dumps(dict_workflow_run)
decoded_json = json.loads(json_dict)
deserialized_object = workflow_run.dict_to_object(decoded_json)

# Debug of block display, kept for now, will be removed soon
gg = workflow_run._display_from_selector('plot_data')
json.dumps(workflow_run.to_dict())
workflow_run._displays
