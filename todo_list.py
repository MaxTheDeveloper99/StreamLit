import streamlit as st

st.title("To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []


st.subheader("Add a Task")

task = st.text_input("Enter a task")

if st.button("Add Task"):

    if task.strip() != "":
        st.session_state.tasks.append({
            "task": task,
            "completed": False
        })

        st.success("Task added!")
    else:
        st.warning("Please enter a task.")


st.divider()

st.subheader("My Tasks")

if len(st.session_state.tasks) == 0:

    st.info("You don't have any tasks yet.")

else:

    for i, item in enumerate(st.session_state.tasks):

        completed = st.checkbox(
            item["task"],
            value=item["completed"],
            key=f"task_{i}"
        )

        st.session_state.tasks[i]["completed"] = completed


if st.button("Clear Completed Tasks"):

    st.session_state.tasks = [
        task
        for task in st.session_state.tasks
        if not task["completed"]
    ]

    st.rerun()