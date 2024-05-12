import pytest

from calculator import square


# def main():
#     test_square()

## default python way with [test_<original_function_name>]    
# def test_square():
#     try:
#         assert square(2) == 4
#         assert square(3) == 9
#     except AssertionError:
#         print("square() failed")

# def test_assert():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(0) == 0
#     assert square(-2) == 4
#     assert square(-3) == 9

# if __name__ == "__main__":
#     main()