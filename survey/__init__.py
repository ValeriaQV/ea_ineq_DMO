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

    ###########  Locus of Control ###################

    LOC_1 = models.BooleanField(
        label="1.",
        choices=[[True, "a. Children get into trouble because their parents punish them too much."],
                 [False, "b. The trouble with most children nowadays is that their parents are too easy with them."]],
        widget=widgets.RadioSelect
    )

    LOC_2 = models.BooleanField(
        label="2.",
        choices=[[True, "a. Many of the unhappy things in people's lives are partly due to bad luck."],
                 [False, "b. People's misfortunes result from the mistakes they make."]],
        widget=widgets.RadioSelect
    )

    LOC_3 = models.BooleanField(
        label="3.",
        choices=[[True, "a. One of the major reasons why we have wars is because people don't take "
                        "enough interest in politics."],
                 [False, "b. There will always be wars, no matter how hard people try to prevent them."]],
        widget=widgets.RadioSelect
    )

    LOC_4 = models.BooleanField(
        label="4.",
        choices=[[True, "a. In the long run people get the respect they deserve in this world."],
                 [False, "b. Unfortunately, an individual's worth often passes unrecognized no "
                         "matter how hard he tries."]],
        widget=widgets.RadioSelect
    )

    LOC_5 = models.BooleanField(
        label="5.",
        choices=[[True, "a. The idea that teachers are unfair to students is non-sense."],
                 [False, "b. Most students don't realize the extent to which their grades are "
                         "influenced by accidental happenings."]],
        widget=widgets.RadioSelect
    )

    LOC_6 = models.BooleanField(
        label="6.",
        choices=[[True, "a. Without the right breaks one cannot be an effective leader."],
                 [False, "b. Capable people who fail to become leaders have not taken "
                         "advantage of their opportunities."]],
        widget=widgets.RadioSelect
    )
    LOC_7 = models.BooleanField(
        label="7.",
        choices=[[True, "a. No matter how hard you try some people just don't like you."],
                 [False, "b. People who can't get others to like them don't understand how "
                         "to get along with others."]],
        widget=widgets.RadioSelect
    )
    LOC_8 = models.BooleanField(
        label="8.",
        choices=[[True, "a. Heredity plays the major role in determining one's personality."],
                 [False, "b. It is one's experiences in life which determine what they're like."]],
        widget=widgets.RadioSelect
    )
    LOC_9 = models.BooleanField(
        label="9.",
        choices=[[True, "a. I have often found that what is going to happen will happen."],
                 [False, "b. Trusting to fate has never turned out as well for me as making a "
                         "decision to take a definite course of action."]],
        widget=widgets.RadioSelect
    )
    LOC_10 = models.BooleanField(
        label="10.",
        choices=[[True, "a. In the case of the well prepared student there is rarely if ever "
                        "such a thing as an unfair test."],
                 [False, "b. Many times exam questions tend to be so unrelated to course work "
                         "that studying is really useless"]],
        widget=widgets.RadioSelect
    )
    LOC_11 = models.BooleanField(
        label="11.",
        choices=[[True, "a. Becoming a success is a matter of hard work, luck has little or nothing to do with it."],
                 [False, "b. Getting a good job depends mainly on being in the right place at the right time."]],
        widget=widgets.RadioSelect
    )
    LOC_12 = models.BooleanField(
        label="12.",
        choices=[[True, "a. The average citizen can have an influence in government decisions."],
                 [False, "b. This world is run by the few people in power, and there is "
                         "not much the little guy can do about it."]],
        widget=widgets.RadioSelect
    )
    LOC_13 = models.BooleanField(
        label="13.",
        choices=[[True, "a. When I make plans, I am almost certain that I can make them work."],
                 [False, "b. It is not always wise to plan too far ahead because many things "
                         "turn out to be a matter of good or bad fortune anyhow."]],
        widget=widgets.RadioSelect
    )
    LOC_14 = models.BooleanField(
        label="14.",
        choices=[[True, "a. There are certain people who are just no good."],
                 [False, "b. There is some good in everybody."]],
        widget=widgets.RadioSelect
    )
    LOC_15 = models.BooleanField(
        label="15.",
        choices=[[True, "a. In my case getting what I want has little or nothing to do with luck."],
                 [False, "b. Many times we might just as well decide what to do by flipping a coin."]],
        widget=widgets.RadioSelect
    )
    LOC_16 = models.BooleanField(
        label="16.",
        choices=[[True, "a. Who gets to be the boss often depends on who was lucky enough "
                        "to be in the right place first."],
                 [False, "b. Getting people to do the right thing depends upon ability, luck has "
                         "little or nothing to do with it."]],
        widget=widgets.RadioSelect
    )
    LOC_17 = models.BooleanField(
        label="17.",
        choices=[[True, "a. As far as world affairs are concerned, most of us are the victims of "
                        "forces we can neither understand, nor control."],
                 [False, "b. By taking an active part in political and social affairs the people can "
                         "control world events."]],
        widget=widgets.RadioSelect
    )
    LOC_18 = models.BooleanField(
        label="18.",
        choices=[[True, "a. Most people don't realize the extent to which their lives are controlled by "
                        "accidental happenings."],
                 [False, "b. There really is no such thing as 'luck'."]],
        widget=widgets.RadioSelect
    )
    LOC_19 = models.BooleanField(
        label="19.",
        choices=[[True, "a. One should always be willing to admit mistakes."],
                 [False, "b. It is usually best to cover up one's mistakes."]],
        widget=widgets.RadioSelect
    )
    LOC_20 = models.BooleanField(
        label="20.",
        choices=[[True, "a. It is hard to know whether or not a person really likes you."],
                 [False, "b. How many friends you have depends upon how nice a person you are."]],
        widget=widgets.RadioSelect
    )
    LOC_21 = models.BooleanField(
        label="21.",
        choices=[[True, "a. In the long run the bad things that happen to us are balanced by the good ones."],
                 [False, "b. Most misfortunes are the result of lack of ability, ignorance, laziness, or all three."]],
        widget=widgets.RadioSelect
    )
    LOC_22 = models.BooleanField(
        label="22.",
        choices=[[True, "a. With enough effort we can wipe out political corruption."],
                 [False, "b. It is difficult for people to have much control over the things politicians do in office."]],
        widget=widgets.RadioSelect
    )
    LOC_23 = models.BooleanField(
        label="23.",
        choices=[[True, "a. Sometimes I can't understand how teachers arrive at the grades they give."],
                 [False, "b. There is a direct connection between how hard I study and the grades I get."]],
        widget=widgets.RadioSelect
    )
    LOC_24 = models.BooleanField(
        label="24.",
        choices=[[True, "a. A good leader expects people to decide for themselves what they should do."],
                 [False, "b. A good leader makes it clear to everybody what their jobs are."]],
        widget=widgets.RadioSelect
    )
    LOC_25 = models.BooleanField(
        label="25.",
        choices=[[True, "a. Many times I feel that I have little influence over the things that happen to me."],
                 [False, "b. It is impossible for me to believe that chance or luck plays an important "
                         "role in my life."]],
        widget=widgets.RadioSelect
    )
    LOC_26 = models.BooleanField(
        label="26.",
        choices=[[True, "a. People are lonely because they don't try to be friendly."],
                 [False, "b. There's not much use in trying too hard to please people, if they like you, "
                         "they like you."]],
        widget=widgets.RadioSelect
    )
    LOC_27 = models.BooleanField(
        label="27.",
        choices=[[True, "a. There is too much emphasis on athletics in high school."],
                 [False, "b. Team sports are an excellent way to build character."]],
        widget=widgets.RadioSelect
    )
    LOC_28 = models.BooleanField(
        label="28.",
        choices=[[True, "a. What happens to me is my own doing."],
                 [False, "b. Sometimes I feel that I don't have enough control over the direction my life is taking."]],
        widget=widgets.RadioSelect
    )
    LOC_29 = models.BooleanField(
        label="29.",
        choices=[[True, "a. Most of the time I can't understand why politicians behave the way they do."],
                 [False, "b. In the long run the people are responsible for bad government on a "
                         "national as well as on a local level."]],
        widget=widgets.RadioSelect
    )

    ###########  Demographics ###################

    age = models.IntegerField(label='1. What is your age?', min=15, max=80)

    gender = models.StringField(
        label='2. How would you describe yourself?',
        choices=[['1', 'Male'], ['2', 'Female'], ['3', 'In other way']],
        widget=widgets.RadioSelect
    )

    nationality = models.StringField(
        label='3. What is your nationality? (If you have more than one, please indicate all of them.)'
    )

    migration = models.BooleanField(
        label='4. Have you spent most of your life in Germany?',
        choices=[[True, 'Yes'], [False, 'No']]
    )

    migration_parents = models.BooleanField(
        label='5. Is at least one of your parents a foreigner?',
        choices=[[True, 'Yes'], [False, 'No']]
    )

    soc_ladder = models.StringField(
        label='6. If you imagine status in society as a ladder, some groups could be described'
              ' as being closer to the top and others closer to the bottom. Thinking about yourself,'
              ' where would you place yourself in this scale?',
        choices=[['1', '1 (bottom)'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'],
                 ['6', '6'], ['7', '7'], ['8', '8'], ['9', '9'], ['10', '10 (top)'], ['11', 'No answer']],
        widget=widgets.RadioSelectHorizontal
    )

    educ = models.StringField(
        label='7. What is the highest educational level that you have attained?',
        choices=[['1', 'No formal education'], ['2', 'Complete primary school (Grundschulabschluss)'],
                 ['3', 'Complete middle school (Haupt- or Realschulabschluss)'],
                 ['4', 'Complete secondary school (Fachhochschulreife)'],
                 ['5', 'Complete vocational training'],
                 ['6', 'Bachelor degree'], ['7', 'Master degree'], ['8', 'Doctoral degree']],
        widget=widgets.RadioSelect
    )

    employment = models.StringField(
        label='8. Which of the following categories best describes your current employment status?',
        choices=[['1', 'Employed, Full-Time'], ['2', 'Employed, Part-Time'],
                 ['3', 'Unemployed, seeking for work'], ['4', 'Unemployed, NOT seeking for work'],
                 ['5', 'Student'], ['6', 'Retired']],
        widget=widgets.RadioSelect
    )

    income = models.StringField(
        label="9. What is your household's monthly available (net) income after taxes and social security?",
        choices=[['1', '0 - 560 EUR'], ['2', '561 - 999 EUR'], ['3', '1.000 - 1.999 EUR'],
                 ['4', '2.000 - 2.999 EUR'], ['5', '3.000 - 3.999 EUR'],
                 ['6', '4.000 EUR or more'], ['7', 'No answer']],
        widget=widgets.RadioSelect
    )


# FUNCTIONS
# PAGES

class LOC_Page1(Page):
    form_model = 'player'
    form_fields = ['LOC_1', 'LOC_2','LOC_3', 'LOC_4','LOC_5', 'LOC_6']

class LOC_Page2(Page):
    form_model = 'player'
    form_fields = ['LOC_7','LOC_8', 'LOC_9','LOC_10', 'LOC_11', 'LOC_12']

class LOC_Page3(Page):
    form_model = 'player'
    form_fields = ['LOC_13', 'LOC_14', 'LOC_15', 'LOC_16', 'LOC_17','LOC_18']

class LOC_Page4(Page):
    form_model = 'player'
    form_fields = ['LOC_19','LOC_20', 'LOC_21', 'LOC_22','LOC_23', 'LOC_24']

class LOC_Page5(Page):
    form_model = 'player'
    form_fields = ['LOC_25', 'LOC_26', 'LOC_27','LOC_28', 'LOC_29']


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'nationality', 'migration', 'migration_parents',
                   'soc_ladder', 'educ', 'employment', 'income']



page_sequence = [LOC_Page1, LOC_Page2, LOC_Page3, LOC_Page4, LOC_Page5, Demographics]
