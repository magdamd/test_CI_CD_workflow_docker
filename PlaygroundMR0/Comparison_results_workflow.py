import numpy as np

vectorGroundTruth = np.loadtxt("./PlaygroundMR0/results_GroundTruth/FID_signal.txt", dtype = np.complex64)
vectorLastPush = np.loadtxt("./PlaygroundMR0/results/FID_signal.txt", dtype = np.complex64)

class TestPythonScript:

    def test_compare_PlaygroundMR0_results(self):
        assert np.array_equal(vectorGroundTruth, vectorLastPush)

