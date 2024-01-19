import unittest


from autograding import TestInputOutput, TestFunction
from autograding.case import InOut, FuncCall


class TestSciNotation(TestInputOutput):
    def setUp(self):
        self.testcases = [
            InOut(input="1.1x10^-3", output="This number in E notation is 1.1E-3."),
            InOut(input="-1.5x10^3", output="This number in E notation is -1.5E3."),
        ]


if __name__ == '__main__':
    import os
    if not os.listdir("autograding"):
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
    unittest.main()
