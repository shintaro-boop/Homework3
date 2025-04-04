
def scrabble(word):
    costbukv = {1 : ('а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т'),
                2 : ('д', 'к', 'л', 'м', 'п', 'у'),
                3 : ('б', 'г', 'ь', 'а', 'я'),
                4 : ('ы', 'й'),
                5 : ('ж', 'з', 'х', 'ц', 'ч'),
                8 : ('ф', 'ш', 'э', 'ю'),
                15 :('ъ')
                }
    costword = {i : i for i in word}
    for key, value in costword.items() :
        if costword[value] == costbukv[value] :
            costword[key] = costbukv[key]
        else :
            c = costword.keys()
            points = sum(c)
        return print(points)
scrabble('привет')