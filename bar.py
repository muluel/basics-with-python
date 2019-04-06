def chart(score):
    print('#'*score)

for i in range(1,4):
    score=int(input(f'Score {i}: '))
    print(f'Score {i}: ',end='')
    chart(score)