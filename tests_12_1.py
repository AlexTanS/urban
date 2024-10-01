import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj = runner.Runner("Any")
        for _ in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        obj = runner.Runner("Any")
        for _ in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        obj_1 = runner.Runner("Alpha")
        obj_2 = runner.Runner("Beta")
        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)


if __name__ == '__main__':
    unittest.main()
