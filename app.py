import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the dataset (replace 'path_to_dataset' with your actual dataset file)
@st.cache_data
def load_data():
    df = pd.read_csv('/content/UCoursera_Courses.csv')
    return df

df = load_data()

# Combine relevant columns into a single feature
df['combined_features'] = df['course_title'] + ' ' + df['course_organization'] + ' ' + df['course_Certificate_type'] + ' ' + df['course_rating'].astype(str) + ' ' + df['course_difficulty'] + ' ' + df['course_students_enrolled'].astype(str)

# Create a TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Construct the TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(df['combined_features'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on course title and user's final grade
def get_recommendations(course_title, final_grade, cosine_sim=cosine_sim, df=df):
    # Get the index of the course that matches the title
    idx = df[df['course_title'] == course_title].index[0]

    # Determine course level based on final grade
    if final_grade <= 50:
        level = 'beginner'
    elif final_grade <= 80:
        level = 'mixed'
    else:
        level = 'intermediate and advanced'

    # Get the pairwise similarity scores of all courses with that course
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Filter courses based on level
    recommended_courses = []
    for i, score in sim_scores:
        course_level = df['course_difficulty'].iloc[i]
        if level in course_level.lower():
            recommended_courses.append((df['course_title'].iloc[i], score))

    # Sort the courses based on the similarity scores
    recommended_courses = sorted(recommended_courses, key=lambda x: x[1], reverse=True)

    # Get the top 5 most similar courses
    recommended_courses = recommended_courses[:5]

    # Return the top 5 most similar courses
    return [course[0] for course in recommended_courses]

# Streamlit UI
st.title('Course Recommendation System')

# Course title input from the user
course_title = st.text_input('Enter the course title:', 'A Crash Course in Data Science')

# User's final grade input
final_grade = st.slider('Enter your final grade (0-100):', 0, 100, 50)

if st.button('Get Recommendations'):
    recommendations = get_recommendations(course_title, final_grade)
    st.write(recommendations)
