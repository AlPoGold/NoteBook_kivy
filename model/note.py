from datetime import datetime
import model.counter_id




class Note:
    def __init__(self, title="title", body="text",
                 creation_date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S")), edit_date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = str(model.counter_id.count())
        self.title = title
        self.body = body
        self.creation_date = creation_date
        self.edit_date = edit_date


    def __repr__(self):
        return f"Note({self.id}, {self.title}, {self.body}, {self.creation_date}, {self.edit_date})"

    def __str__(self):
        return f"""
ID: {self.id}
Title: {self.title}
Text: {self.body}
Creation date: {self.creation_date}
Edit date: {self.edit_date}
"""



##return values
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_creation_date(self):
        return self.creation_date

    def get_edit_date(self):
        return self.edit_date


##set values

    def set_id(self, id=None):
        if id==None:
            self.id = str(model.counter_id.count())
        else:
            self.id = id

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body = body

    def set_edit_date(self):
        self.edit_date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(self):
        return self.id + ';' + self.title + ';' + self.body + ';' + self.creation_date + ';' + self.edit_date


