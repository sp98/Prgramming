from peewee import *

db = SqliteDatabase("Test1.db")


class TestResult(Model):
    date = DateTimeField(unique=True)
    total = CharField()
    passed = CharField()
    failed = CharField()
    ignored = CharField()
    pending = CharField()
    total_time = CharField()

    class Meta:
        database = db


def initialize_db():
    """create database"""
    db.connect()
    db.create_tables([TestResult], safe=True)


def add_entries(testResults):

    try:
        TestResult.create(date = testResults.get("date"), total=testResults.get("total"), passed=testResults.get("passed"),
                          failed=testResults.get("failed"), ignored=testResults.get("ignored"),
                          pending=testResults.get("pending"), total_time=testResults.get("time"))
        print("New Entries Added")

    except IntegrityError:
        result = TestResult.get(date = testResults.get("date"))
        result.date = testResults["date"]
        result.total = testResults.get("total")
        result.passed = testResults.get("passed")
        result.failed = testResults.get("failed")
        result.ignored = testResults.get("ignored")
        result.pending = testResults.get("pending")
        result.total_time = testResults.get("time")
        rows_affected = result.save();
        print("{} rows affected".format(rows_affected))


def get_entries():
    result_lst = [TestResult.date, TestResult.total, TestResult.passed, TestResult.failed,
                  TestResult.ignored, TestResult.pending, TestResult.total_time]
    result = TestResult.select(*result_lst).get()
    # result = TestResult.select().order_by(TestResult.date.desc())
    for test in TestResult.select():
        # print(test.total_time)
        print(test.date)

    return result

if __name__ == "__main__":
    print("Database test")