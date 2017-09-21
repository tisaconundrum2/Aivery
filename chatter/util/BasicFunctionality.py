import sys

from Qtickle import Qtickle


class Basics:
    """
    This class is a scaffolding class, it holds global
    functionality for all classes inheriting from it.
    It is here to simplify and globalize certain
    variables and functionalities to each of the
    UI classes.

    *Note: Rigorous prototyping is still occurring
    So, naturally, assume that something in this class
    is always getting changed or added to better serve
    all cases in each UI class.

    ...

    Since `Basics` is shared among all the UI
    classes it would make sense that we would have
    some variables, that are necessary among all these
    classes, be put here in a high place where they
    can be referenced often.
    """
    def __init__(self):
        self.qt = Qtickle.Qtickle(self)

    def setupUi(self, Form):
        """
        Get the Ui_Form, it is like the HTML of the UI
        It will show the styling of the UI. But buttons
        and widgets have no function. connectWidgets
        fixes this
        :param Form:
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "SetupUI()" was not found in this module ')

    def get_widget(self):
        """
        This function specifies the variable that holds the
        styling. Use this function to get the variable
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "get_widget()" was not found in this module')

    def connectWidgets(self):
        """
        Connect the necessary widgets.
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "connectWidgets()" was not found in this module')

    def function(self):
        """
        Each Module's functionality will be ran in this function.
        You will define what will happen to the data and parameters in here
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "function()" was not found in this module')

    def isEnabled(self):
        """
        Checks to see if current widget isEnabled or not
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "isEnabled()" was not found in this module')

    def setDisabled(self, bool):
        """
        After every execution we want to prevent the user from changing something.
        So, disable the layout by greying it out
        :param bool:
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "setDisabled()" was not found in this module')
