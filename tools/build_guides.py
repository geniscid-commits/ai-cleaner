"""Generate the SEO guide pages (EN + ES) and sitemap.xml.

Usage:  python tools/build_guides.py
Edit the GUIDES list below to change or add articles, then run the script and commit.
"""
import html, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://iacleaner.com'
UPDATED = '2026-11-07'

T = {
  'en': {'home': '/', 'guides': '/guides/', 'guides_name': 'Guides', 'open': 'Open IA Cleaner', 'files': '/#files',
         'cta_title': 'Clean your files in seconds', 'cta_text': 'Free, no sign-up, and everything runs in your browser — nothing is uploaded.',
         'related': 'More guides', 'updated': 'Updated', 'read': 'min read', 'footer': 'IA Cleaner · Private by design — your files never leave your device.',
         'idx_title': 'Guides — remove AI metadata and hidden characters | IA Cleaner',
         'idx_desc': 'Step-by-step guides to remove C2PA, EXIF and PDF metadata and to clean hidden characters from AI-generated text.',
         'idx_h1': 'Guides', 'idx_lead': 'Practical, step-by-step guides about the hidden data inside your files — and how to remove it.',
         'locale': 'en_US'},
  'es': {'home': '/es/', 'guides': '/es/guias/', 'guides_name': 'Guías', 'open': 'Abrir IA Cleaner', 'files': '/es/#files',
         'cta_title': 'Limpia tus archivos en segundos', 'cta_text': 'Gratis, sin registro y todo se procesa en tu navegador: no se sube nada.',
         'related': 'Más guías', 'updated': 'Actualizado', 'read': 'min de lectura', 'footer': 'IA Cleaner · Privado por diseño: tus archivos nunca salen de tu dispositivo.',
         'idx_title': 'Guías: elimina metadatos de IA y caracteres ocultos | IA Cleaner',
         'idx_desc': 'Guías paso a paso para quitar metadatos C2PA, EXIF y de PDF, y para limpiar caracteres ocultos de textos generados con IA.',
         'idx_h1': 'Guías', 'idx_lead': 'Guías prácticas, paso a paso, sobre los datos ocultos que llevan tus archivos y cómo eliminarlos.',
         'locale': 'es_ES'},
}

