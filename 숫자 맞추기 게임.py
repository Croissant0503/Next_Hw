#숫자 맞추기 게임

max_num = int(input("숫자 게임 최대값을 입력해주세요: "))
min_num = 0
count = 1

print("1부터", max_num, "까지의 숫자를 하나 생각하세요")
input("준비가 되었으면 enter를 누르세요")

while True:
    mid = int((max_num + min_num) / 2)
    print("당신이 생각한 숫자가", mid, "입니까?")
    result = input("제가 맞췄다면 '맞음'을, 제가 제시한 숫자보다 크다면 '큼'을, 작다면 '작음'을 입력해주세요: ")

    if result == "맞음":
        print(count, "번만에 맞췄다.")
        break
    elif result == "큼":
        min_num = mid + 1
        count += 1
    elif result == "작음":
        max_num = mid - 1
        count += 1
    else :
      print("잘못된 값을 입력하셨습니다.")