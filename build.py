"""Builds the harspec documentation site (plain HTML, no dependencies).
Edit the PAGES list below, then run:  python build.py   (needs Python 3.12+)
"""
import html
import os

GH = "https://github.com/AYUSH-PANDEY023/harspec"
SITE = "https://AYUSH-PANDEY023.github.io/harspec-docs/"
ROOT = os.path.dirname(os.path.abspath(__file__))


def c(text):
    return '<pre><code>' + html.escape(text.strip("\n")) + '</code></pre>'


def table(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    r = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in row) + "</tr>" for row in rows)
    return f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def note(kind, text):
    return f'<div class="note {kind}"><b>{ {"warn": "Important", "tip": "Tip"}[kind] }:</b> {text}</div>'


PAGES = []


def page(slug, title, desc, body):
    PAGES.append((slug, title, desc, body))


# ---------------------------------------------------------------- Home
page("index", "Home", "harspec turns a browser HAR capture into an OpenAPI spec and typed API clients. Free, open source, zero dependencies.", f"""
<section class="hero">
<p class="eyebrow">Open source · MIT · Python 3.9+</p>
<h1>Undocumented API?<br>Get the docs in 30 seconds.</h1>
<p class="lead">harspec reads a <b>HAR file</b> (the network recording from your browser) and writes an <b>OpenAPI spec</b>, <b>TypeScript and Python clients</b>, <b>curl examples</b>, a <b>Postman collection</b> and an <b>auth summary</b>. No dependencies. Nothing leaves your machine.</p>
<div class="cta"><a class="btn" href="getting-started.html">Get started</a><a class="btn ghost" href="{GH}">View on GitHub</a></div>
{c("pip install harspec\nharspec capture.har")}
</section>
<h2>What you get</h2>
<div class="cards">
<div class="card"><h3>OpenAPI spec</h3><p>Paths, parameters, request and response schemas for every status code, examples and security schemes.</p></div>
<div class="card"><h3>Typed clients</h3><p>A TypeScript <code>fetch</code> client and a Python <code>requests</code> client with a method per endpoint.</p></div>
<div class="card"><h3>Ready to test</h3><p>Runnable curl commands and a Postman collection, grouped by resource.</p></div>
<div class="card"><h3>Auth explained</h3><p>Bearer, Basic, API key and cookie auth, plus the login endpoint and CSRF headers.</p></div>
<div class="card"><h3>Safe by default</h3><p>Tokens, cookies, passwords and JWTs are redacted while the file is read.</p></div>
<div class="card"><h3>Extensible</h3><p>Add a generator for any language in about 15 lines. Plugins install with pip.</p></div>
</div>
<h2>How it works in 3 steps</h2>
<ol class="steps">
<li><b>Record.</b> Open the site, press F12, use the app, then save the Network tab as a HAR file.</li>
<li><b>Run.</b> <code>harspec capture.har</code></li>
<li><b>Use.</b> Open <code>harspec-out/</code>: import the spec, copy a client, run the curl examples.</li>
</ol>
{note("warn", "A HAR file contains your live session (tokens and cookies). Record on a test account, never share the .har itself, and only analyse services you are allowed to use.")}
""")