GUIDES = [
 {
  'id': 'c2pa',
  'en': {
   'slug': 'remove-c2pa-content-credentials',
   'title': 'How to remove C2PA / Content Credentials from an image',
   'seo_title': 'How to Remove C2PA & Content Credentials from an Image (Free)',
   'desc': 'What C2PA Content Credentials are, how to check if your image has them, and how to remove them for free without losing quality.',
   'lead': 'Images made or edited with AI tools often carry a hidden, signed record of how they were created. Here is what it is, how to check for it and how to remove it.',
   'cta': 'files', 'mins': 4,
   'body': '''
<h2>What is C2PA?</h2>
<p><strong>C2PA</strong> (Coalition for Content Provenance and Authenticity) is an open standard for attaching a <em>provenance record</em> to a file. Adobe calls it <strong>Content Credentials</strong>. The record — called a <em>manifest</em> — is cryptographically signed and can say which app created the image, whether AI was used and what edits were made.</p>
<p>Images exported by tools such as ChatGPT / DALL·E, Adobe Firefly or Microsoft Designer, and some cameras and phones, can include a C2PA manifest. Some platforms read it to show an “AI info” or “Made with AI” label.</p>

<h2>Where is it stored?</h2>
<ul>
<li><strong>JPEG:</strong> inside <code>APP11</code> segments (JUMBF boxes).</li>
<li><strong>PNG:</strong> in a <code>caBX</code> chunk.</li>
<li><strong>WebP:</strong> in a dedicated RIFF chunk.</li>
</ul>
<p>It often travels together with <strong>XMP</strong> metadata that includes the IPTC field <code>DigitalSourceType</code> with values like <code>trainedAlgorithmicMedia</code> — another common “AI-generated” marker.</p>

<h2>How to check if an image has Content Credentials</h2>
<ol>
<li>Upload it to the official verifier at <a href="https://contentcredentials.org/verify" rel="noopener">contentcredentials.org/verify</a>, or</li>
<li>Drop it into <a href="/#files">IA Cleaner</a>: it lists every metadata block it finds and flags AI-related ones before removing them.</li>
</ol>

<h2>How to remove C2PA with IA Cleaner (step by step)</h2>
<ol>
<li>Open <a href="/#files">IA Cleaner → Images &amp; documents</a>.</li>
<li>Drag your JPG, PNG or WebP onto the drop zone (you can add several at once).</li>
<li>Check the report: blocks such as <em>JUMBF / C2PA Content Credentials (APP11)</em> or <em>XMP</em> are listed and marked <strong>AI</strong>.</li>
<li>Click <strong>Download</strong>. The image is cleaned <strong>losslessly</strong> — only metadata is removed, pixels stay untouched.</li>
</ol>
<p>Verify the result by running the cleaned file through the verifier again: it should report that no Content Credentials were found.</p>

<h2>Other ways</h2>
<ul>
<li><strong>ExifTool</strong> (command line): <code>exiftool -all= image.jpg</code> removes EXIF, XMP and IPTC. Check its documentation for C2PA/JUMBF support in your version.</li>
<li><strong>Screenshot or re-export:</strong> works, but recompresses the image and loses quality.</li>
</ul>

<h2>What removing C2PA does not do</h2>
<p>Some AI images also carry <strong>invisible watermarks</strong> woven into the pixels themselves (for example Google’s SynthID). These are not metadata, so no metadata tool can remove them. And if a platform, publication or law requires you to disclose AI use, removing metadata doesn’t change that obligation.</p>
'''},
  'es': {
   'slug': 'quitar-c2pa-content-credentials',
   'title': 'Cómo quitar C2PA / Content Credentials de una imagen',
   'seo_title': 'Cómo quitar C2PA y Content Credentials de una imagen (gratis)',
   'desc': 'Qué son las Content Credentials (C2PA), cómo saber si tu imagen las tiene y cómo eliminarlas gratis sin perder calidad.',
   'lead': 'Las imágenes creadas o editadas con herramientas de IA suelen llevar un registro oculto y firmado de cómo se hicieron. Te explicamos qué es, cómo detectarlo y cómo quitarlo.',
   'cta': 'files', 'mins': 4,
   'body': '''
<h2>¿Qué es C2PA?</h2>
<p><strong>C2PA</strong> (Coalition for Content Provenance and Authenticity) es un estándar abierto para añadir a un archivo un <em>registro de procedencia</em>. Adobe lo llama <strong>Content Credentials</strong> («credenciales de contenido»). Ese registro —el <em>manifiesto</em>— va firmado criptográficamente y puede indicar qué aplicación creó la imagen, si se usó IA y qué ediciones se hicieron.</p>
<p>Las imágenes exportadas por herramientas como ChatGPT / DALL·E, Adobe Firefly o Microsoft Designer, y algunas cámaras y móviles, pueden incluir un manifiesto C2PA. Algunas plataformas lo leen para mostrar etiquetas como «Información de IA» o «Hecho con IA».</p>

<h2>¿Dónde se guarda?</h2>
<ul>
<li><strong>JPEG:</strong> en segmentos <code>APP11</code> (cajas JUMBF).</li>
<li><strong>PNG:</strong> en un bloque <code>caBX</code>.</li>
<li><strong>WebP:</strong> en un bloque RIFF propio.</li>
</ul>
<p>A menudo va acompañado de metadatos <strong>XMP</strong> con el campo IPTC <code>DigitalSourceType</code> y valores como <code>trainedAlgorithmicMedia</code>, otra marca habitual de «generado con IA».</p>

<h2>Cómo saber si una imagen tiene Content Credentials</h2>
<ol>
<li>Súbela al verificador oficial en <a href="https://contentcredentials.org/verify" rel="noopener">contentcredentials.org/verify</a>, o</li>
<li>Arrástrala a <a href="/es/#files">IA Cleaner</a>: muestra todos los bloques de metadatos que encuentra y marca los relacionados con IA antes de eliminarlos.</li>
</ol>

<h2>Cómo quitar C2PA con IA Cleaner (paso a paso)</h2>
<ol>
<li>Abre <a href="/es/#files">IA Cleaner → Imágenes y documentos</a>.</li>
<li>Arrastra tu JPG, PNG o WebP a la zona de carga (puedes añadir varios a la vez).</li>
<li>Revisa el informe: aparecen bloques como <em>JUMBF / C2PA Content Credentials (APP11)</em> o <em>XMP</em>, marcados con <strong>IA</strong>.</li>
<li>Pulsa <strong>Descargar</strong>. La imagen se limpia <strong>sin pérdida</strong>: solo se quitan los metadatos y los píxeles no se tocan.</li>
</ol>
<p>Comprueba el resultado pasando la imagen limpia otra vez por el verificador: debería indicar que no hay Content Credentials.</p>

<h2>Otras formas</h2>
<ul>
<li><strong>ExifTool</strong> (línea de comandos): <code>exiftool -all= imagen.jpg</code> elimina EXIF, XMP e IPTC. Revisa su documentación para saber si tu versión elimina también C2PA/JUMBF.</li>
<li><strong>Captura de pantalla o volver a exportar:</strong> funciona, pero recomprime la imagen y pierde calidad.</li>
</ul>

<h2>Lo que no hace quitar C2PA</h2>
<p>Algunas imágenes de IA llevan además <strong>marcas de agua invisibles</strong> integradas en los propios píxeles (por ejemplo, SynthID de Google). No son metadatos, así que ninguna herramienta de metadatos puede quitarlas. Y si una plataforma, una publicación o la ley te exige indicar que usaste IA, borrar los metadatos no cambia esa obligación.</p>
'''},
 },
 {
  'id': 'chatgpt',
  'en': {
   'slug': 'chatgpt-hidden-characters',
   'title': 'ChatGPT hidden characters: what they are and how to remove them',
   'seo_title': 'ChatGPT Hidden Characters, oaicite & utm_source: How to Remove Them',
   'desc': 'Why text copied from ChatGPT can contain invisible characters, contentReference[oaicite] markers and utm_source=chatgpt.com links — and how to clean them.',
   'lead': 'Pasted some text from an AI chat and found strange gaps, “oaicite” codes or tracking tags in your links? Here is where they come from and how to clean them in one click.',
   'cta': 'text', 'mins': 5,
   'body': '''
<h2>What can be hidden in copied AI text</h2>
<ul>
<li><strong>Invisible Unicode characters</strong>: zero-width spaces (<code>U+200B</code>), word joiners (<code>U+2060</code>), byte-order marks (<code>U+FEFF</code>) and soft hyphens. They take up no space on screen but are still in the text.</li>
<li><strong>Special spaces</strong>: no-break (<code>U+00A0</code>) and narrow no-break spaces (<code>U+202F</code>) that look like normal spaces.</li>
<li><strong>Citation leftovers</strong>: when an answer cites sources, copying it into another app can leave markers such as <code>contentReference[oaicite:0]{index=0}</code> or <code>【4:0†source】</code>.</li>
<li><strong>Tracking parameters</strong>: links suggested by ChatGPT often end in <code>?utm_source=chatgpt.com</code>.</li>
<li><strong>Private-use characters</strong>: internal markers from the chat interface that show up as empty boxes in some apps.</li>
</ul>

<h2>Are they a watermark?</h2>
<p>Mostly no. In 2025 users noticed that some newer models occasionally produced narrow no-break spaces, and many assumed it was a watermark; OpenAI said it was not intentional. Most hidden characters come from formatting and copy-paste. They are still worth removing: they can break code, search, word counts and formatting, and they reveal where the text was copied from.</p>
<p>Note that AI-text detectors judge the <em>wording</em>, not these characters — cleaning them won’t change what a detector thinks of your writing.</p>

<h2>How to check and clean your text with IA Cleaner</h2>
<ol>
<li>Open <a href="/">IA Cleaner → Text</a> and paste your text.</li>
<li>A live counter tells you how many hidden characters were found.</li>
<li>Click <strong>Clean text</strong>. You’ll see every hidden character highlighted in place, with its Unicode code and name.</li>
<li>Copy the clean result or download it as a <code>.txt</code>.</li>
</ol>
<p>Compound emoji (👨‍👩‍👧) and flags are kept intact. An optional setting also converts curly quotes, em dashes and ellipses into plain characters.</p>

<h2>Hidden messages in Unicode tags</h2>
<p>A less common trick uses <strong>Unicode tag characters</strong> (<code>U+E0000–E007F</code>) to hide whole sentences inside normal-looking text — sometimes used for prompt injection. IA Cleaner decodes and shows any hidden message before removing it.</p>

<h2>Cleaning text inside Word and PowerPoint files</h2>
<p>If you already pasted AI text into a document, drop the <code>.docx</code>, <code>.pptx</code> or <code>.xlsx</code> into <a href="/#files">Images &amp; documents</a>: invisible characters are removed from the document text and its metadata is cleaned too.</p>
'''},
  'es': {
   'slug': 'caracteres-ocultos-chatgpt',
   'title': 'Caracteres ocultos de ChatGPT: qué son y cómo eliminarlos',
   'seo_title': 'Caracteres ocultos de ChatGPT, oaicite y utm_source: cómo quitarlos',
   'desc': 'Por qué el texto copiado de ChatGPT puede tener caracteres invisibles, marcas contentReference[oaicite] y enlaces con utm_source=chatgpt.com, y cómo limpiarlo.',
   'lead': '¿Has pegado un texto de un chat de IA y te han aparecido huecos raros, códigos «oaicite» o etiquetas en los enlaces? Te explicamos de dónde salen y cómo limpiarlos con un clic.',
   'cta': 'text', 'mins': 5,
   'body': '''
<h2>Qué puede esconder un texto copiado de una IA</h2>
<ul>
<li><strong>Caracteres Unicode invisibles</strong>: espacios de ancho cero (<code>U+200B</code>), uniones de palabras (<code>U+2060</code>), marcas BOM (<code>U+FEFF</code>) y guiones suaves. No ocupan espacio en pantalla, pero siguen en el texto.</li>
<li><strong>Espacios especiales</strong>: espacios de no separación (<code>U+00A0</code>) y estrechos (<code>U+202F</code>) que parecen espacios normales.</li>
<li><strong>Restos de citas</strong>: cuando una respuesta cita fuentes, al copiarla en otra aplicación pueden quedar marcas como <code>contentReference[oaicite:0]{index=0}</code> o <code>【4:0†source】</code>.</li>
<li><strong>Parámetros de seguimiento</strong>: los enlaces que sugiere ChatGPT suelen terminar en <code>?utm_source=chatgpt.com</code>.</li>
<li><strong>Caracteres de uso privado</strong>: marcadores internos de la interfaz del chat que en algunas aplicaciones se ven como cuadros vacíos.</li>
</ul>

<h2>¿Son una marca de agua?</h2>
<p>En general, no. En 2025 algunos usuarios vieron que ciertos modelos nuevos generaban a veces espacios estrechos de no separación y muchos pensaron que era una marca de agua; OpenAI dijo que no era intencionado. La mayoría de caracteres ocultos vienen del formato y de copiar y pegar. Aun así conviene quitarlos: pueden romper código, búsquedas, recuentos de palabras y el formato, y delatan de dónde se copió el texto.</p>
<p>Ten en cuenta que los detectores de texto de IA analizan la <em>redacción</em>, no estos caracteres: limpiarlos no cambia lo que un detector opine de tu texto.</p>

<h2>Cómo revisar y limpiar tu texto con IA Cleaner</h2>
<ol>
<li>Abre <a href="/es/">IA Cleaner → Texto</a> y pega tu texto.</li>
<li>Un contador en directo te dice cuántos caracteres ocultos ha encontrado.</li>
<li>Pulsa <strong>Limpiar texto</strong>. Verás cada carácter oculto resaltado en su sitio, con su código Unicode y su nombre.</li>
<li>Copia el resultado limpio o descárgalo como <code>.txt</code>.</li>
</ol>
<p>Los emojis compuestos (👨‍👩‍👧) y las banderas se conservan. Una opción adicional convierte las comillas tipográficas, las rayas y los puntos suspensivos en caracteres simples.</p>

<h2>Mensajes ocultos en etiquetas Unicode</h2>
<p>Un truco menos habitual usa <strong>caracteres de etiqueta Unicode</strong> (<code>U+E0000–E007F</code>) para esconder frases enteras dentro de un texto normal; a veces se usa para inyección de prompts. IA Cleaner descodifica y te muestra el mensaje oculto antes de eliminarlo.</p>

<h2>Limpiar el texto dentro de archivos Word y PowerPoint</h2>
<p>Si ya pegaste el texto en un documento, arrastra el <code>.docx</code>, <code>.pptx</code> o <code>.xlsx</code> a <a href="/es/#files">Imágenes y documentos</a>: se eliminan los caracteres invisibles del texto y también se limpian sus metadatos.</p>
'''},
 },
 {
  'id': 'pdf',
  'en': {
   'slug': 'remove-pdf-metadata',
   'title': 'How to remove metadata from a PDF',
   'seo_title': 'How to Remove Metadata from a PDF (Author, Creator, XMP) — Free',
   'desc': 'See what metadata a PDF contains (author, creator app, dates, XMP) and remove it for free, without Acrobat and without uploading the file.',
   'lead': 'Every PDF carries information about who made it and with what software. Here is what is inside, why it matters and how to strip it without uploading your file anywhere.',
   'cta': 'files', 'mins': 4,
   'body': '''
<h2>What metadata does a PDF contain?</h2>
<ul>
<li><strong>Document Info:</strong> Title, Author, Subject, Keywords, <em>Creator</em> (the app that made the original, e.g. Word) and <em>Producer</em> (the PDF engine), plus creation and modification dates.</li>
<li><strong>XMP metadata:</strong> an XML block that can repeat all of the above and add much more — editing history, tool names and, increasingly, AI-related tags.</li>
<li><strong>Page-level data</strong> and attachments, including C2PA provenance manifests in newer files.</li>
</ul>
<p>These fields can reveal your name, your company, the software you used (including AI writing or design tools) and when you worked on the file.</p>

<h2>How to remove PDF metadata with IA Cleaner</h2>
<ol>
<li>Open <a href="/#files">IA Cleaner → Images &amp; documents</a>.</li>
<li>Drop your PDF. The report lists every field found — Author, Creator, Producer, XMP — and flags AI-related values.</li>
<li>Click <strong>Download</strong> to get the cleaned copy.</li>
</ol>
<p>The PDF is <strong>rewritten from scratch</strong>, so the old values are not left behind in the file. Password-protected PDFs can’t be modified — remove the password first.</p>

<h2>Other ways</h2>
<ul>
<li><strong>Adobe Acrobat Pro:</strong> <em>Tools → Redact → Sanitize Document</em> removes hidden information (paid).</li>
<li><strong>Microsoft Word, before exporting:</strong> <em>File → Info → Check for Issues → Inspect Document</em>, then in the PDF export options untick <em>Document properties</em>.</li>
<li><strong>ExifTool:</strong> <code>exiftool -all:all= file.pdf</code>. Note that ExifTool edits PDFs <em>incrementally</em>, so the original metadata can still be recovered unless you rewrite the file afterwards (for example with <code>qpdf</code>).</li>
</ul>

<h2>Don’t forget the content</h2>
<p>Metadata is only part of the story: comments, tracked changes, hidden layers or text covered by black boxes can still be in the file. Clean the original document before exporting, and use proper redaction for sensitive text.</p>
'''},
  'es': {
   'slug': 'borrar-metadatos-pdf',
   'title': 'Cómo borrar los metadatos de un PDF',
   'seo_title': 'Cómo borrar los metadatos de un PDF (autor, creador, XMP) gratis',
   'desc': 'Descubre qué metadatos tiene un PDF (autor, aplicación, fechas, XMP) y elimínalos gratis, sin Acrobat y sin subir el archivo.',
   'lead': 'Todo PDF lleva información sobre quién lo hizo y con qué programa. Te contamos qué contiene, por qué importa y cómo eliminarla sin subir tu archivo a ningún sitio.',
   'cta': 'files', 'mins': 4,
   'body': '''
<h2>¿Qué metadatos tiene un PDF?</h2>
<ul>
<li><strong>Información del documento:</strong> Título, Autor, Asunto, Palabras clave, <em>Creator</em> (la aplicación del original, por ejemplo Word) y <em>Producer</em> (el motor que generó el PDF), además de las fechas de creación y modificación.</li>
<li><strong>Metadatos XMP:</strong> un bloque XML que puede repetir todo lo anterior y añadir mucho más: historial de edición, nombres de herramientas y, cada vez más, etiquetas relacionadas con IA.</li>
<li><strong>Datos por página</strong> y adjuntos, incluidos manifiestos de procedencia C2PA en archivos recientes.</li>
</ul>
<p>Estos campos pueden revelar tu nombre, tu empresa, el software que usaste (incluidas herramientas de IA para escribir o diseñar) y cuándo trabajaste en el archivo.</p>

<h2>Cómo borrar los metadatos de un PDF con IA Cleaner</h2>
<ol>
<li>Abre <a href="/es/#files">IA Cleaner → Imágenes y documentos</a>.</li>
<li>Arrastra tu PDF. El informe muestra cada campo encontrado (Autor, Creator, Producer, XMP) y marca los valores relacionados con IA.</li>
<li>Pulsa <strong>Descargar</strong> para obtener la copia limpia.</li>
</ol>
<p>El PDF se <strong>reescribe desde cero</strong>, así que los valores antiguos no quedan escondidos dentro del archivo. Los PDF protegidos con contraseña no se pueden modificar: quita antes la contraseña.</p>

<h2>Otras formas</h2>
<ul>
<li><strong>Adobe Acrobat Pro:</strong> <em>Herramientas → Censurar → Desinfectar documento</em> elimina la información oculta (de pago).</li>
<li><strong>Microsoft Word, antes de exportar:</strong> <em>Archivo → Información → Comprobar si hay problemas → Inspeccionar documento</em> y, en las opciones de exportación a PDF, desmarca <em>Propiedades del documento</em>.</li>
<li><strong>ExifTool:</strong> <code>exiftool -all:all= archivo.pdf</code>. Ojo: ExifTool modifica los PDF de forma <em>incremental</em>, así que los metadatos originales se pueden recuperar si no reescribes el archivo después (por ejemplo con <code>qpdf</code>).</li>
</ul>

<h2>No te olvides del contenido</h2>
<p>Los metadatos son solo una parte: comentarios, control de cambios, capas ocultas o texto tapado con recuadros negros pueden seguir en el archivo. Limpia el documento original antes de exportarlo y usa una censura de verdad para el texto sensible.</p>
'''},
 },
]

