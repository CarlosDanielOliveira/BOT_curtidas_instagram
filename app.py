import pyautogui as pa
from time import sleep 
import webbrowser
import pyperclip
import pyscreeze


def logout():
    pa.click(174,779, duration=3)
    pa.click(51,978, duration=2)
    pa.click(76,912, duration=2)
    pa.click(1900,24, duration=3)
while True:
    #Abrir instagram

    sleep(7)

    url = "https://www.instagram.com/"
    webbrowser.open(url)

    #informações login
    sleep(2.5)
    login = pa.prompt(text= 'Digite seu login, por favor:', title= 'Informações de Login')
    passw = pa.password(text= 'Senha: ', title= 'Informações de Login', mask='*')

    #fazer login


    login_ref = pa.locateCenterOnScreen('login.png')
    pa.moveTo(login_ref[0], login_ref[1],duration=1.5)
    sleep(0.5)
    pa.click()

    pa.typewrite(login)
    sleep(1)
    pa.press('tab')
    sleep(1)
    pa.typewrite(passw)
    sleep(2)


    pa.moveTo(1179,462, duration=1)
    pa.leftClick()
    sleep(4)

    pa.click(1101,634, duration= 2)

    sleep(4)

    #pesquisar marca

    pa.moveTo(44,330, duration=1)
    pa.leftClick()
    sleep(3)
    pa.typewrite('nike')
    sleep(2)


    nike = pa.locateCenterOnScreen('nike.png')
    pa.moveTo(nike[0], nike[1],duration=1)
    sleep(1)
    pa.click()

    #verificar postagem atual 
    sleep(3)
    pa.scroll(-100)
    pa.click(732,564, duration=1)

    sleep(2)


    pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
    likes = pa.locateCenterOnScreen ('likes.png')
    sleep(1.5)

    if likes is not None:
        sleep(10)
        logout()
        
        

    #curtir e comentar
    elif likes == None:
        pa.click(1047, 863, duration=1)
        sleep(1)
        pa.click(1146,977,duration=1)
        pa.typewrite('Amazing!!!')
        sleep(1.5)
        pa.press('Enter')
        sleep(10)
        logout()
        
        

























