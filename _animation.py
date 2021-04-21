import os, time

os.system('cls')
fileNames = []
delayr = .0333333
repeat = 2

try:
    if os.path.exists('data/txt'):
        fileNames = os.listdir('data/txt')
        fileNames = [i[:-4] for i in fileNames]
        fileNames = [int(i) for i in fileNames]
        fileNames.sort()
        fileNames = [str(i) for i in fileNames]
except:
    print('The path was not found')

while True:
    delay = float(input('what is the animation delay?'))
    repeat = int(input('how many times it will repeat?'))
    if (isinstance(delayr, float) and delayr > 0 and delayr < 2) and (isinstance(repeat, int) and repeat > 0):
        print('Creating the animation....')
        break
    else:
        print('Please, insert a valid number' )

def animator(filesnames, delay = .041, repeats = 10):
    frames = []
    for name in filesnames:
        with open ('data/txt/' + str(name) + '.txt' , 'r', encoding='utf8') as f:
            frames.append(f.readlines())

    for i in range(repeats):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            print('\033c')

animator(fileNames, delayr, repeat)