CSS = '''
:root{--bg:#f5f7fa;--surface:#fff;--surface-2:#f0f3f7;--ink:#24344b;--muted:#6c7a8e;--faint:#9aa6b6;--line:#e2e7ee;--brand:#3f5a7d;--brand-2:#5a78a0;--brand-soft:#e7edf5;--shadow:0 1px 2px rgba(36,52,75,.04),0 8px 28px rgba(36,52,75,.06)}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(1200px 500px at 50% -180px,#e3eaf3 0%,transparent 70%),var(--bg);color:var(--ink);font:16px/1.7 Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--brand-2)}
code{font-family:ui-monospace,Consolas,monospace;font-size:.88em;background:var(--surface-2);padding:1px 6px;border-radius:5px;word-break:break-word}
.top{max-width:1040px;margin:0 auto;padding:22px 24px;display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);font-weight:700;font-size:18px}
.brand img{width:38px;height:38px;object-fit:contain;mix-blend-mode:multiply}
.brand b{color:var(--brand-2)}
.top-right{display:flex;align-items:center;gap:18px}
.top-right>a{color:var(--muted);text-decoration:none;font-size:14px;font-weight:500}
.lang{display:flex;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:3px;box-shadow:var(--shadow)}
.lang a{font-size:12px;font-weight:700;letter-spacing:.04em;color:var(--muted);padding:5px 10px;border-radius:7px;text-decoration:none}
.lang a[aria-current=page]{background:var(--brand);color:#fff}
main{max-width:740px;margin:0 auto;padding:20px 24px 40px}
.crumbs{font-size:13px;color:var(--faint);margin-bottom:14px}
.crumbs a{color:var(--muted);text-decoration:none}
h1{font-size:clamp(28px,4.5vw,40px);line-height:1.18;letter-spacing:-.03em;margin:0 0 14px}
.lead{font-size:18px;color:var(--muted);margin:0 0 10px}
.meta{font-size:13px;color:var(--faint);margin-bottom:26px}
article h2{font-size:23px;letter-spacing:-.02em;margin:36px 0 10px}
article li{margin:6px 0}
.cta{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:18px 22px;box-shadow:var(--shadow);margin:28px 0}
.cta img{width:46px;height:46px;mix-blend-mode:multiply}
.cta div{flex:1;min-width:200px}
.cta strong{display:block;font-size:16px}
.cta span{color:var(--muted);font-size:14px}
.btn{display:inline-block;background:var(--brand);color:#fff;text-decoration:none;font-weight:600;font-size:14px;padding:11px 20px;border-radius:11px;box-shadow:0 4px 14px rgba(63,90,125,.22)}
.btn:hover{background:#3d5577}
.cards{display:grid;gap:12px;margin-top:14px}
.card{display:block;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px 20px;text-decoration:none;color:var(--ink);box-shadow:var(--shadow);transition:.2s}
.card:hover{border-color:var(--brand-2);transform:translateY(-2px)}
.card strong{display:block;font-size:17px;margin-bottom:4px}
.card span{color:var(--muted);font-size:14px}
footer{text-align:center;color:var(--faint);font-size:12.5px;padding:24px 24px 40px}
'''

FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">')

def e(s): return html.escape(s, quote=True)

def page(lang, url, alt, title, desc, body, ld):
    t = T[lang]
    other = 'es' if lang == 'en' else 'en'
    alts = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{u}">' for l, u in alt.items())
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE}{alt["en"]}">'
    return f'''<!DOCTYPE html>
<!-- Generated by tools/build_guides.py. Do not edit by hand. -->
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{url}">
{alts}
<meta property="og:type" content="article"><meta property="og:site_name" content="IA Cleaner">
<meta property="og:url" content="{SITE}{url}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:locale" content="{t['locale']}"><meta property="og:image" content="{SITE}/logo.webp"><meta name="twitter:card" content="summary">
<meta name="theme-color" content="#3f5a7d">
<link rel="icon" href="/logo.webp" type="image/webp">
{FONT}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<div class="top">
  <a class="brand" href="{t['home']}"><img src="/logo.webp" alt=""><span>IA <b>Cleaner</b></span></a>
  <div class="top-right">
    <a href="{t['guides']}">{t['guides_name']}</a>
    <nav class="lang" aria-label="Language"><a href="{alt['en']}" hreflang="en" lang="en" data-lang="en"{' aria-current="page"' if lang == 'en' else ''}>EN</a><a href="{alt['es']}" hreflang="es" lang="es" data-lang="es"{' aria-current="page"' if lang == 'es' else ''}>ES</a></nav>
  </div>
</div>
<main>
{body}
</main>
<footer>{t['footer']}</footer>
<script>document.addEventListener('click', function(e){{ var a = e.target.closest('.lang a'); if (a) try{{ localStorage.setItem('iacleaner-lang', a.dataset.lang); }}catch(_){{}} }});</script>
</body>
</html>
'''

