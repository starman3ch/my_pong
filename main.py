# MyPong의 주된 파일을 만듭니다.

from tkinter import *
import table, ball, bat

# 전역변수 선언
x_velocity = 10
y_velocity = 10

# tkinter 공장으로부터 윈도우 주문
window = Tk()
window.title("MyPong")

# 테이블 공장으로부터 테이블 주문
my_table = table.Table(window, net_colour="green", vertical_net=True)

# 볼 공장으로부터 볼을 주문합니다.
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity, 
                    width=24, height=24, colour="red", x_start=288, y_start=188)

# 배트 공장으로부터 왼쪽과 오른쪽 배트를 주문합니다
bat_L = bat.Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, colour="blue")
bat_R = bat.Bat(table=my_table, width=15, height=100, x_posn=575, y_posn=150, colour="yellow")

# 함수
def game_flow():
    # 공이 배트에 닿으면
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

    my_ball.move_next()
    window.after(50, game_flow)

# 배트를 제어하기 위해 키보드의 키에 연결
window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

# game_flow 반복문 호출
game_flow()

# GUI를 계속 그리는 반복문 시작
window.mainloop()
