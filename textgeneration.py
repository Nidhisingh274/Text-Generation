import streamlit as st
from transformers import pipeline

# Load the text generation pipeline
generator = pipeline("text-generation", model="gpt2")


def main():
    st.title("Text Generation App 💬")

    # Slider for number of responses
    num_outputs = st.slider('How many responses to generate?', 1, 10)

    # Text input
    user_input = st.text_input("Enter the starting sentence:", placeholder="Example: In order to achieve")

    if user_input:
        # Generate text (fixed length)
        result = generator(user_input, max_length=20, num_return_sequences=num_outputs)

        # Toast after successful generation
        st.toast("Text Generated!", icon="✅")

        # Show results
        st.subheader("Generated Responses:")
        for i, output in enumerate(result):
            st.write(f"{i+1}. {output['generated_text']}")

if __name__ == "__main__":
    main()
