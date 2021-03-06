# MyPong의 주된 파일을 만듭니다.

from tkinter import *
import table, ball, bat

# 전역변수 선언
x_velocity = 10
y_velocity = 0
score_left = 0
score_right = 0
first_serve = True

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
    global first_serve
    global score_left
    global score_right
	# 첫번째 서브를 기다립니다
    if (first_serve == True):
	    my_ball.stop_ball()
	    first_serve = False

    # 공이 배트에 충돌했는지 감지합니다
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

    # 공이 왼쪽 벽에 충돌했는지 감지합니다
    if (my_ball.x_posn <= 3):
    	my_ball.stop_ball()
    	my_ball.start_position()
    	bat_L.start_position()
    	bat_R.start_position()
    	my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
    	my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
    	score_left = score_left + 1
    	if (score_left >= 10):
    		score_left = "W"
    		score_right = "L"
    	first_serve = True
    	my_table.draw_score(score_left, score_right)

    # 공이 오른쪽 벽에 충돌했는지 감지합니다
    if (my_ball.x_posn + my_ball.width >= my_table.width-3):
    	my_ball.stop_ball()
    	my_ball.start_position()
    	bat_L.start_position()
    	bat_R.start_position()
    	my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
    	my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
    	score_right = score_right + 1
    	if (score_right >= 10):
    		score_right = "W"
    		score_left = "L"
    	first_serve = True
    	my_table.draw_score(score_left, score_right)

    my_ball.move_next()
    window.after(50, game_flow)


def restart_game(master):
    global score_left
    global score_right
    my_ball.start_ball(x_speed=x_velocity, y_speed=0)
    if (score_left=="W" or score_left=="L"):
        score_left = 0
        score_right = 0
    my_table.draw_score(score_left, score_right)



# 배트를 제어하기 위해 키보드의 키에 연결
window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)


# 스페이스 바를 눌렀을 때 게임을 재시작하도록 연결합니다.
window.bind("<space>", restart_game)


# game_flow 반복문 호출
game_flow()

# GUI를 계속 그리는 반복문 시작 (tkenter 반복문 프로세스)
window.mainloop()
