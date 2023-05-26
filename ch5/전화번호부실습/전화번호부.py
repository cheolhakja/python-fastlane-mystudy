import pandas as pd 

df = pd.DataFrame(columns=["Name", "Age", "Money"]) #전역변수

def main_menu() -> int:
    menu = int(input("1에서 5사이의 수를 입력하시오"))


    """사용자의 입력을 받아서 검증하고 적절하다면 정수로 반환합니다."""

    return menu  # 교체


def show_all():
    """모든 데이터 출력"""

    pass


def find_person():
    """이름을 입력받고 그 이름으로 찾아서 해당 데이터 출력"""

    pass


def update_person():
    """사람 추가 또는 수정
    사용자로부터 이름, 전화번호, 이메일을 입력받아서
    이미 있는 이름이면 업데이트를 하고
    없는 이름이면 새로 추가
    """
    list_row = ["황동혁", "010-1111-1111", "hwang@naver.com"]


    name = "황동혁"
    phone_num = "010-1111-1111"
    email = "hwang@naver.com"
    criterion = df["Name"] == name



    if(name in df['Name'].values):
        df.loc[name] = [name, phone_num, email]
    else:
        df.loc[len(df)] = [name, phone_num, email]


def delete_person():
    """이름을 입력받아서 데이터 삭제"""

    pass



#데이터프레임을 초기화할 때 비어있는 기둥들을 추가할 수도 있습니다.
if __name__ == "__main__":

    

    df["Name"] = []
    df["phone"] = []
    df["email"] = []

    #추가를 어떻게하지?

'''
while (selected := main_menu()) != 5:  # 5는 종료 메뉴

    if(selected == 1):


        pass

    elif(selected == 2):
        pass
    elif(selected == 3):
        pass
    else:
        pass
    

else:
    # 종료하기 전 파일로 데이터 저장
    pass

    print("종료합니다.")'''