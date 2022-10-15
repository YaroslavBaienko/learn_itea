from student_homework import main, PHONE_INTERFACE


def check_exceptions(line: str, encode: bool):
    """Check for exceptions in PHONE_INTERFACE keys"""
    try:
        main(PHONE_INTERFACE, line + '@', encode=encode)
    except KeyError as error:
        print(error)


def test_encode_decode():
    """Test phone interface encode, decode funcs"""
    assert test_encode == test_code
    assert test_decode == test_message.upper()

    check_exceptions(test_decode, True)
    check_exceptions(test_encode, False)


test_message = 'Hello, world!'
test_encode = main(PHONE_INTERFACE, test_message)

test_code = "44|33|555|555|666|11|0|9|666|777|555|3|1111"
test_decode = main(PHONE_INTERFACE, test_code, False)


if __name__ == '__main__':
    test_encode_decode()