# ---------------------------------------------------------------- Getting started
page("getting-started", "Getting started", "Install harspec, record a HAR file in your browser, generate an OpenAPI spec and clients.", f"""
<h1>Getting started</h1>
<p class="lead">From zero to a generated client in five minutes. You only need Python 3.9 or newer.</p>
<h2>1. Install</h2>
{c("pip install harspec")}
<p>Check it worked: <code>harspec --version</code>. If the command is not found, use <code>python -m harspec</code> instead.</p>
<h2>2. Record a HAR file</h2>
<p>A HAR file is a recording of every request the page made. All major browsers can export one.</p>
{table(["Browser", "How"], [
 ["Chrome / Edge", "F12, <b>Network</b> tab, tick <b>Preserve log</b>, use the site, right click a request, <b>Save all as HAR with content</b>."],
 ["Firefox", "F12, <b>Network</b> tab, use the site, click the gear icon, <b>Save All As HAR</b>."],
 ["Safari", "Develop menu, <b>Show Web Inspector</b>, <b>Network</b> tab, use the site, <b>Export</b>."],
])}
<p>Tips for a good capture: log in, open the main screens, search, create and delete something. Every action you do adds endpoints to the spec. Use the <b>Fetch/XHR</b> filter if the list is noisy (harspec also filters automatically).</p>
{note("warn", "The HAR contains live credentials. Use a test account, delete the file when done, and never commit it. harspec redacts secrets in its output, not in your original file.")}
<p><b>Mobile apps?</b> Route the phone through a proxy such as mitmproxy or Charles and export the session as HAR, then use harspec the same way.</p>
<h2>3. Run harspec</h2>
{c("harspec capture.har")}
<p>You will see a summary like this:</p>
{c("harspec 0.1.0: 14 requests -> 11 API calls on api.petshop.example\n  6 endpoints across 4 paths\n  auth: bearerAuth, cookieAuth (login: POST /v1/auth/login)\n  wrote to harspec-out/: openapi.yaml, AUTH.md, examples.sh, ...")}
<p>If the capture has several hosts (for example an API plus analytics), harspec picks the busiest and tells you the others. Choose one with <code>--host api.example.com</code>.</p>
<h2>4. Use the output</h2>
{table(["File", "What to do with it"], [
 ["<code>openapi.yaml</code>", "Open in Swagger Editor (editor.swagger.io), import into Postman or Insomnia, or feed to any OpenAPI tool."],
 ["<code>client.ts</code>", "Copy into your TypeScript project. Works with any runtime that has <code>fetch</code> (browsers, Node 18+, Deno, Bun)."],
 ["<code>client.py</code>", "Copy into your Python project. Needs <code>pip install requests</code>."],
 ["<code>examples.sh</code>", "Set <code>TOKEN</code> and run any command to try an endpoint."],
 ["<code>postman_collection.json</code>", "Postman: Import, then set the <code>token</code> variable."],
 ["<code>AUTH.md</code>", "Read first: it explains how to obtain a token."],
])}
<h3>Python client</h3>
{c('from client import Client\n\napi = Client(token="YOUR_TOKEN")\npets = api.get_pets(params={"limit": 10})\npet = api.get_pet(42)')}
<h3>TypeScript client</h3>
{c('import { Client } from "./client";\n\nconst api = new Client({ token: "YOUR_TOKEN" });\nconst pets = await api.getPets({ limit: 10 });')}
<p>Errors throw <code>ApiError</code> with the HTTP <code>status</code> and parsed <code>body</code>.</p>
<h2>Try it without a HAR</h2>
<p>The repository ships a sample capture of a fake pet shop API:</p>
{c("git clone " + GH + ".git\ncd harspec\npython -m harspec examples/sample.har")}
""")

