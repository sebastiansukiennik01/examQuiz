from django.shortcuts import render

from .quiz import get_random_question

# Create your views here.
SHOW_ANSWER = False


def home(request):
    return render(request, 'questions/base.html')

def question(request):
    data = request.POST
    print(data)
    qa  = get_random_question(start=data.get('from'), 
                              end=data.get('to'))
    CURRENT = {
        "nr": qa["nr"],
        "question": qa["q"],
        "answer": qa["a"],
        "show_answer": False,  # Initially set to False
        "from": data.get('from'),
        "to": data.get('to')
    }
    return render(request, 'questions/question.html', CURRENT)
   
   

    
        
    