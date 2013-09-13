
def quiz(file_name):
    import random
    import sys
    if not file_name:
        print('no file name')
        sys.exit()
    with open(file_name) as af:
        statecap= af.read()
    states = statecap.strip().split('\n')
    state_capitals={}
    for each in states:
        (stat,cap)=each.split(',')
        state_capitals[stat] = cap
    while True:
        chosen=random.choice(list(state_capitals.keys()))
        print(chosen + '?')
        city=input()
        if city == state_capitals[chosen]:
            print("its correct!!")
        elif city == 'Exit':
            break
        else:
            print("answer is wrong. the correct answer is " + state_capitals[chosen])

        



    
    
    
    



