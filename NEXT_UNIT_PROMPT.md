# Ready prompts for the next units (v14 "Notion pastel" design)

**How to use:** start a **new chat**. Attach (1) the course ZIP for that unit (PDFs, summaries, lab instructions, `.ipynb`,
and your unfinished HTML if you have one) and (2) the **newest TenderYar ZIP** (it must contain `html/RAG_C1_Guide_v14.html`,
the design reference, and `html/build_v14.py`; add both to the ZIP once if it still only has the v13 files). Copy Prompt A, replace every `{{…}}` with the values from the table at the bottom, send.
If the run stops, open a new chat, attach the newest ZIP from the checkpoint page and send Prompt B.

---
## Prompt A — new course guide + TenderYar part (C2 … C10)

```
I'm self-studying the IBM "RAG and Agentic AI" Professional Certificate in Google Colab (Gemini models, not the IBM lab).
Attached: (1) {{COURSE_ZIP}} = Course {{N}} "{{COURSE_TITLE}}" materials (PDFs, summaries, lab instructions,
Colab notebooks{{, and my unfinished HTML guide}}); (2) {{TENDERYAR_ZIP}} = my TenderYar project, newest checkpoint.

STEP 0 — read, in this order, before writing anything:
  tenderyar/_checkpoints/PROGRESS.md · tenderyar/kit/HTML_STYLE_GUIDE.md (all of it, §9 = theme) ·
  tenderyar/kit/courses/C{{NN}}.md (exact project brief) · tenderyar/docs/MASTER_PLAN.md · tenderyar/docs/AUDIT.md ·
  tenderyar/html/RAG_C1_Guide_v14.html (design reference: copy its <head>, all <style> blocks and all <script> blocks).
  If HTML_STYLE_GUIDE.md §9 still describes the v13 "Claude" theme, the v14 theme below wins — update §9 to match it.
  Then list every lesson, video, reading, lab and quiz in my course materials (this list becomes the coverage matrix).

JOB 1 — Course {{N}} HTML revision guide, ONE self-contained file "RAG_C{{N}}_Guide_v1.html":
 Design (must look identical to the C1 v14 guide — calm, low-distraction "Notion pastel" look):
  - Surfaces: white page #FFFFFF, sidebar = page colour with a thin #E6E5E3 divider, flat soft-gray cards / diagram
    panels / quizzes #F9F8F7, borders #E6E5E3, text #2C2C2B, muted #7D7A75, code background #F6F5F3. No shadows,
    no gradients, radius 14px (cards) / 10px (callouts, inputs).
  - Pastel accents, always as a strong colour + its soft tint: blue #2783DE/#E5F2FC (primary: links, eyebrow,
    progress), purple #9065B0/#F3EBF8, green #46A171/#E8F1EC, orange #D5803B/#FBEBDE, red #E56458/#FCE9E7.
    Callouts = 4px left border in the strong colour on the tint; tags = pastel pills.
  - Fonts: ONE system sans stack for everything incl. headings (-apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, Helvetica, Arial), bold headings with slight negative tracking (hero h1 44px, h2 28px, h3 19px),
    body 16.5px / 1.65; code Menlo/Consolas; Vazirmatn only for Persian (.prs/.rtl). No serif, no Inter/JetBrains.
  - Buttons: quiet pills; primary/active = text-coloured pill (#2C2C2B bg, white text), secondary = outline.
  - Dark mode = calm gray: page #191919, cards #202020, soft2 #2A2A29, borders rgba(255,255,255,.18), text #FFFFFF,
    accents #5E9FE8 · #BF8EDA · #72BC8F · #DE9255 · #E97366 on 12 % tints. Follows the system setting, ◐ toggle kept.
  - Keep <style id="v14-theme"> (from html/build_v14.py) as the LAST <style> block in <head>. Use only the CSS
    variables/classes from the style guide — no new hex colours in content or SVG.
  - Same skeleton: sidebar (search, progress bar, collapsible groups) · hero (eyebrow, h1, lead, 4 stat cards,
    "How to use" + study plan, quiz dashboard) · #start orientation (concept-map diagram + Colab setup cell) ·
    one section.week per module · Appendix A (comparisons, IBM→Colab mapping, troubleshooting) · Appendix B toolkit ·
    Appendix C TenderYar · coverage matrix · mixed exam · glossary · flashcards · cheat sheet · Colab exercises.
  - Every lesson = the lesson card from style guide §3: secnum, h2, meta, "In a nutshell", 🎯 objectives,
    💡 in plain words, ≥1 inline SVG diagram (classes n/n2/n3/n4/ln/mt), closed <details> Colab cells
    (Gemini: gemini-3.8-flash main, gemini-3.5-flash-lite cheap, gemini-2.5-flash fallback, models/gemini-embedding-2;
    key from Colab Secrets GOOGLE_API_KEY), "✅ You should see" with concrete output, key takeaways (why/pit/rem).
  - All practice + graded quiz questions (my words if needed) + extra checks, with explanation and a 📖 review link.
  - localStorage prefix c{{N}}m_ everywhere (replace c1m13_), title "Course {{N}} Revision Guide (v1) · RAG & Agentic AI".
  {{If I attached an unfinished HTML: keep its content, re-theme it with html/build_v14.py, list what is missing
    against the sources, and complete it.}}

JOB 2 — TenderYar v{{VERSION}} exactly as specified in kit/courses/C{{NN}}.md (do not invent a different scope):
  - Code in the tenderyar/ package + pytest tests (all old tests must still pass), Colab notebook
    notebooks/C{{N}}_TenderYar_v{{VERSION_}}.ipynb (built by a script like notebooks/build_nb.py), data files,
    docs/RESULTS.md rows, README roadmap + START_HERE update, git tag v{{VERSION}} instructions.
  - Appendix C (#proj) in the guide: proj-why (what v{{VERSION}} adds, pipeline diagram, position in the 10-course
    roadmap) → proj-setup (restore v{{PREV_VERSION}}, install, run tests) → proj-s1…sN (one per module concept;
    secnum says which lesson it re-uses) → proj-done (Done-when checklist pd{{N}}_<n>, results table, GitHub push
    cell, resume bullet, what the next course adds). Week-end "🏗 TenderYar checkpoint" bridge boxes, sidebar group.
  - Teach me every step: why → how → diagram → code (closed cells, numbered "Cell n") → "You should see" with numbers →
    takeaways. At least 3 "🌱 Beyond the course" boxes on related topics worth learning (with 1–2 good links each).
  - Persian text: normalise ي→ی, ك→ک, digits, ZWNJ; never mix Persian and Latin in one SVG <text>.

QUALITY CHECK before delivering: pytest passes; notebook JSON valid; HTML has 0 console errors; screenshots in
light AND dark mode of hero, one lesson diagram, one code cell, one quiz, the project section; every source item
appears in the coverage matrix; numbers in HTML = numbers in RESULTS.md and the notebook.

CHECKPOINTS (very important — limited free account, runs can stop any time):
  - Work in /data/tenderyar. BEFORE and AFTER every small step append one line to tenderyar/_checkpoints/PROGRESS.md
    (done / decision / NEXT:). One file, one HTML part (html/parts/C{{N}}_A_….html) or one fix per step.
  - Immediately create a Notion page "TenderYar — build checkpoints (C{{N}}, run 1)" with the task list; every 2–3
    steps zip the folder (tenderyar_c{{N}}_cpNN.zip), attach it to that page and add the log line.
  - If something is unclear, choose sensibly, write the decision into PROGRESS.md and continue.
At the end give me: the HTML file, the project ZIP, and a short "what to do in Colab, in order" list.
```