# ---------------------------------------------------------------- How it works
page("how-it-works", "How it works", "The harspec pipeline: parse, redact, group endpoints, infer schemas, detect auth, generate.", f"""
<h1>How it works</h1>
<p class="lead">harspec is a small pipeline. Each stage is a short Python module you can read in a few minutes.</p>
{table(["Stage", "Module", "What happens"], [
 ["1. Parse and filter", "<code>har.py</code>", "Reads <code>log.entries</code>, decodes bodies, drops html, js, css, images, fonts, failed requests and CORS preflights."],
 ["2. Redact", "<code>redact.py</code>", "Removes secrets immediately, before the data goes anywhere else."],
 ["3. Group endpoints", "<code>paths.py</code>", "Turns concrete URLs into templates with path parameters."],
 ["4. Infer schemas", "<code>schema.py</code>", "Builds a JSON schema per sample and merges them."],
 ["5. Detect auth", "<code>auth.py</code>", "Finds credential types, login endpoints and CSRF headers."],
 ["6. Build the spec", "<code>openapi.py</code>", "Assembles OpenAPI 3.0.3 with operations, parameters, bodies, responses, security."],
 ["7. Generate", "<code>generators/</code>", "Each output format is produced <b>from the spec</b>, not from raw traffic."],
])}
<h2>Path parameters</h2>
<p>These segments become parameters: numbers, UUIDs, long hex strings, dates, and long mixed alphanumeric IDs. The parameter is named after the previous word.</p>
{c("/users/42/posts/7        ->  /users/{user_id}/posts/{post_id}\n/owners/3f2a-...-9c1/pets ->  /owners/{owner_id}/pets\n/v1/pets                 ->  /v1/pets          (v1 stays literal)")}
<p>Short mixed IDs such as <code>sku123</code> are detected by clustering: if three or more different values share the same surrounding path, harspec treats that position as a parameter. Turn this off with <code>--no-cluster</code>.</p>
<h2>Schema inference</h2>
{table(["Seen in the capture", "Result"], [
 ["Field in every sample", "<code>required</code>"],
 ["Field missing in some samples", "optional"],
 ["<code>null</code> in some samples", "<code>nullable: true</code>"],
 ["Integer in one sample, decimal in another", "<code>number</code>"],
 ["String in one, number in another", "<code>oneOf</code>"],
 ["UUID, date-time, date, email, URL strings", "<code>format</code> set accordingly"],
 ["Same path, several status codes", "one response per status"],
 ["Query parameter in every call", "required; otherwise optional"],
])}
<p>Query values arrive as text, so <code>limit=10</code> is typed <code>integer</code>. Repeated keys become arrays.</p>
<h2>Auth detection</h2>
<p>harspec looks at request headers and cookies (values already redacted) and responses of login-like endpoints:</p>
{table(["Signal", "Detected as"], [
 ["<code>Authorization: Bearer ...</code>", "<code>bearerAuth</code> (HTTP bearer)"],
 ["<code>Authorization: Basic ...</code>", "<code>basicAuth</code>"],
 ["<code>X-API-Key</code>, <code>X-Auth-Token</code> and similar", "API key in header"],
 ["Cookie named like session, sid, auth, jwt", "<code>cookieAuth</code>"],
 ["2xx JSON response on a login, token or oauth path containing a token field", "login endpoint, listed in <code>AUTH.md</code>"],
 ["<code>X-CSRF-Token</code> and similar", "CSRF header, listed in <code>AUTH.md</code>"],
])}
<p>When a request sends both a token and a session cookie, the operation is marked with the token scheme only.</p>
<h2>Why generators read the spec</h2>
<p>Because every generator takes the OpenAPI dictionary, a generator never needs to understand HAR files, redaction or inference. It just walks <code>paths</code>. That keeps each generator around 60 lines and makes new ones easy to write.</p>
""")

# ---------------------------------------------------------------- Reference
page("reference", "Reference", "Command line options, output files and the OpenAPI extensions harspec writes.", f"""
<h1>Reference</h1>
<h2>Command line</h2>
{c("harspec HAR_FILE [options]")}
{table(["Option", "Default", "Meaning"], [
 ["<code>-o, --out DIR</code>", "<code>harspec-out</code>", "Output directory (created if missing)."],
 ["<code>-f, --formats LIST</code>", "all", "Comma list of generators, e.g. <code>typescript,python</code>."],
 ["<code>--host HOST</code>", "busiest host", "Only use requests to this host."],
 ["<code>--title TEXT</code>", "host name", "Title in the OpenAPI <code>info</code> block."],
 ["<code>--json</code>", "off", "Write <code>openapi.json</code> instead of <code>openapi.yaml</code>."],
 ["<code>--no-cluster</code>", "off", "Do not detect mixed alphanumeric IDs."],
 ["<code>--include-static</code>", "off", "Keep html, js, css and image requests."],
 ["<code>--list-generators</code>", "", "List built-in and plugin generators, then exit."],
 ["<code>--version</code>", "", "Print the version."],
])}
<p><b>Exit codes:</b> <code>0</code> success, <code>1</code> unreadable or invalid HAR, or no API traffic found, <code>2</code> bad arguments.</p>
<h2>Output files</h2>
{table(["File", "Generator", "Notes"], [
 ["<code>openapi.yaml</code> / <code>.json</code>", "built in", "OpenAPI 3.0.3. Always written."],
 ["<code>AUTH.md</code>", "built in", "Always written."],
 ["<code>client.ts</code>", "<code>typescript</code>", "No runtime dependencies. Passes <code>tsc --strict</code>."],
 ["<code>client.py</code>", "<code>python</code>", "Needs <code>requests</code>."],
 ["<code>examples.sh</code>", "<code>curl</code>", "Uses <code>$TOKEN</code> and <code>$BASE</code>."],
 ["<code>postman_collection.json</code>", "<code>postman</code>", "Collection v2.1 with <code>baseUrl</code> and <code>token</code> variables."],
])}
<h2>Operation naming</h2>
<p>Operation IDs come from the method and path: <code>GET /users/{{user_id}}/posts</code> becomes <code>getUserPosts</code>. Collections keep the plural (<code>getPets</code>), items use the singular (<code>getPet</code>). Duplicates get a numeric suffix. Python methods are the snake_case form (<code>get_user_posts</code>).</p>
<h2>OpenAPI extensions</h2>
{table(["Field", "Meaning"], [
 ["<code>x-harspec-samples</code>", "Number of captured requests behind the operation. Low numbers mean low confidence."],
])}
<h2>Using the spec with other tools</h2>
{table(["Tool", "How"], [
 ["Swagger Editor / Swagger UI", "Paste or upload <code>openapi.yaml</code>."],
 ["Postman, Insomnia, Bruno", "Import the OpenAPI file or the Postman collection."],
 ["openapi-generator", "<code>openapi-generator-cli generate -i openapi.yaml -g go -o ./client</code> for languages harspec does not cover yet."],
 ["Mock servers (Prism)", "<code>prism mock openapi.yaml</code>"],
])}
""")

