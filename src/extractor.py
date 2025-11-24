from newspaper import Article

def extract_title_paragraphs(url: str, max_paras: int = 8):
    print(f"[INFO] Fetching: {url}")  # Show the link in terminal
    try:
        a = Article(url)
        a.download()
        a.parse()
        title = a.title
        paragraphs = [p for p in a.text.split("\n") if p.strip()]
        for idx, para in enumerate(paragraphs[:max_paras], 1):
            print(f"[PARA {idx}] {para}")
        return title, paragraphs[:max_paras]
    except Exception as e:
        print(f"[WARN] Failed {url}: {e}")
        return "", []