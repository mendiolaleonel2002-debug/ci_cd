from generator.password_generator import (
    generate_password,
    has_upercase,
    has_number,
    has_symbol
)

def test_password_length():
    password = generate_password(12)
    assert len(password) == 12

def test_password_is_string():
    password = generate_password(10)
    assert isinstance(password, str)