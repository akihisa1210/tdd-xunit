class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun("test_method")
        assert(not test.was_run)
        test.run()
        assert test.was_run


class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        super().__init__(name)

    def test_method(self):
        self.was_run = 1


TestCaseTest("test_running").run()
