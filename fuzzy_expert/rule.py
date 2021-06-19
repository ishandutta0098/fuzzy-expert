"""
Zadeh-Mamdani Rules
===============================================================================

"""


class FuzzyRule:
    """Creates a Zadeh-Mamdani fuzzy rule.

    Args:
        antecedents (list of tuples): Fuzzy variables in the rule antecedent.
        consequent (tuple): Fuzzy variable in the consequence.
        is_and (bool): When True, membership values are combined using the specified AND operator; when False, the OR operator is used.

    """

    def __init__(
        self,
        premises,
        consequence,
    ):
        self.premises = premises
        self.consequence = consequence

    def __repr__(self):

        text = "IF  "
        space = " " * 4

        for i_premise, premise in enumerate(self.premises):

            if i_premise == 0:
                text += premise[0].name + " IS"
                for t in premise[1:]:
                    text += " " + t
                text += "\n"
            else:
                text += space + premise[0] + " " + premise[1].name + " IS"
                for t in premise[2:]:
                    text += " " + t
                text += "\n"

        text += "THEN\n"
        text += space + self.consequence[0].name + " IS"
        for t in self.consequence[1:]:
            text += " " + t
        return text
