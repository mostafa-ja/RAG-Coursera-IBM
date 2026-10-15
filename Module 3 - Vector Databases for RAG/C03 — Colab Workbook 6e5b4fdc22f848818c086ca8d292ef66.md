# C03 — Colab Workbook

Colab notebooks for Course 03, on the Google Gemini stack (CP-G.3, Oct 11, 2026). Add `GOOGLE_API_KEY` to Colab 🔑 Secrets; CPU runtime is enough. Each notebook was converted from the legacy CP4 notebook, JSON-validated and syntax-checked (every code cell and `%%writefile` script).

## C03–M1–L1 · Similarity Search by Hand

[C03-M1-L1_Similarity_Search_by_Hand_Colab.ipynb](C03-M1-L1_Similarity_Search_by_Hand_Colab.ipynb)

`C03-M1-L1_Similarity_Search_by_Hand_Colab.ipynb`
**What changed:** Groq/HF setup cell + watsonx shim removed → Cell 1/Cell 2 · `SentenceTransformer('paraphrase-MiniLM-L6-v2')` → `model = embeddings` (`gemini-embedding-2`), `model.encode` → `np.array(model.embed_documents(...))` / `embed_query` (3072-d instead of 384-d) · manual L2 / dot / cosine code and Exercises 1–3 unchanged · Colab exercises rewritten (embedding-2 vs 001, unit vectors ⇒ dot = cosine, LLM-made tricky sentences via `.text`, brute-force search at scale).

## C03–M1–L2 · Similarity Search on Text Using Chroma DB and Python

[C03-M1-L2_Similarity_Search_Text_ChromaDB_Colab.ipynb](C03-M1-L2_Similarity_Search_Text_ChromaDB_Colab.ipynb)

`C03-M1-L2_Similarity_Search_Text_ChromaDB_Colab.ipynb`
**What changed:** new `%%writefile gemini_ef.py` — `GeminiEmbeddingFunction` (Chroma embedding function over `gemini-embedding-2`, batches ≤ 100) · `similarity_search.py`: `SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2")` → `GeminiEmbeddingFunction()` · Granite-embedding exercise → `gemini-embedding-001` comparison · mini RAG uses `llm.invoke(...).text`.

## C03–M2–L1 · Similarity Search on Employee Records using Python and Chroma DB

[C03-M2-L1_Similarity_Search_Employee_Records_ChromaDB_Colab.ipynb](C03-M2-L1_Similarity_Search_Employee_Records_ChromaDB_Colab.ipynb)

`C03-M2-L1_Similarity_Search_Employee_Records_ChromaDB_Colab.ipynb`
**What changed:** `gemini_ef.py` added · `similarity_employeedata.py` and `books_advanced_search.py` use `GeminiEmbeddingFunction()` (`data.py` unchanged) · notebook exercises (filters, `where_document`, LLM staffing assistant) on Gemini.

## C03–M2–L2 · Practice Project: Food Recommendation System Using Chroma DB

[C03-M2-L2_Food_Recommendation_System_ChromaDB_Colab.ipynb](C03-M2-L2_Food_Recommendation_System_ChromaDB_Colab.ipynb)

`C03-M2-L2_Food_Recommendation_System_ChromaDB_Colab.ipynb`
**What changed:** `llm_factory.py` → `gemini_ef.py` · `shared_functions.py` uses `GeminiEmbeddingFunction()` · `enhanced_rag_chatbot.py`: watsonx credentials + `ModelInference(granite-3-3-8b)` → `ChatGoogleGenerativeAI("gemini-3.8-flash")`, `model.generate(...)["results"][0]["generated_text"]` → `model.invoke(prompt).text` · other scripts unchanged · exercises: Gemini model comparison (3.8-flash / 3.5-flash-lite / 2.5-flash), `gemini-embedding-001`, Gradio 6 chat UI (`type="messages"` dropped).