import streamlit as st

questions = (
    "Which data structure allows you to access elements in LIFO (Last In, First Out) order?",
    "What is the time complexity of the best-case scenario for Bubble Sort?",
    "Which sorting algorithm works by repeatedly swapping adjacent elements if they are in the wrong order?",
    "What data structure does a Breadth-First Search (BFS) algorithm typically use?",
    "Which of the following is not a type of tree?",
    "What does DFS stand for in terms of graph traversal?",
    "Which of the following is a divide and conquer algorithm?",
    "In which data structure is FIFO (First In, First Out) principle followed?",
    "What is the average-case time complexity of Quick Sort?",
    "Which of the following is used to search for a pattern in a string?",
)

options = (
    ["A. Queue", "B. Heap", "C. Stack", "D. Linked List"],
    ["A. O(n)", "B. O(n log n)", "C. O(1)", "D. O(n^2)"],
    ["A. Quick Sort", "B. Merge Sort", "C. Insertion Sort", "D. Selection Sort"],
    ["A. Stack", "B. Queue", "C. Heap", "D. Array"],
    ["A. Binary Tree", "B. Trie", "C. Linked List", "D. AVL Tree"],
    ["A. Depth-First Search", "B. Dijkstra's Fast Search", "C. Direct Function Search", "D. Divided File Structure"],
    ["A. Breadth-First Search (BFS)", "B. Dijkstra's Algorithm", "C. Merge Sort", "D. Linear Search"],
    ["A. Queue", "B. Stack", "C. Heap", "D. Tree"],
    ["A. O(n)", "B. O(n log n)", "C. O(1)", "D. O(n^2)"],
    ["A. Breadth-First Search (BFS)", "B. Depth-First Search (DFS)", "C. Binary Search", "D. String Matching Algorithm"]
)

answers = ("C", "D", "A", "A", "B")

def display_question(question, options):
    st.write(question)
    for option in options:
        st.write(option)

def get_guess(key, options):
    return st.radio(key, options, format_func=lambda x: "")

def evaluate_answer(guess, correct_answer):
    if guess == correct_answer:
        return True
    else:
        return False

# Streamlit UI
st.title('Quiz Game')
st.write("Answer the following questions:")

score = 0

for i in range(len(questions)):
    st.write("----------------------")
    display_question(questions[i], options[i])
    guess = get_guess(str(i), options[i]).upper()
    if evaluate_answer(guess, answers[i]):
        score += 1
        st.write("CORRECT!")
    else:
        st.write("INCORRECT!")
        st.write(f"{answers[i]} is the correct answer")

st.write("----------------------")
st.write("RESULTS")
st.write("----------------------")

st.write("Your score is:", score, "/", len(questions))
percentage = (score / len(questions)) * 100
st.write("Percentage:", percentage, "%")
