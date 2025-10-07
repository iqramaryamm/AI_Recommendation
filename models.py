# recommender/models.py

from typing import List, Optional, Dict

class BookCandidate:
    def __init__(
        self,
        title: str,
        authors: List[str],
        description: Optional[str] = None,
        pub_year: Optional[int] = None,
        page_count: Optional[int] = None,
        subjects: Optional[List[str]] = None,
        average_rating: Optional[float] = None,
        ratings_count: Optional[int] = None,
        formats: Optional[Dict[str, bool]] = None,
        cover_url: Optional[str] = None,
        preview_link: Optional[str] = None,
        identifier: Optional[str] = None,
    ):
        self.title = title
        self.authors = authors or []
        self.description = description or ""
        self.pub_year = pub_year
        self.page_count = page_count
        self.subjects = subjects or []
        self.average_rating = average_rating
        self.ratings_count = ratings_count
        self.formats = formats or {}  # e.g. {"ebook": True, "print": False, "audiobook": False}
        self.cover_url = cover_url
        self.preview_link = preview_link
        self.identifier = identifier

    def __repr__(self):
        return f"<BookCandidate {self.title} by {self.authors}>"
