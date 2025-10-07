import streamlit as st
from recommender.api_clients import search_openlibrary, search_google_books,make_cover_url
from recommender.models import BookCandidate


def main():
    st.title("Book Recommendation")
    # Simple questions
    topics = st.text_input("What topics are you interested in? (e.g. AI, history, fiction)")
    recency = st.selectbox("Recency preference", ["Any", "Last 10 years", "Last 3 years"])
    formats = st.multiselect("Preferred formats", ["Ebook", "Print", "Audiobook"])
    if st.button("Get recommendations"):
        # Call your backend logic
        results = get_recommendations(topics, recency, formats)
        for book in results:
            st.markdown(f"**{book.title}** by {', '.join(book.authors)}")
            if book.cover_url:
                st.image(book.cover_url, width=120)
            st.write(book.description or "")
            if book.preview_link:
                st.write(f"[Preview]({book.preview_link})")
            st.write("---")

def get_recommendations(topics, recency, formats):
    # For MVP: just call Open Library search + maybe Google Books
    results = []
    # Try Open Library
    docs = search_openlibrary(topics, limit=20)
    # Convert docs to normalized candidate objects (simple)
    for doc in docs:
        # Simple normalization
        bc = BookCandidate(
            title=doc.get("title"),
            authors=doc.get("author_name", []),
            pub_year=doc.get("first_publish_year"),
            description=doc.get("subtitle") or "",
            cover_url=make_cover_url(doc),
            preview_link=None,
            formats={"ebook": True, "print": True, "audiobook": False}
        )
        results.append(bc)
    # Optionally enrich from Google Books, combine lists, dedupe
    return results[:5]

if __name__ == "__main__":
    main()
