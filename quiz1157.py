# 알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
#  단, 대문자와 소문자를 구분하지 않는다.
words = input().upper()
word = list(set(words))  # 입력받은 문자열에서 중복값을 제거

count_list = []
for i in word :
    count = words.count(i)
    count_list.append(count)  # count 숫자를 리스트에 append

if count_list.count(max(count_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = count_list.index(max(count_list))  # count 숫자 최대값 인덱스(위치)
    print(word[max_index])