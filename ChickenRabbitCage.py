# coding:utf-8

"""

P.S. : The translation is not accurate!

Chicken rabbit cages are one of the mathematical problems of ancient China.
About 1500 years ago, this interesting question was recorded <Sun Tzu Arithmetic>[1].
The book goes translated into English like this[2]:
    Now there are chickens and rabbits in the same cage,
    with thirty-five heads on top and ninety-four feet on the bottom,
    ask how many chickens and rabbits there are?

-------------------------------------------------------------------------------

[1]: <Sun Tzu Arithmetic> The name of the book is translated as Chinese is 《孙子算经》(Sun Zi Suan Jing)
[2]: The original text is as follows:
        今有雉兔同笼，
        Now there are chickens and rabbits in the same cage,
        上有三十五头，
        with thirty-five heads on top
        下有九十四足，
        and ninety-four feet on the bottom,
        问雉兔各几何？
        ask how many chickens and rabbits there are?

"""


class NumberError(Exception):
    """
    Chickens' num isn't positive number.
    """

    def __init__(self, *args, **kwargs):
        pass


def Chicken_rabbit_cages_1(feet: int,
                           heads: int,
                           chicken_feet: int,
                           rabbit_feet: int,
                           chicken: str = "chicken",
                           rabbit: str = "rabbit"
                           ) -> dict:
    """
    Chicken rabbit cages(ordinary).
    :param feet: The number of heads in total.
    :param heads: The number of heads in total.
    :param chicken_feet: Each chicken has a few feet.
    :param rabbit_feet: Each rabbit has a few feet.
    :param chicken: "chicken" 's name.
    :param rabbit: "rabbit" 's name.
    :return: results -> dict
    """

    if rabbit_feet < chicken_feet:
        raise ValueError("'chicken_feet' is greater than 'rabbit_feet'")
    results = {chicken: None, rabbit: int((feet - heads * chicken_feet) / (rabbit_feet - chicken_feet))}
    results[chicken] = heads - results[rabbit]
    if results[chicken] <= 0:
        raise NumberError(f"{chicken}'s num isn't positive number.")
    if results[rabbit] <= 0:
        raise NumberError(f"{rabbit}'s num isn't positive number.")
    return results


def Chicken_rabbit_cages_2(score: int,
                           number_of_questions: int,
                           answer_the_score_correctly: int or float,
                           answer_the_wrong_score_value: int or float,
                           correctly: str = "correctly",
                           wrong: str = "wrong",
                           ) -> dict:
    """
    Chicken rabbit cages("answer_the_wrong_score_value" is positive number).
    :param score: The number of score in total.
    :param number_of_questions: The number of questions in total.
    :param answer_the_score_correctly: The score of the question that is answered correctly.
    :param answer_the_wrong_score_value: The score of the question that is answered incorrect (deducted score).
    :param correctly: "correctly" 's name.
    :param wrong: "wrong" 's name.
    :return: results -> dict
    """

    if str(answer_the_wrong_score_value)[0] != "-":
        raise ValueError("'answer_the_wrong_score_value' is positive number.")
    if answer_the_score_correctly < answer_the_wrong_score_value:
        raise ValueError("'answer_the_score_correctly' is greater than 'answer_the_wrong_score_value'")
    results = {correctly:None,
               wrong: int(
                   (number_of_questions * answer_the_score_correctly - score)
                   /
                   (answer_the_score_correctly - answer_the_wrong_score_value)
               )
               }
    results[correctly] = number_of_questions - results[wrong]
    if results[correctly] <= 0:
        raise NumberError(f"{correctly}'s num isn't positive number.")
    if results[wrong] <= 0:
        raise NumberError(f"{wrong}'s num isn't positive number.")
    return results


if __name__ == "__main__":
    r = Chicken_rabbit_cages_1(94, 35, 2, 4)
    print(r)
    r = Chicken_rabbit_cages_2(64, 8, 10, -6)
    print(r)
