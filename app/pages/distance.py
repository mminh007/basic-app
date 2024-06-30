import streamlit as st
from wc.levenshtein_distance import levenshtein_distance, load_vocab

file_path='C://Users/tuanm/OneDrive/projects/streamlit-basic/wc/sources/vocab.txt'
def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    vocabs = load_vocab(file_path)

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)
        
        # sorted by distance
        sorted_distences = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        
        col2.write('Distances:')
        col2.write(sorted_distences)

if __name__ == "__main__":
    main()