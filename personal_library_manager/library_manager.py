import streamlit as st
import pandas as pd

LIBRARY_FILE = "library.txt"

def load_library():
    library = []
    try:
        with open(LIBRARY_FILE, "r") as file:
            for line in file:
                title, author, year, genre, read_status = line.strip().split(" | ")
                library.append({
                    "Title": title,
                    "Author": author,
                    "Year": int(year),
                    "Genre": genre,
                    "Read": read_status == "Read"
                })
    except FileNotFoundError:
        pass
    return library

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        for book in library:
            file.write(f"{book['Title']} | {book['Author']} | {book['Year']} | {book['Genre']} | {'Read' if book['Read'] else 'Unread'}\n")

if "library" not in st.session_state:
    st.session_state.library = load_library()

st.title("📖 My Digital Bookshelf")

st.header("🔍 Search Your Collection")
search_query = st.text_input("Enter book title or author")

if st.button("Search"):
    results = [book for book in st.session_state.library if search_query.lower() in book["Title"].lower() or search_query.lower() in book["Author"].lower()]
    if results:
        st.write("🎯 Search Results:")
        df = pd.DataFrame(results)
        df["Read"] = df["Read"].apply(lambda x: "✅ Yes" if x else "❌ No")
        st.dataframe(df)
    else:
        st.warning("No matching books found.")

st.header("📚 Add a New Book")
title = st.text_input("Book Title")
author = st.text_input("Author")
year = st.number_input("Publication Year", min_value=1000, max_value=2100, step=1)
genre = st.text_input("Genre")
read_status = st.radio("Have you read this book?", ["Unread", "Read"])

if st.button("Add Book"):
    if title and author and genre and year:
        st.session_state.library.append({
            "Title": title,
            "Author": author,
            "Year": int(year),
            "Genre": genre,
            "Read": read_status == "Read"
        })
        save_library(st.session_state.library)
        st.success(f"📖 '{title}' added to your collection!")
    else:
        st.error("⚠️ Please fill in all fields.")

st.header("📜 Your Collection")
if st.session_state.library:
    df = pd.DataFrame(st.session_state.library)
    df["Read"] = df["Read"].apply(lambda x: "✅ Yes" if x else "❌ No")
    st.dataframe(df)
else:
    st.warning("Your collection is empty! Start adding books.")

st.header("🗑️ Remove a Book")
titles = [book["Title"] for book in st.session_state.library]
book_to_remove = st.selectbox("Select a book to remove", ["None"] + titles)

if st.button("Remove Book") and book_to_remove != "None":
    st.session_state.library = [book for book in st.session_state.library if book["Title"] != book_to_remove]
    save_library(st.session_state.library)
    st.success(f"🗑️ '{book_to_remove}' removed successfully!")

st.header("📊 Library Insights")
total_books = len(st.session_state.library)
read_books = sum(1 for book in st.session_state.library if book["Read"])
percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

st.write(f"📚 Total Books: {total_books}")
st.write(f"✅ Books Read: {read_books} ({percentage_read}%)")
