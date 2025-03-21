import random
import streamlit as st

def build_markov_chain(text, n=2):
    words = text.split()
    index = n
    markov_chain = {}
    
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)
    
    return markov_chain

def generate_text(chain, n=2, length=50):
    start = random.choice(list(chain.keys()))
    result = list(start)
    
    for _ in range(length):
        state = tuple(result[-n:])
        next_words = chain.get(state)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
    
    return ' '.join(result)

def main():
    st.title("📝 Markov Chain Text Composer")
    st.write("Upload a text file, and this app will generate random text based on it!")

    uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])

    if uploaded_file is not None:
        text = uploaded_file.read().decode('utf-8')
        st.write("Original Text Sample:")
        st.write(text[:500])  # Show first 500 chars
        
        n = st.slider("Order of Markov Chain (n-gram)", 1, 5, 2)
        length = st.slider("Generated Text Length (words)", 10, 200, 50)

        if st.button("Generate Text"):
            chain = build_markov_chain(text, n)
            generated = generate_text(chain, n, length)
            st.subheader("Generated Text:")
            st.write(generated)

if __name__ == "__main__":
    main()