# ---------------------------------------------------------------- Generators
page("generators", "Write a generator", "Add your own output format to harspec in about 15 lines, and ship it as a pip-installable plugin.", f"""
<h1>Write a generator</h1>
<p class="lead">A generator is a Python function that receives the OpenAPI spec (a dict) and returns <code>{{filename: content}}</code>.</p>
<h2>Minimal example</h2>
{c('''from harspec.generators import register

@register("routes", "List of METHOD /path lines")
def routes(spec):
    lines = []
    for path, item in spec["paths"].items():
        for method in item:
            lines.append(f"{method.upper()} {path}")
    return {"routes.txt": "\\n".join(lines)}''')}
<p>Run <code>harspec capture.har -f routes</code> and you get <code>routes.txt</code>.</p>
<h2>Helpers</h2>
<p>Import from <code>harspec.generators.base</code>:</p>
{table(["Helper", "Returns"], [
 ["<code>iter_ops(spec)</code>", "Yields <code>(path, METHOD, operation)</code> for every endpoint."],
 ["<code>base_url(spec)</code>", "The server URL."],
 ["<code>params_of(op, \"path\" | \"query\")</code>", "Parameter objects with <code>name</code>, <code>required</code>, <code>schema</code>, <code>example</code>."],
 ["<code>body_of(op)</code>", "<code>(mime, schema, example)</code> or <code>None</code>."],
 ["<code>success_schema(op)</code>", "Schema of the first 2xx JSON response, or <code>None</code>."],
 ["<code>auth_style(spec)</code>", "<code>(header_name, \"Bearer {{}}\")</code> style tuple, or <code>None</code>."],
 ["<code>snake(name)</code>", "<code>getUserPosts</code> to <code>get_user_posts</code>."],
])}
<h2>Add it to harspec itself</h2>
<ol class="steps">
<li>Create <code>harspec/generators/yourname.py</code> with the decorator above.</li>
<li>Add <code>yourname</code> to the import line in <code>load_all()</code>.</li>
<li>Write a test that generates from <code>examples/sample.har</code> and checks the output.</li>
<li>Open a pull request.</li>
</ol>
<h2>Ship it as a plugin package</h2>
<p>You do not need to touch harspec. Publish your own package that registers through an entry point:</p>
{c('''# pyproject.toml of your plugin
[project]
name = "harspec-go"
dependencies = ["harspec"]

[project.entry-points."harspec.generators"]
go = "harspec_go.generator"''')}
<p>After <code>pip install harspec-go</code>, the generator shows up in <code>harspec --list-generators</code> and works with <code>-f go</code>.</p>
<h2>Ideas wanted</h2>
<p>Go, Rust, Kotlin, Swift, Dart, Java, C#, PHP and Ruby clients. Bruno and Insomnia collections. k6 load tests. Playwright API tests. WireMock and MSW mock servers. Zod and Pydantic models. Markdown API docs.</p>
""")

