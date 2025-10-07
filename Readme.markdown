# Book Recommendation App Documentation

## Overview
This application is a web-based book recommendation system built using **Streamlit**, a Python library for creating interactive web applications. It allows users to input their preferences for book topics, recency, and formats, and returns a list of recommended books sourced from the **Open Library API**. The application is designed as a Minimum Viable Product (MVP) with potential for future enhancements, such as integrating additional data from the **Google Books API**.

The system consists of three main files:
- `app.py`: The main Streamlit application that handles the user interface and recommendation logic.
- `api_clients.py`: Contains functions for interacting with external APIs (Open Library and Google Books).
- `models.py`: Defines the `BookCandidate` data model to standardize book information across different APIs.

---

## File Structure
- **`app.py`**: Entry point for the Streamlit app, containing the main UI and recommendation logic.
- **`api_clients.py`**: Handles API calls to Open Library and Google Books, including cover image URL generation.
- **`models.py`**: Defines the `BookCandidate` class to normalize book data.

---

## Dependencies
The application relies on the following Python libraries:
- **Streamlit**: For building the web interface.
- **Requests**: For making HTTP requests to external APIs.
- **Typing**: For type hints in the `BookCandidate` class.

To install dependencies, run:
```bash
pip install streamlit requests
```

---

## Functionality

### 1. User Interface (`app.py`)
The application provides a simple web interface where users can:
- Input **topics** of interest (e.g., "science fiction", "history").
- Select a **recency preference** ("Any", "Last 10 years", or "Last 3 years").
- Choose preferred **book formats** (Ebook, Print, Audiobook).
- Click a **"Get recommendations"** button to retrieve book recommendations.

The interface displays:
- Book title and author(s).
- Cover image (if available).
- Book description (if available).
- A preview link (if available).

### 2. Recommendation Logic (`app.py`)
The `get_recommendations` function:
- Takes user inputs (topics, recency, formats).
- Queries the Open Library API via `search_openlibrary` to fetch book data.
- Converts API results into `BookCandidate` objects for standardized data handling.
- Returns up to 5 book recommendations (with potential for future filtering based on recency and formats).

### 3. API Clients (`api_clients.py`)
This module provides functions to interact with external book APIs:
- **`search_openlibrary(query, limit=20)`**:
  - Queries the Open Library API with a search term (`query`) and a limit on results (default: 20).
  - Returns a list of book documents in JSON format.
- **`search_google_books(query, max_results=20, api_key=None)`**:
  - Queries the Google Books API with a search term (`query`) and a maximum number of results (default: 20).
  - Optionally accepts an API key (not currently used in the MVP).
  - Returns a list of book items in JSON format.
- **`make_cover_url(doc)`**:
  - Generates a cover image URL for a book document from Open Library using the `cover_i` field.
  - Returns `None` if no cover is available.

**Note**: The `make_cover_url` function appears twice in `api_clients.py`, which is redundant and should be consolidated in future updates.

### 4. Data Model (`models.py`)
The `BookCandidate` class standardizes book data with the following attributes:
- `title`: Book title (string, required).
- `authors`: List of authors (list of strings, required).
- `description`: Book description or subtitle (string, optional).
- `pub_year`: Publication year (integer, optional).
- `page_count`: Number of pages (integer, optional).
- `subjects`: List of subjects or genres (list of strings, optional).
- `average_rating`: Average rating (float, optional).
- `ratings_count`: Number of ratings (integer, optional).
- `formats`: Dictionary indicating available formats (e.g., `{"ebook": True, "print": True, "audiobook": False}`).
- `cover_url`: URL for the book cover image (string, optional).
- `preview_link`: URL for a book preview (string, optional).
- `identifier`: Unique identifier for the book (string, optional).

The class includes a `__repr__` method for a readable string representation of a book.

---

## How It Works
1. **User Input**:
   - The user enters topics, selects a recency preference, and chooses preferred formats via the Streamlit UI.
2. **API Query**:
   - When the user clicks "Get recommendations," the `get_recommendations` function queries the Open Library API using the `search_openlibrary` function.
3. **Data Normalization**:
   - The API response is processed, and each book is converted into a `BookCandidate` object with normalized fields (e.g., title, authors, cover URL).
4. **Display Results**:
   - Up to 5 recommendations are displayed with title, authors, cover image, description, and preview link (if available).

---

## Running the Application
1. Ensure dependencies are installed:
   ```bash
   pip install streamlit requests
   ```
2. Save the three files (`app.py`, `api_clients.py`, `models.py`) in the same directory.
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open the provided local URL (e.g., `http://localhost:8501`) in a web browser.

---

## Limitations
- **API Usage**: The MVP only uses Open Library for recommendations. Google Books integration is present but not utilized in the recommendation logic.
- **Recency and Format Filtering**: The current implementation does not filter results based on recency or format preferences.
- **Redundant Code**: The `make_cover_url` function is duplicated in `api_clients.py`.
- **Error Handling**: Limited error handling for API failures or invalid inputs.
- **Static Formats**: The `BookCandidate` objects assume all books are available as ebooks and print, with audiobooks set to `False`.

---

## Future Improvements
1. **Integrate Google Books**: Enrich recommendations with data from the Google Books API (e.g., ratings, preview links).
2. **Filter by Recency and Formats**: Implement logic to filter results based on user-selected recency and format preferences.
3. **Deduplication**: Combine results from multiple APIs and remove duplicates based on book identifiers or titles.
4. **Error Handling**: Add robust error handling for API failures, invalid inputs, or missing data.
5. **Enhanced UI**: Improve the Streamlit interface with better styling, loading indicators, or additional filters (e.g., genres, ratings).
6. **Remove Redundant Code**: Consolidate the duplicate `make_cover_url` function in `api_clients.py`.
7. **API Key Support**: Add support for Google Books API keys for authenticated queries.

---

## Example Usage
1. User inputs:
   - Topics: "science fiction"
   - Recency: "Last 10 years"
   - Formats: ["Ebook", "Print"]
2. Clicks "Get recommendations."
3. The app queries Open Library with "science fiction" and displays up to 5 books with titles, authors, cover images, and descriptions.

---

## Code Structure Diagram
```
Book Recommendation App
├── app.py
│   ├── main(): Streamlit UI and recommendation trigger
│   └── get_recommendations(): Fetches and processes book data
├── api_clients.py
│   ├── search_openlibrary(): Queries Open Library API
│   ├── search_google_books(): Queries Google Books API
│   └── make_cover_url(): Generates cover image URLs
├── models.py
│   └── BookCandidate: Data model for books
```

---

## License
This project is intended for educational and demonstration purposes. Ensure compliance with the terms of use for the Open Library and Google Books APIs when deploying or extending this application.