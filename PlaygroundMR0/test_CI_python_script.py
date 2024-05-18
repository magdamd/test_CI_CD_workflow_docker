import numpy as np

vectorGroundTruth = np.loadtxt("./results_GroundTruth/arrayX.txt")
vectorLastPush = np.loadtxt("./results_LastPush/arrayX.txt")

class TestPythonScript:

    def compare(self):
        assert np.array_equal(vectorGroundTruth, vectorLastPush)

