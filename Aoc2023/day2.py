import sys
file = open('day2.txt').read().strip()
gameCounter = 0
totalScore = 0

for line in file.split('\n'):
    gameCounter += 1
    red = 0
    green = 0
    blue = 0
    game = line.split(':')
    sets = game[1].split(';')
    isValidGame = True
    for subset in sets:
        cubes = subset.split(',')
        for singleCube in cubes:
            singleCubeCounter = singleCube.split(' ')
            if(singleCubeCounter[2] == 'blue'):
                blue = blue if blue > int(singleCubeCounter[1]) else int(singleCubeCounter[1])
            elif(singleCubeCounter[2] == 'red'):
                red = red if red > int(singleCubeCounter[1]) else int(singleCubeCounter[1])
            elif(singleCubeCounter[2] == 'green'):
                green = green if green > int(singleCubeCounter[1]) else int(singleCubeCounter[1])
            else:
                isValidGame = False
                break
    
    totalScore += red*blue*green


print(totalScore)