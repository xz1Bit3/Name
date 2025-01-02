import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        # Инициализация словаря для хранения результатов
        cls.all_results = {}

    def setUp(self):
        # Создание объектов бегунов
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    def test_race_1(self):
        # Забег: Усэйн и Ник
        tournament = Tournament(distance=90)
        tournament.participants.append(self.runner1)  # Усэйн
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_race_1'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == 'Ник')

    def test_race_2(self):
        # Забег: Андрей и Ник
        tournament = Tournament(distance=90)
        tournament.participants.append(self.runner2)  # Андрей
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_race_2'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == "Ник")

    def test_race_3(self):
        # Забег: Усэйн, Андрей и Ник
        tournament = Tournament(distance=90)
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
