from django import forms

class TaskForm(forms.Form):
    task_title = forms.CharField(label="Your task's name ")
    task_description = forms.CharField(label="Give your task a more detailed description ")
    task_priority = forms.IntegerField(label="Pick a priority (1-10 where 1 is high) ")
    task_status = forms.CharField(label="Task status: (backlog, ready, doing, done) ")
