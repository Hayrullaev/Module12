import unittest
from Homework3_test import RunnerTest, TournamentTest


loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)