def cta(lang, kind):
    t = T[lang]
    href = t['files'] if kind == 'files' else t['home']
    return (f'<div class="cta"><img src="/logo.webp" alt=""><div><strong>{t["cta_title"]}</strong><span>{t["cta_text"]}</span></div>'
            f'<a class="btn" href="{href}">{t["open"]}</a></div>')

def url_of(lang, g):
    return f"{T[lang]['guides']}{g[lang]['slug']}/"

def write(url, content):
    p = ROOT / url.strip('/') / 'index.html'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')

sitemap_groups = [{'en': '/', 'es': '/es/'}, {'en': '/guides/', 'es': '/es/guias/'}]

for g in GUIDES:
    alt = {l: url_of(l, g) for l in ('en', 'es')}
    sitemap_groups.append(alt)
    for lang in ('en', 'es'):
        t, c = T[lang], g[lang]
        related = ''.join(f'<a class="card" href="{url_of(lang, o)}"><strong>{e(o[lang]["title"])}</strong><span>{e(o[lang]["desc"])}</span></a>'
                          for o in GUIDES if o is not g)
        body = f'''<nav class="crumbs"><a href="{t['home']}">IA Cleaner</a> › <a href="{t['guides']}">{t['guides_name']}</a></nav>
<article>
<h1>{e(c['title'])}</h1>
<p class="lead">{e(c['lead'])}</p>
<div class="meta">{t['updated']} {UPDATED} · {c['mins']} {t['read']}</div>
{cta(lang, c['cta'])}
{c['body'].strip()}
{cta(lang, c['cta'])}
</article>
<h2>{t['related']}</h2>
<div class="cards">{related}</div>'''
        ld = [{'@context': 'https://schema.org', '@type': 'TechArticle', 'headline': c['title'], 'description': c['desc'],
               'inLanguage': lang, 'datePublished': UPDATED, 'dateModified': UPDATED, 'url': SITE + alt[lang],
               'image': SITE + '/logo.webp', 'author': {'@type': 'Organization', 'name': 'IA Cleaner', 'url': SITE + t['home']},
               'publisher': {'@type': 'Organization', 'name': 'IA Cleaner', 'logo': {'@type': 'ImageObject', 'url': SITE + '/logo.webp'}}},
              {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                  {'@type': 'ListItem', 'position': 1, 'name': 'IA Cleaner', 'item': SITE + t['home']},
                  {'@type': 'ListItem', 'position': 2, 'name': t['guides_name'], 'item': SITE + t['guides']},
                  {'@type': 'ListItem', 'position': 3, 'name': c['title'], 'item': SITE + alt[lang]}]}]
        write(alt[lang], page(lang, alt[lang], alt, c['seo_title'] + ' | IA Cleaner', c['desc'], body, ld))