---
## Prompt B — resume after a run stopped

```
Continue TenderYar from the checkpoint page. Attached: newest tenderyar_…_cpNN.zip {{+ course ZIP}}.
Read tenderyar/_checkpoints/PROGRESS.md and continue from the last "NEXT:" line (do not redo finished steps).
Create a new Notion checkpoint page for this run (old pages may not be reachable). Same rules: small steps,
log before/after each step, zip + attach to the checkpoint page every 2–3 steps, same v14 "Notion pastel" design
(html/RAG_C1_Guide_v14.html + html/build_v14.py).
```

---
## Prompt C — add only the TenderYar part to a finished course guide

```
Attached: my finished Course {{N}} HTML guide + newest TenderYar ZIP. Read tenderyar/kit/HTML_STYLE_GUIDE.md and
tenderyar/kit/courses/C{{NN}}.md. (1) If the guide is not in the v14 theme yet, run html/build_v14.py on it.
(2) Build TenderYar v{{VERSION}} (code, tests, notebook, docs). (3) Insert Appendix C with a build script like
html/build_v12.py (section before #cover, sidebar group, bridge boxes after each week, checklist JS, .prs/.rtl/.pdone).
Do not change my existing lessons. Same checkpoint and quality rules as Prompt A.
```

---
## Values for each course
| N | NN | Course title (Coursera) | VERSION | VERSION_ | PREV_VERSION |
|---|---|---|---|---|---|
| 2 | 02 | Build RAG Applications: Get Started | 0.2 | 0_2 | 0.1 |
| 3 | 03 | Vector Databases for RAG: An Introduction | 0.3 | 0_3 | 0.2 |
| 4 | 04 | Advanced RAG with Vector Databases and Retrievers | 0.4 | 0_4 | 0.3 |
| 5 | 05 | Build Multimodal Generative AI Applications | 0.5 | 0_5 | 0.4 |
| 6 | 06 | Fundamentals of Building AI Agents | 0.6 | 0_6 | 0.5 |
| 7 | 07 | Agentic AI with LangChain and LangGraph | 0.7 | 0_7 | 0.6 |
| 8 | 08 | Agentic AI with LangGraph, CrewAI, AutoGen and BeeAI | 0.8 | 0_8 | 0.7 |
| 9 | 09 | Build AI Agents using MCP | 0.9 | 0_9 | 0.8 |
| 10 | 10 | Develop Generative AI Applications Capstone (RAG and Agentic AI) | 1.0 | 1_0 | 0.9 |

Course titles are from the certificate outline; use the exact titles printed in your Coursera materials if they differ.

**Example (Course 2) — the only lines that change:**
`{{COURSE_ZIP}}` → `C02_Build_RAG_Applications.zip` · `{{N}}` → `2` · `{{NN}}` → `02` · `{{COURSE_TITLE}}` → `Build RAG Applications: Get Started`
· `{{VERSION}}` → `0.2` · `{{VERSION_}}` → `0_2` · `{{PREV_VERSION}}` → `0.1` · `{{TENDERYAR_ZIP}}` → the newest ZIP name.
