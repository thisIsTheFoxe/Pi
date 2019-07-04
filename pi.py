#! /usr/bin/env python
"""
Pi In Bf interpreter
@author stranjo and thotypous
"""
import sys, random

def bf(string):


    dpointer = pointer = 0
    plist = [0]*3000
    stack = []
    string = list(string)
    
    while pointer < len(string):
        if pointer == 0:
            stack.append(-1)
            
        if string[pointer] == '+':
            plist[dpointer] +=1
            plist[dpointer] &= 0xFF

        elif string[pointer] == '-':
            plist[dpointer] -= 1
            plist[dpointer] &= 0xFF
            
        elif string[pointer] == '>':
            dpointer += 1
            
        elif string[pointer] == '<':
            dpointer-=1
            if dpointer < 0: dpointer = 0
            
        elif string[pointer] == ']':
            pointer = stack.pop()
            
        elif string[pointer] == '[':
            if plist[dpointer]:
                stack.append(pointer-1)
            else:
                while string[pointer] != ']': pointer+=1
            
        elif string[pointer] == '.':
            sys.stdout.write(chr(plist[dpointer]))
            sys.stdout.flush()
        elif string[pointer] == ',':
	    lines = sys.stdin.readline()
	    if(len(lines) == 0):
		plist[dpointer] = 0
	    else:
            	plist[dpointer] = ord(lines[0])
            sys.stdin.flush()
        pointer+=1

def pi2bf(string):
    #print("PI2BF")
    out = ""
    t = { 0:'>', 1:'<', 2:'+', 3:'-', 4:'.', 5:',', 6:'[', 7:']' }
    k, a, b, a1, b1, r = 2, 4, 1, 12, 4, True
    while r:
        p, q, k = k*k, 2*k+1, k+1
        a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
        d = int(a / b)
        d1 = int(a1 / b1)
        while d == d1:
            if len(string):
                c = string[0]
                string = string[1:]
            else: c = ""
            if len(c) == 0:
                r = False
                break
            try: c = int(c)
            except: continue
            if c != d: out += t[c - (c > d)]
            a, a1 = 10*(a%b), 10*(a1%b1)
            d, d1 = int(a/b), int(a1/b1)
    return out

def bf2pi(string):
    random.seed()
    out = ""
    t = { '>':0, '<':1, '+':2, '-':3, '.':4, ',':5, '[':6, ']':7 }
    k, a, b, a1, b1, cl, r = 2, 4, 1, 12, 4, random.randint(20,30), True
    while r:
        p, q, k = k*k, 2*k+1, k+1
        a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
        d = int(a / b)
        d1 = int(a1 / b1)
        while d == d1:
            if cl:
                out+= str(d)
                cl -= 1
            else:
                if len(string):
                    c = string[0]
                    string = string[1:]
                else: c = ""
                if len(c) == 0:
                    r = False
                    break
                try: c = t[c]
                except: continue
                out += str(c + (c >= d))
                cl = random.randint(2,7)
            a, a1 = 10*(a%b), 10*(a1%b1)
            d, d1 = int(a/b), int(a1/b1)
    return "%s.%s"%(out[0],out[1:])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        #reading from stdin
        bf(pi2bf(sys.stdin.read()))

    elif sys.argv[1] == '-':
        bf(pi2bf(" ".join(sys.argv[2:])))
    elif sys.argv[1] == '-bf':
        bf(" ".join(sys.argv[2:]))
    elif sys.argv[1] == '--bf':
        f = open(sys.argv[2])
        bf(f.read())
    elif sys.argv[1] == '--convert':
        f = open(sys.argv[2])
        print(bf2pi(f.read()))
    elif sys.argv[1] == '-c':
        print(bf2pi(" ".join(sys.argv[2:])))
    elif sys.argv[1] == '--tobf':
        f = open(sys.argv[2])
        print(pi2bf(f.read()))
    elif sys.argv[1] == '-2bf':
        print(pi2bf(" ".join(sys.argv[2:])))
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("""pi language commands:
                * -bf: parses a bf command
                * --bf: parses a bf file
                * - : parses a pi number from command line
                * -h --help: displays dis help
                * --convert: convert a bf file into pi
                * -c: convert a bf command into pi
                * --tobf convert a pi file into bf
                * -2bf convert a pi command into bf""")
    else:
        f = open(sys.argv[1])
        bf(pi2bf(f.read()))

