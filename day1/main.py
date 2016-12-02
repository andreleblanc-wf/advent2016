#!/usr/bin/env python

'''
Advent of Code 2016 - Day 1
Andre LeBlanc  (andre.leblanc@workiva.com)
'''

input = '''L5, R1, R4, L5, L4, R3, R1, L1, R4, R5, L1, L3, R4, L2, L4, R2, L4, L1, R3, R1, R1, L1, R1, L5, R5, R2, L5, R2, R1, L2, L4, L4, R191, R2, R5, R1, L1, L2, R5, L2, L3, R4, L1, L1, R1, R50, L1, R1, R76, R5, R4, R2, L5, L3, L5, R2, R1, L1, R2, L3, R4, R2, L1, L1, R4, L1, L1, R185, R1, L5, L4, L5, L3, R2, R3, R1, L5, R1, L3, L2, L2, R5, L1, L1, L3, R1, R4, L2, L1, L1, L3, L4, R5, L2, R3, R5, R1, L4, R5, L3, R3, R3, R1, R1, R5, R2, L2, R5, L5, L4, R4, R3, R5, R1, L3, R1, L2, L2, R3, R4, L1, R4, L1, R4, R3, L1, L4, L1, L5, L2, R2, L1, R1, L5, L3, R4, L1, R5, L5, L5, L1, L3, R1, R5, L2, L4, L5, L1, L1, L2, R5, R5, L4, R3, L2, L1, L3, L4, L5, L5, L2, R4, R3, L5, R4, R2, R1, L5'''

moves = input.split(", ")

def turnleft(facing):
    if facing == 'N':
        return "W"
    elif facing == "E":
        return "N"
    elif facing == "S":
        return "E"
    elif facing == "W":
        return "S"

def turnright(facing):
    if facing == 'N':
        return 'E'
    elif facing == 'E':
        return 'S'
    elif facing == 'S':
        return 'W'
    elif facing == 'W':
        return 'N'

def domove(pos, direction, blocks):
    
    if direction == 'N':
        newpos = (pos[0] + blocks, pos[1])
    elif direction == 'E':
        newpos = (pos[0], pos[1] + blocks)
    elif direction == 'S':
        newpos = (pos[0] - blocks, pos[1])
    elif direction == 'W':
        newpos = (pos[0], pos[1] - blocks)
    print "Moving %s %s From %s => %s" % (blocks, direction, pos, newpos)
    return newpos

def parta():
    facing = "N"
    pos = (0, 0)
    for move in moves:
        if move.startswith("L"):
            facing = turnleft(facing)
        else:
            facing = turnright(facing)

        pos = domove(pos, facing, int(move[1:]))


    print "End Position: ", pos
    print "Distance: ", abs(pos[0]) + abs(pos[1])


def get_points(pos, newpos):
    if pos[0] != newpos[0]:
        # N/S
        if pos[0] < newpos[0]:
            for x in range(pos[0]+1, newpos[0]+1):
                yield (x, pos[1])
        elif pos[0] > newpos[0]:
            for x in range(pos[0]-1, newpos[0]-1, -1):
                yield (x, pos[1])

    elif pos[1] != newpos[1]:
        # E/W
        if pos[1] < newpos[1]:
            for y in range(pos[1]+1, newpos[1]+1):
                yield (pos[0], y)
        elif pos[1] > newpos[1]:
            for y in range(pos[1]-1, newpos[1]-1, -1):
                yield (pos[0], y)


def partb():
    facing = "N"
    pos = (0, 0)
    visited = set((0, 0))
    for move in moves:
        if move.startswith("L"):
            facing = turnleft(facing)
        else:
            facing = turnright(facing)

        newpos = domove(pos, facing, int(move[1:]))
        for p in get_points(pos, newpos):
            print p
            if p in visited:
                print "already visited", p
                print "Actual Location: ", p
                print "Actual Distance: ", abs(p[0]) + abs(p[1])
                return

            visited.add(p)
        pos = newpos



parta()
partb()


