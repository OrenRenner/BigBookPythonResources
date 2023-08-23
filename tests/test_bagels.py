from bagels import bagels


def test_getSecretNum():
    assert isinstance(bagels.getSecretNum(), str)
    assert bagels.NUM_DIGITS == len(bagels.getSecretNum())


def test_getClues():
    pass
