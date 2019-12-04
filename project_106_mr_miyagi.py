# Game code ----------------------------------------------------------------
question = ['?', 'who', 'why', 'when', 'what', 'how', 'where']
miyagi_response = {'sensei': 'You are smart, but not wise. Address me as Sensei please.',
                   'block': 'Remember, best block, not to be there.',
                   'question': 'Questions are wise, but for now, wax on and wax off.',
                   'ignore': 'do not lose focus. Wax on. Wax off.',
                   'bye': 'Sometimes, what heart know, head forget.',}

def question_detect (your_response):
    for object in question:
        if object in your_response:
            return True
        else:
            continue

def miyagi_brain (your_response):
    if your_response[0:5] not in 'sensei':
        return miyagi_response['sensei']
    elif question_detect(your_response):
        return  miyagi_response['question']
    elif 'block' in your_response:
        return miyagi_response['block']
    elif 'peace' in your_response:
        return  miyagi_response['bye']
    else:
        return miyagi_response['ignore']


while True:
    your_response = input('(MR.Miyagi)... -.-').strip().lower()
    print(miyagi_brain(your_response))
    if 'peace' in your_response:
        break
