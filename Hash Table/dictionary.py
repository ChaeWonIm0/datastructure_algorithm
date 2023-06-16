score = [97, 49, 89]
# 어떤게 과목의 점수인지 알수 없음

score2 = {
    'math':97,
    'english':97,
    'korean':89
}

# 'key' : value

print(score2['math'])
# 덮어쓰기
score2['math'] = 45
print(score2)
score2['science'] = 100
print(score2['science'])

# 검색
print('math' in score2)
if 'music' in score2:
    print(score2['music'])
else:
    score2['music'] = 0