from Lib.ejptest.expectation import expect


def test_pass():
    expect(1+1).to_equal(2)


def test_fail():
    expect(1+2).to_equal(2)
