from tests.test import test
from tests.test2 import test2
from tests.test3 import test3
from tests.test4 import test4
from tests.test5 import test5
from tests.test6 import test6
from tests.test7 import test7
from tests.test8 import test8
from tests.test9 import test9
from tests.test10 import test10
from tests.test11 import test11
from tests.test12 import test12
from tests.test13 import test13
from custom_function.account_generate import return_new_user_info, return_new_admin_info
# admin 帳號(亂數) * 2
first_admin = return_new_admin_info()
second_admin = return_new_admin_info()
firstgroup = first_admin['groupname']
secondgroup = second_admin['groupname']
# user 帳號(亂數) * 2
first_user = return_new_user_info()
first_user['groupname'] = firstgroup
second_user = return_new_user_info()
second_user['groupname'] = secondgroup

# 一個貼文 (string)
posts = [
    "Just hiked to the summit of Mount Everest! The breathtaking view was worth every step. #BucketListAdventure",
    "Excited to announce the launch of my new book, 'The Power of Imagination.' It's been a labor of love, and I can't wait for you all to read it! #AuthorLife",
    "Visited a local animal shelter today and adopted the sweetest rescue pup. Meet Max, my new fur baby! #AdoptDontShop #RescueDogLove"
        ]
# 一個留言 (string)
comments = [
    "test comment",
        ]
# 一個記帳 (date, string, int)
things = [
    {
        "date":"002012/01/23",
        "thing":"test",
        "expense":"1212",
    }
]
if __name__ == "__main__":
    do_the_test = \
    [
    # 測試1
    test(first_admin['groupname'], first_admin['username'], first_admin['password']),
    # 測試2
    test2(first_user['groupname'], first_user['username'], first_user['password']),
    # 測試3
    test3(first_user['groupname'], "", ""),
    # 測試4
    test4(first_user['groupname'], first_user['username'], first_user['password']),
    # 測試5
    test5(first_user['groupname'], first_user['username'], first_user['password']),
    # 測試6
    test6(first_user['groupname'], "WrongUser", "WrongUser"),
    # 測試7
    test7(first_user['groupname'], first_user['username'], first_user['password']),
    # 測試8
    test8(first_user['groupname'], first_user['username'], first_user['password'], posts[0]),
    # 測試9
    test9(first_user['groupname'], first_user['username'], first_user['password'], comments[0]),
    # 測試10
    test10(first_user['groupname'], first_user['username'], first_user['password'], things[0]),
    # 測試11
    test11(first_admin['groupname'], first_admin['username'], first_admin['password']),
    # 測試12
    test12(first_admin['groupname'], first_admin['username'], first_admin['password']),
    # 測試13
    test13(first_admin['groupname'], first_admin['username'], first_admin['password'])
    ]
    # 總測試
    for i, dtt in enumerate(do_the_test):
        if not dtt:
            print(f"test{i + 1} successful!")
        else:
            print(f"test{i + 1} fail!")

