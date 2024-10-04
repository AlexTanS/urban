import runner
import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        obj = runner.Runner("Any")
        for _ in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        obj = runner.Runner("Any")
        for _ in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        obj_1 = runner.Runner("Alpha")
        obj_2 = runner.Runner("Beta")
        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = []

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.usain = runner_and_tournament.Runner("Усэйн", 10)
        self.andrey = runner_and_tournament.Runner("Андрей", 9)
        self.nik = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_result:
            temp = {}
            for k, v in result.items():
                temp[k] = v.__str__()
            print(temp)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        tournament = runner_and_tournament.Tournament(90, self.usain, self.nik)
        TournamentTest.all_result.append(tournament.start())
        self.assertTrue(self.all_result[-1][max(self.all_result[-1].keys())] == self.nik)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        tournament = runner_and_tournament.Tournament(90, self.andrey, self.nik)
        TournamentTest.all_result.append(tournament.start())
        self.assertTrue(self.all_result[-1][max(self.all_result[-1].keys())] == self.nik)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        tournament = runner_and_tournament.Tournament(90, self.usain, self.andrey, self.nik)
        TournamentTest.all_result.append(tournament.start())
        self.assertTrue(self.all_result[-1][max(self.all_result[-1].keys())] == self.nik)


if __name__ == '__main__':
    unittest.main()
