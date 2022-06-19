from flask import Flask, request
from flask_cors import CORS

import json
application = Flask(__name__)
data = {}
CORS(application)


@application.route('/acetaria', methods=["GET", "POST", "OPTIONS"])
def choose_category():
    answers = ["нет", "нет", "да", "нет", "да", "нет", "нет", "да"]
    choose = ["Дизайн интерфейсов",
              "VK Mini Apps",
              "Web",
              "Мобильная разработка",
              "Анализ данных",
              "Оптимизация и RL",
              "GameDev",
              "Back End",
              "Маруся"]
    tts_choose = ["дизайн интерфэйсов",
              "вэ ка мини эпс",
              "вэб",
              "мобильная разработка",
              "анализ данных",
              "оптимизация и эр эл",
              "гейм дэв",
              "бэк энд",
              "маруся"]
    correct_answer = "Ты абсолютно прав!\n"
    correct_tts = "<speaker audio=marusia-sounds/game-win-1>  Ты ^абсалютно^ прав!\n"
    incorrect_answer = " К {сожалению}{^сажаленью^ - }, ты не прав!\n"
    incorrect_tts = "<speaker audio=marusia-sounds/game-loss-1> К ^сажаленью^ - ты не прав!\n"
    if request.method == "OPTIONS":
        return "OK"
    if request.method == "POST":
        req = json.loads(request.get_data().decode("UTF-8"))
        response = {}
        response["version"] = req["version"]
        response["session"] = req["session"]
        response["response"] = {"end_session": False}
        if req["session"]["user_id"] not in data:
            data[req["session"]["user_id"]] = {"count": 0, "points": 0}
        if data[req["session"]["user_id"]]["count"] == 0 and not (("acetaria" in req["request"]["command"] or "ацетария" in req["request"]["command"]) \
                and ("вездекод" in req["request"]["command"] or "вездеход" in req["request"]["command"] or "везде код" in req["request"]["command"])):
            response["response"]["text"] = "^Я не хочу на такое отвечать!^"
            response["response"]["end_session"] = True
        else:
            if data[req["session"]["user_id"]]['count'] > 0 and req["request"]["command"] not in ["да", "нет"]:
                response["response"]["text"] = "Не поняла твой ответ! Повтори его еще раз!"
                response["response"]["tts"] = "<speaker audio=marusia-sounds/game-ping-1>  Не понял`а твой отв`ет! ^Повтори^ его ещ`ё раз!"
            elif data[req["session"]["user_id"]]['count'] == 0:
                response["response"]["text"] = "Привет вездекодерам!"
                response["response"]["tts"] = "Привет вездек`одерам!"
                response["response"]["text"] += "\nЯ помогу тебе выбрать категорию на вездекоде!\nОтвечай на мои вопросы кратким ответом: Да или Нет\nНу что, давай начинать!\nПервый вопрос: \"Python++\" - это язык программирования?"
                response["response"]["tts"] += "<speaker audio=marusia-sounds/game-boot-1> - Я ^памаг`у^ теб`е в`ыбрать ^катег`орию^ на вездек`оде\nОтвеч`ай на мо`и вапр`осы кр`атким атв`етом Д`а или Н`ет\nНу ^что^?\n ^дав`ай^ начин`ать!\nП`ервый вопр`ос <speaker audio=marusia-sounds/music-gong-2> \nП`айтон плюс плюс\n ^эта яз`ык^ программ`ированья?"
                data[req["session"]["user_id"]]['count'] += 1
                data[req["session"]["user_id"]]['count'] %= 9
            elif data[req["session"]["user_id"]]['count'] == 1:
                if req["request"]["command"] == answers[data[req["session"]["user_id"]]['count'] - 1]:
                    response["response"]["text"] = correct_answer
                    response["response"]["tts"] = correct_tts
                    data[req["session"]["user_id"]]['points'] += 1
                else:
                    response["response"]["text"] = incorrect_answer
                    response["response"]["tts"] = incorrect_tts
                response["response"]["text"] += "Второй вопрос: Figma - это язык программирования?"
                response["response"]["tts"] += "Втор`ой вопр`ос <speaker audio=marusia-sounds/music-gong-2> \n Ф`игма \n ^эта яз`ык^ программ`ированья?"
                data[req["session"]["user_id"]]['count'] += 1
                data[req["session"]["user_id"]]['count'] %= 9
            elif data[req["session"]["user_id"]]['count'] == 2:
                if req["request"]["command"] == answers[data[req["session"]["user_id"]]['count'] - 1]:
                    response["response"]["text"] = correct_answer
                    response["response"]["tts"] = correct_tts
                    data[req["session"]["user_id"]]['points'] += 1
                else:
                    response["response"]["text"] = incorrect_answer
                    response["response"]["tts"] = incorrect_tts
                response["response"]["text"] += "Третий вопрос: Используется ли Swift для разработки приложений на MacOS и iOS?"
                response["response"]["tts"] += "Тр`етий вопр`ос <speaker audio=marusia-sounds/music-gong-2> \n ^Используется ли ^Свифт для разработки приложений на ^мак о эс^ и ^ай о эс^?"
                data[req["session"]["user_id"]]['count'] += 1
                data[req["session"]["user_id"]]['count'] %= 9
            elif data[req["session"]["user_id"]]['count'] == 3:
                if req["request"]["command"] == answers[data[req["session"]["user_id"]]['count'] - 1]:
                    response["response"]["text"] = correct_answer
                    response["response"]["tts"] = correct_tts
                    data[req["session"]["user_id"]]['points'] += 1
                else:
                    response["response"]["text"] = incorrect_answer
                    response["response"]["tts"] = incorrect_tts
                response["response"]["text"] += "Четвертый вопрос: Является ли HTTP безопасным протоколом передачи данных?"
                response["response"]["tts"] += "Четв`ёртый вопр`ос <speaker audio=marusia-sounds/music-gong-2> \n ^Является ли^ : эйч : ти : ти : пи безопасным протоколом передачи данных?"
                data[req["session"]["user_id"]]['count'] += 1
                data[req["session"]["user_id"]]['count'] %= 9
            elif data[req["session"]["user_id"]]['count'] == 4:
                if req["request"]["command"] == answers[data[req["session"]["user_id"]]['count'] - 1]:
                    response["response"]["text"] = correct_answer
                    response["response"]["tts"] = correct_tts
                    data[req["session"]["user_id"]]['points'] += 1
                else:
                    response["response"]["text"] = incorrect_answer
                    response["response"]["tts"] = incorrect_tts
                response["response"]["text"] += "Пятый вопрос: HTML - это язык разметки?"
                response["response"]["tts"] += "П`ятый вопр`ос <speaker audio=marusia-sounds/music-gong-2> \n эйч : тиэмэл \n эта ^яз`ык разм`етки^?"
                data[req["session"]["user_id"]]['count'] += 1
                data[req["session"]["user_id"]]['count'] %= 9
            elif data[req["session"]["user_id"]]['count'] == 5:
                if req["request"]["command"] == answers[data[req["session"]["user_id"]]['count'] - 1]:
                    response["response"]["text"] = correct_answer
                    response["response"]["tts"] = correct_tts
                    data[req["session"]["user_id"]]['points'] += 1
                else:
                    response["response"]["text"] = incorrect_answer
                    response["response"]["tts"] = incorrect_tts
                response["response"]["text"] += "Шестой вопрос: Является ли С объектно-ориентированным языком программирования?"
                response["response"]["tts"] += "Шэст`ой вопр`ос <speaker audio=marusia-sounds/music-gong-2> \n ^Является ли^ Си : объ`ектно орент`ированным язык`ом программ`ированья?"
                data[req["session"]["user_id"]]['count'] += 1
                data[req["session"]["user_id"]]['count'] %= 9
            elif data[req["session"]["user_id"]]['count'] == 6:
                if req["request"]["command"] == answers[data[req["session"]["user_id"]]['count'] - 1]:
                    response["response"]["text"] = correct_answer
                    response["response"]["tts"] = correct_tts
                    data[req["session"]["user_id"]]['points'] += 1
                else:
                    response["response"]["text"] = incorrect_answer
                    response["response"]["tts"] = incorrect_tts
                response["response"]["text"] += "Седьмой вопрос: В языке C++ float будет точнее, чем double?"
                response["response"]["tts"] += "Седьм`ой вопр`ос <speaker audio=marusia-sounds/music-gong-2> \n В языке Си плюс плюс фл`оут ^будет точн`ее^ - чем д`абл?"
                data[req["session"]["user_id"]]['count'] += 1
                data[req["session"]["user_id"]]['count'] %= 9
            elif data[req["session"]["user_id"]]['count'] == 7:
                if req["request"]["command"] == answers[data[req["session"]["user_id"]]['count'] - 1]:
                    response["response"]["text"] = correct_answer
                    response["response"]["tts"] = correct_tts
                    data[req["session"]["user_id"]]['points'] += 1
                else:
                    response["response"]["text"] = incorrect_answer
                    response["response"]["tts"] = incorrect_tts
                response["response"]["text"] += "Ну и последний, восьмой вопрос, будет очень и очень простой для тебя!\nВездекод - это хакатон для IT-специалистов?"
                response["response"]["tts"] += "Ну и посл`едний - восьм`ой вопр`ос - будет очень и очень простой для тебя!<speaker audio=marusia-sounds/music-gong-2> \nВездекод - ^это^ хакатон для ^ай ти^ -специалистов?"
                data[req["session"]["user_id"]]['count'] += 1
                data[req["session"]["user_id"]]['count'] %= 9
            elif data[req["session"]["user_id"]]['count'] == 8:
                if req["request"]["command"] == answers[data[req["session"]["user_id"]]['count'] - 1]:
                    response["response"]["text"] = correct_answer
                    response["response"]["tts"] = correct_tts
                    data[req["session"]["user_id"]]['points'] += 1
                else:
                    response["response"]["text"] = incorrect_answer
                    response["response"]["tts"] = incorrect_tts
                response["response"]["text"] += "Наиболее подходящая категория: " + choose[data[req["session"]["user_id"]]['points']] + "\nСпасибо, что поучаствовал в нашем тесте!"
                response["response"]["tts"] += "Наиб`олее подход`ящая категория - это " + choose[data[req["session"]["user_id"]]['points']]  + "\nСпасибо что ^поучаствовал^ в нашем т`эсте!"
                response["response"]["card"] = {"type": "MiniApp", "url": ["https://vk.com/app7598034"]}
                data[req["session"]["user_id"]]['points'] = 0
                data[req["session"]["user_id"]]['count'] += 1
                data[req["session"]["user_id"]]['count'] %= 9
                response["response"]["end_session"] = True
        return json.dumps(response)
    return "Навык для Маруси"


if __name__ == '__main__':
    application.run(host="localhost", port=3000, debug=False)
