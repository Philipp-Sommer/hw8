#!/usr/bin/env python3

import collections
import importlib
import inspect
import unittest

Test = collections.namedtuple('Test', ['module', 'cls', 'points', 'min_tests'])

tests = [Test('test_vrptw_writer', 'TestVrptwWriter', 2, min_tests=1),
         Test('test_comprehensions', 'TestComprehensions', 2, min_tests=4),
         Test('test_simulation', 'TestSimulation', 3, min_tests=2),
         Test('test_knapsack', 'TestKnapsack', 2, min_tests=2)]

for test in tests:
    try:
        vars()[test.module] = importlib.import_module(test.module)
        vars()[test.cls] = getattr(vars()[test.module],
                                   test.cls)
    except (AttributeError, ImportError):
        vars()[test.module] = vars()[test.cls] = None
        print("{} test class cannot be imported (0 points)".format(
            test.cls))


def add_docstring_tests(test_case):
    """
    Define closures for test functions to be added to all testcases.
    """
    module_name = test_case.target[:-3]
    module = importlib.import_module(module_name)
    msg_no_docstring = '{}.{} has no docstring'
    msg_useless_docstring = '{}.{} requires a meaningful docstring.'

    def test_module_docstring(self):
        self.assertTrue(module.__doc__, 'module documentation required')
        self.assertTrue(len(module.__doc__) > 20,
                        'module documentation cannot be too short')

    def test_function_docstring(self):
        for name in dir(module):
            if name.startswith('_'):
                continue  # ignore hidden and special functions
            if not inspect.isfunction(getattr(module, name)):
                continue  # only consider functions and classes
            if name == 'main':
                continue
            if getattr(module, name).__module__ != module_name:
                continue
            docstring = getattr(module, name).__doc__
            self.assertTrue(isinstance(docstring, str),
                            msg_no_docstring.format(module_name, name))
            self.assertTrue(len(docstring) > 30, msg_useless_docstring
                            .format(module_name, name))

    def test_class_docstring(self):
        for name in dir(module):
            obj = getattr(module, name)
            if name.startswith('_'):
                continue  # ignore hidden and special functions
            if not inspect.isclass(obj):
                continue  # only consider functions and classes
            if obj.__module__ != module_name:
                continue
            b = getattr(obj, '__bases__', ())
            if len(b) == 1 and b[0] == tuple and getattr(obj, '_fields', None):
                continue  # avoid testing named tuples
            docstring = obj.__doc__
            self.assertTrue(isinstance(docstring, str),
                            msg_no_docstring.format(module_name, name))
            self.assertTrue(len(docstring) > 30, msg_useless_docstring
                            .format(module_name, name))

    has_class = False
    for name in dir(module):
        obj = getattr(module, name)
        if inspect.isclass(obj):
            b = getattr(obj, '__bases__', ())
            if len(b) == 1 and b[0] == tuple and getattr(obj, '_fields', None):
                continue  # avoid testing named tuples
            has_class = True
            break
    test_case.test_module_docstring = test_module_docstring
    test_case.test_function_docstring = test_function_docstring
    if has_class:
        test_case.test_class_docstring = test_class_docstring


def grader(result):
    """Return the number of points obtained by the result"""
    total = result.testsRun
    successes = total - len(result.errors) - len(result.failures)
    points = successes / total * result.points
    print(round(points, 2), "points for", result.target)
    return points


def build_test_cases(tests):
    max_total = 0.0
    test_cases = []
    for test in tests:
        max_total += test.points
        test_case = globals()[test.cls]
        if test_case is not None:
            test_functions = [e for e in vars(test_case)
                              if e.startswith('test_')]
            if len(test_functions) < test.min_tests:
                print('not enough tests in {} (0 points)'.format(test.cls))
                continue
            test_case.points = test.points
            test_case.target = test.module[5:] + '.py'
            add_docstring_tests(test_case)
            test_cases.append(test_case)
    return test_cases, max_total

if __name__ == "__main__":
    test_cases, max_total = build_test_cases(tests)
    total = 0.0
    for test_case in test_cases:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        runner = unittest.TextTestRunner()
        result = runner.run(suite)
        result.target = test_case.target
        result.points = test_case.points
        total += grader(result)
    print()
    print("{}/{} points in total".format(total, max_total))
