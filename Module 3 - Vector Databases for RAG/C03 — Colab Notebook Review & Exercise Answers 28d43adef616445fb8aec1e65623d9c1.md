# C03 — Colab Notebook Review & Exercise Answers

<aside>
📍

**Status (run 4, Oct 13):** CP0–CP3 ✅ restored on this page from the last export (3 corrected .ipynb re-attached). CP4 ✅ CP5 ✅ — **review complete.** All 4 corrected notebooks are attached; nothing left to continue. Optional next step: run each notebook once in Colab with a real key to confirm the live Gemini outputs match the "Expected" notes.

</aside>

Review of the 4 Module 3 (Vector Databases for RAG) Colab notebooks against the IBM originals and the Gemini conversion plan (CP-G.3 workbook): Cell 1 minimal pip, Cell 2 Colab Secrets → `ChatGoogleGenerativeAI("gemini-3.8-flash")` + `GoogleGenerativeAIEmbeddings("models/gemini-embedding-2")`, `.text`, LangChain 1.x imports.

## Checkpoint log

| CP | Scope | State | Notes |
| --- | --- | --- | --- |
| CP0 | Setup: unpack, venv, fake Gemini, Notion page | ✅ | venv Python 3.13, superset of all Cell 1 lines resolved to: langchain-core 1.6.10 · langchain-google-genai 4.4.1 · google-genai 2.30.0 · langchain-chroma 1.1.0 · chromadb 1.5.9 · gradio 6.30.0 · numpy 2.5.4 · scipy 1.18.1 · pydantic 2.14.1 (+ torch CPU, preinstalled on Colab). Harness: `google.colab` stub (userdata/output), fake Gemini that patches only the network calls of the real `ChatGoogleGenerativeAI` / `GoogleGenerativeAIEmbeddings` (list-of-blocks content like Gemini 3, `.text`, streaming, tool calls, JSON/ReAct replies, model-ID check), loaded via `sitecustomize` so `!python script.py` subprocesses get it too; nbclient runner with venv on PATH. Model IDs checked on [ai.google.dev](http://ai.google.dev) (models page updated 2026-10-09): `gemini-3.8-flash`, `gemini-3.5-flash-lite`, `gemini-embedding-2`, `gemini-embedding-001` exist; `gemini-2.5-flash` exists but is limited to accounts that used it before. |
| CP1 | C03-M1-L1 Similarity Search by Hand | ✅ | as-is 129 cells / 0 errors; corrected 137 cells / 0 errors with run_answer=True; 2 bugs fixed, starters restored, 7 answers; .ipynb attached |
| CP2 | C03-M1-L2 Similarity Search on Text (Chroma) | ✅ | page re-created in this workspace (Oct 13) from the CP1 export (same pinned versions re-resolved) · as-is 18 cells / 1 error (C5 `NotFoundError`) · corrected 29 cells / 0 errors · 2 issues fixed, lab Practice Ex. 1–3 added, 6 answers; .ipynb attached |
| CP3 | C03-M2-L1 Employee Records (Chroma) | ✅ | corrected 45 cells (28 code) / 0 errors with run_answer=True · 3 issues fixed in books script, lab Ex. 1–4 + Bonus added, 10 answers; .ipynb attached · earlier notes: compare done · as-is 11 code cells / 0 errors (Oct 13 re-run, harness rebuilt) · bugs: books Ex. 3 genre filter `Fantasy` only (2 of 4 books), wrong print labels ("Searching for Python developers" in books script), combined dystopian search has no genre filter (returns Gatsby/HP/Dune too) · tested for C4.1: `where_document={"$contains": "Python"}` is case-sensitive (misses "python scripting"); metadata list `skills_list=["Python",…]`  • `{"skills_list": {"$contains": "Python"}}` works (Chroma 1.5.9); `$contains` on a plain string field silently returns [] · plan for corrected nb: 💡 note after Cell 2; lab Ex. 1–4 + Bonus as task + starter + ✅ Answer (Ex. 4 answer writes the fixed full script and runs it); C2/C3 → starters + answers; C4.1–3 answers; C1 stays as given setup code · corrected notebook pending |
| CP4 | C03-M2-L2 Food Recommendation (Chroma + Gradio) | ✅ | compare started: 8 scripts diffed vs IBM files — `shared_functions.py` only EF swap; `enhanced_rag_chatbot.py` watsonx → `ChatGoogleGenerativeAI`  • `.invoke().text` (max_new_tokens 400 dropped — good for Gemini 3 thinking); interactive/advanced/system_comparison/calorie_checker identical; `result_limitter.py` = IBM `result_limiter.py` but misspelled name; Ex. 1 written as new `interactive_search_2.py` (lab: modify `interactive_search.py`). Dataset: GitHub raw URL and IBM cf-courses URL both HTTP 200, identical md5, 185 items (2 embedding calls per populate). To check: Step 3 md still says "swapped to the shim"; C4 `.launch(share=True, debug=True)` blocks the cell; C4 needs `bot` from C2; `gemini-2.5-flash` in C2. **CP4a ✅ (run 4):** harness rebuilt (same versions: langchain-core 1.6.10 · langchain-google-genai 4.4.1 · google-genai 2.30.0 · chromadb 1.5.9 · gradio 6.30.0 · numpy 2.5.4) · as-is run: 24 code cells / 0 errors (only patch: C4 blocking launch → non-blocking launch + close; Gradio served on 7860 and answered). Calls: 10 full populates × 2 batch embed calls (100 + 85 texts) + 26 query embeds. To fix: lab exercise cells already solved (→ starters + answers), result_limitter.py typo, Step 3 md "shim", chatbot banner "Powered by IBM Granite", C4 blocking debug=True. **CP4b ✅:** ai.google.dev models page (Oct 13): gemini-3.8-flash + gemini-3.5-flash-lite exist; 2.5 models served only "to users who have actively used them in the past … for any new projects use 3.5 Flash-Lite or 3.8 Flash" → C2 drop gemini-2.5-flash + try/except per model. Rate-limit docs give no free-tier RPM numbers (refer to AI Studio rate-limit page) → noted as risk only, not proven. Gradio 6.30 test: re-running launch() without close() moves to port 7861 (no crash); fixed server_port=7860 twice → OSError "Cannot find empty port". **CP4c ✅:** corrected notebook 48 cells (30 code) / 0 errors with run_answer=True · 3 issues fixed + text fixes, Ex. 1–3 back to tasks, 6 answers; .ipynb attached |
| CP5 | Final: corrected .ipynb attached, summary | ✅ | all 4 corrected notebooks attached under their sections; verdicts: M1-L1 ✅ · M1-L2 ⚠️ · M2-L1 ⚠️ · M2-L2 ⚠️; expected outputs for M2-L2 checked against FoodDataSet.json (no burger, 5 chicken dishes) |

## Notebooks

### C03-M1-L1 — Similarity Search by Hand

<aside>
✅

**Verdict: ✅ works** (0 errors as-is and 0 errors corrected, answers run). Minor fixes: re-run-safe `model`, IBM starter cells restored, lighter C4.

</aside>

| Original (IBM, sentence-transformers) | Converted (Gemini) | Correct? |
| --- | --- | --- |
| `!pip install sentence-transformers==4.1.0`  • Restart-kernel section | Cell 1 `!pip install -q -U langchain-google-genai langchain-core langchain-chroma google-genai`, no restart | ✅ (torch/scipy preinstalled on Colab) |
| — | Cell 2: `userdata.get("GOOGLE_API_KEY")`, `gemini-3.8-flash`, `models/gemini-embedding-2` | ✅ plan IDs (⚠️ `temperature=0.2`, see Things to know) |
| `from sentence_transformers import SentenceTransformer` | removed, comment | ✅ |
| `model = SentenceTransformer('paraphrase-MiniLM-L6-v2')` | `model = embeddings` | ⚠️ breaks on re-run → fixed: `model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")` |
| `embeddings = model.encode(documents)` | `np.array(model.embed_documents(documents))` | ✅ shape (4, 3072) instead of (4, 384); note added |
| Exercise 3 `model.encode([query])` | `np.array([model.embed_query(query)])` (also in `<details>` solution) | ✅ |
| L2 / dot / cosine / torch normalize code, all markdown, TOC, change log | unchanged (diffed cell by cell — 0 markdown lost) | ✅ |
| Exercise 1/2/3 starter cells (`### YOUR CODE GOES HERE ###`) | contained the full solution (copied from a solved copy) | ❌ → restored starters, answers moved to hidden cells |
| — | 🧪 Colab exercises C1–C4 | ✅ added; C2 had an open TODO → answered |

**Bugs proven:** (1) `model = embeddings` → after cell "Generate embeddings" rebinds `embeddings` to a NumPy array, re-running the model cell gives `AttributeError: 'numpy.ndarray' object has no attribute 'embed_query'` (reproduced). (2) C4 `np.random.randn(100_000, 3072).astype("float32")` allocates a 2.46 GB float64 temp + 1.2 GB copy → now `default_rng().standard_normal(..., dtype=float32)` (1.2 GB).

**Corrected notebook (7 ✅ Answer cells + 💡 note):**

[C03-M1-L1_Similarity_Search_by_Hand_Colab.ipynb](C03-M1-L1_Similarity_Search_by_Hand_Colab.ipynb)

### C03-M1-L2 — Similarity Search on Text (Chroma)

<aside>
⚠️

**Verdict: ⚠️ works with fixes** — as-is 18 cells / 1 error (C5); corrected 29 cells / 0 errors with run_answer=True (Run all with boxes unticked stops at the first ✅ Answer, as intended). Lab script itself runs fine.

</aside>

| Original (IBM lab + GitHub `similarity_search.py`) | Converted (Gemini) | Correct? |
| --- | --- | --- |
| Task 1 `pip install chromadb==1.0.12 sentence-transformers==4.1.0` in Cloud IDE terminal | Cell 1 `!pip install -q -U langchain-google-genai langchain-core langchain-chroma google-genai chromadb`, no restart → chromadb 1.5.9 | ✅ (1.0.12 → 1.5.9: `configuration={"hnsw":…, "embedding_function": ef}` still valid) |
| — | Cell 2 Colab Secrets, `gemini-3.8-flash`, `models/gemini-embedding-2` | ✅ plan |
| `embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")` | `%%writefile gemini_ef.py` → `GeminiEmbeddingFunction()` (batches ≤ 100, `name()/get_config()/build_from_config()`) | ✅ (tested: re-opening a persisted collection works when `gemini_ef` is imported) |
| Tasks 2–5 code (client, `my_grocery_collection` cosine, 14 texts, ids, metadata, `get()`, `perform_similarity_search`) | `%%writefile similarity_search.py` | ✅ diffed against IBM GitHub file: only the import + `ef =` line differ. Stale comment "using SentenceTransformers" → fixed |
| Task 6 `python3.11 similarity_search.py` with `query_term="apple"` | `!python similarity_search.py` with IBM's final `["red","fresh"]` | ✅ runs (subprocess gets `GOOGLE_API_KEY` from Cell 2) · ⚠️ "apple" step only via the answer cell |
| Lab text Tasks 1–6 (explanations) | condensed into one markdown cell | ⚠️ shortened, nothing code-relevant lost (Cloud-IDE file-creation steps not needed) |
| **Practice Exercises 1–4** (str→list, `[query_term]`→`query_term`, outer loop, verify) | ❌ missing — script was already the solved version and has **no str→list conversion** | ❌ → added task cell + starter + ✅ Answer |
| — | 🧪 C1–C5 (interactive query, cosine/L2/IP, embedding-001, PersistentClient, mini RAG `.text`) | ⚠️ were solved code only, C5 broken → starters + ✅ Answers |

**Bugs proven:** (1) **C5 `NotFoundError: Collection [...] does not exist`** — C2's loop calls `build("grocery_cosine")`, which deletes and recreates the collection that C1 stored in `col`; the old handle is dead (reproduced as-is). Fixed: C2 uses `cmp_cosine / cmp_l2 / cmp_ip`. (2) Lab Ex. 1 missing: with a bare string the outer loop runs over the letters and fails with `list index out of range` (reproduced). Checked and *not* bugs: `!python` subprocess sees the API key; 14 texts = 1 embedding call per build (no free-tier 429 risk); `PersistentClient` re-open works only with `gemini_ef` imported (otherwise `Embedding function gemini not found` — documented in C4 answer).

**Corrected notebook (6 ✅ Answer cells + 💡 note):**

[C03-M1-L2_Similarity_Search_Text_ChromaDB_Colab.ipynb](C03-M1-L2_Similarity_Search_Text_ChromaDB_Colab.ipynb)

### C03-M2-L1 — Similarity Search on Employee Records (Chroma)

<aside>
⚠️

**Verdict: ⚠️ works with fixes** — as-is 11 code cells / 0 errors, but the books practice script gave wrong results (2 of 4 books for *Fantasy or Science Fiction*) and the lab's Exercises 1–4 + Bonus were not tasks. Corrected: 28 code cells / 0 errors with run_answer=True; with boxes unticked only the 10 ✅ Answer cells stop (as intended).

</aside>

| Original (IBM lab PDF + GitHub scripts) | Converted (Gemini) | Correct? |
| --- | --- | --- |
| Task 1 `pip install chromadb sentence-transformers` in Cloud IDE | Cell 1 `!pip install -q -U langchain-google-genai langchain-core langchain-chroma google-genai chromadb`, no restart → chromadb 1.5.9 | ✅ |
| — | Cell 2 Colab Secrets, `gemini-3.8-flash` (temperature 0.2), `models/gemini-embedding-2`; extra `llm_model` lambda alias | ✅ plan (alias unused, harmless) |
| `SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2")` | `%%writefile gemini_ef.py` → `GeminiEmbeddingFunction()` | ✅ same file as M1-L2 |
| `data.py` (15 `EMPLOYEES`, 8 `BOOKS`) | `%%writefile data.py` | ✅ matches lab list (8 books) |
| Tasks 2–6 `similarity_employeedata.py` (cosine collection, documents, metadata, similarity / `$eq` / `$gte` / `$in` / combined search) | `%%writefile`  • `!python` | ✅ only EF line differs; stale comment "using SentenceTransformers" → fixed |
| **Practice Ex. 1–4 + Bonus** (books: documents, metadata, advanced search, run; decade / page count / themes) | one solved `books_advanced_search.py` from a GitHub student solution | ❌ → Ex. 1–4 + Bonus as task cells + empty cells + ✅ Answers; script cell is now a runnable skeleton; Ex. 4 answer writes the fixed script |
| Ex. 3 *Filter books by genre (Fantasy or Science Fiction)* | `where={"genre": "Fantasy"}` | ❌ found 2 books → `{"genre": {"$in": ["Fantasy", "Science Fiction"]}}` finds 4 |
| Ex. 3 labels | "1. Searching for Python developers:" for the book query, numbering 1/3/4/6 | ❌ → fixed labels |
| Ex. 3 *highly-rated dystopian books* | only `rating >= 4.0` filter, `n_results=5` → Gatsby, Harry Potter, Dune also listed | ⚠️ → `$and` genre = Dystopian + rating ≥ 4.0 |
| Bonus *specific decade* | 1950–1970 (two decades) | ⚠️ → `[decade, decade+9]` |
| — | 🧪 C1 (build `col`) · C2 filters · C3 LLM staffing (`.text`) · C4 Try it yourself 1–3 | ⚠️ C2/C3 were solved code, C4 had no answers → starters + ✅ Answers; C1 kept as given setup code |

**Bugs proven:** (1) books Ex. 3 genre filter returns 2 instead of 4 books (run output). (2) Combined dystopian search lists non-dystopian books (run output). (3) Tested for C4.1 on Chroma 1.5.9: `where_document` `$contains` is case-sensitive (`'python'` → `[]`), metadata lists support `$contains` (exact element), `$contains` on a plain string metadata field silently returns `[]`. Checked and *not* bugs: `!python` scripts see `GOOGLE_API_KEY`; each `!python` run is a fresh in-memory client, so `create_collection` never hits *already exists*; 15 / 8 documents = 1 embedding call each (no free-tier 429 risk).

**Corrected notebook (10 ✅ Answer cells + 💡 note):**

[C03-M2-L1_Similarity_Search_Employee_Records_ChromaDB_Colab.ipynb](C03-M2-L1_Similarity_Search_Employee_Records_ChromaDB_Colab.ipynb)

### C03-M2-L2 — Food Recommendation System (Chroma + Gradio)

<aside>
⚠️

**Verdict: ⚠️ works with fixes** — as-is 24 code cells / 0 errors (only the Gradio cell blocks with `debug=True`), but the lab exercises were pre-solved, C2 used `gemini-2.5-flash` (not offered to new API users) and some text was stale. Corrected: 48 cells (30 code) / 0 errors with run_answer=True; with boxes unticked Run all stops at the first ✅ Answer (as intended).

</aside>

| Original (IBM lab PDF + GitHub scripts) | Converted (Gemini) | Correct? |
| --- | --- | --- |
| Part 1 Task 1 `pip install` numpy 2.3.1, scipy 1.16.0, chromadb 1.0.12, sentence-transformers 4.1.0, ibm-watsonx-ai 1.3.24 | Cell 1 `!pip install -q -U langchain-google-genai langchain-core langchain-chroma google-genai chromadb gradio`, no restart → chromadb 1.5.9, gradio 6.30.0 | ✅ |
| — | Cell 2 Colab Secrets, `gemini-3.8-flash` (temperature 0.2), `models/gemini-embedding-2`, unused `llm_model` alias | ✅ plan |
| Task 1 B `wget` FoodDataSet.json (cf-courses) | `wget` from GitHub raw | ✅ both URLs HTTP 200, same file, 185 items |
| Part 2 `shared_functions.py` with `SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2")` | `%%writefile`  • `GeminiEmbeddingFunction` | ✅ only the EF line differs |
| Part 2 Task 2 `interactive_search.py` · Part 3 `advanced_search.py` · Part 5 `system_comparison.py` | `%%writefile` unchanged + piped `!printf … | python` demos | ✅ identical to IBM files |
| Part 4 `enhanced_rag_chatbot.py`: `ModelInference(ibm/granite-3-3-8b-instruct, max_new_tokens 400)`, `.generate()["results"][0]["generated_text"]` | `ChatGoogleGenerativeAI("gemini-3.8-flash")`, `.invoke(prompt).text`; variable `model` kept | ✅ (no `max_output_tokens` → no thinking-token truncation) · ⚠️ banner still "Powered by IBM Granite" → fixed |
| Step 3 markdown | "swapped to the shim" (old conversion) | ⚠️ → describes the real change |
| **Practice Ex. 1** search history (modify `interactive_search.py`) | already solved in new `interactive_search_2.py`; `help` did not list `history` | ❌ → task cell + empty cell + ✅ Answer (help lists `history`) |
| **Practice Ex. 2** `calorie_checker.py` | already solved | ❌ → task + ✅ Answer |
| **Practice Ex. 3** `result_limiter.py` | already solved, file misspelled `result_limitter.py` | ❌ → task + ✅ Answer, lab file name |
| — | 🧪 C1 build `col` · C2 3 models · C3 embedding-001 · C4 Gradio | C1 kept as setup · C2 `gemini-2.5-flash` ❌ → 3.8 Flash + 3.5 Flash-Lite with try/except · C3 re-run safe · C4 `debug=True` blocks ⚠️ → `launch(share=True)`  • close old app; all three → starters + ✅ Answers |

**Bugs proven:** (1) `gemini-2.5-flash` in C2 — Google's models page (Oct 13): 2.5 models are served only *"to users who have actively used them in the past … for any new projects, use 3.5 Flash-Lite or 3.8 Flash"* → a new key gets an error and, without try/except, the loop stops. (2) C4 `launch(debug=True)` blocks the cell until interrupted (Run all never finishes); re-running without `close()` opens a new port each time (tested on Gradio 6.30: 7860 → 7861; a fixed `server_port=7860` twice raises `OSError: Cannot find empty port`). (3) Lab exercise cells contained the solutions (nothing to try). Checked and *not* bugs: every script is a new process with its own in-memory Chroma, so collection names never clash; `create_similarity_search_collection` deletes + recreates by name; C1/C3 use their own names; 185 items = 2 batch embed calls per populate (≤ 100 per call).

**Corrected notebook (6 ✅ Answer cells + 💡 note):**

[C03-M2-L2_Food_Recommendation_System_ChromaDB_Colab.ipynb](C03-M2-L2_Food_Recommendation_System_ChromaDB_Colab.ipynb)

## Things to know when running it

- **Run all stops at the first ✅ Answer cell on purpose** ("Answer not run"). Tick `run_answer` to see an answer, or run the following cells one by one.
- **Gemini 3 temperature:** Google recommends keeping Gemini 3 models at the default `temperature=1.0`; Cell 2 uses `0.2` (plan value). It works, but if you see looping/odd answers, drop the `temperature` argument.
- **gemini-embedding-2 + LangChain:** `langchain-google-genai` 4.4.1 still sends `task_type` (RETRIEVAL_DOCUMENT / RETRIEVAL_QUERY) by default; Google's docs say embedding-2 does not use `task_type` (put task prefixes in the text instead). LangChain's own docstring uses embedding-2 this way, so this is quality info, not an error.
- **Chroma collections are shared per kernel:** `chromadb.Client()` is one in-memory store per Python process — re-creating a collection with the same name kills every older handle (`NotFoundError`). Use distinct names or rebuild the handle.
- **Persisted Chroma + custom EF:** before re-opening `./chroma_store` in a new session, run Cell 2 and the `gemini_ef.py` cell and pass `embedding_function=ef`; `./chroma_store` vanishes when the runtime resets (use a Drive path to keep it).
- **Never mix embedding models in one index:** gemini-embedding-001 and gemini-embedding-2 spaces are incompatible (both 3072-d, so it won't error — it just gives nonsense).
- **Filtered similarity search always returns `n_results` hits** if enough documents pass the filter — even when none is really relevant (M2-L1 C2: no junior ML person exists). Look at the distances. If fewer documents pass the filter, Chroma just returns fewer hits.
- **`where_document={"$contains": …}` is a case-sensitive substring match** (`"Java"` also matches *JavaScript*); for tags store a list in metadata and use `{"field": {"$contains": "Python"}}`.
- **Food project re-embeds 185 items per script run** (≈ 10 runs × 2 batch calls in the notebook). Google's rate-limit page does not publish the free-tier numbers (see aistudio.google.com/rate-limit); if a script prints `429 RESOURCE_EXHAUSTED`, wait a minute and re-run that cell.
- **Gradio in Colab:** use `demo.launch(share=True)` (no `debug=True`) so the cell finishes; call `demo.close()` before re-launching.
- **`gemini-2.5-flash` is not available to new API keys** — use `gemini-3.8-flash` or `gemini-3.5-flash-lite`.

## Exercise answers (try first, then open)

### ✅ Answer: C03-M1-L1 · Exercise 1 · efficient L2 matrix

```python
l2_dist_manual_improved = np.zeros([4, 4])
for i in range(embeddings.shape[0]):
    for j in range(embeddings.shape[0]):
        if j > i:      # compute the upper triangle only (diagonal stays 0)
            l2_dist_manual_improved[i, j] = euclidean_distance_fn(embeddings[i], embeddings[j])
        elif i > j:    # mirror it into the lower triangle
            l2_dist_manual_improved[i, j] = l2_dist_manual_improved[j, i]

print("same as full loop:", np.allclose(l2_dist_manual_improved, l2_dist_manual))
l2_dist_manual_improved
```

**Expected / what you should see:** `same as full loop: True`, then a symmetric 4×4 matrix with zeros on the diagonal. With real Gemini embeddings [0,1] and [2,3] are the smallest off-diagonal values (software pair, insect pair).

### ✅ Answer: C03-M1-L1 · Exercise 2 · vectors are normalized

```python
lengths = np.sqrt(np.sum(normalized_embeddings_manual**2, axis=1))   # L2 norm of every row
print(lengths)
print("all unit length:", np.allclose(lengths, 1.0))
```

**Expected / what you should see:** `[1. 1. 1. 1.]` and `all unit length: True` (gemini-embedding-2 3072-d vectors are already unit length, so the norms before normalizing are ≈1 too).

### ✅ Answer: C03-M1-L1 · Exercise 3 · similarity search with a query

```python
# 1. embed the query (embed_query = the query side of the same Gemini model)
query_embedding = np.array([model.embed_query(
    "Who is responsible for a coding project and fixing others' mistakes?"
)])
# 2. normalize it
normalized_query_embedding = torch.nn.functional.normalize(torch.from_numpy(query_embedding)).numpy()
# 3. cosine similarity = dot product of unit vectors  -> shape (4, 1)
cosine_similarity_q3 = normalized_embeddings_manual @ normalized_query_embedding.T
print(np.round(cosine_similarity_q3.ravel(), 3))
# 4.-5. best match
highest_cossim_position = cosine_similarity_q3.argmax()
documents[highest_cossim_position]
```

**Expected / what you should see:** The highest cosine is for a software sentence; IBM's expected answer is document 0 *'Bugs introduced by the intern had to be squashed by the lead developer.'* With Gemini you should get one of the two software sentences (0 is expected, 1 is also defensible); the two insect sentences must score clearly lower.

### ✅ Answer: C03-M1-L1 · C1 · compare Gemini embedding models

```python
for name in ["models/gemini-embedding-2", "models/gemini-embedding-001"]:
    m = GoogleGenerativeAIEmbeddings(model=name)
    e = np.array(m.embed_documents(documents))
    e /= np.linalg.norm(e, axis=1, keepdims=True)
    sim = e @ e.T
    np.fill_diagonal(sim, -np.inf)            # ignore self-similarity
    partner = sim.argmax(axis=1)              # nearest other document for each row
    print(f"{name}: dim={e.shape[1]}  nearest partner per doc = {partner.tolist()}  "
          f"doc0->doc1 cos = {sim[0, 1]:.3f}  {'✅ correct' if partner[0] == 1 else '❌ wrong'}")
```

**Expected / what you should see:** Both models print `dim=3072` and `nearest partner per doc = [1, 0, 3, 2]` with ✅ for doc0→doc1. Note the absolute cosine values differ between models — the two embedding spaces are incompatible, never mix them in one collection.

### ✅ Answer: C03-M1-L1 · C2 · unit vectors: dot = cosine, and L2 ranks the same

```python
e_norm = normalized_embeddings_manual
print("dot of unit vectors == cosine:", np.allclose(e_norm @ e_norm.T, cosine_similarity_manual, atol=1e-5))
l2_unit = scipy.spatial.distance.cdist(e_norm, e_norm, "euclidean")
print("||a-b||² == 2 - 2·cos:", np.allclose(l2_unit**2, 2 - 2 * cosine_similarity_manual, atol=1e-6))
# same ranking: smallest L2 distance  ⇔  largest cosine similarity
print("same ranking per row:", all((np.argsort(l2_unit[r]) == np.argsort(-cosine_similarity_manual[r])).all()
                                   for r in range(len(e_norm))))
```

**Expected / what you should see:** Three `True` lines: dot = cosine, ‖a−b‖² = 2 − 2·cos, and L2 ranking = cosine ranking for every row. That's why Chroma's `l2`, `ip` and `cosine` spaces give the same order on normalized embeddings.

### ✅ Answer: C03-M1-L1 · C3 · LLM-made tricky sentences

```python
raw = llm.invoke("Write 6 short sentences, one per line, no numbering: 3 pairs where each pair "
                 "shares many words but has a different meaning.").text
tricky = [s.strip().lstrip("-*• ").strip() for s in raw.splitlines() if s.strip()][:6]
e = np.array(model.embed_documents(tricky)); e /= np.linalg.norm(e, axis=1, keepdims=True)
sim = e @ e.T
for k in range(0, len(tricky) - 1, 2):
    others = [sim[k, j] for j in range(len(tricky)) if j not in (k, k + 1)]
    print(f"pair {k//2+1}: cos={sim[k, k+1]:.2f}  (vs other sentences max {max(others):.2f})")
    print("   ", tricky[k], "|", tricky[k+1])
# If a pair's cosine is clearly higher than with the other sentences, the embedding is
# "fooled" by shared words/topic; a low value means it captured the different meaning.
```

**Expected / what you should see:** Six sentences (3 pairs, e.g. *bank* = money vs river). For each pair, the printed cosine vs. the other sentences tells you if the embedding was fooled: Gemini embeddings usually give such pairs only moderate similarity (meaning wins over shared words). Output varies per run.

### ✅ Answer: C03-M1-L1 · C4 · brute-force search at scale

```python
import time
dim = e_norm.shape[1]
rng = np.random.default_rng(0)
db = rng.standard_normal((100_000, dim), dtype=np.float32)   # ~1.2 GB, no float64 copy
db /= np.linalg.norm(db, axis=1, keepdims=True)
q = e_norm[0].astype("float32")
t = time.time(); scores = db @ q; top5 = np.argsort(-scores)[:5]; t_sort = time.time() - t
t = time.time(); part = np.argpartition(-scores, 5)[:5]; t_part = time.time() - t
print(f"matmul+argsort: {t_sort:.3f}s   argpartition only: {t_part:.4f}s   top-5: {top5.tolist()}")
print("same top-5 set:", set(top5) == set(part))
del db   # free the RAM
```

**Expected / what you should see:** Full sort ~0.1–0.5 s on Colab CPU, `argpartition` ~10–100× faster, `same top-5 set: True`. Cost still grows linearly with n — ANN indexes (HNSW) avoid scanning every vector.

### ✅ Answer: C03-M1-L2 · Lab Practice Exercises 1–3 · multiple query terms

```python
import chromadb
from gemini_ef import GeminiEmbeddingFunction
texts = ['fresh red apples','organic bananas','ripe mangoes','whole wheat bread','farm-fresh eggs','natural yogurt',
         'frozen vegetables','grass-fed beef','free-range chicken','fresh salmon fillet','aromatic coffee beans',
         'pure honey','golden apple','red fruit']
lab_client = chromadb.Client()
lab_col = lab_client.get_or_create_collection(
    "lab_practice_grocery",
    configuration={"hnsw": {"space": "cosine"}, "embedding_function": GeminiEmbeddingFunction()})
lab_col.upsert(documents=texts, ids=[f"food_{i + 1}" for i in range(len(texts))],
               metadatas=[{"source": "grocery_store", "category": "food"} for _ in texts])

def perform_similarity_search(collection, all_items, query_term=["red", "fresh"]):   # Ex. 1
    try:
        if isinstance(query_term, str):          # Ex. 1: a single string -> list with one query
            query_term = [query_term]
        results = collection.query(
            query_texts=query_term,              # Ex. 2: no extra [ ] around query_term
            n_results=3)
        if not results or not results['ids'] or len(results['ids'][0]) == 0:
            print(f'No documents found similar to "{query_term}"')
            return
        for q in range(len(query_term)):         # Ex. 3: outer loop = one block per query
            print(f'Top 3 similar documents to "{query_term[q]}":')
            for i in range(min(3, len(results['ids'][q]))):
                doc_id = results['ids'][q][i]
                score = results['distances'][q][i]
                text = results['documents'][q][i]
                if not text:
                    print(f' - ID: {doc_id}, Text: "Text not available", Score: {score:.4f}')
                else:
                    print(f' - ID: {doc_id}, Text: "{text}", Score: {score:.4f}')
    except Exception as error:
        print(f"Error in similarity search: {error}")

all_items = lab_col.get()
perform_similarity_search(lab_col, all_items, "apple")            # Ex. 4: string still works
perform_similarity_search(lab_col, all_items, ["red", "fresh"])   # Ex. 4: two queries
```

**Expected / what you should see:** Two blocks for `"apple"`: one block *Top 3 similar documents to "apple"* (expected: `golden apple`, `fresh red apples`, then another fruit), then one block each for `"red"` (`red fruit`, `fresh red apples`, …) and `"fresh"` (`fresh salmon fillet` / `farm-fresh eggs` / `fresh red apples`). Scores are cosine distances (0 = identical, smaller = more similar). Why the `isinstance` line matters (tested): Chroma accepts a bare string as one query, but the outer loop then runs over the letters of `"apple"` — it prints a block for `"a"` and then fails with *Error in similarity search: list index out of range*.

### ✅ Answer: C03-M1-L2 · C1 · query interactively

```python
for q in ["something sweet for breakfast", "seafood", "a hot drink"]:
    r = col.query(query_texts=[q], n_results=3)
    print(f"{q!r:32} →", list(zip(r["documents"][0], [round(d, 3) for d in r["distances"][0]])))
```

**Expected / what you should see:** Three lines, each with 3 `(document, distance)` pairs sorted by increasing cosine distance. With real Gemini embeddings: breakfast → `pure honey` / `natural yogurt` / `whole wheat bread` (order may vary), seafood → `fresh salmon fillet` first, hot drink → `aromatic coffee beans` first. No re-embedding of the 14 texts happens — only the query is embedded.

### ✅ Answer: C03-M1-L2 · C2 · cosine vs L2 vs inner product

```python
res = {}
for space in ["cosine", "l2", "ip"]:
    r = build(f"cmp_{space}", space).query(query_texts=["red"], n_results=3)   # own names: keeps C1's `col` alive
    res[space] = r
    print(f"{space:6}", list(zip(r["documents"][0], [round(d, 3) for d in r["distances"][0]])))
same = res["cosine"]["documents"][0] == res["l2"]["documents"][0] == res["ip"]["documents"][0]
print("same top-3 order:", same)
cos_d = res["cosine"]["distances"][0]
print("ip distance == cosine distance:", all(abs(a - b) < 1e-4 for a, b in zip(res["ip"]["distances"][0], cos_d)))
print("l2 distance == 2 × cosine distance:", all(abs(a - 2 * b) < 1e-4 for a, b in zip(res["l2"]["distances"][0], cos_d)))
```

**Expected / what you should see:** `same top-3 order: True` with real Gemini embeddings (items with exactly equal distance may swap places — the offline test hit such a tie) and two more `True` lines. Gemini embeddings are unit length, so Chroma's `ip` distance (1 − a·b) equals the cosine distance (1 − cos), and Chroma's `l2` (squared L2 = 2 − 2·cos) is exactly 2 × the cosine distance — only the numbers change, never the ranking.

### ✅ Answer: C03-M1-L2 · C3 · gemini-embedding-001 vs gemini-embedding-2

```python
ef_001 = GeminiEmbeddingFunction("models/gemini-embedding-001")
col_001 = build("grocery_gemini_001", fn=ef_001)
queries = ["red", "fresh"]
r1 = col_001.query(query_texts=queries, n_results=3)
r2 = col.query(query_texts=queries, n_results=3)          # C1 collection = gemini-embedding-2
for q, d1, d2 in zip(queries, r1["documents"], r2["documents"]):
    print(f"{q:6} 001 → {d1}\n{'':6} 2   → {d2}   overlap {len(set(d1) & set(d2))}/3")
```

**Expected / what you should see:** For each query two lists of 3 documents; `red` should give `red fruit` and `fresh red apples` in both models, `fresh` gives the *fresh …* items. Overlap is usually 2/3 or 3/3, but the distances are different (separate embedding spaces — never put vectors from both models into one collection).

### ✅ Answer: C03-M1-L2 · C4 · persist the database

```python
pclient = chromadb.PersistentClient(path="chroma_store")
pcol = pclient.get_or_create_collection("grocery", configuration={"hnsw": {"space": "cosine"}, "embedding_function": ef})
pcol.upsert(documents=texts, ids=[f"food_{i+1}" for i in range(len(texts))])   # upsert = safe to re-run
print(pcol.count(), "docs stored in ./chroma_store")

# simulate a new session: a fresh client on the same folder sees the data without re-adding it
reopened = chromadb.PersistentClient(path="chroma_store").get_collection("grocery", embedding_function=ef)
print("reopened:", reopened.count(), "docs →", reopened.query(query_texts=["apple"], n_results=1)["documents"][0])
```

**Expected / what you should see:** `14 docs stored in ./chroma_store` (still 14 after re-running, because `upsert` replaces by id) and `reopened: 14 docs → ['golden apple']` (or `fresh red apples`). In a new Colab session run Cell 2 and the `gemini_ef.py` cell first and pass `embedding_function=ef` — without it Chroma raises *Embedding function gemini not found*. `./chroma_store` is deleted when the runtime resets; use a Google Drive path to keep it.

### ✅ Answer: C03-M1-L2 · C5 · mini RAG

```python
question = "I want a healthy protein for dinner — what do you have?"
hits = col.query(query_texts=[question], n_results=3)["documents"][0]
print("retrieved:", hits)
prompt = (f"You are a grocery assistant. Answer ONLY from these grocery items: {hits}. "
          f"If none of them fits, say so.\nQuestion: {question}")
print(llm.invoke(prompt).text)        # .text = plain string (Gemini 3 returns a list of content blocks)
```

**Expected / what you should see:** `retrieved:` shows 3 protein items (typically `free-range chicken`, `grass-fed beef`, `fresh salmon fillet`, maybe `farm-fresh eggs`), then a short Gemini answer that recommends only those items.

### ✅ Answer: C03-M2-L1 · Lab Exercise 1 · book documents for semantic search

```python
from data import BOOKS
def make_book_document(book):
    # combine title, author, genre, year, description, setting, themes, rating and pages into one text
    document = f"The book titled '{book['title']}' by {book['author']} is a {book['genre']} novel published in {book['year']}. "
    document += f"It tells {book['description']}. "
    document += f"The story is set in {book['setting']} and explores themes such as {book['themes']}. "
    document += f"It has a reader rating of {book['rating']} and spans {book['pages']} pages."
    return document

book_documents = [make_book_document(b) for b in BOOKS]
print(len(book_documents), "documents")
print(book_documents[3])
```

**Expected / what you should see:** `8 documents`, then the Harry Potter text: *The book titled 'Harry Potter and the Philosopher's Stone' by J.K. Rowling is a Fantasy novel published in 1997. It tells A young wizard discovers … The story is set in England, magical world and explores themes such as friendship, courage, … It has a reader rating of 4.5 and spans 223 pages.* Title + description + themes + setting all end up in the embedded text, so a query like *magical adventure* can match on any of them.

### ✅ Answer: C03-M2-L1 · Lab Exercise 2 · add the books with full metadata

```python
import chromadb
from data import BOOKS
from gemini_ef import GeminiEmbeddingFunction
book_documents = [make_book_document(b) for b in BOOKS]          # from Exercise 1
books_client = chromadb.Client()
books_col = books_client.get_or_create_collection(
    name="books_nb",                                               # own name: does not clash with other collections
    metadata={"description": "A collection for storing books data"},
    configuration={"hnsw": {"space": "cosine"}, "embedding_function": GeminiEmbeddingFunction()})
books_col.upsert(                                                  # upsert = safe to re-run
    ids=[b["id"] for b in BOOKS],
    documents=book_documents,
    metadatas=[{k: b[k] for k in ["title", "author", "genre", "year", "rating", "pages",
                                  "description", "themes", "setting"]} for b in BOOKS])
print(books_col.count(), "books |", books_col.get(ids=["book_7"])["metadatas"][0])
```

**Expected / what you should see:** `8 books | {'title': 'Dune', 'author': 'Frank Herbert', 'genre': 'Science Fiction', 'year': 1965, 'rating': 4.3, 'pages': 688, …}` (key order may differ). `year`, `rating`, `pages` stay numbers, so `$gte`/`$lte` filters work on them.

### ✅ Answer: C03-M2-L1 · Lab Exercise 3 · advanced search function

```python
def show(results, query=None):
    """Print query() results (nested lists) or get() results (flat lists)."""
    if query is not None:
        for i, (m, d) in enumerate(zip(results["metadatas"][0], results["distances"][0]), 1):
            print(f"  {i}. {m['title']} — {m['author']} ({m['genre']}, {m['year']}, ★{m['rating']})  distance {d:.4f}")
    else:
        for m in results["metadatas"]:
            print(f"  - {m['title']} — {m['author']} ({m['genre']}, ★{m['rating']})")

def perform_advanced_search(collection, all_items):
    print("\n1. Similarity search: 'magical fantasy adventure'")
    show(collection.query(query_texts=["magical fantasy adventure"], n_results=3), query=True)

    print("\n2. Books with genre Fantasy or Science Fiction:")
    r = collection.get(where={"genre": {"$in": ["Fantasy", "Science Fiction"]}})
    print(f"Found {len(r['ids'])} books"); show(r)

    print("\n3. Books with rating 4.0 or higher:")
    r = collection.get(where={"rating": {"$gte": 4.0}})
    print(f"Found {len(r['ids'])} books"); show(r)

    print("\n4. Combined: highly-rated dystopian books (similarity + metadata filter)")
    show(collection.query(query_texts=["dystopian society under oppressive control"], n_results=3,
                          where={"$and": [{"genre": "Dystopian"}, {"rating": {"$gte": 4.0}}]}), query=True)

perform_advanced_search(books_col, books_col.get())
```

**Expected / what you should see:** 1 → Harry Potter and The Lord of the Rings in the top 2 (3rd is usually The Hitchhiker's Guide or Dune). 2 → **Found 4 books**: Harry Potter, The Lord of the Rings, The Hitchhiker's Guide to the Galaxy, Dune (the original GitHub solution used `{"genre": "Fantasy"}` and found only 2). 3 → **Found 8 books** (every book in the list is rated ≥ 4.1, so this filter keeps all of them). 4 → only **1984** and **The Hunger Games** (just 2 hits although `n_results=3` — the filter leaves only 2 candidates; Chroma returns fewer results instead of an error).

### ✅ Answer: C03-M2-L1 · Lab Exercise 4 · run the complete books_advanced_search.py

```python
from pathlib import Path
Path("books_advanced_search.py").write_text(r"""
import chromadb
from gemini_ef import GeminiEmbeddingFunction  # Colab: Gemini embeddings (was SentenceTransformerEmbeddingFunction)
from data import BOOKS

def print_query(results):
    for i, (doc_id, document, distance) in enumerate(zip(
            results['ids'][0], results['documents'][0], results['distances'][0])):
        m = results['metadatas'][0][i]
        print(f"  {i+1}. {m['title']} ({doc_id}) - Distance: {distance:.4f}")
        print(f"     author: {m['author']}, genre: {m['genre']}, year: {m['year']}, rating: {m['rating']}")
        print(f"     Document: {document[:100]}...")

def print_get(results):
    for m in results['metadatas']:
        print(f"  - {m['title']}: {m['author']} ({m['genre']}, {m['year']}, rating {m['rating']}, {m['pages']} pages)")

def perform_advanced_search(collection, all_items):
    print("=== Similarity Search ===")
    print("\n1. Searching for magical fantasy adventures:")
    query_text = "magical fantasy adventure"
    print(f"Query: '{query_text}'")
    print_query(collection.query(query_texts=[query_text], n_results=3))

    print("\n=== Metadata Filtering ===")
    print("\n2. Finding all Fantasy or Science Fiction books:")
    results = collection.get(where={"genre": {"$in": ["Fantasy", "Science Fiction"]}})
    print(f"Found {len(results['ids'])} Fantasy / Science Fiction books:")
    print_get(results)

    print("\n3. Finding books with rating 4.0 or higher:")
    results = collection.get(where={"rating": {"$gte": 4.0}})
    print(f"Found {len(results['ids'])} highly rated books:")
    print_get(results)

    print("\n=== Combined Search: Similarity + Metadata Filtering ===")
    print("\n4. Finding highly-rated dystopian books:")
    query_text = "dystopian society under oppressive control"
    print(f"Query: '{query_text}' with filters (genre = Dystopian, rating >= 4.0)")
    print_query(collection.query(query_texts=[query_text], n_results=3,
                                 where={"$and": [{"genre": "Dystopian"}, {"rating": {"$gte": 4.0}}]}))

if __name__ == "__main__":
    ef = GeminiEmbeddingFunction()
    client = chromadb.Client()
    collection = client.create_collection(
        name="books_collection",
        metadata={"description": "A collection for storing books data"},
        configuration={"hnsw": {"space": "cosine"}, "embedding_function": ef})
    book_documents = []
    for book in BOOKS:                                   # Exercise 1
        document = f"The book titled '{book['title']}' by {book['author']} is a {book['genre']} novel published in {book['year']}. "
        document += f"It tells {book['description']}. "
        document += f"The story is set in {book['setting']} and explores themes such as {book['themes']}. "
        document += f"It has a reader rating of {book['rating']} and spans {book['pages']} pages."
        book_documents.append(document)
    collection.add(                                      # Exercise 2
        ids=[book["id"] for book in BOOKS],
        documents=book_documents,
        metadatas=[{k: book[k] for k in ["title", "author", "genre", "year", "rating", "pages",
                                         "description", "themes", "setting"]} for book in BOOKS])
    print(f"Collection created: {collection.name}")
    all_items = collection.get()
    print(f"Number of documents: {len(all_items['documents'])}")
    perform_advanced_search(collection, all_items)       # Exercise 3
""".lstrip())
!python books_advanced_search.py
```

**Expected / what you should see:** `Collection created: books_collection`, `Number of documents: 8`, then 4 blocks: (1) Harry Potter + The Lord of the Rings on top, (2) **Found 4 Fantasy / Science Fiction books**, (3) **Found 8 highly rated books**, (4) only 1984 and The Hunger Games. The file is overwritten, so later `!python books_advanced_search.py` runs use this fixed version. Each `!python` run is a new process with a fresh in-memory `chromadb.Client()`, so `create_collection` never hits *already exists*.

### ✅ Answer: C03-M2-L1 · Lab Bonus Challenge · decade, similar page counts, multiple themes

```python
def books_in_decade(collection, decade):
    # a decade = [decade, decade + 9]; e.g. 1950 → 1950–1959
    r = collection.get(where={"$and": [{"year": {"$gte": decade}}, {"year": {"$lte": decade + 9}}]})
    return sorted((m["year"], m["title"]) for m in r["metadatas"])

def books_with_similar_pages(collection, title, tolerance=0.25):
    ref = collection.get(where={"title": title})["metadatas"][0]["pages"]
    lo, hi = int(ref * (1 - tolerance)), int(ref * (1 + tolerance))
    r = collection.get(where={"$and": [{"pages": {"$gte": lo}}, {"pages": {"$lte": hi}}, {"title": {"$ne": title}}]})
    return ref, (lo, hi), sorted((m["pages"], m["title"]) for m in r["metadatas"])

def books_matching_themes(collection, themes, n=3):
    # semantic: embed all themes in one query text, then rank
    r = collection.query(query_texts=[", ".join(themes)], n_results=n)
    semantic = [m["title"] for m in r["metadatas"][0]]
    # exact: every theme word must appear in the document (where_document is case-sensitive!)
    exact = collection.get(where_document={"$and": [{"$contains": t} for t in themes]})
    return semantic, [m["title"] for m in exact["metadatas"]]

print("1950s:", books_in_decade(books_col, 1950))
print("1960s:", books_in_decade(books_col, 1960))
print("pages like 'The Hunger Games':", books_with_similar_pages(books_col, "The Hunger Games"))
print("themes friendship + good vs evil:", books_matching_themes(books_col, ["friendship", "good vs evil"]))
```

**Expected / what you should see:** `1950s: [(1954, 'The Lord of the Rings')]`, `1960s: [(1960, 'To Kill a Mockingbird'), (1965, 'Dune')]` (the original script's 1950–1970 range mixes two decades). Pages like The Hunger Games (374, range 280–467): `[(328, '1984'), (376, 'To Kill a Mockingbird')]`. Themes: the exact list is `['Harry Potter and the Philosopher's Stone', 'The Lord of the Rings']` (both have *friendship* and *good vs evil*); the semantic top-3 should start with the same two books.

### ✅ Answer: C03-M2-L1 · C2 · your own filters

```python
r = col.query(query_texts=["machine learning and data analysis"], n_results=5,
              where={"$and": [{"experience": {"$lt": 8}}, {"employment_type": "Full-time"}]})
print("data/ML, < 8 years, full-time:")
for m, d in zip(r["metadatas"][0], r["distances"][0]):
    print(f"  {m['name']:<18} {m['role']:<28} {m['experience']}y  {m['employment_type']}  {d:.3f}")
hits = col.get(where_document={"$contains": "Python"})
print("documents containing 'Python':", [m["name"] for m in hits["metadatas"]])
```

**Expected / what you should see:** 5 rows, all `Full-time` with `< 8y` — e.g. Matthew Garcia, John Doe, Jessica Taylor, Hannah White, Alice Johnson. **Lesson:** the data has *no* junior data/ML person (the only ML skills belong to Alex Rodriguez, 18 years, removed by the filter), yet `query()` still returns `n_results` hits — the nearest of whatever is left, with large distances. Check the distances (or add a threshold) before trusting a filtered similarity search. The `$contains` line prints `['John Doe', 'Alex Rodriguez']` — the only documents with the exact, case-sensitive string `Python`.

### ✅ Answer: C03-M2-L1 · C3 · LLM staffing assistant (mini RAG)

```python
need = "We need two people to build a customer-facing web app with a machine learning recommendation feature."
r = col.query(query_texts=[need], n_results=5)
context = "\n".join(f"- {m['name']}: {d}" for m, d in zip(r["metadatas"][0], r["documents"][0]))
print("Retrieved candidates:\n" + context + "\n")
prompt = (f"Employee records:\n{context}\n\nTask: {need}\n"
          "Pick the best two people using only these records and explain why in 3 bullets. "
          "If the records do not support a choice, say so.")
print(llm.invoke(prompt).text)     # .text: Gemini 3 returns a list of content blocks; .text joins the text parts
```

**Expected / what you should see:** First the 5 retrieved records (web developers and ML/data people), then Gemini names exactly two of **those** people (expected: **Alex Rodriguez** — full-stack + machine learning — plus a web engineer such as **John Doe** or Matthew Garcia) with 3 bullets quoting their skills. If it names someone not in the list, the prompt is not grounded enough.

### ✅ Answer: C03-M2-L1 · C4.1 · skills: where_document vs metadata

```python
for e in EMPLOYEES:   # store skills as a list -> metadata arrays support $contains (exact element match)
    col.update(ids=[e["id"]], metadatas=[{"skills_list": [s.strip() for s in e["skills"].split(",")]}])
by_doc   = {m["name"] for m in col.get(where_document={"$contains": "Python"})["metadatas"]}
by_doc_l = {m["name"] for m in col.get(where_document={"$contains": "python"})["metadatas"]}
by_meta  = {m["name"] for m in col.get(where={"skills_list": {"$contains": "Python"}})["metadatas"]}
print("where_document 'Python':", sorted(by_doc))
print("where_document 'python':", sorted(by_doc_l), "  <- case-sensitive substring")
print("metadata skills_list ∋ 'Python':", sorted(by_meta))
print("$contains on a plain string field:", col.get(where={"name": {"$contains": "John"}})["ids"])
```

**Expected / what you should see:** Prints `['Alex Rodriguez', 'John Doe']` for `where_document 'Python'`, `[]` for `'python'` and `['Alex Rodriguez', 'John Doe']` for the metadata list. `where_document` is a **case-sensitive substring** test on the whole text (`'python'` finds nothing; `'Java'` would also match John Doe's *JavaScript*). The metadata list is an **exact element** test: robust against other words in the text, but only as clean as your list (`'Python'` ≠ `'python'` too). The last line prints `[]` — `$contains` on a plain string metadata field silently matches nothing (tested on Chroma 1.5.9). `update(metadatas=…)` merges the new key into the existing metadata.

### ✅ Answer: C03-M2-L1 · C4.2 · gemini-embedding-001 vs gemini-embedding-2

```python
ef_001 = GeminiEmbeddingFunction("models/gemini-embedding-001")
col_001 = client.get_or_create_collection("employees_nb_001",
                                          configuration={"hnsw": {"space": "cosine"}, "embedding_function": ef_001})
col_001.upsert(ids=[e["id"] for e in EMPLOYEES], documents=docs)
q = "team leader manager with experience"
for label, c in [("embedding-2  ", col), ("embedding-001", col_001)]:
    r = c.query(query_texts=[q], n_results=3)
    print(label, [(EMPLOYEES[int(i.split('_')[1]) - 1]["name"], round(d, 3)) for i, d in zip(r["ids"][0], r["distances"][0])])
```

**Expected / what you should see:** Two lines with 3 `(name, distance)` pairs. Both models should rank the managers/directors first (e.g. *David Lee – Engineering Manager*, *Sarah Clark – HR Manager*, *Rachel Brown – Marketing Director*); order and distances differ because the two embedding spaces are different. The 001 data lives in its own collection — never mix models in one collection.

### ✅ Answer: C03-M2-L1 · C4.3 · dystopian heroine, rating ≥ 4.0

```python
r = books_col.query(query_texts=["dystopian future with a strong heroine"], n_results=3,
                    where={"rating": {"$gte": 4.0}})
for m, d in zip(r["metadatas"][0], r["distances"][0]):
    print(f"{m['title']:<42} {m['genre']:<16} ★{m['rating']}  {d:.4f}")
# In books_advanced_search.py add the same call as a 5th block inside perform_advanced_search():
#     print("\n5. Dystopian future with a strong heroine (rating >= 4.0):")
#     print_query(collection.query(query_texts=["dystopian future with a strong heroine"],
#                                  n_results=3, where={"rating": {"$gte": 4.0}}))
```

**Expected / what you should see:** **The Hunger Games** first (teenage girl, dystopian future, ★4.2), then **1984**; the 3rd is a non-dystopian book because only the rating is filtered. Add `{"genre": "Dystopian"}` inside an `$and` if you want dystopian books only.

### ✅ Answer: C03-M2-L2 · Lab Exercise 1 · search history

```python
%%writefile interactive_search_2.py
from shared_functions import *

# Global variable to store loaded food items
food_items = []
search_history = []

def main():
    """Main function for interactive CLI food recommendation system"""
    try:
        print("🍽️  Interactive Food Recommendation System")
        print("=" * 50)
        print("Loading food database...")
        
        # Load food data from file
        global food_items
        global search_history
        food_items = load_food_data('./FoodDataSet.json')
        print(f"✅ Loaded {len(food_items)} food items successfully")
        
        # Create and populate search collection
        collection = create_similarity_search_collection(
            "interactive_food_search",
            {'description': 'A collection for interactive food search'}
        )
        populate_similarity_collection(collection, food_items)
        
        # Start interactive chatbot
        interactive_food_chatbot(collection)
        
    except Exception as error:
        print(f"❌ Error initializing system: {error}")

def interactive_food_chatbot(collection):
    """Interactive CLI chatbot for food recommendations"""
    print("\n" + "="*50)
    print("🤖 INTERACTIVE FOOD SEARCH CHATBOT")
    print("="*50)
    print("Commands:")
    print("  • Type any food name or description to search")
    print("  • 'help' - Show available commands")
    print("  • 'history' - Show your previous searches")
    print("  • 'quit' or 'exit' - Exit the system")
    print("  • Ctrl+C - Emergency exit")
    print("-" * 50)
    
    while True:
        try:
            # Get user input
            user_input = input("\n🔍 Search for food: ").strip()
            
            # Handle empty input
            if not user_input:
                print("   Please enter a search term or 'help' for commands")
                continue
            
            # Handle exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you for using the Food Recommendation System!")
                print("   Goodbye!")
                break
            
            # Handle help command
            elif user_input.lower() in ['help', 'h']:
                show_help_menu()
            
            elif user_input.lower() in ['history']:
                handle_history_command()
            
            # Handle food search
            else:
                handle_food_search(collection, user_input)
                
        except KeyboardInterrupt:
            print("\n\n👋 System interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error processing request: {e}")

def show_help_menu():
    """Display help information for users"""
    print("\n📖 HELP MENU")
    print("-" * 30)
    print("Search Examples:")
    print("  • 'chocolate dessert' - Find chocolate desserts")
    print("  • 'Italian food' - Find Italian cuisine")
    print("  • 'sweet treats' - Find sweet desserts")
    print("  • 'baked goods' - Find baked items")
    print("  • 'low calorie' - Find lower-calorie options")
    print("\nCommands:")
    print("  • 'help' - Show this help menu")
    print("  • 'history' - Show your search history")
    print("  • 'quit' - Exit the system")

def handle_food_search(collection, query):
    """Handle food similarity search with enhanced display"""
    search_history.append(query)
    print(f"\n🔍 Searching for '{query}'...")
    print("   Please wait...")
    
    # Perform similarity search
    results = perform_similarity_search(collection, query, 5)
    
    if not results:
        print("❌ No matching foods found.")
        print("💡 Try different keywords like:")
        print("   • Cuisine types: 'Italian', 'Thai', 'Mexican'")
        print("   • Ingredients: 'chicken', 'vegetables', 'cheese'")
        print("   • Descriptors: 'spicy', 'sweet', 'healthy'")
        return
    
    # Display results with rich formatting
    print(f"\n✅ Found {len(results)} recommendations:")
    print("=" * 60)
    
    for i, result in enumerate(results, 1):
        # Calculate percentage score
        percentage_score = result['similarity_score'] * 100
        
        print(f"\n{i}. 🍽️  {result['food_name']}")
        print(f"   📊 Match Score: {percentage_score:.1f}%")
        print(f"   🏷️  Cuisine: {result['cuisine_type']}")
        print(f"   🔥 Calories: {result['food_calories_per_serving']} per serving")
        print(f"   📝 Description: {result['food_description']}")
        
        # Add visual separator
        if i < len(results):
            print("   " + "-" * 50)
    
    print("=" * 60)
    
    # Provide suggestions for further exploration
    suggest_related_searches(results)

def suggest_related_searches(results):
    """Suggest related searches based on current results"""
    if not results:
        return
    
    # Extract cuisine types from results
    cuisines = list(set([r['cuisine_type'] for r in results]))
    
    print("\n💡 Related searches you might like:")
    for cuisine in cuisines[:3]:  # Limit to 3 suggestions
        print(f"   • Try '{cuisine} dishes' for more {cuisine} options")
    
    # Suggest calorie-based searches
    avg_calories = sum([r['food_calories_per_serving'] for r in results]) / len(results)
    if avg_calories > 350:
        print("   • Try 'low calorie' for lighter options")
    else:
        print("   • Try 'hearty meal' for more substantial dishes")

def handle_history_command():
    """Display user's search history"""
    if not search_history:
        print("📝 No search history available")
        return
    
    print("\n📝 Your Search History:")
    print("-" * 30)
    for i, search in enumerate(search_history[-10:], 1):  # Show last 10
        print(f"{i}. {search}")

if __name__ == "__main__":
    main()
```

**Expected / what you should see:** Run the demo `!printf 'pizza\ncurry\nhistory\nquit\n' | python interactive_search_2.py`: after the two result lists, `history` prints *📝 Your Search History:* `1. pizza` `2. curry`, then the goodbye message. The banner and `help` now list the `history` command; with no searches yet it prints *📝 No search history available*. Only the last 10 searches are shown. (The lab modifies `interactive_search.py`; a separate `_2` file keeps Step 1 unchanged — copy it over if you want the lab's exact file name.)

### ✅ Answer: C03-M2-L2 · Lab Exercise 2 · calorie checker

```python
%%writefile calorie_checker.py
# Create a file called calorie_checker.py
from shared_functions import *

def calorie_checker():
    """Interactive calorie budget checker for foods"""
    print("🔥 FOOD CALORIE BUDGET CHECKER")
    print("=" * 35)
    
    # Setup data
    food_items = load_food_data('FoodDataSet.json')
    collection = create_similarity_search_collection("calorie_checker")
    populate_similarity_collection(collection, food_items)
    print("✅ Food database loaded!")
    
    # Get user's calorie budget
    while True:
        try:
            budget = int(input("\n💪 What's your calorie budget per meal? "))
            if budget > 0:
                break
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"\n🎯 Your calorie budget: {budget} calories")
    print("Now search for foods to see if they fit your budget!")
    
    # Interactive search loop
    while True:
        print("\n" + "-" * 40)
        search_term = input("🔍 Search for a food (or 'quit' to exit): ").strip()
        
        if search_term.lower() == 'quit':
            print("👋 Thanks for using the Calorie Checker!")
            break
        
        if not search_term:
            print("Please enter a food to search for!")
            continue
        
        # Search for foods within budget
        budget_results = perform_filtered_similarity_search(
            collection, search_term, max_calories=budget, n_results=5
        )
        
        # Also get regular results to show what's over budget
        all_results = perform_similarity_search(collection, search_term, 5)
        
        print(f"\n📋 Results for '{search_term}':")
        
        if budget_results:
            print(f"✅ FITS YOUR BUDGET ({budget} cal limit):")
            for i, result in enumerate(budget_results, 1):
                calories = result['food_calories_per_serving']
                remaining = budget - calories
                print(f"  {i}. {result['food_name']}")
                print(f"     Calories: {calories} (🟢 {remaining} cal remaining)")
                print(f"     Cuisine: {result['cuisine_type']}")
        else:
            print(f"❌ No foods found within your {budget} calorie budget!")
        
        # Show over-budget options
        over_budget = []
        for result in all_results:
            if result['food_calories_per_serving'] > budget:
                over_budget.append(result)
        
        if over_budget:
            print(f"\n🚫 OVER BUDGET (but similar to your search):")
            for i, result in enumerate(over_budget[:3], 1):
                calories = result['food_calories_per_serving']
                excess = calories - budget
                print(f"  {i}. {result['food_name']}")
                print(f"     Calories: {calories} (🔴 {excess} cal over budget)")
        
        # Show budget summary
        if budget_results:
            avg_calories = sum(r['food_calories_per_serving'] for r in budget_results) / len(budget_results)
            print(f"\n📊 Budget-friendly options average: {avg_calories:.0f} calories")

if __name__ == "__main__":
    calorie_checker()
```

**Expected / what you should see:** With the demo input `500 / burger / salad / quit`: *🎯 Your calorie budget: 500 calories*, then for each search a **✅ FITS YOUR BUDGET** list (≤ 5 dishes ≤ 500 kcal with *🟢 N cal remaining*), an optional **🚫 OVER BUDGET** list (similar dishes > 500 kcal with *🔴 N cal over budget*, e.g. Chicken Biryani 600 kcal → 🔴 100 over). Note: the dataset (185 items) has **no burger**, so *burger* returns the nearest American/fast-food style dishes (e.g. BBQ Chicken Pizza 350 kcal) — that is semantic search working, not a bug; *salad* should list Caesar Salad (250 kcal) and the average calories of the fitting dishes. A non-number budget asks again (*Please enter a valid number!*).

### ✅ Answer: C03-M2-L2 · Lab Exercise 3 · result limiter

```python
%%writefile result_limiter.py
from shared_functions import *

def test_result_limits():
    """Test how different result limits affect search quality"""
    print("📊 SIMILARITY SEARCH RESULT LIMITER")
    print("=" * 45)
    
    # Setup
    food_items = load_food_data('FoodDataSet.json')
    collection = create_similarity_search_collection("result_test")
    populate_similarity_collection(collection, food_items)
    
    # Test query
    query = "spicy chicken"
    print(f"🔍 Testing query: '{query}'\n")
    
    # Test different result limits
    result_limits = [1, 3, 5, 10]
    
    for limit in result_limits:
        print(f"📋 Getting top {limit} result(s):")
        print("-" * 30)
        
        results = perform_similarity_search(collection, query, limit)
        
        if results:
            for i, result in enumerate(results, 1):
                score = result['similarity_score']
                print(f"  {i}. {result['food_name']}")
                print(f"     Score: {score:.3f}")
                print(f"     Cuisine: {result['cuisine_type']}")
                print(f"     Calories: {result['food_calories_per_serving']}")
                print()
            
            # Show quality analysis
            scores = [r['similarity_score'] for r in results]
            avg_score = sum(scores) / len(scores)
            print(f"  📈 Average score: {avg_score:.3f}")
            print(f"  🎯 Best score: {max(scores):.3f}")
            if len(scores) > 1:
                print(f"  📉 Worst score: {min(scores):.3f}")
        else:
            print("  No results found!")
        
        print("=" * 45)
    
    # Interactive test with user input
    print("\n🎮 INTERACTIVE MODE:")
    print("Test your own queries with different result limits!")
    
    while True:
        user_query = input("\nEnter search query (or press Enter to exit): ").strip()
        if not user_query:
            break
        
        try:
            limit_input = input("How many results? (1-20): ").strip()
            limit = int(limit_input) if limit_input.isdigit() and 1 <= int(limit_input) <= 20 else 5
        except:
            limit = 5
        
        print(f"\n🔍 Searching for '{user_query}' (limit: {limit})")
        results = perform_similarity_search(collection, user_query, limit)
        
        if results:
            print(f"Found {len(results)} results:")
            for i, result in enumerate(results, 1):
                print(f"  {i}. {result['food_name']} (Score: {result['similarity_score']:.3f})")
            
            # Show quality analysis
            scores = [r['similarity_score'] for r in results]
            avg_score = sum(scores) / len(scores)
            print()
            print(f"  📈 Average score: {avg_score:.3f}")
            print(f"  🎯 Best score: {max(scores):.3f}")
            if len(scores) > 1:
                print(f"  📉 Worst score: {min(scores):.3f}")
        else:
            print("No results found!")
    
    print("\n👋 Thanks for testing result limits!")

if __name__ == "__main__":
    test_result_limits()
```

**Expected / what you should see:** Four blocks for *spicy chicken* (top 1, 3, 5, 10). The top results are the same in every block (more results only appends items) — the dataset has only 5 chicken dishes (Chicken Tikka Masala 540, Chicken Biryani 600, Chicken Dum Biryani 600, BBQ Chicken Pizza 350, Salted Roasted Chicken 130), so expect those in the top 5 (Tikka Masala / the biryanis first with real Gemini embeddings). Best score stays the same, the average and worst score drop as `n_results` grows: beyond ~3–5 the extra hits are only loosely related (other chicken dishes or other spicy dishes). Then the interactive part: the demo searches *grilled fish* with 4 results and exits on an empty line. Similarity scores here are `1 − cosine distance` (higher = better).

### ✅ Answer: C03-M2-L2 · C2 · compare Gemini models

```python
import time
import enhanced_rag_chatbot as bot          # importing does not start the CLI (main() is behind __name__ guard)
question = "vegetarian high protein lunch"
hits = perform_similarity_search(col, question, n_results=3)
names = [h["food_name"] for h in hits]
print("retrieved:", names)
for name in ["gemini-3.8-flash", "gemini-3.5-flash-lite"]:
    bot.model = ChatGoogleGenerativeAI(model=name)   # default temperature (Google's recommendation for Gemini 3)
    t = time.time()
    try:
        ans = bot.generate_llm_rag_response(question, hits)
    except Exception as e:                            # e.g. 429 RESOURCE_EXHAUSTED on the free tier
        print(f"--- {name}: {type(e).__name__}: {str(e)[:150]}"); continue
    grounded = [n for n in names if n.lower() in ans.lower()]
    print(f"--- {name} ({time.time()-t:.1f}s) · mentions {len(grounded)}/{len(names)} retrieved dishes: {grounded}")
    print(ans[:600])
bot.model = llm                                   # restore the Cell 2 model
```

**Expected / what you should see:** `retrieved:` 3 vegetarian/protein dishes from the dataset, then one block per model with the time and *mentions k/3 retrieved dishes*. A well-grounded answer mentions the retrieved dishes (k = 2–3) and no others; Flash-Lite is usually faster but shorter. If a model prints `ChatGoogleGenerativeAIError … 429` you hit the free-tier limit — wait a minute and re-run. `bot.model` is reset to Cell 2's `llm` at the end.

### ✅ Answer: C03-M2-L2 · C3 · gemini-embedding-001 vs gemini-embedding-2

```python
import chromadb
from gemini_ef import GeminiEmbeddingFunction
gcol = chromadb.Client().get_or_create_collection(
    "food_gemini_001",                                  # own name: C1's `col` stays alive
    configuration={"hnsw": {"space": "cosine"},
                   "embedding_function": GeminiEmbeddingFunction("models/gemini-embedding-001")})
if gcol.count() == 0:                                   # re-run safe: embed the 185 items only once
    populate_similarity_collection(gcol, food_items)
for label, c in [("embedding-2  ", col), ("embedding-001", gcol)]:
    res = perform_similarity_search(c, "spicy chicken", n_results=5)
    print(label, [(r["food_name"], round(r["similarity_score"], 3)) for r in res])
```

**Expected / what you should see:** Two lines with 5 `(dish, score)` pairs each. Both models should put chicken dishes with chili/spice (the dataset's chicken dishes: Chicken Tikka Masala, Chicken Biryani, Chicken Dum Biryani, BBQ Chicken Pizza, Salted Roasted Chicken) on top; order and scores differ because the two embedding spaces differ — judge by which list looks more *spicy* **and** *chicken*. The 001 collection is built once (185 items, 2 batch calls) and is re-run safe.

### ✅ Answer: C03-M2-L2 · C4 · Gradio chat UI

```python
import gradio as gr
import enhanced_rag_chatbot as bot
def chat(msg, history):
    hits = perform_similarity_search(col, msg, n_results=3)
    return bot.generate_llm_rag_response(msg, hits)
try:
    demo.close()                     # re-run safe: stop the previous app (frees its port)
except NameError:
    pass
demo = gr.ChatInterface(chat, title="Food RAG bot")
demo.launch(share=True)              # no debug=True -> the cell finishes, the app keeps running
```

**Expected / what you should see:** `* Running on local URL: http://127.0.0.1:7860`, a public `https://….gradio.live` link and the chat UI inline; the cell finishes, so the next cells (and Run all) are not blocked. Asking *something spicy for dinner* returns a Gemini answer built from 3 retrieved dishes. Re-running the cell closes the old app first (no new port each time).