import streamlit as st
import pandas as pd
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://ha5755420:NtH7Uiig4Wy75nEJ@cluster0.4whod.mongodb.net/digital_bookshelf?retryWrites=true&w=majority&appName=Cluster0"

DATABASE_NAME = "digital_bookshelf"
COLLECTION_NAME = "books"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def load_library():
    return list(collection.find({}, {"_id": 0}))  # Exclude `_id` field

def save_book(book):
    collection.insert_one(book)

def search_books(query):
    return list(collection.find(
        {"$or": [{"Title": {"$regex": query, "$options": "i"}}, {"Author": {"$regex": query, "$options": "i"}}]},
        {"_id": 0}
    ))

def remove_book(title):
    collection.delete_one({"Title": title})

if "library" not in st.session_state:
    st.session_state.library = load_library()

st.title("📖 My Digital Bookshelf")

st.header("🔍 Search Your Collection")
search_query = st.text_input("Enter book title or author")

if st.button("Search"):
    results = search_books(search_query)
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
        # Check if book already exists
        if collection.find_one({"Title": title}):
            st.error(f"⚠️ The book titled '{title}' is already in your collection!")
        else:
            book = {
                "Title": title,
                "Author": author,
                "Year": int(year),
                "Genre": genre,
                "Read": read_status == "Read"
            }
            save_book(book)
            st.session_state.library.append(book)
            st.success(f"📖 '{title}' added to your collection!")
    else:
        st.error("⚠️ Please fill in all fields.")

st.header("📜 Your Collection")
if st.session_state.library:
    df = pd.DataFrame(st.session_state.library)
    
    if "_id" in df.columns:
        df = df.drop(columns=["_id"])

    df["Read"] = df["Read"].apply(lambda x: "✅ Yes" if x else "❌ No")
    st.dataframe(df)
else:
    st.warning("Your collection is empty! Start adding books.")

st.header("🗑️ Remove a Book")
titles = [book["Title"] for book in st.session_state.library]
book_to_remove = st.selectbox("Select a book to remove", ["None"] + titles)

if st.button("Remove Book") and book_to_remove != "None":
    remove_book(book_to_remove)

    st.session_state.library = [book for book in st.session_state.library if book["Title"] != book_to_remove]

    st.session_state.success_message = f"🗑️ '{book_to_remove}' removed successfully!"

    st.rerun() 

if "success_message" in st.session_state:
    st.success(st.session_state.success_message)
    del st.session_state.success_message  # Clear the message after displaying

st.header("📊 Library Insights")
total_books = len(st.session_state.library)
read_books = sum(1 for book in st.session_state.library if book["Read"])
percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

st.write(f"📚 Total Books: {total_books}")
st.write(f"✅ Books Read: {read_books} ({percentage_read:.2f}%)")
