# IA Cleaner

Remove the hidden metadata and invisible characters that link your text, images and documents to AI tools.

Everything runs locally in your browser — no file is ever uploaded.

- **Images** (JPG, PNG, WebP, GIF, AVIF): EXIF, XMP, IPTC, comments, C2PA / Content Credentials and embedded prompts.
- **Documents** (DOCX, XLSX, PPTX, ODT…): author, company, generating app, template, custom properties and embedded images.
- **PDF**: Info dictionary, XMP metadata and attached C2PA manifests.
- **Text**: zero-width characters, special spaces, bidi controls, hidden Unicode tags and chat leftovers (`oaicite`, `utm_source=chatgpt.com`…).

It cannot remove watermarks embedded in the content itself (e.g. SynthID).

## Development

- `index.html` is the English page and the source of truth. Spanish texts live in the `UI_ES` / `ES` objects inside it.
- After editing `index.html`, regenerate the Spanish page and commit both files:

```bash
python tools/build_es.py
```

- Guides (`/guides/…`, `/es/guias/…`) and `sitemap.xml` are generated from `tools/build_guides.py`. Edit the `GUIDES` list there and run:

```bash
python tools/build_guides.py
```

- `robots.txt` and `404.html` are served as-is by GitHub Pages at https://iacleaner.com.
