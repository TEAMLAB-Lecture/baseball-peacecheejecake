# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number가 정수로 변환 가능할 경우는 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    result = user_input_number.isdigit()

    # ==================================
    return result


def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    # Output:
    #   - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    user_input_number = int(user_input_number)
    result = user_input_number >= 100 and user_input_number < 1000

    # ==================================
    return result


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    #   ex) 117 - True, 123 - False, 103 - False, 113 - True
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    result = False
    d0, d1, d2 = three_digit
    result = any([d0 == d1, d1 == d2, d2 == d0])
    # ==================================
    return result


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    
    result = True

    if not is_digit(user_input_number):
        result = False
    elif not is_between_100_and_999(user_input_number):
        result = False
    elif is_duplicated_number(user_input_number):
        result = False
    # ==================================
    return result


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # get_random_number() 함수를 사용하여 random number 생성
    while True:
        random_number = get_random_number()
        if not is_duplicated_number(str(random_number)):
            result = random_number
            break
    # ==================================
    return result


def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    #   - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    # Output:
    #   - [strikes, ball] : 규칙에 따라 정수형 값인 strikes와 ball이 반환됨
    #   변환 규칙은 아래와 같음
    #   - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    #     한 숫자와 자릿수가 모두 일치하면 1 Strike
    #   - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
    #   - 세자리 숫자를 정확히 입력하면 3 Strike
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_strikes_or_ball("123", "472")
    #   [0, 1]
    #   >>> bg.get_strikes_or_ball("547", "472")
    #   [0, 2]
    #   >>> bg.get_strikes_or_ball("247", "472")
    #   [0, 3]
    #   >>> bg.get_strikes_or_ball("742", "472")
    #   [1, 2]
    #   >>> bg.get_strikes_or_ball("472", "472")
    #   [3, 0]
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    strikes = balls = 0
    for d_user, d_cpu in zip(user_input_number, random_number):
        if d_user == d_cpu:
            strikes += 1
        elif d_user in random_number:
            balls += 1

    result = [strikes, balls]
    # ==================================
    return result


def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    one_more_input = one_more_input.upper()
    result = one_more_input in ('Y', 'YES')
    # ==================================
    return result


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    one_more_input = one_more_input.upper()
    result = one_more_input in ('N', 'NO')
    # ==================================
    return result



def end_game():
    print("Thank you for using this program")
    print("End of the Game")


# def main():
#     print("Play Baseball")
#     user_input = '99'
#     random_number = str(get_not_duplicated_three_digit_number())
#     print("Random Number is : ", random_number)
#     # ===Modify codes below=============
#     # 위의 코드를 포함하여 자유로운 수정이 가능함
    
#     while True:
#         random_number = str(get_not_duplicated_three_digit_number())
#         while random_number != user_input:
#             # 규칙에 맞는 숫자를 입력할 때까지 숫자 입력
#             while True:
#                 user_input = input('Input guess number : ')
#                 if is_validated_number(user_input):
#                     break
#                 elif user_input == '0':
#                     print_end()
#                     return
#                 print("Wrong Input, Input again")

#             # 스트라이크, 볼 판정 -> 출력
#             strikes, balls = get_strikes_or_ball(user_input, random_number)
#             print(f'Strikes : {strikes} , Balls : {balls}')
#             print(user_input, random_number)

#         # 한 번 더? - 올바른 입력이 될 때까지 물어서 답을 얻기
#         while True:
#             input_for_again = input('You win, one more(Y/N)?')
#             if is_yes(input_for_again):
#                 break
#             elif input_for_again == '0' or is_no(input_for_again):
#                 print_end()
#                 return
#             else:
#                 print("Wrong Input")


def get_validated_input():
    user_input = input('Input guess number : ')
    if user_input == '0':
        return False
    if is_validated_number(user_input):
        return user_input

    print('Wrong Input, Input again')
    return get_validated_input()


def get_validated_input_again():
    user_input = input('You win, one more(Y/N)?')
    if is_yes(user_input):
        return True
    if is_no(user_input) or user_input == '0':
        return False
    print('Wrong input')
    return get_validated_input_again()


def play(target_number):
    input_number = get_validated_input()
    if not input_number:
        end_game()
        return False

    # 스트라이크, 볼 판정 -> 출력
    strikes, balls = get_strikes_or_ball(input_number, target_number)
    print(f'Strikes : {strikes} , Balls : {balls}')
    # print(input_number, target_number)

    if target_number == input_number:
        return True
    return play(target_number)


def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is :", random_number)

    target_number = random_number
    one_more_game = True
    while one_more_game:
        if not play(target_number):
            return
        one_more_game = get_validated_input_again()
        target_number = str(get_not_duplicated_three_digit_number())
    else:
        end_game()
        return


# def play_in_test(input_number, target_number):
#     strikes, balls = get_strikes_or_ball(input_number, target_number)
#     print(f'Strikes : {strikes} , Balls : {balls}')
#     print(input_number, target_number)

#     return target_number == input_number


# def get_strikes_or_ball_tc(user_input_number, random_number):
#     result = []
#     if random_number == user_input_number:
#         result = [3, 0]

#     strikes = 0
#     ball = 0

#     for number in user_input_number:
#         if (number in random_number):
#             if user_input_number.index(number) is random_number.index(number):
#                 strikes += 1
#             else:
#                 ball += 1
#     result = [strikes, ball]
#     return result


# def test():
#     for target_number in range(100, 1000):
#         target_number = str(target_number)
#         for test_number in range(100, 1000):
#             test_number = str(test_number)
#             if not is_validated_number(target_number) or not is_validated_number(test_number):
#                 continue
#             print(test_number, target_number)
#             assert get_strikes_or_ball(test_number, target_number) == get_strikes_or_ball_tc(test_number, target_number)
            

if __name__ == "__main__":
    # test()
    main()
