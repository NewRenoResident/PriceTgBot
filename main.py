
from typing import final
import logging
from aiogram import Bot, Dispatcher, executor, types
import pendulum
import json

def time():
    now = pendulum.now("Europe/Moscow")
    Weekends_or_weekdays = 'Weekdays'
    print(now.day_of_week)
    print()
    if now.day_of_week > 5 and now.day_of_week != 0:
        Weekends_or_weekdays = 'Weekends'
    
    timelist = [[8, 9, 10, 11, 12], [13], [14, 15], [16], 
    [17, 18, 19], [20], [21], [22, 23, 0, 1, 2, 3, 4, 5, 6, 7]]
    pathlists = [
    [Weekends_or_weekdays, '8-12'],
    [Weekends_or_weekdays, '13'],
    [Weekends_or_weekdays, '14-15'],
    [Weekends_or_weekdays, '16'],
    [Weekends_or_weekdays, '17-19'],
    [Weekends_or_weekdays, '20'],
    [Weekends_or_weekdays, '21'],
    [Weekends_or_weekdays, '22-7']]
    
    for i in range(len(timelist)):
        if now.hour in timelist[i]:
            return pathlists[i]


def result_str():
    currentDateTimeAndSoOn = time()
    if currentDateTimeAndSoOn[1] == '22-7':
        with open("C:/PriceTgBot/night.json",'r', encoding='utf-8') as file:

            now = pendulum.now("Europe/Moscow")
            choose = "OtherDays"
            if now.day_of_week == 5 and not now.hour in [0, 1, 2, 3, 4, 5, 6, 7]:
                choose = "FridayAndSaturday"
            elif now.day_of_week == 6:
                choose = "FridayAndSaturday"
            elif now.day_of_week == 0 and now.hour in [0, 1, 2, 3, 4, 5, 6, 7]:
                choose = "FridayAndSaturday"
                
            data = file.read()
            data = json.loads(data)
            
            return f'''
            Общий зал:
            Час - {data[choose]["Общий зал"]["Час"]}
            10 Часов Ночь - {data[choose]["Общий зал"]["10 Часов Ночь"]}

            Буткемп - VIP:
            Час - {data[choose]["Буткемп - VIP"]["Час"]}
            10 Часов Ночь - {data[choose]["Буткемп - VIP"]["10 Часов Ночь"]}
            
            Буткемп Pro:
            Час - {data[choose]["Буткемп Pro"]["Час"]}
            10 Часов Ночь - {data[choose]["Буткемп Pro"]["10 Часов Ночь"]}

            Аренда TV 65:
            Час - {data[choose]["Аренда TV 65"]["Час"]}
            10 Часов Ночь - {data[choose]["Аренда TV 65"]["10 Часов Ночь"]}

            '''
    with open("C:/PriceTgBot/sheulder.json", 'r', encoding='UTF-8') as file:
        data = file.read()
        data = json.loads(data)
        return f'''
Общий зал:
Час - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Общий зал"]["Час"]}
3 часа - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Общий зал"]["3 Часа"]}
5 часов - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Общий зал"]["5 Часов"]}

Буткемп - VIP
Час - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Буткемп - VIP"]["Час"]}
3 часа - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Буткемп - VIP"]["3 Часа"]}
5 часов - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Буткемп - VIP"]["5 Часов"]}

Буткемп Pro
Час - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Буткемп Pro"]["Час"]}
3 часа - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Буткемп Pro"]["3 Часа"]}
5 часов - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Буткемп Pro"]["5 Часов"]}

Аренда TV 65
Час - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Аренда TV 65"]["Час"]}
3 часа - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Аренда TV 65"]["3 Часа"]}
5 часов - {data[currentDateTimeAndSoOn[0]][currentDateTimeAndSoOn[1]]["Аренда TV 65"]["5 Часов"]}
'''

# Объект бота
bot = Bot(token="5658784604:AAEcdaf2AxVe_drdbawwrma-_f4sTzW_L_I")
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup()
	button_1 = types.KeyboardButton(text="Прайс")
	keyboard.add(button_1)
	button_2 = "Акции"
	keyboard.add(button_2)
	await message.answer('Добавляю конпки', reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Прайс")
async def cmd_test1(message: types.Message):
    await message.reply(result_str(), parse_mode=types.ParseMode.HTML)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True) 

