from mycroft import MycroftSkill, intent_file_handler


# this is a major comment

class Example(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('example.intent')
    def handle_example(self, message):
        self.speak_dialog('example')
        print("oh yeah im also here")


def create_skill():
    return Example()
