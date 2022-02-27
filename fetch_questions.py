import requests

class QuestionBank():

    def __init__(self,):
        
        self.categories = {
            'animals' : 27,
            'history' : 23,
            'sports' : 21,
            'geography' : 22, 
        }

        self.params = {
            'amount' : 10,
            'category' : self.categories['animals'],
            'difficulty' : 'easy',
            'type' : 'boolean',
        }

    def set_params(self,):
        pass
    
    def get_questions(self,):
        self.request = requests.get("https://opentdb.com/api.php?", params=self.params)
        self.question_bank = self.request.json()['results']