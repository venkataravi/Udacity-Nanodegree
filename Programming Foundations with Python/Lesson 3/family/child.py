class Child():
    """ This Class is just an example program with a purpose of learning

    It will constuct a Parent with a last name and eye color.

    Args:
        last_name: A Parent's Last Name
        eye_color: A Parent's Eye Color

    Returns:
        An Object with the last name and eye color
    """

    def __init__(self, parent):
        """Inits child with last_name and eye_color."""
        self.last_name = parent.last_name
        self.eye_color = parent.eye_color

    def inhertence():
        """Check if able to give inhertence."""
        if(self.last_name == "Gates"):
            return True
        else:
            return False
