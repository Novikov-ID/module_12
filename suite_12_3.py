import unittest
import tests_12_3

run_walk_TS = unittest.TestSuite()
run_walk_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
run_walk_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

start_test = unittest.TextTestRunner(verbosity=2)
start_test.run(run_walk_TS)
