import numpy as np

vectorGroundTruth = np.loadtxt("./PlaygroundMR0/results_GroundTruth/arrayX.txt")
vectorLastPush = np.loadtxt("./PlaygroundMR0/results_LastPush/arrayX.txt")

class TestPythonScript:

    def compare(self):
        assert np.array_equal(vectorGroundTruth, vectorLastPush)

