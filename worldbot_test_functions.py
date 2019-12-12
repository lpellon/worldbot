from my_module import worldbot_functions

def test_end_chat():
    assert callable(end_chat)
    assert isinstance(end_chat(["a", "b"]), bool)
    assert end_chat(["quit"]) == True


def test_return_country():
    assert callable(return_country)
    assert isinstance(return_country("abc"), bool)
    assert return_country("Asia") == True

def test_all():
    test_return_country()
    test_end_chat()