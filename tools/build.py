#!/usr/bin/env python3
"""Generate the language versions of plumbline.nl from tools/template.html.

Run from the repository root:  python3 tools/build.py
Edit copy in the LANGS dict below; the wordmark, layout and tag live in the template.
"""
import html, json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "tools" / "template.html").read_text()

LANGS = {
  "en": dict(
    path="", hreflang="en", og_locale="en_GB", nav="EN",
    title="Plumbline · AI and Agentic transition advisory",
    description="Plumbline is a boutique advisory firm working with executives and technology leaders on AI and Agentic transitions within their organizations.",
    og_description="A boutique advisory firm working with executives and technology leaders on AI and Agentic transitions within their organizations.",
    knows_about=["AI adoption", "Agentic AI", "AI transition", "AI strategy", "Organizational readiness"],
    h1="Enabling AI transitions.",
    intro="Plumbline is a boutique advisory firm working with executives and technology leaders on <strong>AI and Agentic transitions</strong> within their organizations. We help you set the AI strategy, test whether the organization is ready, and turn pilots into everyday practice.",
    s1_h="Direction", s1_p="Where (Agentic) AI belongs in your business and where it does not, judged against your own needs and ambitions.",
    s2_h="Readiness", s2_p="The data, processes, and skills that determine whether a promising generative or agentic AI pilot ever survives contact with production.",
    s3_h="Adoption",  s3_p="The vision, strategy, best practices, and tools that will make your Agentic AI transition succeed.",
    faq_label="Questions we get asked",
    faq=[
      ("What is an &ldquo;agentic transition&rdquo;?",
       "The shift from AI as a tool individuals use to AI agents that carry out parts of the organization&rsquo;s own processes. It changes how work is divided, checked and owned, which is why it is an organizational transition and not only a technical one."),
      ("Is this AI strategy or AI implementation?",
       "Strategy first, then the organizational work that makes implementation possible. Plumbline helps you decide, prepare, and adopt."),
      ("What does an AI readiness assessment cover?",
       "Data, processes, skills and governance: the four things that decide whether a generative or agentic AI pilot solution will deliver on its promises. The result is a plain account of where the organization stands and what has to change."),
      ("Who is the typical client?",
       "Executives, boards, and CTOs of mid-sized and large organizations in the Netherlands and the wider EU that have run AI experiments and want the next step to hold."),
      ("Who is Plumbline?",
       "Plumbline is a boutique advisory firm run by senior academics with years of technical experience in AI, generative AI and agentic AI, and with the methods and insights needed to strategize and plan your AI transition."),
    ],
    country="The Netherlands",
    consent_aria="Cookie notice",
    consent_text="This site uses Google Analytics to count visits. Nothing is stored unless you accept.",
    decline="Decline", accept="Accept",
    nav_aria="English version",
  ),
  "nl": dict(
    path="nl/", hreflang="nl", og_locale="nl_NL", nav="NL",
    title="Plumbline · Advies bij AI- en agentic transities",
    description="Plumbline is een boutique adviesbureau dat bestuurders en technologieleiders begeleidt bij AI- en agentic transities binnen hun organisatie.",
    og_description="Een boutique adviesbureau dat bestuurders en technologieleiders begeleidt bij AI- en agentic transities binnen hun organisatie.",
    knows_about=["AI-adoptie", "Agentic AI", "AI-transitie", "AI-strategie", "Organisatiegereedheid"],
    h1="AI-transities mogelijk maken.",
    intro="Plumbline is een boutique adviesbureau dat bestuurders en technologieleiders begeleidt bij <strong>AI- en agentic transities</strong> binnen hun organisatie. Wij helpen u de AI-strategie te bepalen, te toetsen of de organisatie er klaar voor is, en pilots om te zetten in dagelijkse praktijk.",
    s1_h="Richting",   s1_p="Waar (agentic) AI thuishoort in uw bedrijf en waar niet, beoordeeld aan de hand van uw eigen behoeften en ambities.",
    s2_h="Gereedheid", s2_p="De data, processen en vaardigheden die bepalen of een veelbelovende generatieve of agentic AI-pilot de stap naar productie overleeft.",
    s3_h="Adoptie",    s3_p="De visie, strategie, best practices en tools die uw agentic AI-transitie laten slagen.",
    faq_label="Veelgestelde vragen",
    faq=[
      ("Wat is een &lsquo;agentic transitie&rsquo;?",
       "De verschuiving van AI als hulpmiddel voor individuen naar AI-agents die delen van de processen van de organisatie zelf uitvoeren. Dat verandert hoe werk wordt verdeeld, gecontroleerd en toegewezen, en daarom is het een organisatorische transitie en niet alleen een technische."),
      ("Gaat dit over AI-strategie of over AI-implementatie?",
       "Eerst de strategie, daarna het organisatorische werk dat implementatie mogelijk maakt. Plumbline helpt u beslissen, voorbereiden en adopteren."),
      ("Wat omvat een AI-readiness assessment?",
       "Data, processen, vaardigheden en governance: de vier zaken die bepalen of een generatieve of agentic AI-pilot waarmaakt wat ervan verwacht wordt. Het resultaat is een helder beeld van waar de organisatie staat en wat er moet veranderen."),
      ("Wie is de typische opdrachtgever?",
       "Bestuurders, raden van bestuur en CTO&rsquo;s van middelgrote en grote organisaties in Nederland en de bredere EU die met AI ge&euml;xperimenteerd hebben en willen dat de volgende stap standhoudt."),
      ("Wie is Plumbline?",
       "Plumbline is een boutique adviesbureau, gerund door senior academici met jarenlange technische ervaring met AI, generatieve AI en agentic AI, en met de methoden en inzichten die nodig zijn om uw AI-transitie te doordenken en te plannen."),
    ],
    country="Nederland",
    consent_aria="Cookiemelding",
    consent_text="Deze site gebruikt Google Analytics om bezoeken te tellen. Er wordt niets opgeslagen tenzij u akkoord gaat.",
    decline="Weigeren", accept="Akkoord",
    nav_aria="Nederlandse versie",
  ),
  "it": dict(
    path="it/", hreflang="it", og_locale="it_IT", nav="IT",
    title="Plumbline · Consulenza per transizioni AI e agentiche",
    description="Plumbline è una boutique di consulenza che affianca dirigenti e leader tecnologici nelle transizioni verso l'AI e l'AI agentica all'interno delle loro organizzazioni.",
    og_description="Una boutique di consulenza che affianca dirigenti e leader tecnologici nelle transizioni verso l'AI e l'AI agentica all'interno delle loro organizzazioni.",
    knows_about=["Adozione dell'AI", "AI agentica", "Transizione AI", "Strategia AI", "Prontezza organizzativa"],
    h1="Rendere possibili le transizioni AI.",
    intro="Plumbline è una boutique di consulenza che affianca dirigenti e leader tecnologici nelle <strong>transizioni verso l&rsquo;AI e l&rsquo;AI agentica</strong> all&rsquo;interno delle loro organizzazioni. Vi aiutiamo a definire la strategia AI, a verificare se l&rsquo;organizzazione è pronta e a trasformare i progetti pilota in pratica quotidiana.",
    s1_h="Direzione", s1_p="Dove l&rsquo;AI (agentica) ha senso nella vostra azienda e dove no, valutato in base alle vostre esigenze e ambizioni.",
    s2_h="Prontezza", s2_p="I dati, i processi e le competenze che determinano se un promettente progetto pilota di AI generativa o agentica sopravviverà all&rsquo;impatto con la produzione.",
    s3_h="Adozione",  s3_p="La visione, la strategia, le buone pratiche e gli strumenti che faranno riuscire la vostra transizione verso l&rsquo;AI agentica.",
    faq_label="Domande frequenti",
    faq=[
      ("Che cos&rsquo;è una &laquo;transizione agentica&raquo;?",
       "Il passaggio dall&rsquo;AI come strumento usato dai singoli ad agenti AI che eseguono parti dei processi dell&rsquo;organizzazione stessa. Cambia il modo in cui il lavoro viene suddiviso, controllato e attribuito: per questo è una transizione organizzativa e non solo tecnica."),
      ("Si tratta di strategia AI o di implementazione AI?",
       "Prima la strategia, poi il lavoro organizzativo che rende possibile l&rsquo;implementazione. Plumbline vi aiuta a decidere, prepararvi e adottare."),
      ("Che cosa comprende un AI readiness assessment?",
       "Dati, processi, competenze e governance: i quattro fattori che decidono se una soluzione pilota di AI generativa o agentica manterrà le promesse. Il risultato è un quadro chiaro di dove si trova l&rsquo;organizzazione e di che cosa deve cambiare."),
      ("Chi è il cliente tipico?",
       "Dirigenti, consigli di amministrazione e CTO di organizzazioni medie e grandi nei Paesi Bassi e nel resto dell&rsquo;UE che hanno sperimentato con l&rsquo;AI e vogliono che il passo successivo regga."),
      ("Chi è Plumbline?",
       "Plumbline è una boutique di consulenza guidata da accademici senior con anni di esperienza tecnica in AI, AI generativa e AI agentica, e con i metodi e le conoscenze necessari per impostare e pianificare la vostra transizione AI."),
    ],
    country="Paesi Bassi",
    consent_aria="Avviso sui cookie",
    consent_text="Questo sito usa Google Analytics per contare le visite. Nulla viene memorizzato senza il vostro consenso.",
    decline="Rifiuta", accept="Accetta",
    nav_aria="Versione italiana",
  ),
  "zh": dict(
    path="zh/", hreflang="zh-Hans", og_locale="zh_CN", nav="中文", html_lang="zh-Hans",
    title="Plumbline · AI 与智能体转型咨询",
    description="Plumbline 是一家精品咨询公司，协助高管与技术负责人推进组织内的 AI 与智能体（Agentic AI）转型。",
    og_description="一家精品咨询公司，协助高管与技术负责人推进组织内的 AI 与智能体（Agentic AI）转型。",
    knows_about=["AI 采纳", "智能体 AI", "AI 转型", "AI 战略", "组织就绪度"],
    h1="让 AI 转型成为可能。",
    intro="Plumbline 是一家精品咨询公司，协助高管与技术负责人推进组织内的<strong>AI 与智能体转型</strong>。我们帮助您制定 AI 战略，检验组织是否准备就绪，并把试点项目转化为日常实践。",
    s1_h="方向", s1_p="（智能体）AI 在您的业务中适用于何处、不适用于何处，依据您自身的需求与抱负来判断。",
    s2_h="就绪", s2_p="决定一个有前景的生成式或智能体 AI 试点能否经受住生产环境考验的数据、流程与技能。",
    s3_h="采纳", s3_p="让您的智能体 AI 转型取得成功所需的愿景、战略、最佳实践与工具。",
    faq_label="常见问题",
    faq=[
      ("什么是“智能体转型”？",
       "从个人使用的 AI 工具，转向由 AI 智能体执行组织自身部分流程的转变。它改变了工作如何分配、核查与归责，因此这是一场组织转型，而不仅仅是技术转型。"),
      ("这是 AI 战略还是 AI 实施？",
       "先有战略，再做使实施成为可能的组织工作。Plumbline 帮助您决策、准备与采纳。"),
      ("AI 就绪评估涵盖哪些内容？",
       "数据、流程、技能与治理：这四项决定了一个生成式或智能体 AI 试点方案能否兑现承诺。评估结果是对组织现状以及需要改变之处的清晰说明。"),
      ("典型客户是谁？",
       "荷兰及欧盟范围内中大型组织的高管、董事会与 CTO：他们已开展过 AI 实验，并希望下一步能够站得住脚。"),
      ("Plumbline 是谁？",
       "Plumbline 是一家由资深学者运营的精品咨询公司，拥有多年 AI、生成式 AI 与智能体 AI 的技术经验，以及规划您的 AI 转型所需的方法与洞见。"),
    ],
    country="荷兰",
    consent_aria="Cookie 提示",
    consent_text="本网站使用 Google Analytics 统计访问量。除非您同意，否则不会存储任何数据。",
    decline="拒绝", accept="同意",
    nav_aria="中文版",
    extra_head='  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600&family=Noto+Sans+SC:wght@400;500&display=swap">\n'
               '  <style>:root{--serif:Spectral,"Noto Serif SC",Georgia,serif;--sans:"Instrument Sans","Noto Sans SC",system-ui,sans-serif} h1,h2,.faq dt{letter-spacing:0} .hero h1{line-height:1.25}</style>\n',
  ),
}

