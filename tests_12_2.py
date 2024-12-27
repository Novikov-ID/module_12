from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
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

    def test_first_race(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results['1'] = results
        self.assertTrue(str(results[max(results.keys())]) == 'Ник')

    def test_second_race(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['2'] = results
        self.assertTrue(str(results[max(results.keys())]) == 'Ник')

    def test_third_race(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['3'] = results
        self.assertTrue(str(results[max(results.keys())]) == 'Ник')

# Тест при котором Ник приходит вторым
#    def test_fourth_race(self):
#        tournament = Tournament(5, self.runner1, self.runner2, self.runner3)
#        results = tournament.start()
#        self.all_results['4'] = results
#        self.assertTrue(str(results[max(results.keys())]) == 'Ник')


if __name__ == "__main__":
    unittest.main()
