import requests

def search_openlibrary(query, limit=20):
    url = "https://openlibrary.org/search.json"
    params = {
        "q": query,
        "limit": limit
    }
    resp = requests.get(url, params=params)
    return resp.json().get("docs", [])

def make_cover_url(doc):
    # if 'cover_i' present, use Open Library covers API
    cover_id = doc.get("cover_i")
    if cover_id:
        return f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"
    # else try edition key etc.
    return None


def search_google_books(query, max_results=20, api_key=None):
    """
    Search Google Books volumes API.
    Returns a list of item dicts (JSON from Google Books) or empty list.
    """
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "maxResults": max_results
    }
    if api_key:
        params["key"] = api_key
    resp = requests.get(url, params=params)
    data = resp.json()
    return data.get("items", [])



def make_cover_url(doc):
    cover_id = doc.get("cover_i")
    if cover_id:
        return f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"
    return None

