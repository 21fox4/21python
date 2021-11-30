print("Exit from the Hell에 오신걸 환영합니다.")
print("당신에게 주어진 목숨은 단 40개!")
print("각 라운드를 통과하실 때마다 당신의 시간은 줄어들수도, 연장될수도 있어.")
print("시간을 모두 탕진하면 탈출실패... 지옥의 맛을 보게 될거야!")

next_level = input("게임을 시작하지. (Y or Y)")
if next_level == 'Y':
    print("Game Start")


import random
rock = '''
       *****
        ***
'''
scissor = '''
         *     *
          *   *
           ***
            *
'''
paper = '''
       *****
       *****
       *****
       *****
'''
       
game_option = [rock, scissor, paper]
com_choice = random.randint(0,2)

hart = 40

while hart > 0:
    user_choice = int(input("0: 바위, 1: 가위, 2: 보 >>>    "))
    
    print("너의 선택은? :  ")
    print(game_option[user_choice])

    print("나의 선택은? :  ")
    print(game_option[com_choice])

    print("너의 남은 목숨의 개수는 %d개 이다." %hart)
    if com_choice == user_choice :
        print("비겼습니다.")
        continue
    elif user_choice - com_choice == -1 or (user_choice ==2 and com_choice ==0): 
        print("이겼습니다. ")
        print("너의 남은 목숨의 개수는 %d개 이다." %hart)
        print("다음게임을 시작하지")
        break
        
    else:
        print("졌습니다.")
        hart -= 10
        print("너의 남은 목숨의 개수는 %d개 이다." %hart)
        
        continue


yabawi ='''

    ╭════════╮      ╭════════╮      ╭════════╮
    ║░░░░░░░░║      ║░░░░░░░░║      ║░░░░░░░░║
    ║░░░░░░░░║      ║░░░░░░░░║      ║░░░░░░░░║
    ║░░░①░░░║      ║░░░②░░░║      ║░░░③░░░║
    ║░░░░░░░░║      ║░░░░░░░░║      ║░░░░░░░░║
    ║░░░░░░░░║      ║░░░░░░░░║      ║░░░░░░░░║
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
             << Choice One Nunmber >>
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

'''
yabawi_1 = '''

    ╭════════╮
    ║░░░░░░░░║
    ║░░░░░░░░║      ╭════════╮      ╭════════╮
    ║░░░①░░░║      ║░░░░░░░░║      ║░░░░░░░░║
    ║░░░░░░░░║      ║░░░░░░░░║      ║░░░░░░░░║
    ║░░░░░░░░║      ║░░░②░░░║      ║░░░③░░░║
                    ║░░░░░░░░║      ║░░░░░░░░║
     <<PASS>>       ║░░░░░░░░║      ║░░░░░░░░║
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
              << You Succeeded !! >>
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

'''
yabawi_2 = '''

                    ╭════════╮
                    ║░░░░░░░░║
    ╭════════╮      ║░░░░░░░░║      ╭════════╮
    ║░░░░░░░░║      ║░░░②░░░║      ║░░░░░░░░║
    ║░░░░░░░░║      ║░░░░░░░░║      ║░░░░░░░░║
    ║░░░①░░░║      ║░░░░░░░░║      ║░░░③░░░║
    ║░░░░░░░░║                      ║░░░░░░░░║
    ║░░░░░░░░║       <<PASS>>       ║░░░░░░░░║
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
               << You Succeeded !! >>
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

'''
yabawi_3 = '''

                                    ╭════════╮
                                    ║░░░░░░░░║
    ╭════════╮      ╭════════╮      ║░░░░░░░░║
    ║░░░░░░░░║      ║░░░░░░░░║      ║░░░③░░░║
    ║░░░░░░░░║      ║░░░░░░░░║      ║░░░░░░░░║
    ║░░░①░░░║      ║░░░②░░░║      ║░░░░░░░░║
    ║░░░░░░░░║      ║░░░░░░░░║      
    ║░░░░░░░░║      ║░░░░░░░░║       <<PASS>>
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
               << You Succeeded !! >>
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

'''
import random

