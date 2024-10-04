import unittest
import tests_12_3

obj_TS = unittest.TestSuite()

obj_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
obj_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

ttrunner = unittest.TextTestRunner(verbosity=2)
ttrunner.run(obj_TS)
