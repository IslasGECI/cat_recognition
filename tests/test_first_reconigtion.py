import cat_recognition as cr


def test_return_one():
    expected = 1
    obtained = cr.return_one()
    assert expected == obtained
