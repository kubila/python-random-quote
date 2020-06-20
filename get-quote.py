import random


def primary():

    f = open("quotes.txt", 'a')
    #quotes = f.readlines()
    lazyCat = "lazy cat jums over the jox in a second"
    lazyDog = "lazy dog jumps over the cat in two seconds"
    ragnarQuote = "Man is the master of his own fate, not the gods. Gods are man's creation, to give answers that they are too afraid to give themselves."
    f.write(lazyCat + '\n')
    f.write(lazyDog + '\n')
    f.write(ragnarQuote + '\n')
    f.close()
   # last = len(quotes) - 1
   # rnd = random.randint(0, last)
   # print(quotes[rnd])

    c = open('cats.txt', 'a+')
    catThings = ['sleeping', 'meowing',
                 'eating catnips', 'watching birds', 'sunbathing', 'sleeping_again']
    for i in catThings:
        c.write('\n%s' % i)
    c.close()

    coronaThings = ['corona_virus', 'sitting_all_day',
                    'losing_muscle', 'gaining_weight', 'how_much_spike_it_has']
    a = open('corona.txt', 'a')
    a.writelines('%s\n' % i for i in coronaThings)
    a.close()

    devThings = ['github', 'frontal_lob', 'catLoveIndex', 'monthlyPizzaOrderRate',
                 'messing_up_with_python', 'how_much_overweight', 'asociality_level', 'crazy_mushrooms']
    with open('devs.txt', 'a+') as f:
        f.writelines('%s\n' % d for d in devThings)
    f.close()


if __name__ == "__main__":
    primary()
