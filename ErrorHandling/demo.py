def colorize(text,color):
    if type(text) is not str:
        raise TypeError('text must be instance of str')
    print(f'printed {text} in {color}')

colorize('upal','green')
colorize(1,'green')