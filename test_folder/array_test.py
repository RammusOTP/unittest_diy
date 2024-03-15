from ejptest.expectation import expect


def test_include_pass():
    expect([1, 2, 3]).to_include(2)


def test_include_fail():
    expect([1, 2, 3]).to_include(4)


def test_not_include_pass():
    expect([1, 2, 3]).to_not_include(4)


def tess_not_include_fail():
    expect([1, 2, 3]).to_not_include(2)