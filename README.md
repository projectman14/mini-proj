# MiniProject

A Python project for claim verification using web search, OCR, and text similarity.

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/MiniProject.git
cd MiniProject
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure SerpAPI Key

Create a `.env` file in the project root:

```
SERPAPI_KEY=your_serpapi_key_here
```

Replace `your_serpapi_key_here` with your actual SerpAPI key.

### 5. Install Tesseract (for OCR)

- Download the Windows installer from:  
  [UB Mannheim Tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki)
- Run the installer and check the option to add Tesseract to PATH.
- If you forget to check PATH, add the install directory (e.g., `C:\Program Files\Tesseract-OCR`) to your system PATH manually.

### 6. Download NLTK Data

Open a Python shell and run:

```python
import nltk
nltk.download('punkt')
```

### 7. Prepare Data

- Place your claims in `data/claims.csv` with columns: `text,image,label`
- Example:
  ```
  text,image,label
  Vitamin and mineral supplements cannot cure COVID-19,,Real
  ```

### 8. Run the Project

```sh
python main.py
```

### 9. Outputs

- Features will be saved to `outputs/features.csv`.

---

## Notes

- The project uses SerpAPI for Google search (each claim triggers one API call).
- The code processes only the headline (title) of each search result.
- The first 8 paragraphs of each article are available for further processing if needed.
- The virtual environment and output files are excluded from version control via `.gitignore`.

---

10 -------- 0%
100 -------- 70%
200 -------- 71%