# ---------------------------------------------------------------- Security
page("security", "Privacy and security", "How harspec redacts secrets, what it never does, and how to use it responsibly.", f"""
<h1>Privacy and security</h1>
<h2>Everything stays local</h2>
<p>harspec makes <b>no network requests</b> and has no telemetry. It reads your HAR file and writes files to your output folder.</p>
<h2>Redaction</h2>
<p>Redaction runs while the HAR is parsed, before inference or generation. A secret cannot reach the spec, an example or a client.</p>
{table(["Where", "What happens"], [
 ["<code>Authorization</code> header", "Scheme kept (<code>Bearer</code>), value replaced by <code>&lt;redacted&gt;</code>."],
 ["<code>Cookie</code>, <code>Set-Cookie</code>", "Cookie names kept, values redacted."],
 ["API key and CSRF headers", "Value redacted."],
 ["JSON, form and query fields named like password, token, secret, api_key, session, csrf, card, otp, jwt", "Value redacted."],
 ["Any string containing a JWT", "JWT replaced by <code>&lt;jwt&gt;</code>."],
])}
<p>The test suite greps every output file for the secrets in the sample HAR and fails if any appear.</p>
{note("warn", "Redaction is pattern based. Business data in example values (names, emails, IDs) is kept. Skim the output before you publish it anywhere.")}
<h2>Your HAR file is the sensitive part</h2>
<ul>
<li>Record on a test account when possible.</li>
<li>Do not email, upload or commit the <code>.har</code>. Add <code>*.har</code> to <code>.gitignore</code>.</li>
<li>Delete it when finished, and rotate any real credentials that were in it.</li>
</ul>
<h2>Use it responsibly</h2>
<p>Only analyse traffic you are allowed to capture, and only call APIs you are allowed to use. Check the terms of service. harspec describes what a client already sends; it does not bypass authentication.</p>
<h2>Report a vulnerability</h2>
<p>Use GitHub private reporting (Security tab) on the <a href="{GH}/security">repository</a>. Do not open a public issue for security problems.</p>
""")

# ---------------------------------------------------------------- FAQ
page("faq", "FAQ", "Answers to common questions about harspec, HAR files and generated specs.", f"""
<h1>FAQ</h1>
<h3>What is a HAR file?</h3>
<p>HTTP Archive: a JSON file that records every request and response a page made. Browsers export it from the Network tab of DevTools.</p>
<h3>Is the generated spec complete?</h3>
<p>No. It describes only what you captured. Unseen endpoints, fields and errors are missing, and "required" means "present in every sample". Treat the result as a strong draft and review it.</p>
<h3>How do I get a better spec?</h3>
<p>Capture more: every screen, search, create, update, delete, and a few failures. Merge knowledge by running several captures and comparing.</p>
<h3>Does it support GraphQL?</h3>
<p>Calls show up as one <code>POST /graphql</code> operation with the request and response shapes seen. Per-query modelling is on the roadmap.</p>
<h3>Does it work with mobile apps or desktop apps?</h3>
<p>Yes, if you can record their traffic as HAR (mitmproxy, Charles and Proxyman can export HAR).</p>
<h3>My response bodies are empty in the spec.</h3>
<p>Some exports omit bodies. In Chrome use <b>Save all as HAR with content</b>. Some responses (large or binary) are never stored.</p>
<h3>Is it safe to run on a HAR with tokens?</h3>
<p>Secrets are redacted in all output and nothing leaves your machine. Still treat the HAR itself as sensitive.</p>
<h3>Which Python versions?</h3>
<p>3.9 and newer. No third-party packages.</p>
<h3>Why does the generated Python client need requests?</h3>
<p>harspec itself has no dependencies, but the generated client uses <code>requests</code> because most Python developers already have it. A generator for <code>httpx</code> or the standard library is a nice first contribution.</p>
<h3>Can I use the output in a commercial project?</h3>
<p>harspec is MIT licensed, so the tool and its generated code are free to use. Whether you may use a given third-party API is governed by that service's terms.</p>
<h3>How is this different from other tools?</h3>
<p>Many tools show you traffic; harspec turns it into documentation and code and is built to be extended. Note: another unrelated project uses a similar name; harspec is not affiliated with it.</p>
<h3>How do I contribute or report a bug?</h3>
<p>See <a href="contributing.html">Contributing</a>.</p>
""")

# ---------------------------------------------------------------- Contributing
page("contributing", "Contributing", "How to contribute to harspec: report bugs, add generators, improve detection.", f"""
<h1>Contributing</h1>
<p class="lead">harspec is open source (MIT). Bug reports, docs fixes and new generators are all welcome.</p>
{c("git clone " + GH + ".git\ncd harspec\npython -m unittest discover -s tests -v")}
{table(["I want to...", "Do this"], [
 ["Report a wrong result", "Open an <a href=\"" + GH + "/issues\">issue</a> with a <b>redacted</b> snippet, what you expected and what you got."],
 ["Add a generator", "See <a href=\"generators.html\">Write a generator</a>."],
 ["Improve detection", "Edit <code>paths.py</code> or <code>schema.py</code> and add a test."],
 ["Fix these docs", "Edit <code>build.py</code> in the docs repository, run <code>python build.py</code>, open a pull request."],
])}
<h2>Ground rules</h2>
<ul>
<li>Never include real secrets or private captures in tests, issues or examples.</li>
<li>Keep the core dependency-free.</li>
<li>Add a test for every behaviour change. One change per pull request.</li>
<li>Be kind: see the <a href="{GH}/blob/main/CODE_OF_CONDUCT.md">Code of Conduct</a>.</li>
</ul>
<p>Full details: <a href="{GH}/blob/main/CONTRIBUTING.md">CONTRIBUTING.md</a>.</p>
""")

