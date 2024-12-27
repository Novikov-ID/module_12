from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner('пешеход')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)


    def test_run(self):
        runner_1 = Runner('бегун')
        for i in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)


    def test_challenge(self):
        athlete_1 = Runner('участник_1')
        athlete_2 = Runner('участник_2')
        for i in range(10):
            athlete_1.walk()
            athlete_2.run()
        self.assertNotEqual(athlete_1.distance, athlete_2.distance)


if __name__ == "__main__":
    unittest.main()

