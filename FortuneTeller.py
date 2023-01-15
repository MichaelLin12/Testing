import requests
import re


class Oracle:
    
    def __init__(self):
        pass

    def predictFuture(self,s):
        s = self.synthesizeQuestion(s)
        r = requests.get(f'https://eightballapi.com/api?question=${s}?&lucky=true')
        return r.json()["reading"]

    def synthesizeQuestion(self,s):
        newS = ''
        s=s.strip()
        for char in s:
            if re.match('[A-Za-z]',char):
                newS+=char
            elif re.match(' ',char):
                newS+='+'
        
        newS = newS.lower()
        return newS

def main():
    ans = input('Do you want anything to be fortold?(y/n)')
    oracle = Oracle()
    while(ans == 'y' or ans == 'Y'):
        question = input('What is it that you need to be fortold?')
        print(oracle.predictFuture(question))
        ans = input('Do you want anything to be fortold?(y/n)')


if __name__ == '__main__':
    main()