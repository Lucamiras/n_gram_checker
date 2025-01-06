import streamlit as st
import nltk
import matplotlib.pyplot as plt
from src.ngrams import generate_ngrams
from src.web_request import get_span_labels_content
nltk.download("stopwords")
nltk.download("punkt")


def main():
    # TITLE
    st.title("N-gram Generator")
    
    # SIDEBAR
    sidebar = st.sidebar
    sidebar.header("Settings")
    sidebar.subheader("N-gram range")
    min_col, max_col = sidebar.columns(2)
    minimum = min_col.number_input("N-gram range minimum", value=1, min_value=1, max_value=10, step=1)
    maximum = max_col.number_input("N-gram range maximum", value=3, min_value=minimum, max_value=20)
    sidebar.subheader("Top items")
    top_k = sidebar.number_input("Number of items per chart", value=10, min_value=1, max_value=50, step=1)
    
    # MAIN APP
    text_col, url_col = st.tabs(["Text", "URL"])
    text = text_col.text_area("Paste your text here")
    url = url_col.text_input("Paste your URL here")
    button = st.button("Analyze") 

    # APP LOGIC
    n = maximum - minimum + 1
    if (button and text) or (button and url):
        if url:
            text = get_span_labels_content(url)
        expander = st.expander("Show scraped text")
        expander.write(text)
        fig, axes = plt.subplots(nrows=n, figsize=(10,10))
        for j in range(n):
            # 0, 1, 2
            i = j + 1
            n_gram = generate_ngrams(text, i)
            labels, values = [' '.join(g[0]) for g in n_gram][:top_k][::-1], [g[1] for g in n_gram][:top_k][::-1]
            axes[j].barh(labels, values)
            axes[j].set_title(f"{i}-grams")
            plt.tight_layout()
        st.pyplot(fig)
    
if __name__ == "__main__":
    main()