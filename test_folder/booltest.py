from Lib.ejptest.expectation import expect


def test_pass():
    expect(True).to_equal(True)


def test_fail():
    expect(True).to_equal(False)


def test_not_equal_pass():
    expect(False).to_not_equal(True)


def test_not_equal_fail():
    expect(False).to_not_equal(False)
