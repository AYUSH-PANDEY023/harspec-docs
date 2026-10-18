# harspec documentation website

Source of the [harspec](https://github.com/AYUSH-PANDEY023/harspec) docs site. Plain HTML, CSS and a tiny bit of JavaScript. No framework, no build tools, no dependencies. Fully open source (MIT).

**Live site:** https://AYUSH-PANDEY023.github.io/harspec-docs/

## What is inside

| Path | Purpose |
| --- | --- |
| `*.html` | The generated pages (this is what gets published) |
| `assets/` | `style.css` (light and dark theme) and `site.js` (theme toggle, mobile menu, copy buttons) |
| `build.py` | **Single source of truth.** All page content lives here; it regenerates every HTML file |
| `sitemap.xml`, `robots.txt`, `404.html` | SEO and error page |
| `.github/workflows/pages.yml` | Deploys to GitHub Pages on every push to `main` |
| `personalize.py` | Replaces the `AYUSH-PANDEY023` placeholders |

Pages: Home, Getting started, How it works, Reference, Write a generator, Privacy and security, FAQ, Contributing.

## Preview locally

```bash
python -m http.server 8000
# open http://localhost:8000
```

## Edit the docs

1. Open `build.py` and change the text in the `page(...)` blocks.
2. Run `python build.py` (needs Python 3.12+). It rewrites all `.html` files.
3. Commit the changed files and push.

## Publish on GitHub Pages (free)

```bash
python personalize.py YOUR_GITHUB_USERNAME "Your Name" you@example.com
python build.py
git init -b main
git add .
git commit -m "Docs site"
gh repo create harspec-docs --public --source=. --remote=origin --push
```

Then on GitHub: **Settings > Pages > Build and deployment > Source: GitHub Actions**. Open the **Actions** tab; when `deploy docs` is green the site is live at `https://AYUSH-PANDEY023.github.io/harspec-docs/`.

No `gh` CLI? Create an empty repo named `harspec-docs` on github.com, then `git remote add origin https://github.com/AYUSH-PANDEY023/harspec-docs.git` and `git push -u origin main`.

**Custom domain (optional):** Settings > Pages > Custom domain, and add a `CNAME` DNS record pointing to `AYUSH-PANDEY023.github.io`.

**Other free hosts:** the folder is a static site, so Netlify, Cloudflare Pages and Vercel work too. Drag the folder in or connect the repo, with no build command and the root as the publish directory.

## Contributing

Fixes and improvements are welcome: open an issue or a pull request. Please keep pages short, accurate and free of real secrets.

## License

MIT. See [LICENSE](LICENSE).
