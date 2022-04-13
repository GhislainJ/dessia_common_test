#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 14:35:47 2021

@author: steven
"""

import json

MIN_MODULE_COVERAGE = 47.95
MIN_GLOBAL_COVERAGE = 74.2
RATCHET_COVERAGE = 3.

untracked_modules = ["dessia_common/templates.py",
                     "dessia_common/utils.py",
                     "dessia_common/optimization.py",
                     'workflows/forms_simulation.py',
                     'workflows/vectored_workflow.py',
                     'models/tests.py']

print("untracked modules:", untracked_modules)

with open("coverage.json", "r") as file:
    d = json.load(file)

global_coverage = d['totals']['percent_covered']
print('global coverage', global_coverage, '%')
if global_coverage > MIN_GLOBAL_COVERAGE + RATCHET_COVERAGE:
    raise RuntimeError(f'MIN_GLOBAL_COVERAGE is too low: raise it to maximum {global_coverage}')
if global_coverage < MIN_GLOBAL_COVERAGE:
    raise RuntimeError('Package is not covered enough by tests: {}% expected minimum {}%'.format(
        global_coverage, MIN_GLOBAL_COVERAGE))

print('[Coverage] You can increase MIN_MODULE_COVERAGE to maximum {}% (actual {}%)'.format(
    global_coverage, MIN_GLOBAL_COVERAGE))

min_actual_coverage = 100
for file_name, data in d['files'].items():
    print(file_name, data['summary']['percent_covered'], '%')
    # print('/'.join(file_name.split('/')[-2:]))
    if '/'.join(file_name.split('/')[-2:]) in untracked_modules:
        print(file_name, '-> in untrack list')
    else:
        # print('Testing if {} is above {}'.format(file_name, MIN_FILE_COVERAGE))
        if data['summary']['percent_covered'] < MIN_MODULE_COVERAGE:
            raise RuntimeError('Module {} is not covered enough by tests: {}% expected minimum {}%'.format(
                file_name, data['summary']['percent_covered'], MIN_MODULE_COVERAGE))
        min_actual_coverage = min(
            min_actual_coverage, data['summary']['percent_covered'])

if min_actual_coverage > MIN_MODULE_COVERAGE + RATCHET_COVERAGE:
    raise RuntimeError(f'MIN_MODULE_COVERAGE is too low: raise it to maximum {min_actual_coverage}')
    
print('[Coverage] You can increase MIN_MODULE_COVERAGE to maximum {}% (actual:{})%'.format(
    min_actual_coverage, MIN_MODULE_COVERAGE))
