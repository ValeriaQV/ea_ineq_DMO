from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    ########### SOEP (2005-2020) 10-Item scale Locus of Control [7point Likert] ###################

    LOC_1 = models.IntegerField(
        label='How my life goes depends on me.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    LOC_2 = models.IntegerField(
        label='Compared to other people, I have not achieved what I deserve.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    LOC_3 = models.IntegerField(
        label='What a person achieves is above all a question of fate or luck.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    LOC_4 = models.IntegerField(
        label='If a person is socially or politically active, he/she can have an effect on social conditions.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    LOC_5 = models.IntegerField(
        label='I frequently have the experience that other people have a controlling influence over my life.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    LOC_6 = models.IntegerField(
        label='One has to work hard in order to succeed.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    LOC_7 = models.IntegerField(
        label='If I run up against difficulties in life, I often doubt my own abilities.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    LOC_8 = models.IntegerField(
        label='The opportunities that I have in life are determined by the social conditions.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    LOC_9 = models.IntegerField(
        label='Innate abilities are more important than any efforts one can make.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    LOC_10 = models.IntegerField(
        label='I have little control over the thins that happen in my life.',
        choices=range(1, 8),
        widget=widgets.RadioSelect
    )

    ###########  Demographics ###################

    age = models.IntegerField(label='1. What is your age?', min=15, max=80)

    gender = models.IntegerField(
        label='2. How would you best describe yourself?',
        choices=[[1, 'Male'], [2, 'Female'], [3, 'In other way']],
        widget=widgets.RadioSelect
    )

    nationality = models.BooleanField(
        label='3. Were you born in Germany?',
        choices=[[True, 'Yes'], [False, 'No']]
    )

    migration = models.BooleanField(
        label='4. Have you spent most of your life in Germany?',
        choices=[[True, 'Yes'], [False, 'No']]
    )

    migration_parents = models.BooleanField(
        label='5. Is at least one of your parents raced and born in another country than Germany?',
        choices=[[True, 'Yes'], [False, 'No']]
    )

    soc_ladder = models.IntegerField(
        label='6. If you imagine status in society as a ladder, some groups could be described'
              ' as being closer to the top and others closer to the bottom. Thinking about yourself,'
              ' where would you place yourself in this scale?',
        choices=[[1, '1 (bottom)'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
                 [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10 (top)'], [-99, 'No answer']],
        widget=widgets.RadioSelectHorizontal
    )

    employment = models.IntegerField(
        label='7. Which of the following categories best describes your current employment status?',
        choices=[[1, 'Employed, Full-Time'], [2, 'Employed, Part-Time'],
                 [3, 'Unemployed, seeking for work'], [4, 'Unemployed, NOT seeking for work'],
                 [5, 'Student'], [6, 'Retired']],
    )

    income = models.IntegerField(
        label="8. What is your household's monthly available (net) income after taxes and social security?",
        choices=[[1, '0 - 520 EUR'], [2, '521 - 999 EUR'], [3, '1.000 - 1.999 EUR'],
                 [4, '2.000 - 2.999 EUR'], [5, '3.000 - 3.999 EUR'],
                 [6, '4.000 EUR or more'], [-99, 'No answer']],
    )


# FUNCTIONS
# PAGES

class LOC(Page):
    form_model = 'player'
    form_fields = ['LOC_1', 'LOC_2','LOC_3', 'LOC_4','LOC_5', 'LOC_6', 'LOC_7','LOC_8', 'LOC_9', 'LOC_10']



class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'nationality', 'migration',
                   'migration_parents', 'soc_ladder', 'employment',
                   'income']


class Summary_Payoff(Page):
    pass



page_sequence = [LOC, Demographics, Summary_Payoff]
