#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dessia_common
from dessia_common.forms import DEF_SO

import unittest
from parameterized import parameterized


class TestSerialization(unittest.TestCase):

    @parameterized.expand([
        (DEF_SO,),
    ])
    def test_objects_serialization_deserialization(self, my_obj):
        d = my_obj.to_dict()
        obj = dessia_common.DessiaObject.dict_to_object(d)
        assert obj == my_obj


if __name__ == '__main__':
    unittest.main()