# Guide index pages
for lang in ('en', 'es'):
    t = T[lang]
    cards = ''.join(f'<a class="card" href="{url_of(lang, g)}"><strong>{e(g[lang]["title"])}</strong><span>{e(g[lang]["desc"])}</span></a>' for g in GUIDES)
    body = f'''<nav class="crumbs"><a href="{t['home']}">IA Cleaner</a> › {t['guides_name']}</nav>
<h1>{t['idx_h1']}</h1>
<p class="lead">{t['idx_lead']}</p>
<div class="cards">{cards}</div>
{cta(lang, 'files')}'''
    ld = {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': t['idx_h1'], 'inLanguage': lang, 'url': SITE + t['guides']}
    write(t['guides'], page(lang, t['guides'], {'en': '/guides/', 'es': '/es/guias/'}, t['idx_title'], t['idx_desc'], body, ld))

# Sitemap
rows = []
for grp in sitemap_groups:
    links = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{u}"/>' for l, u in grp.items())
    links += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{grp["en"]}"/>'
    for u in grp.values():
        rows.append(f'  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>{UPDATED}</lastmod>{links}\n  </url>')
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                  'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n', encoding='utf-8')
print(f'{len(GUIDES) * 2} guides + 2 index pages + sitemap ({len(rows)} URLs) written')
