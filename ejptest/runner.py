import importlib.machinery
import types
from inspect import getmembers, isfunction
import sys
import os
from Lib.ejptest import colours
from Lib.ejptest.expectation import FailedExpectationError


class Runner:

    def __init__(self, path):
        self.test_files = []
        self.successes, self.failures = 0, 0
        self.load_test_files(path)


    def load_test_files(self, path):
        if path.endswith('__pycache__'):
            return
        if os.path.isfile(path):
            self.test_files.append(path)
        elif os.path.isdir(path):
            for nested_path in os.listdir(path):
                self.load_test_files(path + '/' + nested_path)


    def load_tests(self, mod):
        return [m for m in getmembers(mod) if isfunction(m[1]) and m[0].startswith('test_')]


    def load_module(self, file):
        loader = importlib.machinery.SourceFileLoader("testmod", file)
        mod = types.ModuleType("testmod")
        loader.exec_module(mod)
        return mod

    def run_single_file(self, file):
        mod = self.load_module(file)
        tests = self.load_tests(mod)
        for test in tests:
            (test_name, test_function) = test
            try:
                test_function()
                print(f"Running test {test_name} - {colours.GREEN}success{colours.RESET}")
                self.successes += 1
            except FailedExpectationError as e:
                print(f"{test_name} - {colours.RED}fail: {e.message} {colours.RESET}")
                self.failures += 1
            except AssertionError:
                print(f"{test_name} - {colours.RED}fail{colours.RESET}")
                self.failures += 1


    def run(self):
        for test_file in self.test_files:
            self.run_single_file(test_file)
        print(f"{colours.MAGENTA}Total tests: {self.successes + self.failures}{colours.RESET}")
        print(f"{colours.MAGENTA}{self.successes} tests passed{colours.RESET}")
        print(f"{colours.MAGENTA}{self.failures} tests failed{colours.RESET}")

def main():
    Runner(sys.argv[1]).run()


