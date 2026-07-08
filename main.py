import random
import time

def invest_in_business
    print('Вы вкладываете деньги в новый бизнес')
    time.sleep(2)
    print("Рынок анализируется, команда работает, клиенты появляются")
    time.sleep(2)

    outcomes = [
        "К сожалению, проект не взлетел.Бизнес прогорел."
        "Поздравляем Бизнес пошёл в рост и стал прибыльным."
    ]
    
    result = random.choice(outcomes)
    print(result)

    if "прогорел" in result:
        print("Но у вас есть ценные уроки.В следующий раз будете умнее")
    else:
        print("Вы получили прибыль и расширяете бизнес по стране.")