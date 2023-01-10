words = input().split()
palindrome = input()
palindrome_list = []
counter = 0

for word in words:
    if word[::-1] == word:
        palindrome_list.append(word)
    if word[::-1] == palindrome:
        counter += 1


print(palindrome_list)
print(f"Found palindrome {counter} times")


# words = input().split()
# palindrome = input()
# palindrome_list = []
# counter = 0
#
# for word in words:
#     rev_word = reversed(word)
#     reversed_word = "".join(rev_word)
#     if reversed_word == word:
#         palindrome_list.append(word)
#     if reversed_word == palindrome:
#         counter += 1
#
# print(palindrome_list)
# print(f"Found palindrome {counter} times")


# def palindrome_filtered(word):
#     if word == word[::-1]:
#         return word
#
#
# words = input().split(' ')
# palindrome = input()
#
# palindrome_list = [word for word in words if palindrome_filtered(word)]
# palindrome_counter = palindrome_list.count(palindrome)
#
# print(palindrome_list)
# print(f'Found palindrome {palindrome_counter} times')
