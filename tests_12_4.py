import logging
import unittest
import rt_with_exceptions

logging.basicConfig(level=logging.INFO, filename="runner_tests.log", encoding="UTF-8", filemode="w",
                    format="%(asctime)s [%(levelname)s] - %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            obj = rt_with_exceptions.Runner("Any", -50)
            for _ in range(10):
                obj.walk()
            self.assertEqual(obj.distance, -50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner => {e}", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            obj = rt_with_exceptions.Runner(["Any", ])
            for _ in range(10):
                obj.run()
            self.assertEqual(obj.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner => {e}", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        obj_1 = rt_with_exceptions.Runner("Alpha")
        obj_2 = rt_with_exceptions.Runner("Beta")
        for _ in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1.distance, obj_2.distance)


if __name__ == '__main__':
    unittest.main()
