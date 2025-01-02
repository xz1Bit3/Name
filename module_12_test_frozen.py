import unittest
import module_12_2
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = module_12_2.Runner('John')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = module_12_2.Runner('Harry')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = module_12_2.Runner('John')
        runner2 = module_12_2.Runner('Harry')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = False
    @classmethod
    def setUpClass(cls):
        # Инициализация словаря для хранения результатов
        cls.all_results = {}

    def setUp(self):
        # Создание объектов бегунов
        self.runner1 = module_12_2.Runner("Усэйн", speed=10)
        self.runner2 = module_12_2.Runner("Андрей", speed=9)
        self.runner3 = module_12_2.Runner("Ник", speed=3)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_1(self):
        # Забег: Усэйн и Ник
        tournament = module_12_2.Tournament(distance=90)
        tournament.participants.append(self.runner1)  # Усэйн
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_race_1'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == 'Ник')

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_2(self):
        # Забег: Андрей и Ник
        tournament = module_12_2.Tournament(distance=90)
        tournament.participants.append(self.runner2)  # Андрей
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_race_2'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == "Ник")

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_3(self):
        # Забег: Усэйн, Андрей и Ник
        tournament = module_12_2.Tournament(distance=90)
        tournament.participants.append(self.runner1)  # Усэйн
        tournament.participants.append(self.runner2)  # Андрей
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_race_3'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == "Ник")

    @classmethod
    def tearDownClass(cls):
        # Вывод результатов в столбец
        print("Результаты всех тестов:")
        for k, v in cls.all_results.items():
            formatted_results = {place: str(runner) for place, runner in v.items()}
            print(f"{formatted_results}")

if __name__ == '__main__':
    unittest.main()