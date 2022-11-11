import json
# from flask import Flask

#function Initialize data with json file path
def init():
    try:
        path = input('Initialize data with file path: ')
        with open(path) as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print(e)

#function to get room by id show match room by given room id. Show the notice message when the room is not found.
def getRoomById(data):
    roomId = int(input('getRoomById: '))
    for room in data['rooms']:
        if room['id'] == roomId:
            print({'id': room['id'], 'name': room['name']})
            return
    print('No room with id: ' , roomId)

#function to get all room show all room in json file
def getAllRoom(data):
    for room in data['rooms']:
        print({'id': room['id'], 'name': room['name']})

#function to get chat by id show match chat by given chat id. Show the notice message when the chat is not found.
def getChatById(data):
    chatId = int(input('getChatById: '))
    for room in data['rooms']:
        for chat in room['chats']:
            if chat['id'] == chatId:
                print({'id': chat['id'], 'name': chat['name'], 'messages': chat['messages']})
                return
    print('No chat with id: ' , chatId)

#function to get all chat in room show all chat in room by given room id. Show the notice message when the room is not found.
def getAllChatInRoom(data):
    roomId = int(input('getAllChatInRoom: '))
    for room in data['rooms']:
        if room['id'] == roomId:
            for chat in room['chats']:
                print({'id': chat['id'], 'name': chat['name'], 'messages': chat['messages']})
            return
    print('No room with id: ' , roomId)


if __name__ == '__main__':
    print('Action\n1. Intialize data\n2. getRoomById\n3. getAllRoom\n4. getChatById\n5. getAllChatInRoom')
    while True:
        selection = int(input('Select the action: '))
        if selection == 1:
            data = init()
        elif selection == 2:
            getRoomById(data)
        elif selection == 3:
            getAllRoom(data)
        elif selection == 4:
            getChatById(data)
        elif selection == 5:
            getAllChatInRoom(data)
        else:
            print('Invalid selection')


# app = Flask(__name__)
# @app.route('/form')
# def form():
#     return render_template('form.html')

# @app.route('/api/getRoomById', methods=['GET'])
# def getRoomById():
#     data = init()
#     roomId = int(input('getRoomById: '))
#     for room in data['rooms']:
#         if room['id'] == roomId:
#             print({'id': room['id'], 'name': room['name']})
#             return
#     print('No room with id: ' , roomId)