def intro():
    print("===== Tele-Adventure =====")
    print("당신은 미지의 방에서 눈을 떴습니다. 무전기가 있습니다.")
    print("방을 살펴보려면 'look'을 입력하고, 무전기를 사용하려면 'radio'를 입력하세요.")

def room():
    while True:
        command = input("\n무엇을 하시겠습니까? (look/radio/quit): ").strip().lower()
        if command == 'look':
            print("방 안에는 문이 하나 있습니다. 무전기가 책상 위에 놓여 있습니다.")
        elif command == 'radio':
            print("무전기를 켭니다... 잡음 속에서 희미하게 '도움이 필요하신가요?'라는 소리가 들립니다.")
            radio_event()
        elif command == 'quit':
            print("게임을 종료합니다.")
            break
        else:
            print("알 수 없는 명령입니다.")

def radio_event():
    while True:
        msg = input("무전기로 무엇을 전송하시겠습니까? ('도움', '구출', '뒤로'): ").strip()
        if msg == '도움':
            print("누군가 응답합니다. '곧 도착합니다. 문을 조심하세요.'")
            break
        elif msg == '구출':
            print("잡음만 들립니다. 다시 시도하세요.")
        elif msg == '뒤로':
            print("무전기를 내려놓습니다.")
            break
        else:
            print("알 수 없는 메시지입니다.")

if __name__ == "__main__":
    intro()
    room()