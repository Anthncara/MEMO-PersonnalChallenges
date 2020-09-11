print("###  This program converts milliseconds into hours, minutes, and seconds ###")
print('(To exit the program, please type "exit")')
while True:
    ms = input("Please enter the milliseconds (should be greater than zero) : ")
    if ms == "exit":
        print("Exiting the program... Good Bye")
        break
    if ms.isdigit():
        print(convert_miliseconds(int(ms)))
        print(convert_miliseconds2(int(ms)))
        print(convert_miliseconds3(int(ms)))
    else:
        print( "Not Valid Input !!!")
def convert_miliseconds2(ms):
    segments = [{'div':3600000, 'remainder':24, 'text':' hour/s '},
                {'div':60000, 'remainder':60,'text':' minute/s '},
                {'div':1000, 'remainder':60,'text':' second/s '}]
    result = ""
    for segment in segments:
        value = (ms // segment['div']) % segment['remainder']
        result += f"{value and (str(value) + segment['text']) or ''}"
        return f"{result or ('just ' + str(ms) + ' miliseconds')}"
from datetime import datetime 
def convert_miliseconds3(ms):
    dtime = datetime.utcfromtimestamp(ms/1000).time() 
    result = ""
    result += f"{dtime.hour and (str(dtime.hour) + ' hour/s ') or ''}"
    result += f"{dtime.minute and (str(dtime.minute) + ' minute/s ') or ''}"
    result += f"{dtime.second and (str(dtime.second) + ' second/s ') or ''}"
    return f"{result or ('just ' + str(ms) + ' miliseconds') }"