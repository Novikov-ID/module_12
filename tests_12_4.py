import logging
import unittest
from rt_with_exceptions import Runner


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            wolker = Runner('Тихоня', -4)
            for i in range(10):
                wolker.walk()
            self.assertEqual(wolker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(True)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')

        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    unittest.main()