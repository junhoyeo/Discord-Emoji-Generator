import sys
def Emoji(text):
    emoji=''
    for letter in text:
        if letter.isalpha(): #숫자가 아닌 문자
            if 65<=ord(letter)<=90 or 97<=ord(letter)<=122: #알파벳
                emoji=emoji+':regional_indicator_'+letter.lower()+': '
            else: #알파벳 이외의 문자
                emoji=emoji+letter
        else: #숫자
            try:
                if int(letter) is 0:
                    emoji=emoji+':zero: '
                elif int(letter) is 1:
                    emoji=emoji+':one: '
                elif int(letter) is 2:
                    emoji=emoji+':two: '
                elif int(letter) is 3:
                    emoji=emoji+':three: '
                elif int(letter) is 4:
                    emoji=emoji+':four: '
                elif int(letter) is 5:
                    emoji=emoji+':five: '
                elif int(letter) is 6:
                    emoji=emoji+':six: '
                elif int(letter) is 7:
                    emoji=emoji+':seven: '
                elif int(letter) is 8:
                    emoji=emoji+':eight: '
                elif int(letter) is 9:
                    emoji=emoji+':nine: '
                else:
                    emoji=emoji+letter
            except ValueError: #숫자가 아니면서 isalpha() 통과하는 문자 걸러내기위함(백슬래시 등)
                if letter==' ': #공백은 너무 티가 안나서 2칸 띄어쓰기로 바꿔버리는걸루~
                    emoji=emoji+'  '
                else:
                    emoji=emoji+letter
    print(emoji)

text=input()
if text=='' or text=='help' or text=='usage':
    sys.stdout.write('type \'file\' to generate emoji from file')
elif text=='file':
    filename=input('input text file name to generate discord emoji : ')
    try:
        f=open(filename, 'r')
        for buff in f.readlines():
            Emoji(buff)
    except IOError:
        sys.stdout.write("cannot open file '%s'\n" % filename)
else:
    Emoji(text)
