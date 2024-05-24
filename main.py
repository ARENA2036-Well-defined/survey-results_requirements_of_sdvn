from nicegui import ui
from nicegui.events import ValueChangeEventArguments
import requests
import json
from enum import Enum
from pydantic import BaseModel
from typing import List
from datetime import datetime

# Modelling of the dataobjects
class Questiontype(Enum):
    single = 'single choice'
    multiple = 'multiple choice'
    text = 'text'

class Question(BaseModel):
    q_id : str
    category : str
    question : str
    questiontype : Questiontype
    answer_posibilities : list
    free_text_label : str|None

class Answer(BaseModel):
    ref_q_id : str
    answers : list
    free_text : str

class Survey(BaseModel):
    survey_id : str
    answers : List[Answer]
    timestamp : datetime

# Import of the data (questions and surveys)
with open('data/questions.json') as stream:
    questions_data = json.load(stream)
questions = [Question(**q) for q in questions_data]
with open('data/surveys.json') as stream:
    survey_data = json.load(stream)
surveys = [Survey(**s) for s in survey_data]

# Initialization of variables for the evaluation
answers={}
free_texts = {}
filter_q = None
filter_v = None
possibilities =[]
participants = len(surveys)
print(participants)
# Main UI for the evaluation
@ui.refreshable
def evaluation_ui():
    for question in questions:
        answers[question.q_id]={a:0 for a in question.answer_posibilities}
        free_texts[question.q_id]=[]
        for survey in surveys:
            if filter_v in [a for a in survey.answers if a.ref_q_id == filter_q][0].answers if filter_v else [] or not filter_v:
                for answer in survey.answers:
                    if answer.ref_q_id == question.q_id:
                        for a in answer.answers:
                            answers[question.q_id][a]+=1/participants
                        if answer.free_text:
                            free_texts[question.q_id].append(answer.free_text)
        
        with ui.expansion(question.question,value=True).classes('w-full text-3xl').style('background-color: rgb(236 102 7);'):
            with ui.row().classes('w-full'):
                if question.questiontype == Questiontype.multiple:
                    ui.highchart({
                        'title': False,
                        'chart': {'type': 'bar'},
                        'xAxis': {'categories': list(answers[question.q_id].keys())},
                        'series': [
                            {'name': 'Surveys', 'data': list(answers[question.q_id].values())},
                        ],
                    }).classes('w-1/3')
                elif question.questiontype == Questiontype.single:
                    ui.highchart({
                        'title': False,
                        'chart': {'type': 'pie'},
                        'series': [
                            {'name': 'Surveys', 'data': [{'name': k, 'y':v} for k,v in answers[question.q_id].items()]},
                        ],
                    }).classes('w-1/3')
                if question.questiontype != Questiontype.text:
                    with ui.column().classes('w-1/4'):
                        ui.label('Results').classes('text-xl')
                        with ui.grid(columns=2):
                            [[ui.label(k).classes('text-base'),ui.label(f'{v:.2%}').classes('text-base')] for k,v in answers[question.q_id].items()]
                if question.free_text_label:
                    with ui.column().classes('w-1/4'):
                        ui.label('Free-texts').classes('text-xl')
                        [ui.label(f'- {e}').classes('text-base') for e in free_texts[question.q_id]]
                
                

# Filter options in header to view surveys with a specific answer to a selected question

def update_filter(v:ValueChangeEventArguments):
    global filter_v
    filter_v = v.value
    evaluation_ui.refresh()

@ui.refreshable
def sel():
    global _v_sel
    _v_sel = ui.select(possibilities,label='Answer', on_change=update_filter).classes('w-1/6')

def update_possibilities(v:ValueChangeEventArguments):
    global possibilities, filter_q, filter_v
    filter_q = v.value
    filter_v = None
    for q in questions:
        if q.q_id == v.value:
            possibilities = q.answer_posibilities
            break
    sel.refresh()

def delete_filter():
    global filter_v, filter_q
    filter_q = None
    filter_v = None
    _q_sel.value = None
    _v_sel.value = None
    evaluation_ui.refresh()

# Main definition of the UI
ui.colors(primary='#ec6607')
with ui.header():
    ui.image('data/Well-Defined_logo.png').classes('w-60 mt-1')
    ui.label('Industrial Requirements for Software-defined Value Networks').classes('text-3xl m-0 mt-2 text-black')
    ui.space()
    ui.label('Filter:').classes('text-l m-0 mt-5 text-black')
    _q_sel = ui.select({q.q_id:q.question for q in questions if q.questiontype == Questiontype.single or q.questiontype==Questiontype.multiple},label='Question',on_change=update_possibilities).classes('w-1/6 truncate')
    sel()
    ui.button(icon='delete',on_click=delete_filter).classes('m-0 mt-4')
evaluation_ui()

ui.run(title='Well-defined',favicon='data/Well-Defined_icon.png')
        

