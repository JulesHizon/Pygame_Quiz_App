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
            'category' : self.categories['history'],
            'difficulty' : 'easy',
            'type' : 'boolean',
        }

    def set_params(self, category='animals', difficulty='easy'):
        self.params['category'] = self.categories[category]
        self.params['difficulty'] = difficulty

    def set_category(self, category):
        self.params['category'] = self.categories[category]

    def set_difficulty(self, difficulty):
        self.params['difficulty'] = difficulty
    
    def get_questions(self,):
        self.request = requests.get("https://opentdb.com/api.php?", params=self.params)
        self.question_bank = self.request.json()['results']
