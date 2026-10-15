# C02 — Colab Notebook Review & Exercise Answers

<aside>
📍

**Status:** Session 20 (Oct 13, 2026) — ✅ ALL DONE (CP4b + CP5). All 4 corrected notebooks attached; nothing left to continue. Old note: CP4b-c was: wrapper (keeps original `asyncio.run` when `loop_factory` is passed, else nest_asyncio's) now written into `fix_m3_files.py` and the Ex 3 answer in `fix_m3_answers.py`; venv rebuilding. If interrupted, redo: put the `loop_factory`-safe `asyncio.run` wrapper into `LLM_INTERFACE` in `fix_m3_files.py` (+ Ex 3 answer), rerun `fix_m3.py` and `run_nb.py … run_fixed` (work_M3.zip below).

</aside>

[work_M3.zip](work_M3.zip)

[work_M3.zip](work_M3%201.zip)

work_M3.zip (newest, session 20: final fix_m3*.py + harness; the file above is session 19)

Work scripts (work_[M3.zip](http://M3.zip)): Colab stub, fake Gemini (google.genai Models layer), non-blocking launch + gradio_client hook, nbclient runner.

Review of the Module 2 (Course 02 · Build RAG Applications) Colab conversions against the IBM originals and the Gemini conversion plan, with real sandbox execution and reference answers.

## Checkpoint log

| CP | Scope | Status |
| --- | --- | --- |
| CP0 | Setup: unpack, venvs, Colab stub, fake Gemini, model-ID check | ✅ done (rebuilt again in session 4, same resolved versions; `langchain-core 1.6.10`) |
| CP1 | M1-L1 Summarize Private Documents (RAG) | ✅ done — 0 errors |
| CP2 | M2-L1 Simple Gradio Interface | ✅ done — 0 errors after fixes (session 4 re-run: original 14 code cells / 0 errors · corrected 22 code cells incl. 6 answers / 0 errors, 12 Gradio apps served + called) |
| CP0c–CP0m · CP4a–CP4h | Sessions 8–16 (token run-outs): page recreated, venv + harness rebuilt each time from the exact Cell 1 lines → identical versions (`langchain-core 1.6.10`, `langchain-google-genai 4.4.1`, `google-genai 2.29.0`, `gradio 6.30.0`, `chromadb 1.5.9`, `pydantic 2.14.1`, `llama-index-core 0.14.25`, `llama-index-llms-google-genai 0.11.2`, `llama-index-embeddings-google-genai 0.6.0`, `nest-asyncio 1.6.0`). M3-L1 original run reproduced every time: **22 code cells / 5 errors** (cells 25, 35, 37, 39, 41: `asyncio.run() cannot be called from a running event loop` → `'str' object has no attribute 'response'`), C1 prints *Failed to generate initial facts*, every call sends `temperature=0.0`, CLI `printf` first question eaten by URL prompt, `app.py` GET / = 200 | ✅ done |
| CP3 | M2-L2 QA Bot (LangChain + Gradio) | ✅ done — original 17 cells / 0 errors · corrected 22 cells incl. 5 answers / 0 errors |
| CP0b | Session 8 rebuild: venvs `venv_m3` / `venv_m21` from the exact Cell 1 lines → `langchain-core 1.6.10`, `langchain-google-genai 4.4.1`, `google-genai 2.29.0`, `gradio 6.30.0`, `chromadb 1.5.9`, `pydantic 2.14.1`, `numpy 2.5.4`, `llama-index-core 0.14.25`, `llama-index-llms-google-genai 0.11.2`, `llama-index-embeddings-google-genai 0.6.0`; Colab stub + HTTP-level fake Gemini + non-blocking Gradio launch rebuilt and smoke-tested (list-of-blocks content, streaming, MAX_TOKENS from thinking, 404 for unknown IDs, LlamaIndex GoogleGenAI/GoogleGenAIEmbedding) | ✅ done |
| CP4b-1 | M1-L1 corrected file rebuilt (session 10): Cell 2 `temperature=0.2` removed (Gemini 3), 💡 note + 8 hidden answer cells (Ex 1–3, C1–C5), IBM credits restored. Run (run_answer=True): **47 code cells / 0 errors**, 21 s; `qa()` loop driven by scripted input | ✅ done, attached |
| CP4b-2 | M2-L1 corrected file rebuilt (session 10): Cell 2 + `simple_llm.py`  • `llm_chat.py` temperature removed, `thinking_level="low"`; `llm_chat.py` model order restored (3.8-flash = Granite active); lab Exercises 1–2 added (task + `# Your code here`  • hint + answer); C1–C4 answers. Run: **22 code cells / 0 errors**, 26 s, 12 Gradio apps served (GET / = 200) | ✅ done, attached |
| CP4b-3 | M2-L2 corrected file rebuilt (session 10): Cell 2 temperature removed; `qabot.py`: `thinking_level="low"`, no temperature, `chunk_overlap=50`, unique Chroma `collection_name`, `return_source_documents=False`, labels "Output" / "RAG Chatbot" (as lab), comments name the lab models; 💡 note + C1–C5 answers. Run: **22 code cells / 0 errors**, 29 s; 4 Gradio apps GET / = 200; C4 cache: 0.65 s → 0.02 s | ✅ done, attached |
| CP0n | Session 17: page recreated from the uploaded [checkpoint.zip](http://checkpoint.zip); 3 corrected notebooks re-attached | ✅ done |
| CP4i | Session 17: venv from the exact M3-L1 Cell 1 line → identical versions (+ `gradio_client 2.7.2`, `requests 2.34.2`). Original re-run: **22 code cells / 5 errors** (cells 25, 35, 37, 39, 41). Log: all 5 LLM calls sent `temperature=0.0` (4× 3.8-flash, 1× 3.5-flash-lite), no thinking setting. CLI: 1st piped question eaten by the URL prompt (cell 27 answers only Q2; cell 28 answers nothing). `app.py`: GET / = 200, `/process_profile`  • `/chat_with_profile` answer | ✅ done |
| CP0o | Session 18: page recreated again from the uploaded [checkpoint.zip](http://checkpoint.zip); 3 corrected notebooks + work_[M3.zip](http://M3.zip) re-attached | ✅ done |
| CP0p | Session 19: page recreated from checkpoint.zip; files re-attached | ✅ done |
| CP0q | Session 20: page recreated from checkpoint.zip; files re-attached | ✅ done |
| CP4b | M3-L1 corrected notebook (session 20): Cell 2 temperature removed; `llm_interface.py`: no temperature on `gemini-3*`, `thinking_level="low"`, `max_output_tokens` in `GenerateContentConfig`, nest_asyncio with a `loop_factory`-safe `asyncio.run` wrapper; `query_engine.py` error path returns a `Response`; `main.py --mock` skips the URL prompt; `test_config.py` added; 5 lab exercises (task + `# Your code here`  • answer) + C1–C5 answers + 💡 note (77 cells). Run (run_answer=True): **39 code cells / 0 errors**, 41 s; 3 Gradio apps served + `/process_profile` & `/chat_with_profile` called; 174 fake-API calls, no temperature sent to Gemini 3, all `STOP`. Extra bug found+fixed in the run: Ex 4 answer imported `modules.llm_interface` → `modules/__init__.py` imports `query_engine` (not written yet) → ModuleNotFoundError; answer now loads the file directly | ✅ done, attached |
| CP5 | Final: 4 corrected .ipynb files attached, verdicts + tips updated | ✅ done |

## CP0 · Test setup

- **Materials:** 4 Colab notebooks (M1-L1, M2-L1, M2-L2, M3-L1); IBM originals: 2 versions of the M1 notebook (root = older Llama-3.3/Mixtral version, `week1/` = newer Granite-3.3/Mistral-Small version), lab PDFs + scripts for Gradio, QA bot and Icebreaker.
- **One venv per notebook**, installed with that notebook's exact Cell 1 `pip install -q -U …` line (Python 3.13). Resolved versions (Oct 12, 2026): `langchain-core 1.6.9`, `langchain-google-genai 4.4.1`, `google-genai 2.29.0`, `langchain-classic 1.0.8`, `langchain-community 0.4.2`, `langchain-text-splitters 1.1.3`, `langchain-chroma 1.1.0`, `chromadb 1.5.9`, `gradio 6.30.0`, `pypdf 6.20.0`, `pydantic 2.14.1`, `numpy 2.5.4`, `llama-index-core 0.14.25`, `llama-index-llms-google-genai 0.11.2`, `llama-index-embeddings-google-genai 0.6.0`, `wget 3.2`.
- **google.colab stub** (`userdata.get`, `output`), loaded through `PYTHONPATH`, so `!python script.py` subprocesses get it too (venv `bin/` is first on `PATH`).
- **Offline fake Gemini at the HTTP layer** (`google-genai` `BaseApiClient.request*`), so the real `ChatGoogleGenerativeAI` / `GoogleGenerativeAIEmbeddings` / LlamaIndex `GoogleGenAI` code runs unchanged. It returns Gemini-3-style list-of-blocks content with thought signatures, streaming chunks, function calls for `bind_tools`, JSON for `with_structured_output` / format instructions, ReAct text, `countTokens`, 404 for unknown or shut-down model IDs, 400 for invalid tool names / unsupported thinking levels, and **simulates thinking tokens counting toward `max_output_tokens`** (returns `MAX_TOKENS` + truncated or empty text, as documented). It logs every call (model, temperature, finish reason).
- **Runner:** nbclient, top to bottom, every code cell. Only `input()` (scripted queue) and blocking Gradio `.launch()` are replaced. Launch is patched to start on 127.0.0.1, `GET /`, call the endpoint with `gradio_client`, then close.

### Model IDs vs Google's current docs ([ai.google.dev](https://ai.google.dev/gemini-api/docs/models), last updated Oct 9, 2026)

| Model ID used | Exists? | Note |
| --- | --- | --- |
| `gemini-3.8-flash` | ✅ stable | Default thinking = medium; supports low/medium/high (**not** minimal) |
| `gemini-3.5-flash-lite` | ✅ stable | Default thinking = minimal |
| `gemini-2.5-flash-lite` | ⚠️ exists | Google now limits 2.5 models to accounts that used them before; a new key may be refused → fallback `gemini-3.1-flash-lite` |
| `gemini-2.5-flash` | ⚠️ exists | Same 2.5 access limit |
| `gemini-3.1-flash-lite` | ✅ stable | Good fallback "small" model |
| `models/gemini-embedding-2` | ✅ stable | 3072 dims; docs say `task_type` is not supported (use task prefixes) |
| `models/gemini-embedding-001` | ✅ | Text-only, supports `task_type` |

Google's docs also say that on Gemini 3.x, `temperature` should stay at the default 1.0, because lower values can cause looping or worse output. They also say `max_output_tokens` includes thinking tokens.

## CP1 · M1-L1 Summarize Private Documents (RAG)

**Base version:** the conversion follows the **older** IBM notebook (root file: flan-ul2 → Llama-3.3-70B, Exercise 3 = Mixtral). The newer `week1/` version uses `ibm/granite-3-3-8b-instruct` for both models, says *"you can try with any other model"* in step 53, and uses `mistralai/mistral-small-3-1-24b-instruct-2503` in Exercise 3. Both map to the same Gemini cells, so nothing is functionally missing.

| Original (watsonx) | Converted (Gemini) | Correct? |
| --- | --- | --- |
| `%%capture`  • 7 pinned `pip install --user`  • restart kernel | Cell 1: one `!pip install -q -U …` line, no restart | ✅ |
| `from langchain.document_loaders/text_splitter/vectorstores/embeddings/chains/prompts/memory …` | `langchain_community`, `langchain_text_splitters`, `langchain_chroma`, `langchain_core.prompts`, `langchain_classic.chains/memory` | ✅ |
| `HuggingFaceEmbeddings()`  • `Chroma.from_documents(texts, embeddings)` | `embeddings` (gemini-embedding-2) + `collection_name="company_policies"`  • fixed ids | ✅ (fix: no shared default collection) |
| `model_id='google/flan-ul2'`, GenParams greedy / MIN 130 / MAX 256 / temp 0.5 | `gemini-2.5-flash-lite`, `max_output_tokens=256`, `temperature=0.5` | ✅ (2.5 model → see access note) |
| `credentials` / `project_id` / "API disclaimer" | `None`  • Colab note | ✅ |
| `flan_ul2_llm = WatsonxLLM(model=model)` | `flan_ul2_llm = model` (name kept) | ✅ |
| `meta-llama/llama-3-3-70b-instruct`, MAX 256 | `gemini-3.8-flash`, `max_output_tokens=1024`, `thinking_level="low"`, no temperature; `llama_3_llm` name kept | ✅ |
| RetrievalQA (4×), PromptTemplate + `chain_type_kwargs` | unchanged, `.invoke` | ✅ |
| `ConversationBufferMemory(..., return_message=True)` (IBM typo) | `return_messages=True` | ✅ (IBM bug fixed) |
| `qa({"question": q}, {"chat_history": history})` (deprecated `__call__`, 2nd arg ignored) | `qa.invoke({"question": q})`, memory supplies history | ✅ |
| `qa()` agent with `input()` loop | unchanged | ✅ |
| Exercises 1–3 + `<details>` solution/hints | kept; hint 3 shows `# Colab: 'gemini-3.5-flash-lite'` | ✅ |
| Authors / Contributors / Change log / © cells | **missing** in converted | ⚠️ → restored in corrected file |

**Plan check:** Cell 1 ✅ · Cell 2 Secrets + `ChatGoogleGenerativeAI("gemini-3.8-flash")` + `GoogleGenerativeAIEmbeddings("models/gemini-embedding-2")` ✅ · `.text` in `llm_model` alias ✅ · LangChain 1.x imports ✅ · no `get_relevant_documents` / `.run` / `.predict` / `langchain.prompts` ✅ (grep: 0 hits).

**Execution (real run, fake Gemini, run_answer=True):** 47 code cells incl. 8 answer cells + `qa()` loop with scripted input → **0 errors**, 19 s. `CharacterTextSplitter` → 16 chunks (matches lab text). Log: 110 calls to `gemini-3.8-flash` (temperature unset ✅), `flan_ul2_llm` calls at 0.5, no `MAX_TOKENS` truncation with `thinking_level="low"`.

**Bug proven (already fixed in the notebook):** two `Chroma.from_documents(...)` calls without `collection_name` share the in-memory `langchain` collection → second store had **2 docs** instead of 1. The notebook uses its own collection names everywhere.

**IBM quirk (kept, not a Colab bug):** `get_chat_history=lambda h: h` with `return_messages=True` puts the raw message objects' repr into the *condense question* prompt. It works with a real LLM, but the standalone question can look noisy; Colab practice C3 shows the clean LCEL version.

**Corrected file:** only change = Authors/Contributors/Change log/© markdown restored at the end.

## CP2 · M2-L1 Simple Gradio Interface

**Base version:** lab PDF + `week2/gradio-interfaces/*.py` (Granite 3.3 active, `mistral-small-3-1-24b` commented, labelled "Mixtral 8x7B" in the lab's own comment).

| Original (watsonx) | Converted (Gemini) | Correct? |
| --- | --- | --- |
| `pip install gradio ibm-watsonx-ai langchain langchain-ibm` (venv) | Cell 1 one-line install | ✅ |
| `gradio_demo.py` `launch(server_name="127.0.0.1", server_port=7860)` | `launch(share=True, debug=True)` via `!python` | ✅ |
| **Exercise: combine two sentences** (`gradio_concatenation.py`) | only as practice C1, no lab task cell | ⚠️ missing → added Exercise 1 cells |
| `common_input_types.py` | unchanged + share link | ✅ |
| `simple_llm.py`: `WatsonxLLM(model_id='ibm/granite-3-3-8b-instruct', MAX_NEW_TOKENS 256, TEMPERATURE 0.5)` | `ChatGoogleGenerativeAI('gemini-3.8-flash', max_output_tokens=1024, temperature=0.5)`, `watsonx_llm` name kept, `.text` | ⚠️ temperature 0.5 on Gemini 3 → removed, `thinking_level="low"` |
| `llm_chat.py`: Granite **active**, Mistral-Small commented | `gemini-3.5-flash-lite` **active**, 3.8-flash commented; comment says *mixtral-8x7b-instruct-v01* (older lab) | ⚠️ swapped + old model name → fixed to match the lab |
| `allow_flagging="never"` | `flagging_mode="never"` | ✅ (Gradio 5/6 API) |
| **Exercise: incomplete answers / more tokens** | **missing** | ❌ → added Exercise 2 task + `<details>`  • answer |
| Cell 2 | `ChatGoogleGenerativeAI("gemini-3.8-flash", temperature=0.2)` | ⚠️ → default temperature |

**Plan check:** Cell 1 ✅ · Cell 2 Secrets ✅ (temperature fixed) · `.text` ✅ · imports ✅ · no deprecated APIs ✅ · **no answer cells / 💡 note existed** → added (2 lab exercises + C1–C4).

**Execution:** venv with the exact Cell 1 line (`gradio 6.30.0`). Every `launch()` (in `!python` scripts too, via `sitecustomize`) started on 127.0.0.1, `GET /` = 200, endpoint called with `gradio_client`, then closed. Original notebook: **0 errors**. Corrected notebook (run_answer=True): **0 errors**, 28 s. The only predict failure seen was the test harness's own sample input for the Radio in `common_input_types.py`, not a notebook bug.

**Findings (proven):**

- `langchain-google-genai 4.4.1` has `_FIXED_SAMPLING_AND_NO_PREFILL_MODELS = {"gemini-3.5-flash-lite", "gemini-3.6-flash"}`: it **drops `temperature`** and warns *"uses fixed sampling defaults; temperature will be ignored"* (seen in the run for `llm_chat.py`). So the temperature slider in C3 does nothing for flash-lite.
- `max_output_tokens=256` on `gemini-3.8-flash` (default thinking = medium): the fake, which follows Google's rule that thinking counts toward the limit, returned `finish_reason=MAX_TOKENS` with **0 answer chars**. `thinking_level="low"` + a bigger budget gives `STOP`. This is the Gemini answer to lab Exercise 2.

## CP3 · M2-L2 QA Bot (LangChain + Gradio)

**Base version:** lab PDF `Construct-a-QA-Bot.pdf` (newer: `mistralai/mistral-medium-2505`, `ibm/slate-125m-english-rtrvr-v2`) and `qa-bot/qabot.py` (Mistral-Small-3.1 active). The **uploaded `_Colab.ipynb` follows a different/older version**: `chunk_overlap=200` (lab: 50), `return_source_documents=True` (lab: False), `MAX_NEW_TOKENS 400`, `all-minilm-l6-v2` embeddings, output label "Answer" and title "RAG QA Bot with LangChain" (lab: "Output", "RAG Chatbot"). The lab has **no exercises**, so only the 🧪 Colab practice C1–C5 need answers.

| Original (watsonx) | Converted (Gemini) | Correct? |
| --- | --- | --- |
| `pip install` from `requirements.txt` in a venv | Cell 1 one-line `!pip install -q -U …` | ✅ |
| Cell 2 | `ChatGoogleGenerativeAI("gemini-3.8-flash", temperature=0.2)` | ⚠️ temperature on Gemini 3 → removed |
| `ModelInference` / `GenParams` / `Credentials` / `langchain_ibm` imports | `langchain_google_genai` | ✅ |
| `langchain.text_splitter`, `langchain_community.vectorstores.Chroma`, `langchain.chains.RetrievalQA` | `langchain_text_splitters`, `langchain_chroma`, `langchain_classic.chains` | ✅ |
| `from huggingface_hub import HfFolder` (unused) | commented out | ✅ (`HfFolder` removed in huggingface_hub 1.x) |
| `get_llm()`: `mistral-medium-2505` / `mistral-small-3-1`, temp 0.5, MAX 256 | `gemini-3.8-flash`, `max_output_tokens=1024`, `temperature=0.2` | ⚠️ → `thinking_level="low"`, no temperature; comment names the lab model |
| `PyPDFLoader(file.name)` | `file if isinstance(file, str) else file.name` | ✅ fix (`type="filepath"` gives a str) |
| `chunk_overlap=50` | `200` | ⚠️ older version → 50 |
| `watsonx_embedding()` slate-125m-v2 | `GoogleGenerativeAIEmbeddings("models/gemini-embedding-2")`, name kept | ✅ (comment fixed) |
| `Chroma.from_documents(chunks, embedding_model)` | same | ❌ shared collection bug → unique `collection_name` |
| `return_source_documents=False` | `True` | ⚠️ → False (as lab) |
| `allow_flagging="never"` | `flagging_mode="never"` | ✅ |
| Output "Output", title "RAG Chatbot" | "Answer", "RAG QA Bot with LangChain" | ⚠️ renamed → restored |
| `launch(server_name="0.0.0.0", server_port=7860)` at module level | `if __name__ == "__main__": launch(share=True, debug=True)` | ✅ (lets the notebook `import qabot`) |
| Screenshot tasks 1–6 | test cells per function | ✅ |
| — | **no 💡 note / answer cells** for C1–C5 | ❌ → added |

**Plan check:** Cell 1 ✅ · Cell 2 Secrets ✅ (temperature removed) · `.text` alias ✅ · LangChain 1.x imports ✅ · no `get_relevant_documents`/`.run`/`.predict`/`langchain.prompts` ✅ (`.invoke` everywhere).

**Execution (session 5, venv with the exact Cell 1 line: langchain-core 1.6.10, langchain-google-genai 4.4.1, google-genai 2.29.0, langchain-classic 1.0.8, langchain-community 0.4.2, langchain-chroma 1.1.0, chromadb 1.5.9, gradio 6.30.0, pypdf 6.20.0):** original = 17 code cells / **0 errors**; corrected (run_answer=True) = 22 code cells incl. 5 answers / **0 errors**. `arxiv.org/pdf/2005.11401` → 19 pages, 92 chunks; `1706.03762` downloads fine. `!python qabot.py` and every in-notebook app served `GET /` = 200 (5 apps).

**Bug proven:** two `Chroma.from_documents(...)` calls without `collection_name` → 2nd store count = **2** and `similarity_search` returns the same chunk twice. In the original run the C1 cell printed the *same* chunk ("2 Methods …") 3× because `vdb`, `ret` and the app all appended to one collection. Fixed in `qabot.py` with `collection_name=f"qabot_{uuid…}"`.

**Gemini note:** `max_output_tokens` includes thinking tokens; `gemini-3.8-flash` defaults to medium thinking, so `thinking_level="low"` keeps the 1024 budget for the answer. `langchain-community` prints a *being sunset* DeprecationWarning on import (harmless).

## CP4 · M3-L1 Icebreaker Bot (Granite → Gemini, LlamaIndex)

**Base version:** lab PDF *Build an AI Icebreaker Bot with IBM Granite 3.0 & LlamaIndex* + `week3/icebreaker/*.py` (Granite-3.2-8B + Llama-3.3-70B, slate-125m-v2, port 5000). Converted scripts diffed line by line against the repo files: `data_extraction.py`, `data_processing.py`, `query_engine.py` identical; only `config.py`, `llm_interface.py`, `main.py`, `app.py`, `modules/__init__.py` differ (table).

| Original (watsonx) | Converted (Gemini) | Correct? |
| --- | --- | --- |
| `requirements.txt` (llama-index 0.11.8, `llama-index-llms-ibm`, gradio 4.19) in a venv | Cell 1 one-line `!pip install -q -U … llama-index-core llama-index-llms-google-genai llama-index-embeddings-google-genai gradio` | ✅ |
| — | Cell 2 `ChatGoogleGenerativeAI("gemini-3.8-flash", temperature=0.2)` (not used by the project) | ⚠️ temperature on Gemini 3 → removed |
| `config.py`: `WATSONX_URL`, `WATSONX_PROJECT_ID`, `ibm/granite-3-2-8b-instruct`, `ibm/slate-125m-english-rtrvr-v2` | removed / `gemini-3.8-flash`, `gemini-embedding-2` | ✅ |
| `config.py` `TEMPERATURE = 0.0` | kept and **sent to Gemini 3** | ⚠️ → `llm_interface` omits temperature for `gemini-3*` |
| `test_config.py`  • `python test_config.py` (lab "Testing Your Configuration") | **missing** | ⚠️ → added |
| Lab Step 5 optional `CHUNK_SIZE = 400`, `SIMILARITY_TOP_K = 7` | not mentioned (C3 sweeps similar values) | ✅ (note added) |
| 5 lab **Exercises** ("create the pseudocode" before data_extraction, data_processing, llm_interface, query_engine, [main.py](http://main.py)) | **missing** | ❌ → added task + `# Your code here`  • answer cells |
| `WatsonxEmbeddings(model_id, url, project_id, truncate_input_tokens=3)` | `GoogleGenAIEmbedding(model_name=…)`; name `create_watsonx_embedding` kept | ✅ |
| `WatsonxLLM(… decoding_method, min/max_new_tokens, top_k, top_p)` | `GoogleGenAI(model, temperature, max_tokens=max(n,1024))`; name `create_watsonx_llm` kept | ⚠️ temperature 0.0 on Gemini 3; no thinking control → `generation_config` with `thinking_level="low"`, no temperature on Gemini 3 |
| `main.py` without `import config` (IBM bug: `config.PROXYCURL_API_KEY` NameError) | `import config` added | ✅ IBM bug fixed |
| CLI: `python main.py --mock` (interactive) | `!printf "q1\nq2\nbye\n" | python [main.py](http://main.py) --mock` |
| `app.py` model dropdown Granite / Llama-3.3 | `gemini-3.8-flash` · `gemini-3.5-flash-lite` · `gemini-2.5-flash` | ✅ (2.5 access note) |
| `chat_history + [[q, a]]` (Gradio 4 tuples) | messages-format `_turn()` | ✅ (Gradio 6) |
| `launch(server_name="127.0.0.1", server_port=5000, share=True)` | `launch(share=True, debug=True)` | ✅ |
| ProxyCurl API | mock JSON (URL still serves: HTTP 200, 24 961 bytes on Oct 12, 2026) | ✅ |

**Plan check:** Cell 1 ✅ · Cell 2 Secrets + model IDs ✅ (temperature removed) · `.text` alias ✅ · LlamaIndex lab, so LangChain imports only in Cell 2 ✅ · no deprecated APIs ✅.

**Proven in installed versions (`llama-index-llms-google-genai 0.11.2`):** `GoogleGenAI.__init__` only drops temperature when `temperature is None` and `"gemini-3"` is in the model name ("Gemini 3-series models may error if temperature is set"); the notebook passes `0.0`, so it is sent. With `generation_config=…`, the `temperature` / `max_tokens` arguments are ignored, so the fix puts `max_output_tokens` inside `GenerateContentConfig`. Google's thinking docs: `thinking_level` "low" is supported by `gemini-3.8-flash`, `gemini-3.5-flash-lite` and `gemini-2.5-flash`.

## Notebook verdicts

<aside>
✅

**M1-L1 — ✅ works.** 0 errors top to bottom (incl. answers). Only change: restored IBM credits cells.

</aside>

<aside>
⚠️

**M2-L1 — ⚠️ works with fixes.** Ran without errors, but 2 lab exercises were missing, the model order in `llm_chat.py` was swapped, and temperature was set on Gemini 3. All fixed; answer cells added.

</aside>

<aside>
⚠️

**M2-L2 — ⚠️ works with fixes.** Ran without errors, but it followed an older lab version (overlap 200, sources on, renamed labels), set temperature on Gemini 3, and shared one Chroma collection (duplicate chunks). All fixed; answer cells C1–C5 added.

</aside>

<aside>
⚠️

**M3-L1 — ⚠️ works with fixes.** Original: 22 code cells / **5 errors** (LlamaIndex `asyncio.run` inside Colab's loop → `'str' object has no attribute 'response'`), temperature 0.0 sent to Gemini 3, `--mock` ate the first piped question, 5 lab exercises + `test_config.py` missing. All fixed; corrected run 0 errors.

</aside>

## Things to know when running it

- **M3-L1:** keep the `asyncio.run` wrapper in `llm_interface.py`: plain `nest_asyncio.apply()` breaks every in-notebook `demo.launch()` (uvicorn passes `loop_factory`).
- **M3-L1:** `!python app.py` blocks the cell; press ⏹ before the next cell. The `gemini-2.5-flash` dropdown option may be refused for new keys.
- **M3-L1:** after editing a `%%writefile` module, restart the runtime or `importlib.reload` it — Python caches `modules.*`.
- **M1:** `gemini-2.5-flash-lite` (the "weak" flan-ul2 stand-in) may be refused for brand-new API keys (2.5 access limit). If you get 404/403, set `model_id = 'gemini-3.1-flash-lite'`.
- **M1:** the `qa()` cell loops on `input()`; type `bye` to stop, otherwise later cells wait.
- **M1:** practice C2 (`map_reduce` = 7 calls, `refine` = 6) and C5 can hit the free-tier **429** limit; wait a minute and rerun.
- **M2-L1:** `!python gradio_demo.py` / `common_input_types.py` / `llm_chat.py` **block the cell** (`debug=True`). Open the `*.gradio.live` link, then press ⏹ before running the next cell.
- **M2-L1:** in-notebook practice apps keep running; call `demo.close()` (or `gr.close_all()`) if you rerun many of them, otherwise ports 7860, 7861… pile up.
- **M2-L1:** `gemini-3.5-flash-lite` ignores `temperature` (fixed sampling); don't expect the slider to change anything for it.
- **M2-L2:** `!python qabot.py` blocks the cell (`debug=True`); open the `*.gradio.live` link, press ⏹ before the next cell. After editing `qabot.py`, rerun the `%%writefile` cell **and** the `importlib.reload(qabot)` cell.
- **M2-L2:** each question re-embeds the whole PDF (≈ 92 embedding calls for the sample) — on the free tier use practice C4 (cache) if you get **429**.

## Corrected notebooks

- M1-L1 (rebuilt in session 10 — CP4b-1):

[C02-M1-L1_Summarize_Private_Documents_RAG_Colab.ipynb](C02-M1-L1_Summarize_Private_Documents_RAG_Colab.ipynb)

C02-M1-L1_Summarize_Private_Documents_RAG_Colab.ipynb

- M2-L1 (rebuilt in session 10 — CP4b-2):

[C02-M2-L1_Simple_Gradio_Interface_Colab.ipynb](C02-M2-L1_Simple_Gradio_Interface_Colab.ipynb)

C02-M2-L1_Simple_Gradio_Interface_Colab.ipynb

- M2-L2 (rebuilt in session 10 — CP4b-3):

[C02-M2-L2_QA_Bot_LangChain_Gradio_Colab.ipynb](C02-M2-L2_QA_Bot_LangChain_Gradio_Colab.ipynb)

C02-M2-L2_QA_Bot_LangChain_Gradio_Colab.ipynb

- M3-L1 (session 20 — CP4b):

[C02-M3-L1_Icebreaker_Bot_Granite_LlamaIndex_Colab.ipynb](C02-M3-L1_Icebreaker_Bot_Granite_LlamaIndex_Colab.ipynb)

## Exercise answers (try first, then open)

### M1-L1

#### ✅ Answer: M1-L1 · Exercise 1: Work on your own document

```python
filename = 'stateOfUnion.txt'
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/XVnuuEg94sAE4S_xAsGxBA.txt'
wget.download(url, out=filename)
print('file downloaded')

# Same pipeline as the lab: load → split → embed/store → RetrievalQA
sotu_docs = TextLoader(filename).load()
sotu_texts = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0).split_documents(sotu_docs)
print(len(sotu_texts), "chunks")
# Own collection: without collection_name it would share Chroma's default "langchain" collection
sotu_search = Chroma.from_documents(sotu_texts, embeddings, collection_name="state_of_union",
                                    ids=[f"sotu-{i}" for i in range(len(sotu_texts))])
qa_sotu = RetrievalQA.from_chain_type(llm=llama_3_llm, chain_type="stuff",
                                      retriever=sotu_search.as_retriever(),
                                      chain_type_kwargs=chain_type_kwargs,   # the "say you don't know" prompt
                                      return_source_documents=False)
for q in ["Can you summarize the document for me?",
          "What does the speech say about Russia and Ukraine?",
          "What is the company's mobile phone policy?"]:      # not in this document → "don't know"
    print("\nQ:", q, "\nA:", qa_sotu.invoke(q)["result"])
```

**Expected / what you should see:** `file downloaded`, `42 chunks`, a summary of the 2022 State of the Union (infrastructure, inflation, Ukraine…), a Russia/Ukraine answer, and **"I don't know"** for the mobile-phone question (it is not in this document).

#### ✅ Answer: M1-L1 · Exercise 2: Return the source from the document

```python
qa = RetrievalQA.from_chain_type(llm=llama_3_llm, chain_type="stuff",
                                 retriever=docsearch.as_retriever(),
                                 return_source_documents=True)      # ← the only change
query = "Can I smoke in company vehicles?"
results = qa.invoke(query)
print("Answer:", results["result"])
print("-" * 50)
print(results["source_documents"][0])                 # the exact source chunk
for i, d in enumerate(results["source_documents"]):   # all retrieved chunks
    print(f"[{i}] {d.metadata.get('source')}: {d.page_content[:80]!r}")
```

**Expected / what you should see:** `Answer:` saying smoking is not allowed in company vehicles, then the source `Document` (metadata `source='companyPolicies.txt'`) whose text contains *5. Smoking Policy*.

#### ✅ Answer: M1-L1 · Exercise 3: Use another LLM model

```python
# mistralai/mixtral-8x7b-instruct-v01 → gemini-3.5-flash-lite (Gemini 3: default temperature, minimal thinking by default)
model_id = 'gemini-3.5-flash-lite'
parameters = {"max_output_tokens": 1024}
mistral_llm = ChatGoogleGenerativeAI(model=model_id, **parameters)

query = "Can I smoke in company vehicles?"
for name, model in [("gemini-3.8-flash (llama_3_llm)", llama_3_llm), ("gemini-3.5-flash-lite (mistral_llm)", mistral_llm)]:
    qa = RetrievalQA.from_chain_type(llm=model, chain_type="stuff",
                                     retriever=docsearch.as_retriever(), return_source_documents=True)
    results = qa.invoke(query)
    print(f"\n== {name}\n{results['result']}")
    print("source:", results["source_documents"][0].page_content[:100].replace("\n", " "))
```

**Expected / what you should see:** Two answers to the same question. `gemini-3.5-flash-lite` is faster and shorter; `gemini-3.8-flash` gives more detail. Both should say smoking in company vehicles is not allowed.

#### ✅ Answer: M1-L1 · C1 · gemini-embedding-2 vs gemini-embedding-001

```python
# For each query: which policy title does each store rank first? (expected = the policy in the right column)
tests = [("What is the policy on smoking?", "Smoking"),
         ("Can I use my phone at work?", "Mobile Phone"),
         ("How are new employees hired?", "Recruitment"),
         ("What happens if I break the rules?", "Discipline"),
         ("Is harassment tolerated?", "Anti-discrimination")]
score = {"gemini-embedding-2": 0, "gemini-embedding-001": 0}
for q, expected in tests:
    row = []
    for name, db in [("gemini-embedding-2", docsearch), ("gemini-embedding-001", db_001)]:
        top = db.similarity_search(q, k=1)[0].page_content
        hit = expected.lower() in top.lower()
        score[name] += hit
        row.append(f"{name}: {'✅' if hit else '❌'} {top[:50]!r}")
    print(f"\n{q}\n  " + "\n  ".join(row))
print("\nTop-1 hits:", score)
```

**Expected / what you should see:** A ✅/❌ per query for each embedding model. Both usually rank Smoking / Mobile Phone first; the 4th (vague) query is where they differ.

#### ✅ Answer: M1-L1 · C2 · Summarize with map_reduce and refine

```python
from langchain_core.callbacks import BaseCallbackHandler

class LLMCallCounter(BaseCallbackHandler):
    def __init__(self): self.calls = 0
    def on_chat_model_start(self, serialized, messages, **kwargs): self.calls += 1
    def on_llm_start(self, serialized, prompts, **kwargs): self.calls += 1

import time
for ct in ["stuff", "map_reduce", "refine"]:
    counter = LLMCallCounter()
    qa_ct = RetrievalQA.from_chain_type(llm=llama_3_llm, chain_type=ct,
                                        retriever=docsearch.as_retriever(search_kwargs={"k": 6}))
    t = time.time()
    out = qa_ct.invoke("Can you summarize the document for me?", config={"callbacks": [counter]})["result"]
    print(f"== {ct}: {counter.calls} LLM calls · {time.time()-t:.1f}s · {len(out)} chars")
    time.sleep(1)  # be gentle with the free-tier rate limit
```

**Expected / what you should see:** `stuff` = 1 LLM call; `map_reduce` ≈ k+1 calls (7 with k=6); `refine` = k calls (6). `stuff` is fastest; `refine` is usually the longest summary.

#### ✅ Answer: M1-L1 · C3 · Rewrite the QA chain with LCEL

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

condense_prompt = ChatPromptTemplate.from_messages([
    ("system", "Rewrite the user's last question as a standalone question, using the chat history. "
               "Return only the question."),
    MessagesPlaceholder("chat_history"),
    ("human", "{question}"),
])
condense_chain = condense_prompt | llm | StrOutputParser()

def ask(question, chat_history):
    standalone = condense_chain.invoke({"chat_history": chat_history, "question": question}) if chat_history else question
    answer = rag_chain.invoke(standalone)          # rag_chain from the starter cell
    chat_history += [HumanMessage(question), AIMessage(answer)]
    return standalone, answer

chat_history = []
for q in ["Can I smoke in company vehicles?", "What I cannot do in it?"]:
    standalone, answer = ask(q, chat_history)
    print(f"Q: {q}\n  standalone: {standalone}\n  A: {answer}\n")
```

**Expected / what you should see:** The LCEL chain says it doesn't know about eating in vehicles. With history, the follow-up is rewritten to a standalone question (e.g. *What can't I do in company vehicles?*) and answered from the Smoking policy.

#### ✅ Answer: M1-L1 · C4 · Chunk-size experiment

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
question = "What is the mobile phone policy?"
for size in [200, 500, 1000]:
    chunks = RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=size // 10).split_documents(documents)
    db = Chroma.from_documents(chunks, embeddings, collection_name=f"cs{size}",
                               ids=[f"cs{size}-{i}" for i in range(len(chunks))])
    qa_cs = RetrievalQA.from_chain_type(llm=llama_3_llm, chain_type="stuff",
                                        retriever=db.as_retriever(search_kwargs={"k": 4}))
    print(f"\n== chunk_size={size}: {len(chunks)} chunks\n", qa_cs.invoke(question)["result"][:500])
```

**Expected / what you should see:** 200 → ~122 chunks, 500 → ~50, 1000 → ~26. Small chunks retrieve only fragments; 500–1000 gives the most complete answer for the mobile-phone policy.

#### ✅ Answer: M1-L1 · C5 · Compare free Gemini models

```python
import time
rows = []
for name in ["gemini-3.8-flash", "gemini-3.5-flash-lite", "gemini-3.1-flash-lite", "gemini-2.5-flash"]:
    chat = ChatGoogleGenerativeAI(model=name)   # default temperature (Gemini 3 recommendation)
    chain = ({"context": retriever | format_docs, "question": RunnablePassthrough()}
             | rag_prompt | chat | StrOutputParser())
    t = time.time()
    try:
        ans = chain.invoke("Can you summarize the document for me?")
        rows.append((name, f"{time.time()-t:.1f}s", len(ans), ans[:80].replace("\n", " ")))
    except Exception as e:      # 404 / access refused (2.5 models on new keys) / 429 free-tier limit
        rows.append((name, "-", 0, f"⚠️ {type(e).__name__}"))
    time.sleep(2)

print(f"{'model':24} {'time':>6} {'chars':>6}  first words")
for r in rows:
    print(f"{r[0]:24} {r[1]:>6} {r[2]:>6}  {r[3]}")
```

**Expected / what you should see:** A small table (model, time, chars). 3.x models answer; `gemini-2.5-flash` may show `⚠️ … 404/403` for new API keys or `429` on the free tier — that's expected.

### M2-L1

#### ✅ Answer: M2-L1 · Exercise 1: Combine two sentences

```python
import gradio as gr   # lab answer: gradio_concatenation.py, run inside the notebook

def combine(a, b):
    return a + " " + b

demo = gr.Interface(
    fn=combine,
    inputs=[gr.Textbox(label="Input 1"), gr.Textbox(label="Input 2")],
    outputs=gr.Textbox(label="Output"),
)
demo.launch(share=True)   # in a notebook launch() returns; stop with demo.close()
```

**Expected / what you should see:** A Gradio app with two textboxes; `Hello` + `world` → `Hello world`.

#### ✅ Answer: M2-L1 · Exercise 2: Incomplete answers

```python
from langchain_google_genai import ChatGoogleGenerativeAI
import re

q = "Write a detailed guide on how to be a good data scientist."

# 1) Find the cause: finish_reason MAX_TOKENS = cut off. Gemini 3 counts thinking tokens in the budget.
short = ChatGoogleGenerativeAI(model="gemini-3.8-flash", max_output_tokens=256)   # the lab's 256
r = short.invoke(q)
print("256 tokens  → finish_reason:", r.response_metadata.get("finish_reason"),
      "| thinking tokens:", (r.usage_metadata or {}).get("output_token_details", {}).get("reasoning"),
      "| answer chars:", len(r.text))

# 2) Fix: a bigger budget (and little thinking)
long = ChatGoogleGenerativeAI(model="gemini-3.8-flash", max_output_tokens=4096, thinking_level="low")
r2 = long.invoke(q)
print("4096 tokens → finish_reason:", r2.response_metadata.get("finish_reason"), "| answer chars:", len(r2.text))

# 3) Apply it to the app script and run it again (!python llm_chat.py)
s = open("llm_chat.py").read()
s = re.sub(r'"max_output_tokens": \d+,(?=  # Specifying)', '"max_output_tokens": 4096,', s)
open("llm_chat.py", "w").write(s)
print([l.strip() for l in s.splitlines() if l.strip().startswith('"max_output_tokens"')])
```

**Expected / what you should see:** With 256 tokens: `finish_reason: MAX_TOKENS`, many thinking tokens, a short or empty answer. With 4096 + `thinking_level="low"`: `STOP` and a full answer. The last line shows `"max_output_tokens": 4096` in `llm_chat.py`.

#### ✅ Answer: M2-L1 · C1 · Combine two texts

```python
import gradio as gr

def combine(a, b):
    text = a + " " + b
    return text, len(text.split())          # second output = word count

demo = gr.Interface(fn=combine,
                    inputs=[gr.Textbox(label="Input 1"), gr.Textbox(label="Input 2")],
                    outputs=[gr.Textbox(label="Output"), gr.Number(label="Word count")])
print(combine("Hello there", "general Kenobi"))   # ('Hello there general Kenobi', 4)
demo.launch(share=True)
```

**Expected / what you should see:** `('Hello there general Kenobi', 4)` and an app with *Output* + *Word count*.

#### ✅ Answer: M2-L1 · C2 · Chat UI with memory

```python
from langchain_core.messages import HumanMessage, SystemMessage

def chat_no_memory(message, history):         # history ignored
    return llm.invoke([SystemMessage("You are a concise, friendly assistant."), HumanMessage(_text(message))]).text

# Same 2-turn test without the UI (history in Gradio "messages" format)
h = [{"role": "user", "content": "My name is Sam"},
     {"role": "assistant", "content": chat("My name is Sam", [])}]
print("with memory   :", chat("What is my name?", h))
print("without memory:", chat_no_memory("What is my name?", h))

gr.ChatInterface(chat_no_memory, title="No-memory chat").launch(share=True)
```

**Expected / what you should see:** *with memory* → "Your name is Sam"; *without memory* → the model says it doesn't know your name.

#### ✅ Answer: M2-L1 · C3 · Model and temperature picker

```python
import time
MODELS = ["gemini-3.8-flash", "gemini-3.5-flash-lite", "gemini-3.1-flash-lite", "gemini-2.5-flash"]

def answer(prompt, model_name, temperature, max_tokens):
    chat = ChatGoogleGenerativeAI(model=model_name, temperature=temperature, max_output_tokens=int(max_tokens))
    t = time.time()
    try:
        text = chat.invoke(prompt).text
    except Exception as e:                      # 2.5 access limit / free-tier 429
        text = f"⚠️ {type(e).__name__}: {str(e)[:200]}"
    return text, f"{time.time() - t:.2f} s"

picker = gr.Interface(answer,
    inputs=[gr.Textbox(label="Input", lines=2),
            gr.Dropdown(MODELS, value="gemini-3.8-flash", label="Model"),
            gr.Slider(0, 2, value=1.0, step=0.1, label="Temperature (Gemini 3: keep 1.0)"),
            gr.Slider(64, 4096, value=1024, step=64, label="Max output tokens (includes thinking)")],
    outputs=[gr.Textbox(label="Output"), gr.Textbox(label="Response time")],
    title="Model playground")
print(answer("Say hi in 3 words", "gemini-3.8-flash", 1.0, 1024))
picker.launch(share=True)
```

**Expected / what you should see:** A tuple (answer, `'0.8 s'`-style time); the app has 4 inputs + 2 outputs. flash-lite ignores the temperature (warning).

#### ✅ Answer: M2-L1 · C4 · Streaming answers

```python
with gr.Blocks(title="Streaming chatbot (Blocks)") as blocks_demo:
    with gr.Row():
        with gr.Column():
            box = gr.Textbox(label="Input", lines=3)
            btn = gr.Button("Ask", variant="primary")
        out = gr.Markdown()
    btn.click(stream_answer, inputs=box, outputs=out)   # generator → streams into the Markdown
    box.submit(stream_answer, inputs=box, outputs=out)

print("chunks:", len(list(stream_answer("Explain RAG in one sentence"))))
blocks_demo.launch(share=True)
```

**Expected / what you should see:** `chunks: N` (N ≥ 1), then a Blocks app: textbox + button on the left, streaming Markdown on the right.

### M2-L2

#### ✅ Answer: M2-L2 · C1 · gemini-embedding-2 vs gemini-embedding-001 (dropdown)

```python
import uuid
import gradio as gr
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA

EMBED_MODELS = ["models/gemini-embedding-2", "models/gemini-embedding-001"]

# 1) watsonx_embedding() with a model name (copy these 2 functions into qabot.py to change the app itself)
def watsonx_embedding(model_name="models/gemini-embedding-2"):
    return GoogleGenerativeAIEmbeddings(model=model_name)

def vector_database(chunks, model_name="models/gemini-embedding-2"):
    return Chroma.from_documents(chunks, watsonx_embedding(model_name),
                                 collection_name=f"c1_{uuid.uuid4().hex[:8]}")   # own collection per call

def retriever_qa(file, query, model_name):
    chunks = qabot.text_splitter(qabot.document_loader(file))
    qa = RetrievalQA.from_chain_type(llm=qabot.get_llm(), chain_type="stuff",
                                     retriever=vector_database(chunks, model_name).as_retriever(),
                                     return_source_documents=False)
    return qa.invoke(query)["result"]

# 2) Same question with both models
q = "What is the difference between RAG-Sequence and RAG-Token?"
for m in EMBED_MODELS:
    print(f"== {m}\n{retriever_qa('sample.pdf', q, m)[:400]}\n")

# 3) The lab interface + a dropdown for the embedding model
c1_app = gr.Interface(
    fn=retriever_qa,
    flagging_mode="never",
    inputs=[gr.File(label="Upload PDF File", file_count="single", file_types=['.pdf'], type="filepath"),
            gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here..."),
            gr.Dropdown(EMBED_MODELS, value=EMBED_MODELS[0], label="Embedding model")],
    outputs=gr.Textbox(label="Output"),
    title="RAG Chatbot (embedding picker)")
c1_app.launch(share=True)   # stop later with c1_app.close()
```

**Expected / what you should see:** Two answers (one per embedding model) for the RAG-Sequence vs RAG-Token question, then a Gradio app with an embedding-model dropdown. Retrieved chunks differ slightly between the two models.

#### ✅ Answer: M2-L2 · C2 · Show the sources (Gradio)

```python
import gradio as gr
from langchain_classic.chains import RetrievalQA

def retriever_qa_with_sources(file, query):
    qa = RetrievalQA.from_chain_type(llm=qabot.get_llm(), chain_type="stuff",
                                     retriever=qabot.retriever(file), return_source_documents=True)
    res = qa.invoke(query)
    pages = sorted({d.metadata.get("page", 0) + 1 for d in res["source_documents"]})   # PyPDFLoader pages are 0-based
    return f"{res['result']}\n\nSources: pages {pages}"

c2_app = gr.Interface(
    fn=retriever_qa_with_sources,
    flagging_mode="never",
    inputs=[gr.File(label="Upload PDF File", file_count="single", file_types=['.pdf'], type="filepath"),
            gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here...")],
    outputs=gr.Textbox(label="Output"),
    title="RAG Chatbot with sources")
print(retriever_qa_with_sources("sample.pdf", "Which retriever does RAG use?"))
c2_app.launch(share=True)   # stop later with c2_app.close()
```

**Expected / what you should see:** The answer followed by `Sources: pages [2, …]` (1-based page numbers), and an app whose output shows the same text.

#### ✅ Answer: M2-L2 · C3 · Refusing prompt inside the app

```python
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA

PROMPT = PromptTemplate.from_template("""Use only the context to answer. If it is not in the context, say "Not in the document."
{context}
Question: {question}
Answer:""")

def retriever_qa_strict(file, query):          # drop-in replacement for qabot.retriever_qa
    qa = RetrievalQA.from_chain_type(llm=qabot.get_llm(), chain_type="stuff",
                                     retriever=qabot.retriever(file),
                                     chain_type_kwargs={"prompt": PROMPT})   # ← the custom prompt
    return qa.invoke(query)["result"]

for q in ["What does RAG combine with a seq2seq model?",   # answerable from the paper
          "What is the capital of France?"]:             # not in the paper
    print(f"{q}\n  → {retriever_qa_strict('sample.pdf', q)}\n")
```

**Expected / what you should see:** In-document questions are answered; *What is the capital of France?* returns exactly **Not in the document.**

#### ✅ Answer: M2-L2 · C4 · Cached retriever in the app

```python
import functools, time
from langchain_classic.chains import RetrievalQA

@functools.lru_cache(maxsize=8)
def cached_retriever(path):                     # one vector DB per uploaded file path
    return qabot.retriever(path)

def retriever_qa_cached(file, query):
    qa = RetrievalQA.from_chain_type(llm=qabot.get_llm(), chain_type="stuff",
                                     retriever=cached_retriever(file), return_source_documents=False)
    return qa.invoke(query)["result"]

cached_retriever.cache_clear()
for fn in (qabot.retriever_qa, retriever_qa_cached):
    times = []
    for q in ["What is RAG?", "Which datasets are used?", "Who wrote the paper?"]:
        t = time.time(); fn("sample.pdf", q); times.append(time.time() - t)
    print(f"{fn.__name__:20}", " · ".join(f"{x:.2f}s" for x in times))
print(cached_retriever.cache_info())

# In the app: use fn=retriever_qa_cached in gr.Interface (same inputs/outputs as the lab)
```

**Expected / what you should see:** Uncached: every call ≈ same time (re-embeds). Cached: 1st call slow, next calls ≈ 0.0 s; `CacheInfo(hits=2, misses=1, …)`.

#### ✅ Answer: M2-L2 · C5 · Ask across several PDFs

```python
import gradio as gr
from langchain_classic.chains import RetrievalQA

!wget -q -O attention.pdf https://arxiv.org/pdf/1706.03762 && ls -lh attention.pdf

def multi_retriever(paths):
    all_chunks = []
    for p in paths:
        all_chunks += qabot.text_splitter(qabot.document_loader(p))
    return qabot.vector_database(all_chunks).as_retriever(search_kwargs={"k": 5})

def multi_qa(files, query):
    paths = [f if isinstance(f, str) else f.name for f in (files or [])]
    qa = RetrievalQA.from_chain_type(llm=qabot.get_llm(), chain_type="stuff",
                                     retriever=multi_retriever(paths), return_source_documents=True)
    res = qa.invoke(query)
    srcs = sorted({f"{d.metadata['source']} p.{d.metadata.get('page', 0) + 1}" for d in res["source_documents"]})
    return res["result"] + "\n\nSources: " + ", ".join(srcs)

print(multi_qa(["sample.pdf", "attention.pdf"],
               "How do the RAG paper and the Transformer paper (Attention Is All You Need) differ in what they propose?"))

c5_app = gr.Interface(
    fn=multi_qa, flagging_mode="never",
    inputs=[gr.File(label="Upload PDF Files", file_count="multiple", file_types=['.pdf'], type="filepath"),
            gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here...")],
    outputs=gr.Textbox(label="Output"), title="RAG Chatbot (multiple PDFs)")
c5_app.launch(share=True)   # stop later with c5_app.close()
```

**Expected / what you should see:** `attention.pdf` downloaded, one answer using chunks from both papers (RAG + Transformer), and an app with `file_count="multiple"`.

### M3-L1

#### ✅ Answer: M3-L1 · Lab Exercise 1 · extract_linkedin_profile

```python
# PSEUDOCODE
# extract_linkedin_profile(url, api_key=None, mock=False):
#   start a timer
#   if mock: GET config.MOCK_DATA_URL (timeout 30 s)
#   else:    require api_key → GET ProxyCurl endpoint with {"url": url, ...} and an
#            "Authorization: Bearer <api_key>" header
#   if status != 200 → log the error, return {}
#   data = response.json()
#   clean it: drop empty values ([], "", None) and unused keys ("people_also_viewed", "certifications")
#   if "groups" exist → drop "profile_pic_url" from each group
#   log the elapsed time, return the cleaned dict   (any exception → log, return {})

# Runnable sketch of the mock branch (same steps, no ProxyCurl):
import time, requests, config
def my_extract(url, api_key=None, mock=True):
    t = time.time()
    r = requests.get(config.MOCK_DATA_URL, timeout=30)
    if r.status_code != 200:
        return {}
    data = {k: v for k, v in r.json().items()
            if v not in ([], "", None) and k not in ("people_also_viewed", "certifications")}
    print(f"loaded in {time.time() - t:.2f}s")
    return data
p = my_extract("https://www.linkedin.com/in/leonkatsnelson/")
print(p.get("full_name"), "|", len(p), "fields |", sorted(p)[:6])
````<br><br>**Expected / what you should see:** `loaded in …s`, then `Leon Katsnelson | N fields | [...]` (the lab's mock profile). Your pseudocode should cover: mock vs API branch, status-code check, JSON cleanup, error → `{}`.

#### ✅ Answer: M3-L1 · Lab Exercise 2 · split / index / verify

````py
# PSEUDOCODE
# split_profile_data(profile):
#   text = json.dumps(profile)                      # whole profile as one string
#   doc  = Document(text=text)
#   nodes = SentenceSplitter(chunk_size=config.CHUNK_SIZE).get_nodes_from_documents([doc])
#   return nodes                                    (exception → log, return [])
# create_vector_database(nodes):
#   embed_model = create_watsonx_embedding()
#   index = VectorStoreIndex(nodes=nodes, embed_model=embed_model, show_progress=False)
#   return index                                    (exception → log, return None)
# verify_embeddings(index):
#   for every node in index.vector_store data: embedding must exist and not be empty
#   log the ids that are missing → return True only if none are missing

import json, requests, config
from llama_index.core import Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
prof = requests.get(config.MOCK_DATA_URL, timeout=30).json()
my_nodes = SentenceSplitter(chunk_size=config.CHUNK_SIZE).get_nodes_from_documents([Document(text=json.dumps(prof))])
my_idx = VectorStoreIndex(nodes=my_nodes, embed_model=GoogleGenAIEmbedding(model_name=config.EMBEDDING_MODEL_ID))
emb = my_idx.vector_store.data.embedding_dict
missing = [nid for nid in emb if not emb[nid]]
print(len(my_nodes), "nodes ·", len(emb), "embeddings · missing:", missing)
````<br><br>**Expected / what you should see:** about 10–20 nodes (chunk size 500), the same number of embeddings, `missing: []`.

#### ✅ Answer: M3-L1 · Lab Exercise 3 · embedding + LLM factory

````py
# PSEUDOCODE
# create_watsonx_embedding(): return an embedding model for config.EMBEDDING_MODEL_ID
#   (IBM: WatsonxEmbeddings(model_id, url, project_id, truncate_input_tokens=3)
#    Colab: GoogleGenAIEmbedding(model_name=config.EMBEDDING_MODEL_ID))
# create_watsonx_llm(temperature, max_new_tokens, decoding_method):
#   greedy → temperature 0
#   build the LLM for config.LLM_MODEL_ID with those generation settings
#   (Colab/Gemini 3: no temperature, thinking_level="low", max_output_tokens ≥ 1024)
# change_llm_model(new_id): config.LLM_MODEL_ID = new_id   (next create_watsonx_llm() uses it)

import asyncio
try:
    asyncio.get_running_loop()
    import nest_asyncio
    _orig_run = asyncio.run
    nest_asyncio.apply()
    _nested_run = asyncio.run
    def _run(main, *, debug=None, loop_factory=None):
        # nest_asyncio's run() has no loop_factory → uvicorn (Gradio launch) would crash
        if loop_factory is not None:
            return _orig_run(main, debug=debug, loop_factory=loop_factory)
        return _nested_run(main, debug=debug)
    asyncio.run = _run
except RuntimeError:
    pass
import config
from google.genai import types
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
def my_llm(max_new_tokens=500):
    return GoogleGenAI(model=config.LLM_MODEL_ID, max_tokens=max(max_new_tokens, 1024),
                       generation_config=types.GenerateContentConfig(
                           max_output_tokens=max(max_new_tokens, 1024),
                           thinking_config=types.ThinkingConfig(thinking_level="low")))
print(len(GoogleGenAIEmbedding(model_name=config.EMBEDDING_MODEL_ID).get_text_embedding("hello")), "dims")
print(my_llm().complete("Say hello in 3 words.").text)
````<br><br>**Expected / what you should see:** `3072 dims` with `gemini-embedding-2` (offline fake: 64), then a short greeting from `gemini-3.8-flash`.

#### ✅ Answer: M3-L1 · Lab Exercise 4 · facts + Q&A

````py
# PSEUDOCODE
# generate_initial_facts(index):
#   llm = create_watsonx_llm(temperature=0.0, max_new_tokens=500)
#   prompt = PromptTemplate(config.INITIAL_FACTS_TEMPLATE)            # uses {context_str}
#   qe = index.as_query_engine(similarity_top_k=config.SIMILARITY_TOP_K, llm=llm, text_qa_template=prompt)
#   return qe.query("Provide three interesting facts …").response   (error → message string)
# answer_user_query(index, question):
#   llm = create_watsonx_llm(max_new_tokens=250, decoding_method="greedy")
#   prompt = PromptTemplate(config.USER_QUESTION_TEMPLATE)            # {context_str} + {query_str}
#   qe = index.as_query_engine(... same ..., text_qa_template=prompt)
#   return qe.query(question)          # a Response object → caller uses .response

from llama_index.core import PromptTemplate
import importlib.util   # load the file directly: modules/__init__.py imports query_engine, which isn't written yet
_spec = importlib.util.spec_from_file_location("llm_interface", "modules/llm_interface.py")
_li = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_li)
create_watsonx_llm = _li.create_watsonx_llm
qe = my_idx.as_query_engine(llm=create_watsonx_llm(max_new_tokens=500), similarity_top_k=config.SIMILARITY_TOP_K,
                            text_qa_template=PromptTemplate(config.INITIAL_FACTS_TEMPLATE))
print(qe.query("Provide three interesting facts about this person's career or education.").response)
qa_engine = my_idx.as_query_engine(llm=create_watsonx_llm(max_new_tokens=250, decoding_method="greedy"),
                                   similarity_top_k=config.SIMILARITY_TOP_K,
                                   text_qa_template=PromptTemplate(config.USER_QUESTION_TEMPLATE))
r = qa_engine.query("What is their favourite food?")
print(type(r).__name__, "→", r.response)
````<br><br>**Expected / what you should see:** 3 numbered facts from the mock profile, then `Response → I don't know. The information is not available on the LinkedIn page.` (needs `my_idx` from the Exercise 2 answer).

#### ✅ Answer: M3-L1 · Lab Exercise 5 · the CLI pipeline

````py
# PSEUDOCODE
# process_linkedin(url, api_key, mock):
#   profile = extract_linkedin_profile(url, api_key, mock)   → stop if empty
#   nodes = split_profile_data(profile); index = create_vector_database(nodes)  → stop if None
#   verify_embeddings(index) (warn only); print generate_initial_facts(index)
#   chatbot_interface(index)
# chatbot_interface(index):
#   loop: q = input("You: "); exit on exit/quit/bye; print answer_user_query(index, q).response
# main(): parse --url --api-key --mock --model; ask for the URL only if needed;
#   --model → change_llm_model; process_linkedin(...)

from modules.data_extraction import extract_linkedin_profile
from modules.data_processing import split_profile_data, create_vector_database, verify_embeddings
from modules.query_engine import generate_initial_facts, answer_user_query
def my_pipeline(questions, url="https://www.linkedin.com/in/leonkatsnelson/"):
    idx = create_vector_database(split_profile_data(extract_linkedin_profile(url, mock=True)))
    print("embeddings ok:", verify_embeddings(idx))
    print("\nHere are 3 interesting facts about this person:\n" + generate_initial_facts(idx))
    for q in questions + ["bye"]:              # a list instead of input()
        if q.lower() in ("exit", "quit", "bye"):
            print("Bot: Goodbye!"); break
        print(f"You: {q}\nBot: {answer_user_query(idx, q).response.strip()}\n")
my_pipeline(["What is this person's current job title?", "Where did they get their education?"])
````<br><br>**Expected / what you should see:** `embeddings ok: True`, 3 facts, two `You:`/`Bot:` turns, `Bot: Goodbye!` — the same flow as `python main.py --mock`.

#### ✅ Answer: M3-L1 · C1 · Your own profile

````py
my_profile = {
    "full_name": "Sara Ahmadi", "headline": "Data Scientist · RAG & LLM apps", "city": "Tehran", "country_full_name": "Iran",
    "summary": "I build retrieval-augmented chatbots and teach Python.",
    "experiences": [
        {"title": "ML Engineer", "company": "Acme AI", "starts_at": {"year": 2022}, "ends_at": None,
         "description": "Built RAG chatbots with LangChain and LlamaIndex on Gemini."},
        {"title": "Data Analyst", "company": "Blue Bank", "starts_at": {"year": 2019}, "ends_at": {"year": 2022},
         "description": "Dashboards and churn models in Python/SQL."}],
    "education": [{"school": "University of Tehran", "degree_name": "MSc", "field_of_study": "Computer Science",
                   "starts_at": {"year": 2017}, "ends_at": {"year": 2019}}],
    "skills": ["Python", "LangChain", "LlamaIndex", "SQL", "Gradio"],
    "languages": ["Persian", "English"],
}
my_index = create_vector_database(split_profile_data(my_profile))
print("nodes ok:", verify_embeddings(my_index))
print(generate_initial_facts(my_index))
for q in ["Where did she work before Acme AI?", "What is her favourite food?"]:
    print(f"\nQ: {q}\nA: {answer_user_query(my_index, q).response}")
````<br><br>**Expected / what you should see:** `nodes ok: True`, 3 facts built only from your JSON, *Blue Bank (Data Analyst, 2019–2022)* for the first question and the *I don't know…* sentence for the second. Real LinkedIn data: *Settings → Data privacy → Get a copy of your data*, then convert the CSVs to a dict like this.

#### ✅ Answer: M3-L1 · C2 · Icebreakers tab in the app

````py
import gradio as gr, app       # app.py's functions + its active_indices dict
def icebreakers_for_session(session_id):
    if not session_id or session_id not in app.active_indices:
        return "No profile loaded. Please process a LinkedIn profile first."
    return generate_icebreakers(app.active_indices[session_id])

with gr.Blocks(title="LinkedIn Icebreaker Bot") as demo_c2:
    gr.Markdown("# LinkedIn Icebreaker Bot")
    with gr.Tab("Process LinkedIn Profile"):
        url = gr.Textbox(label="LinkedIn Profile URL"); key = gr.Textbox(label="ProxyCurl API Key", type="password")
        mock = gr.Checkbox(label="Use Mock Data", value=True)
        model = gr.Dropdown(["gemini-3.8-flash", "gemini-3.5-flash-lite"], value=config.LLM_MODEL_ID, label="Select LLM Model")
        facts = gr.Textbox(label="Initial Facts", lines=10); sid = gr.Textbox(visible=False)
        gr.Button("Process Profile").click(app.process_profile, [url, key, mock, model], [facts, sid], api_name="process_profile")
    with gr.Tab("Icebreakers"):                                    # ← the new third tab
        ice = gr.Textbox(label="Icebreakers", lines=6)
        gr.Button("Generate icebreakers").click(icebreakers_for_session, [sid], [ice], api_name="icebreakers")
    with gr.Tab("Chat"):
        bot = gr.Chatbot(height=400); q = gr.Textbox(label="Ask a question about the profile")
        q.submit(app.chat_with_profile, [sid, q, bot], [bot], api_name="chat_with_profile")
demo_c2.launch(share=True)     # not blocking in the notebook; demo_c2.close() to stop
# To change app.py itself: paste ICEBREAKER_TEMPLATE + generate_icebreakers into modules/query_engine.py
# and the "Icebreakers" tab block into create_gradio_interface(), using the existing session_id Textbox.
````<br><br>**Expected / what you should see:** a `*.gradio.live` link. *Process Profile* → *Icebreakers* tab → *Generate icebreakers* gives 3 friendly questions about the person; before processing it says *No profile loaded…*.

#### ✅ Answer: M3-L1 · C3 · Chunk size × top-k

````py
q = "What was their career progression?"
for cs in [200, 500, 1000]:
    config.CHUNK_SIZE = cs
    nds = split_profile_data(profile)
    idx = create_vector_database(nds)
    for k in [2, 5]:
        config.SIMILARITY_TOP_K = k               # answer_user_query reads it at call time
        ans = answer_user_query(idx, q).response
        print(f"chunk_size={cs:4d} ({len(nds):2d} nodes) · top_k={k} → {len(ans):4d} chars | {ans[:120]!r}")
config.CHUNK_SIZE, config.SIMILARITY_TOP_K = 500, 5      # restore the lab defaults
````<br><br>**Expected / what you should see:** 6 lines. Smaller chunks = more nodes (≈ 40 / 15 / 8). `top_k=2` with 200-char chunks misses roles; `top_k=5` with 500–1000 gives the fullest timeline. The lab's optional tuning (`CHUNK_SIZE = 400`, `SIMILARITY_TOP_K = 7`) sits in between.

#### ✅ Answer: M3-L1 · C4 · Compare Gemini models (with errors handled)

````py
import time
for mid in ["gemini-3.8-flash", "gemini-3.5-flash-lite", "gemini-3.1-flash-lite", "gemini-2.5-flash"]:
    change_llm_model(mid); t = time.time()
    try:
        known = answer_user_query(index, "What is this person's current job title?").response
        unknown = answer_user_query(index, "What is their favourite food?").response
        grounded = "don't know" in unknown.lower()
        print(f"{mid:22s} {time.time() - t:5.1f}s · grounded={grounded} · {known[:90]!r}")
    except Exception as e:          # 2.5 access limit on new keys (404/403) or free-tier 429
        print(f"{mid:22s} ⚠️ {type(e).__name__}: {str(e)[:80]}")
    time.sleep(2)                   # be gentle with the free-tier rate limit
change_llm_model("gemini-3.8-flash")
````<br><br>**Expected / what you should see:** one line per model with time, `grounded=True` (it says *I don't know…* for the food question) and the job title. Flash-lite models are fastest. `gemini-2.5-flash` may show ⚠️ on a new API key; that is the 2.5 access limit, not your code.

#### ✅ Answer: M3-L1 · C5 · Chat with memory in the app

````py
import gradio as gr, app
chat_engines = {}                                 # one memory per session id
def chat_with_memory(session_id, user_query, chat_history):
    if not session_id or session_id not in app.active_indices:
        return chat_history + app._turn(user_query, "No profile loaded. Please process a LinkedIn profile first.")
    if session_id not in chat_engines:
        chat_engines[session_id] = app.active_indices[session_id].as_chat_engine(
            chat_mode="context", llm=create_watsonx_llm(), similarity_top_k=3,
            system_prompt="Answer only from the LinkedIn profile context. If it is not there, say you don't know.")
    answer = chat_engines[session_id].chat(user_query).response
    return chat_history + app._turn(user_query, answer)

with gr.Blocks(title="LinkedIn Icebreaker Bot") as demo_c5:
    url = gr.Textbox(label="LinkedIn Profile URL"); key = gr.Textbox(visible=False)
    mock = gr.Checkbox(label="Use Mock Data", value=True); model = gr.Textbox(value=config.LLM_MODEL_ID, visible=False)
    facts = gr.Textbox(label="Initial Facts", lines=6); sid = gr.Textbox(visible=False)
    gr.Button("Process Profile").click(app.process_profile, [url, key, mock, model], [facts, sid], api_name="process_profile")
    bot = gr.Chatbot(height=400); q = gr.Textbox(label="Ask (follow-ups work)")
    q.submit(chat_with_memory, [sid, q, bot], [bot], api_name="chat_with_profile")
demo_c5.launch(share=True)
# In app.py: put chat_engines + this function in place of chat_with_profile's answer_user_query call.
````<br><br>**Expected / what you should see:** in the app, *Where does this person work now?* then *And before that?* — the second answer names the previous employer, because the chat engine keeps the history (the original `chat_with_profile` would not know what *that* refers to).
```