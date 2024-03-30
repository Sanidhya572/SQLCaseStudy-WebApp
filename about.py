import streamlit as st

def app():
    st.title('Welcome to :violet[SQL Case Study: Analyzing Famous Paintings Dataset]')
    st.image("Dataset.png", use_column_width=True)
    st.markdown("[Explore Famous Paintings Dataset on Kaggle](https://www.kaggle.com/datasets/mexwell/famous-paintings)")
    st.markdown("""
    Welcome to our SQL Case Study where we delve into the world of famous paintings using SQL queries. In this project, 
    we'll leverage a dataset sourced from Kaggle, focusing on renowned paintings. Our objective is to demonstrate how 
    SQL can be utilized to extract meaningful insights and conduct analyses on structured data.
    

    ## Dataset
    We have chosen the famous paintings dataset available on Kaggle for our analysis. This dataset encompasses various 
    attributes related to well-known paintings, including artist information, painting genres, years of creation, and more.
                
    
    ## Project Overview
    1. **Data Acquisition:** We'll begin by downloading the dataset from Kaggle, which will serve as the foundation for 
    our analysis.
    2. **Data Loading:** Using a Python script, we'll upload the dataset into a PostgreSQL database. This step ensures 
    that our data is organized within a structured database environment, facilitating efficient querying.
    3. **SQL Querying:** With the dataset securely stored in our PostgreSQL database, we'll tackle over 20 SQL queries, 
    ranging from basic to intermediate complexity. These queries will address diverse aspects of the famous paintings 
    dataset, such as artist insights, genre distributions, temporal trends, and more.
    4. **Analysis and Interpretation:** Each SQL query will yield specific insights into the dataset, allowing us to 
    glean valuable information about the world of famous paintings. We'll interpret these findings to gain a deeper 
    understanding of the underlying trends and patterns.
    
    ## Why SQL Practice Matters
    SQL proficiency is essential for anyone working with structured data, particularly in fields such as data analysis, 
    data science, and database management. Through this case study, you'll enhance your SQL skills by applying them to a 
    real-world dataset, reinforcing key concepts and techniques along the way.
    
    Join us on this SQL journey as we explore the fascinating realm of famous paintings and uncover hidden insights locked 
    within the data.
    
    *Note: The SQL queries and analyses conducted in this project are intended for educational purposes and serve as 
    valuable practice exercises for honing SQL proficiency.*
    """)

