import streamlit as slt
import functions

todos = functions.get_todos()


def add_todo():
    todo_to_add = slt.session_state['new_todo'] + '\n'
    todos.append(todo_to_add)
    functions.write_todos(todos)


slt.title("My Todo App")
slt.subheader("This is my todo app.")
slt.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = slt.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del slt.session_state[todo]
        slt.experimental_rerun()

slt.text_input(label="", placeholder="Add new todo..",
               on_change=add_todo, key='new_todo')
