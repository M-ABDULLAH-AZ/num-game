import streamlit as st
import random

# Initialize session state variables
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'guess' not in st.session_state:
    st.session_state.guess = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

st.title('Number Guessing Game')

if st.session_state.game_over:
    st.write(f'Congratulations! You guessed the number {st.session_state.target_number} in {st.session_state.attempts} attempts.')
    if st.button('Play Again'):
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.guess = None
        st.session_state.attempts = 0
        st.session_state.game_over = False
else:
    st.write('Guess the number between 1 and 100')
    st.session_state.guess = st.number_input('Your guess:', min_value=1, max_value=100, step=1)

    if st.button('Submit'):
        st.session_state.attempts += 1
        if st.session_state.guess < st.session_state.target_number:
            st.write('Too low! Try again.')
        elif st.session_state.guess > st.session_state.target_number:
            st.write('Too high! Try again.')
        else:
            st.session_state.game_over = True
            st.write(f'Congratulations! You guessed the number {st.session_state.target_number} in {st.session_state.attempts} attempts.')

# Display the number of attempts
st.write(f'Attempts: {st.session_state.attempts}')
