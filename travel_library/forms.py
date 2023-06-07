from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import InputRequired

class TravelForm(FlaskForm):
    """
    A form class for adding a new trip using FlaskForm.

    This class inherits from FlaskForm and defines the fields required
    for a new trip: attraction, city, and country. It also includes a
    submit field to submit the form.
    """
    attraction = StringField("Attraction", validators=[InputRequired()])
    city = StringField("City", validators=[InputRequired()])
    country = StringField("Country", validators=[InputRequired()])
    submit = SubmitField("Add Trip")

class StringListField(TextAreaField):
    """
    A custom form field for handling lists of strings.

    This class inherits from TextAreaField and provides custom processing
    for form data. It transforms the input text into a list of strings,
    where each line of text corresponds to an item in the list.
    """
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        """
        Convert the submitted data into a list of strings.

        Args:
            valuelist (list): A list of values submitted with the form.
        """
        self.data = []
        if valuelist and valuelist[0]:
            for line in valuelist[0].split('\n'):
                self.data.append(line.strip())
        else:
            self.data = []


class ExtendedTravelForm(TravelForm):
    """
    An extended form class for adding and editing trip details.

    This class inherits from TravelForm and adds additional fields to
    capture more information of a trip, such as best season, tags,
    travel days, comments, description, and video link.
    """
    best_season = StringListField("Best Season")
    tags = StringListField("Tags")
    travel_days = StringListField("Days Needed (Recommended)")
    comment = StringListField("Comment")   
    description = TextAreaField("Description")
    video_link = URLField("Video link")
    submit = SubmitField("Submit")



