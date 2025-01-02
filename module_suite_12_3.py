import unittest
import module_12_test_frozen


Runner_Tournament = unittest.TestSuite()
Runner_Tournament.addTest(unittest.TestLoader().loadTestsFromModule(module_12_test_frozen))
test = unittest.TextTestRunner(verbosity=2)
test.run(Runner_Tournament)