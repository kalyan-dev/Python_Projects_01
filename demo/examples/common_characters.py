# Take 2 strings and display the common characters between the 2 strings;

str1 = "This is first string"
str2 = "here is another one"

common = ""

# for ch in str1:
#     if str2.count(ch) > 0:
#         print(ch,end=' ')
#
#

for ch in str1:
    if str2.count(ch) > 0 and common.count(ch) <= 0:
        common = common + ch + ' '
print(common)




