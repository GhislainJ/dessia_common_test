from dessia_common.workflow import InstantiateModel, ModelMethod, Export, TypedVariable,\
    TypedVariableWithDefaultValue, ModelAttribute, Pipe, Workflow, WorkflowBlock, ForEach,\
    Unpacker, Archive
from dessia_common.forms import Generator, Optimizer, StandaloneObject
from dessia_common import MethodType

instanciate_generator = InstantiateModel(model_class=Generator,
                                         name='Instantiate Generator')

generate_method = MethodType(class_=Generator, name='generate')
generator_generate = ModelMethod(method_type=generate_method,
                                 name='Generator Generate')
attribute_selection = ModelAttribute(attribute_name='models',
                                     name='Attribute Selection')

# Subworkflow of model optimization
instanciate_optimizer = InstantiateModel(model_class=Optimizer,
                                         name='Instantiate Optimizer')


generate_method = MethodType(class_=Optimizer, name='optimize')
optimization = ModelMethod(method_type=generate_method, name='Optimization')

model_fetcher = ModelAttribute(attribute_name='model_to_optimize',
                               name='Model Fetcher')

pipe1_opt = Pipe(input_variable=instanciate_optimizer.outputs[0],
                 output_variable=optimization.inputs[0])
pipe2_opt = Pipe(input_variable=optimization.outputs[1],
                 output_variable=model_fetcher.inputs[0])
optimization_blocks = [instanciate_optimizer, optimization, model_fetcher]
optimization_pipes = [pipe1_opt, pipe2_opt]
optimization_workflow = Workflow(blocks=optimization_blocks,
                                 pipes=optimization_pipes,
                                 output=model_fetcher.outputs[0],
                                 name='Optimization Workflow')

optimization_workflow_block = WorkflowBlock(workflow=optimization_workflow,
                                            name='Workflow Block')

parallel_optimization = ForEach(workflow_block=optimization_workflow_block,
                                iter_input_index=0, name='ForEach')

unpack_results = Unpacker(indices=[0, 1], name="Unpack Results")

to_txt = MethodType(class_=StandaloneObject, name="save_to_file")
export_txt = Export(method_type=to_txt, name="Export .txt")
# to_cad = MethodType(class_=StandaloneObject, name="to_step")
# export_cad = Export(method_type=to_cad, name="Export CAD")

zip_export = Archive(number_exports=1, name="Zip")

int_variable = TypedVariable(type_=int, name="Some Integer")

pipe_int_1 = Pipe(input_variable=int_variable,
                  output_variable=instanciate_generator.inputs[1])
pipe_1 = Pipe(input_variable=instanciate_generator.outputs[0],
              output_variable=generator_generate.inputs[0])
pipe_2 = Pipe(input_variable=generator_generate.outputs[1],
              output_variable=attribute_selection.inputs[0])
pipe_3 = Pipe(input_variable=attribute_selection.outputs[0],
              output_variable=parallel_optimization.inputs[0])
pipe_4 = Pipe(input_variable=parallel_optimization.outputs[0],
              output_variable=unpack_results.inputs[0])
pipe_5 = Pipe(input_variable=unpack_results.outputs[0],
              output_variable=export_txt.inputs[0])
# pipe_6 = Pipe(input_variable=unpack_results.outputs[1],
#               output_variable=export_cad.inputs[0])

pipe_export_1 = Pipe(input_variable=export_txt.outputs[0], output_variable=zip_export.inputs[0])
# pipe_export_2 = Pipe(input_variable=export_cad.outputs[0], output_variable=zip_export.inputs[1])
()
blocks = [instanciate_generator, generator_generate, attribute_selection, parallel_optimization,
          unpack_results, export_txt, zip_export]
pipes = [pipe_int_1, pipe_1, pipe_2, pipe_3, pipe_4, pipe_5, pipe_export_1]
workflow_ = Workflow(blocks=blocks, pipes=pipes, output=parallel_optimization.outputs[0])

values = {0: 1, 4: 2}
workflow_run = workflow_.run(input_values=values, verbose=True)

workflow_state = workflow_.start_run(values)
workflow_state.continue_run()
export_output = workflow_state.export_archive()
print(export_output)
# with open("archive.zip", "wb") as f:
#     f.write(export_output.getbuffer())
