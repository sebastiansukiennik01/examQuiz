# import docx
import random
import json

def convert_doc_to_string(doc):
    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text

def convert_to_qa(doc_str: str) -> list[dict]:
    rest = doc_str
    qa = []
    for i in range(1, 601):
        try:
            question, rest = rest.split(f'{i}:', 1)
            question = question.replace(f'{i-1}:', '')
            q, a = question.split(':', 1)
        except ValueError:
            continue
        qa.append({'nr': i-1, 'q': q, 'a': a})
    
    return qa


def read_questions_from_docx(file_path):
    doc = docx.Document(file_path)
    questions = []
    current_question = None
    
    doc_str = convert_doc_to_string(doc)
    qa = convert_to_qa(doc_str)

    print(f"Read {len(qa)} questions\n")
    # save to json
    save_to_json(qa)
    
    return qa


def save_to_json(data: list) -> None:
    with open("qa.json", 'w') as f:
        json.dump(data, f)

def display_random_question(questions, start: int = 0, end: int = 100):
    while True:
        random_question = random.choice(questions[start:end])
        print("Question number:", random_question["nr"])
        print("Question:", random_question["q"])
        input("Press Enter to see the answer...")
        print("Answer:", random_question["a"])
        

def get_random_question(start: int = 0, end: int = 100, **kwargs) -> dict:
    
    r = kwargs.pop('r', True)
    curr_q = kwargs.pop('curr_q', 0)
    print(r, curr_q)
    
    
    start, end = check_input(start, end)
    print(f"Selecting from: {start} to: {end}")    

    with open('./questions/data/questions.json', 'r') as f:
        questions = json.load(f)
    if r:
        return random.choice(questions[start:end])
    else:
        print(f"Selecting {curr_q+1} as next")
        try:
            return questions[curr_q]
        except:
            return random.choice(questions[start:end])
        

def check_input(start, end) -> tuple:
    
    try:
        return int(start), int(end)
    except (TypeError, ValueError):
        return 0, 100 
        
    

# Example usage
# if __name__ == '__main__':
#     file_path = "pytania.docx"
#     # questions = read_questions_from_docx(file_path)
#     with open('questions.json', 'r') as f:
#         questions = json.load(f)
    
#     display_random_question(questions)