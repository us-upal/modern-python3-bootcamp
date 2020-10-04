
def fav_color(**kwargs):
    for person,color in kwargs.items():
        print(f'{person}s fvrt clor is {color}' )

fav_color(upal='green',elon='blue')