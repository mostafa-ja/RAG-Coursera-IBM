#!/usr/bin/env python3
"""build_v14.py — re-theme any course guide to the v14 "Notion pastel" design.
Usage:  python html/build_v14.py IN.html [OUT.html]
- replaces <style id="v13-theme"> / <style id="v14-theme"> (or adds one as the last <head> style block)
- loads only Vazirmatn from Google Fonts (UI = system font stack, code = Menlo/Consolas)
- sets light/dark theme-color meta tags. Content, scripts and localStorage keys are untouched."""
import re, sys
CSS = r'''/* ===== v14 · "Notion pastel" theme — calm white/gray surfaces, soft pastel accents, system font
   (matches 01_foundations-of-generative-ai-and-prompt-engineering.html). CSS only, overrides earlier blocks.
   Change colours ONLY here; every component uses the variables. Light = white + warm-gray cards; dark = #191919 gray. ===== */
:root{
 --font-ui:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 --font-serif:var(--font-ui);
 --font-mono:Menlo,Consolas,"Liberation Mono",monospace;
 --font-fa:Vazirmatn,Tahoma,"Noto Sans Arabic",sans-serif;
 --fs:16.5px;
 --tx:#2C2C2B;--tx2:#2C2C2B;--mut:#7D7A75;
 --bg:#FFFFFF;--card:#FFFFFF;--soft:#F9F8F7;--soft2:#F0EFED;--bd:#E6E5E3;
 --ac:#2783DE;--acH:#1F6FC0;--acS:#E5F2FC;       /* blue   */
 --ac2:#9065B0;--ac2S:#F3EBF8;                    /* purple */
 --ok:#46A171;--okS:#E8F1EC;                      /* green  */
 --warn:#D5803B;--warnS:#FBEBDE;                  /* orange */
 --bad:#E56458;--badS:#FCE9E7;                    /* red    */
 --codeBg:#F6F5F3;--codeTx:#1F2328;--r:14px;
 --shadow:none;
 --kw:#C2410C;--str:#16803C;--fn:#2563EB;--sel:rgba(39,131,222,.18)}
[data-theme=dark]{
 --tx:#FFFFFF;--tx2:#FFFFFF;--mut:rgba(255,255,255,.65);
 --bg:#191919;--card:#191919;--soft:#202020;--soft2:#2A2A29;--bd:rgba(255,255,255,.18);
 --ac:#5E9FE8;--acH:#7DB2EE;--acS:rgba(94,159,232,.12);
 --ac2:#BF8EDA;--ac2S:rgba(191,142,218,.12);
 --ok:#72BC8F;--okS:rgba(114,188,143,.12);
 --warn:#DE9255;--warnS:rgba(222,146,85,.12);
 --bad:#E97366;--badS:rgba(233,115,102,.12);
 --codeBg:#232322;--codeTx:#EDEDED;
 --shadow:none;
 --kw:#FB923C;--str:#86EFAC;--fn:#93C5FD;--sel:rgba(94,159,232,.30)}
html{color-scheme:light}[data-theme=dark]{color-scheme:dark}
body{font-family:var(--font-ui);background:var(--bg);color:var(--tx);line-height:1.65;letter-spacing:normal}
::selection{background:var(--sel)}
a{color:var(--ac);text-decoration-color:color-mix(in srgb,var(--ac) 45%,transparent);text-underline-offset:2px}
a:hover{color:var(--acH)}
/* headings: same sans font, bold, tight tracking */
h1,h2,h3,h4,.hero h1,section>h1,.week>h1,.card h4,.take h4{font-family:var(--font-ui);font-weight:700;color:var(--tx);letter-spacing:-.01em}
.hero h1{font-size:44px;line-height:1.12;font-weight:700;letter-spacing:-.02em}
section>h1,.week>h1{font-size:34px;letter-spacing:-.02em}
.hero .lead{font-family:var(--font-ui);font-size:19px;line-height:1.65;color:var(--mut)}
h2{font-size:28px;letter-spacing:-.01em}h3{font-size:19px}
.eyebrow{font-size:12.5px;color:var(--ac);letter-spacing:.08em;font-weight:700}.secnum{font-size:13px;color:var(--mut);letter-spacing:.06em}
/* sidebar: page-coloured, thin divider, muted links */
#side{background:var(--bg);border-right:1px solid var(--bd)}
#side h2{font-family:var(--font-ui);font-size:14px;font-weight:700}
#side a{border-radius:8px}
#side a:hover,#side a.act{background:var(--soft2);color:var(--tx)}
#side a.act{box-shadow:none}
#side a.done::after{color:var(--ok)}
#side #sq{background:var(--bg);border-radius:10px}
#side #sq:focus,input:focus,textarea:focus,select:focus{outline:2px solid color-mix(in srgb,var(--ac) 45%,transparent);outline-offset:1px;border-color:var(--ac)}
.bar{height:4px}.bar>i,#readbar i,#readbar2{background:var(--ac)}
#topbar{background:color-mix(in srgb,var(--bg) 88%,transparent)}
/* surfaces: flat soft-gray cards, no shadows */
.card,.svgw,details,.pg,.obj>div,.cheat>div,.qdash a,.lnav a,.ba>div{background:var(--soft);border-color:var(--bd);box-shadow:none}
.card{border-radius:var(--r)}
.lesson{background:var(--bg);border-color:var(--bd);border-radius:16px;box-shadow:none}
.lesson.quizblock{background:var(--bg)}
.svgw{border-radius:var(--r)}
details{border-radius:12px}
summary{color:var(--tx)}summary:hover{color:var(--ac)}
.box{border-radius:0 10px 10px 0}
.tldr{background:var(--acS);border:1px solid var(--bd);border-radius:12px}
.tldr>.nut{color:var(--ac);background:var(--bg)}
.glance{background:var(--soft);border-color:var(--bd)}
.g2,.gchips span,.rtl{background:var(--bg)}
.q{background:var(--soft)}
.q .opt{background:var(--bg)}
.recall{background:var(--soft)}
/* tags = pastel pills */
.tag{background:var(--acS);color:var(--ac)}
/* buttons: quiet pills; primary = text-colour pill (like the reference tabs) */
.btn{background:var(--tx);border-color:var(--tx);color:var(--bg);border-radius:999px;font-family:var(--font-ui)}
.btn:hover{background:color-mix(in srgb,var(--tx) 85%,var(--bg));border-color:color-mix(in srgb,var(--tx) 85%,var(--bg))}
.btn.o,.btn.ghost,.btn.sec,button.sec{background:transparent;color:var(--tx);border-color:var(--bd)}
.btn.o:hover,.btn.ghost:hover,.btn.sec:hover,button.sec:hover{border-color:var(--tx);background:transparent}
.tabs button{background:var(--soft);border-color:var(--bd);color:var(--tx)}
.tabs button.on{background:var(--tx);color:var(--bg);border-color:var(--tx)}
/* code */
pre{background:var(--codeBg);color:var(--codeTx);border-color:var(--bd);border-radius:12px;font:13.5px/1.6 var(--font-mono)}
code,.prompt,.outbox,.trace{font-family:var(--font-mono)}
:not(pre)>code{background:var(--soft2);color:inherit;border-radius:5px;padding:1px 6px;font-size:.9em}
.k{color:var(--kw)}.s{color:var(--str)}.f{color:var(--fn)}
[data-theme=dark] .k{color:var(--kw)}[data-theme=dark] .s{color:var(--str)}
mark.hl{background:color-mix(in srgb,var(--warn) 30%,transparent);color:inherit}
/* tables */
th{font-size:13px;color:var(--mut);border-bottom:1px solid var(--bd)}
td{border-color:var(--bd)}
tbody tr:hover td{background:var(--soft)}
/* old hard-coded yellow boxes (v10/v11) -> pastel orange, both modes */
.onq{background:var(--warnS);border:1px solid color-mix(in srgb,var(--warn) 30%,transparent);border-left:4px solid var(--warn)}
.onq .t,.onq .qsrc{color:var(--warn)}.onq .qsrc{background:color-mix(in srgb,var(--warn) 16%,transparent)}
.qfocus{background:var(--warnS);border-color:color-mix(in srgb,var(--warn) 30%,transparent)}
[data-theme="dark"] .onq,[data-theme="dark"] .qfocus{background:var(--warnS);border-color:color-mix(in srgb,var(--warn) 35%,transparent)}
[data-theme="dark"] .onq .t,[data-theme="dark"] .onq .qsrc{color:var(--warn)}
[data-theme="dark"] .onq .qsrc{background:color-mix(in srgb,var(--warn) 18%,transparent)}
.ba .bad{border-top-color:var(--bad)}
/* Persian text */
.prs,.rtl{font-family:var(--font-fa)}
/* diagrams: white/graphite nodes on a soft-gray panel */
svg text{font-family:var(--font-ui);fill:var(--tx)}
svg .n{fill:var(--bg);stroke:var(--ac)}
svg .ln{stroke:var(--mut)}
#ar path,marker path{fill:var(--mut)}
svg [stroke="#8a93a8"]{stroke:var(--mut)}
/* theme switch + top bar buttons */
#v13th{background:transparent;border:1px solid var(--bd);color:var(--tx);border-radius:999px;padding:4px 12px;cursor:pointer;font:600 12.5px var(--font-ui)}
#v13th:hover{border-color:var(--tx)}
#topbar button{border-radius:999px;background:var(--bg);border-color:var(--bd);padding:4px 11px;color:var(--tx)}
#topbar button:hover{border-color:var(--tx)}
#topbar button.on{background:var(--tx);border-color:var(--tx);color:var(--bg)}
.score{background:var(--tx);color:var(--bg)}
*{scrollbar-color:var(--soft2) transparent}
'''
FONT = '<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&amp;display=swap" rel="stylesheet"/>'
META = ('<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)"/>'
        '<meta name="theme-color" content="#191919" media="(prefers-color-scheme: dark)"/>')
def build(s):
    block = '<style id="v14-theme">\n' + CSS + '</style>'
    pat = re.compile(r'<style id="v1[34]-theme">.*?</style>', re.S)
    if pat.search(s): s = pat.sub(lambda m: block, s, count=1)
    else: s = s.replace('</head>', block + '</head>', 1)
    s = re.sub(r'<link href="https://fonts.googleapis.com/css2\?[^"]*" rel="stylesheet"/?>', lambda m: FONT, s, count=1)
    if 'fonts.googleapis.com/css2' not in s: s = s.replace('</head>', FONT + '</head>', 1)
    s = re.sub(r'<meta name="theme-color"[^>]*>', '', s)
    s = s.replace('</head>', META + '</head>', 1)
    return s
if __name__ == '__main__':
    src = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else src
    s = build(open(src, encoding='utf-8').read())
    open(out, 'w', encoding='utf-8').write(s); print('v14 theme ->', out)
