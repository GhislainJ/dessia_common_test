from dessia_common.tests import RandDataD2
from dessia_common.sampling import Sampler
from dessia_common.optimization import FixedAttributeValue, BoundedAttributeValue
from dessia_common.workflow.blocks import InstantiateModel, ModelMethod
from dessia_common.typings import MethodType
from dessia_common.workflow.core import Workflow, Pipe

block_0 = InstantiateModel(model_class=Sampler, name='Sampler')
block_1 = ModelMethod(method_type=MethodType(Sampler, 'make_doe'), name='gytgy')
blocks = [block_0, block_1]

pipe_0 = Pipe(block_0.outputs[0], block_1.inputs[0])
pipes = [pipe_0]

workflow = Workflow(blocks, pipes, output=block_1.outputs[0], name='')

sampled_attributes = [BoundedAttributeValue('p_1', 0.1, 0.5, 250)]
constant_attributes = [FixedAttributeValue('p_2', 25)]

# Workflow run
workflow_run = workflow.run({workflow.index(block_0.inputs[0]): RandDataD2,
                             workflow.index(block_0.inputs[1]): sampled_attributes,
                             workflow.index(block_0.inputs[2]): constant_attributes})

# Workflow tests
workflow._check_platform()
wfrun_plot_data = workflow_run.output_value.plot()