NAV = [("index", "Home"), ("getting-started", "Getting started"), ("how-it-works", "How it works"), ("reference", "Reference"),
       ("generators", "Write a generator"), ("security", "Privacy and security"), ("faq", "FAQ"), ("contributing", "Contributing")]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230f6e56'/%3E%3Ctext x='16' y='22' font-size='16' font-weight='700' text-anchor='middle' fill='white' font-family='monospace'%3E%7B%7D%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="top"><button id="menu" aria-label="Menu">&#9776;</button><a class="brand" href="index.html"><span class="logo">{{}}</span>harspec</a>
<span class="sp"></span><a class="gh" href="{gh}">GitHub</a><button id="theme" aria-label="Toggle theme">&#9680;</button></header>
<div class="wrap">
<nav id="nav">{nav}</nav>
<main>
{body}
<div class="pn">{prev}{next}</div>
<footer>MIT licensed. Open source on <a href="{gh}">GitHub</a>. Not affiliated with any other project that uses a similar name.</footer>
</main>
</div>
<script src="assets/site.js"></script>
</body>
</html>
"""

CSS = """:root{--bg:#fbfaf7;--card:#fff;--ink:#1d1d1b;--mute:#5d5c56;--acc:#0f6e56;--acc2:#e8f3ee;--line:#dedcd3;--code:#f1efe8;
color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14151a;--card:#1c1e24;--ink:#ecebe6;--mute:#a3a29a;--acc:#4cc9a0;--acc2:#1b2a25;--line:#2f323a;--code:#101216;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#14151a;--card:#1c1e24;--ink:#ecebe6;--mute:#a3a29a;--acc:#4cc9a0;--acc2:#1b2a25;--line:#2f323a;--code:#101216;color-scheme:dark}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--acc)}code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.9em;background:var(--code);padding:.1em .35em;border-radius:5px}
.top{position:sticky;top:0;z-index:10;display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--bg);border-bottom:1px solid var(--line)}
.top button{background:none;border:1px solid var(--line);color:var(--ink);border-radius:8px;padding:6px 10px;font-size:16px;cursor:pointer}
.brand{display:flex;align-items:center;gap:8px;font-weight:800;font-size:18px;color:var(--ink);text-decoration:none}
.logo{background:var(--acc);color:#fff;border-radius:7px;padding:1px 7px;font:700 15px ui-monospace,Menlo,monospace}
.sp{flex:1}.gh{color:var(--mute);text-decoration:none;font-weight:600}
.wrap{display:flex;max-width:1100px;margin:0 auto}
nav{width:230px;flex:none;padding:20px 16px;position:sticky;top:57px;align-self:flex-start;height:calc(100vh - 57px);overflow-y:auto}
nav a{display:block;padding:8px 12px;border-radius:8px;color:var(--mute);text-decoration:none;font-weight:600}
nav a:hover{background:var(--acc2)}nav a.on{background:var(--acc2);color:var(--acc)}
main{flex:1;min-width:0;padding:28px 24px 60px;max-width:820px}
h1{font-size:34px;line-height:1.2;margin:.2em 0 .4em}h2{font-size:24px;margin:1.8em 0 .5em;padding-top:.4em}h3{font-size:18px;margin:1.4em 0 .3em}
.lead{font-size:18px;color:var(--mute)}.eyebrow{color:var(--acc);font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase;margin:0}
.hero h1{font-size:42px}.cta{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}
.btn{background:var(--acc);color:#fff;padding:11px 20px;border-radius:999px;font-weight:700;text-decoration:none}
.btn.ghost{background:none;color:var(--acc);border:1.5px solid var(--acc)}
pre{position:relative;background:var(--code);border:1px solid var(--line);border-radius:12px;padding:14px;overflow-x:auto;margin:14px 0;font-size:14px;line-height:1.5}
pre code{background:none;padding:0;font-size:inherit}
.cp{position:absolute;top:6px;right:6px;background:var(--card);color:var(--mute);border:1px solid var(--line);border-radius:6px;padding:3px 8px;font-size:12px;cursor:pointer}
.tw{overflow-x:auto;margin:14px 0}table{border-collapse:collapse;width:100%;min-width:480px;font-size:15px}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}th{background:var(--acc2);color:var(--acc)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:4px 16px 12px}.card h3{margin-top:12px}.card p{margin:0;color:var(--mute);font-size:15px}
.steps{padding-left:22px}.steps li{margin:10px 0}
.note{border-left:4px solid var(--acc);background:var(--acc2);padding:12px 14px;border-radius:0 10px 10px 0;margin:18px 0}
.pn{display:flex;justify-content:space-between;gap:12px;margin-top:44px}.pn a{border:1px solid var(--line);border-radius:12px;padding:10px 16px;text-decoration:none;font-weight:600;background:var(--card)}
footer{margin-top:40px;color:var(--mute);font-size:14px;border-top:1px solid var(--line);padding-top:16px}
#menu{display:none}
@media (max-width:820px){#menu{display:block}nav{display:none;position:fixed;top:57px;left:0;right:0;bottom:0;width:auto;height:auto;background:var(--bg);z-index:9}nav.open{display:block}
main{padding:20px 16px 50px}.hero h1{font-size:32px}h1{font-size:28px}}
"""

JS = """(function(){
var r=document.documentElement,nav=document.getElementById("nav");
try{var t=localStorage.getItem("theme");if(t)r.setAttribute("data-theme",t);}catch(e){}
document.getElementById("theme").onclick=function(){
  var dark=r.getAttribute("data-theme")==="dark"||(!r.getAttribute("data-theme")&&matchMedia("(prefers-color-scheme:dark)").matches);
  var n=dark?"light":"dark";r.setAttribute("data-theme",n);try{localStorage.setItem("theme",n);}catch(e){}
};
document.getElementById("menu").onclick=function(){nav.classList.toggle("open");};
[].forEach.call(document.querySelectorAll("pre"),function(p){
  var b=document.createElement("button");b.className="cp";b.textContent="Copy";
  b.onclick=function(){var x=p.querySelector("code").innerText;
    (navigator.clipboard?navigator.clipboard.writeText(x):Promise.reject()).then(function(){b.textContent="Copied";setTimeout(function(){b.textContent="Copy";},1500);},function(){});};
  p.appendChild(b);
});
})();
"""


def main():
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    open(os.path.join(ROOT, "assets", "style.css"), "w", encoding="utf-8").write(CSS)
    open(os.path.join(ROOT, "assets", "site.js"), "w", encoding="utf-8").write(JS)
    order = [s for s, _ in NAV]
    titles = dict(NAV)
    urls = []
    for slug, title, desc, body in PAGES:
        nav = "".join(f'<a href="{s}.html"{" class=on" if s == slug else ""}>{t}</a>' for s, t in NAV)
        i = order.index(slug)
        prev = f'<a href="{order[i-1]}.html">&larr; {titles[order[i-1]]}</a>' if i > 0 else "<span></span>"
        nxt = f'<a href="{order[i+1]}.html">{titles[order[i+1]]} &rarr;</a>' if i < len(order) - 1 else "<span></span>"
        full = "harspec: HAR to OpenAPI and typed clients" if slug == "index" else f"{title} | harspec"
        out = TEMPLATE.format(title=full, desc=html.escape(desc), nav=nav, body=body, prev=prev, next=nxt, gh=GH).replace("{{}}", "{}")
        open(os.path.join(ROOT, f"{slug}.html"), "w", encoding="utf-8").write(out)
        urls.append(SITE + ("" if slug == "index" else f"{slug}.html"))
    open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(TEMPLATE.format(
        title="Page not found | harspec", desc="Page not found", nav="".join(f'<a href="{s}.html">{t}</a>' for s, t in NAV),
        body='<h1>Page not found</h1><p class="lead">That page does not exist. Try the <a href="index.html">home page</a>.</p>', prev="", next="", gh=GH).replace("{{}}", "{}"))
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    print(f"Built {len(PAGES)} pages")


if __name__ == "__main__":
    main()