hart = 40

print(yabawi)

winning_num = random.randint(1,3)

print(winning_num)
while hart > 0:
     print("\n<<<너의 남은 목숨의 개수 : % d >>>\n" % hart)
     user_choice = int(input("당신의 앞에 세 개의 엎어져 있는 컵이 보일 것이다.\n\n이 세 개의 컵 중에 <<PASS>> 티켓이 들어있는 컵을 맞추어라.\n\n어느 것을 선택하겠는가? 1, 2, 3 >>"))
     if user_choice == winning_num:         
        if user_choice ==1:
            print(yabawi_1)
        elif user_choice ==2:
            print(yabawi_2)
        elif user_choice ==3:
            print(yabawi_3)
        print("<<PASS>> 티켓을 찾아냈군. 다음 단계로 넘어가지\n")
        break
     elif user_choice != winning_num and user_choice < 4:
        print("\n이 바보같은 녀석! 넌 틀린 선택을 했어. 너의 목숨 %d개 중에서 10개를 뺏어간다.\n" % hart)
        hart -= 10
        print("------------------------------------------------------------------------")
        continue
     elif user_choice > 3:
        print("\n⭙다시 한번 문제를 잘 읽고 주어진 문제를 다시 읽고 제대로 입력하라.⭙\n")
        print("------------------------------------------------------------------------")

        continue
if hart == 0:
     print("\n나약한 자식, 너의 목숨은 이제 0이다.\n게임은 끝났어!\n")

user_choice=int(input("번호를 선택하시오(1,2,3): "))

hart = 40

if user_choice==1:
    while hart > 0:
        print("바다가 뜨거우면?")
        answer=str(input())
        print("너의 목숨은 %d만큼 남았다." % hart)
        if (answer == "열받아"):
            print("정답입니다")
            break
        else:
            print("힌트는 답에 '바다'라는 단어는 없음")
            hart -= 10
            print("너는 목숨 10개를 잃어 %d만큼 남았다." %hart)
            continue
        
elif user_choice==2:
    while hart>0:
        print("우유가 쓰러지면?")
        answer=str(input())
        print("너의 목숨은 %d만큼 남았다."%hart)
        if(answer == "아야"):
            print("정답입니다")
            break
        else:
            print("힌트는 글자를 여러 각도에서 보세요")
            hart-=10
            print("너는 목숨 10개를 잃어 %d만큼 남았다."%hart)
            continue
        
else:
    while hart>0:
        print("논리적인 사람이 총을 쏘면?")
        answer=str(input())
        print("너의 목숨은 %d만큼 남았다"%hart)
        if(answer == "타당타당"):
            print("정답입니다")
            break
        else:
            print("힌트는 효과음입니다.")
            hart
door = '''

    ┏━━━━━━━━━━━━┓       ┏━━━━━━━━━━━━┓       ┏━━━━━━━━━━━━┓      
    ┃            ┃       ┃            ┃       ┃            ┃      
    ┃            ┃       ┃            ┃       ┃            ┃
    ┃            ┃       ┃            ┃       ┃            ┃
    ┃     ①     ┃       ┃     ②     ┃       ┃     ③     ┃
    ┃            ┃       ┃            ┃       ┃            ┃
    ┃            ┃       ┃            ┃       ┃            ┃
    ┃            ┃       ┃            ┃       ┃            ┃
 ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩
 ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩


'''
print(door)

while True:
    print("*기회는 한번! 행운을 빈다*")
    door_number=int(input("문을 선택하시오(1/2/3): "))
    if door_number==1:
        #무한루프(처음으로 돌아감)
        print("처음으로 돌아감")  #처음화면이랑 이어서해야됨 
        break
    elif door_number==2:
        print("게임을 종료합니다!")
        print("<당신의 목숨은 n개 입니다>")   #목숨변수 선언해야됨 #%(d)%목숨변수
        break
    elif door_number==3:
        print("당신의 목숨은 0개 입니다.")  
        print("다음에 또 보기를 빈다.")
        break
    else:
        print("문을 잘못 선택하였다. 다시 입력해라! ")





    
    

