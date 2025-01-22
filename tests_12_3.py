import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = Runner('пешеход')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_1 = Runner('бегун')
        for i in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        athlete_1 = Runner('участник_1')
        athlete_2 = Runner('участник_2')
        for i in range(10):
            athlete_1.walk()
            athlete_2.run()
        self.assertNotEqual(athlete_1.distance, athlete_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner(name="Усэйн", speed=10)
        self.runner2 = Runner(name="Андрей", speed=9)
        self.runner3 = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for tournament, results in cls.all_results.items():
            print(f'{{{', '.join([f'{place}: {name}' for place, name in results.items()])}}}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_race(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results['1'] = results
        self.assertTrue(str(results[max(results.keys())]) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_race(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['2'] = results
        self.assertTrue(str(results[max(results.keys())]) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_race(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['3'] = results
        self.assertTrue(str(results[max(results.keys())]) == 'Ник')


if __name__ == "__main__":
    unittest.main()