ORDER = ["en", "nl", "it", "zh"]

def plain(t):
    return html.unescape(re.sub(r"<[^>]+>", "", t))

def hreflangs():
    lines = [f'  <link rel="alternate" hreflang="{LANGS[k]["hreflang"]}" href="https://plumbline.nl/{LANGS[k]["path"]}">' for k in ORDER]
    lines.append('  <link rel="alternate" hreflang="x-default" href="https://plumbline.nl/">')
    return "\n".join(lines)

def lang_nav(current):
    items = []
    for k in ORDER:
        L = LANGS[k]
        if k == current:
            items.append(f'        <span class="current" aria-current="page">{L["nav"]}</span>')
        else:
            items.append(f'        <a href="/{L["path"]}" lang="{L.get("html_lang", L["hreflang"])}" hreflang="{L["hreflang"]}" aria-label="{L["nav_aria"]}">{L["nav"]}</a>')
    return '      <nav class="lang" aria-label="Language">\n' + "\n".join(items) + "\n      </nav>\n"

def faq_dl(faq):
    return "\n".join(f"        <dt>{q}</dt>\n        <dd>{a}</dd>" for q, a in faq)

def faq_ld(lang, faq):
    ld = {"@context": "https://schema.org", "@type": "FAQPage"}
    if lang != "en":
        ld["inLanguage"] = LANGS[lang]["hreflang"]
    ld["mainEntity"] = [{"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faq]
    return '  <script type="application/ld+json">\n  ' + json.dumps(ld, ensure_ascii=False, indent=2).replace("\n", "\n  ") + "\n  </script>\n"

for k in ORDER:
    L = LANGS[k]
    vals = dict(L)
    vals.update(
        lang=L.get("html_lang", L["hreflang"]),
        h1_plain=plain(L["h1"]),
        hreflangs=hreflangs(),
        lang_nav=lang_nav(k),
        faq_dl=faq_dl(L["faq"]),
        faq_ld=faq_ld(k, L["faq"]),
        knows_about=json.dumps(L["knows_about"], ensure_ascii=False),
        extra_head=L.get("extra_head", ""),
    )
    out = TEMPLATE
    for key, val in vals.items():
        if isinstance(val, str):
            out = out.replace("{{" + key + "}}", val)
    leftover = re.findall(r"\{\{(\w+)\}\}", out)
    assert not leftover, (k, leftover)
    dest = ROOT / L["path"] / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out)
    print("wrote", dest.relative_to(ROOT))

# sitemap
today = "2026-09-27"
urls = []
alts = "\n".join(f'    <xhtml:link rel="alternate" hreflang="{LANGS[k]["hreflang"]}" href="https://plumbline.nl/{LANGS[k]["path"]}"/>' for k in ORDER)
alts += '\n    <xhtml:link rel="alternate" hreflang="x-default" href="https://plumbline.nl/"/>'
for k in ORDER:
    L = LANGS[k]
    urls.append(f'''  <url>
    <loc>https://plumbline.nl/{L["path"]}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{"1.0" if k == "en" else "0.9"}</priority>
{alts}
  </url>''')
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
print("wrote sitemap.xml")
