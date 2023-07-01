from django.shortcuts import render

from .quiz import get_random_question

# Create your views here.
SHOW_ANSWER = False
CURR_Q = 0


def home(request):
    return render(request, 'questions/base.html')

def question(request):
    global CURR_Q

    data = request.POST
    r = '' if data.get('random') is None else 'checked'
    qa  = get_random_question(start=data.get('from'), 
                              end=data.get('to'),
                              r=bool(r),
                              curr_q=CURR_Q)
    CURRENT = {
        "nr": qa["nr"],
        "question": qa["q"],
        "answer": qa["a"],
        "show_answer": False,  # Initially set to False
        "from": data.get('from'),
        "to": data.get('to'),
        "random": r
    }
    CURR_Q = qa["nr"]
    
    
    return render(request, 'questions/question.html', CURRENT)
   
   

    
        
    