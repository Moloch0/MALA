# case-11: workflow-design

来源 benchmark bucket：`deep`

## 原始输入

```text
I want to publish an e-book on amazon. I have a file story.txt and ten pictures (picture1, picture2, picture3, etc..) what would a python script need in order to convert my files into a kindle format?
```

## 不用 MALA

```text
For Amazon KDP today, I would have the Python script generate a clean **EPUB**, then validate it with **Kindle Previewer**. Amazon accepts EPUB files that meet its Kindle Publishing Guidelines, and Kindle Create/Kindle Previewer can produce or preview Kindle-ready output. Amazon’s own KDP docs also say KPF is preferred when using Kindle Create, but Python scripts usually create EPUB because KPF is Amazon’s tool-generated publishing package, not a normal open format you hand-author directly. Sources: [KDP supported eBook formats](https://kdp.amazon.com/en_US/help/topic/G200634390), [KDP manuscript formatting guide](https://kdp.amazon.com/en_US/help/topic/G200645680), [Kindle Create guide](https://kdp.amazon.com/en_US/help/topic/GUGQ4WDZ92F733GC), [Kindle Previewer user guide](https://kindlepreviewer3.s3.amazonaws.com/UserGuide320_EN.pdf).

**Recommended Workflow**

Your script should produce:

```text
story.txt + picture1.jpg ... picture10.jpg
        |
        v
book.epub
        |
        v
Kindle Previewer validation / optional KPF conversion
        |
        v
Upload EPUB or KPF to KDP
```

For most text stories with illustrations, use a **reflowable EPUB**. That means the text adapts to the reader’s device, font size, and screen width, while your pictures appear inline between paragraphs or chapters.

Use **fixed-layout EPUB** only if the exact placement of text over images matters, such as a children’s picture book, comic, graphic novel, or heavily designed illustrated book. Fixed layout is more complex and less flexible on Kindle devices.

**What The Script Needs**

At minimum, the script needs these inputs:

```text
story.txt
picture1.jpg
picture2.jpg
...
picture10.jpg
metadata.json
```

The `story.txt` should have some way to tell the script where chapters and pictures go. For example:

```text
# Chapter 1

Once upon a time...

[image: picture1.jpg]

The road disappeared into the forest.

# Chapter 2

[image: picture2.jpg]

The next morning...
```

Or, if your story has no image markers, the script needs a rule like “insert one picture after each chapter” or “insert picture1 after paragraph 5, picture2 after paragraph 10,” etc.

A separate metadata file is strongly recommended:

```json
{
  "title": "My Story Title",
  "author": "Your Name",
  "language": "en",
  "publisher": "Your Name",
  "description": "A short description of the book.",
  "copyright": "Copyright 2026 Your Name. All rights reserved."
}
```

For KDP, you should also prepare a **cover image separately**. Amazon specifically says not to include the cover image inside the manuscript file because KDP adds the cover you provide during title setup.

**What The Python Script Should Do**

The script should:

1. Read `story.txt` as UTF-8 text.

2. Parse chapter headings, paragraphs, and image markers.

3. Convert plain text into valid XHTML pages.

4. Copy and optimize the images.

5. Generate a table of contents.

6. Generate EPUB package files.

7. Zip everything into a valid `.epub`.

8. Optionally run external validation tools.

A valid EPUB is essentially a ZIP file with a required internal structure like this:

```text
book.epub
├── mimetype
├── META-INF/
│   └── container.xml
└── OEBPS/
    ├── content.opf
    ├── nav.xhtml
    ├── styles.css
    ├── chapter1.xhtml
    ├── chapter2.xhtml
    └── images/
        ├── picture1.jpg
        ├── picture2.jpg
        └── ...
```

The important EPUB parts are:

`mimetype`  
Must contain:

```text
application/epub+zip
```

This file must be the first file in the ZIP and must not be compressed.

`META-INF/container.xml`  
Tells reading systems where the book package file is.

`OEBPS/content.opf`  
Contains the book metadata, manifest, spine, image list, XHTML file list, and reading order.

`OEBPS/nav.xhtml`  
Contains the EPUB 3 navigation table of contents.

`chapter*.xhtml`  
Contains the actual book content.

`styles.css`  
Controls simple formatting.

`images/`  
Contains your pictures.

**Python Libraries I’d Use**

For a practical script, use:

```text
ebooklib
Pillow
beautifulsoup4 or lxml
python-slugify
```

`ebooklib` handles much of the EPUB packaging.

`Pillow` resizes, converts, and validates images.

`beautifulsoup4` or `lxml` helps generate or clean XHTML.

`python-slugify` helps create safe filenames and IDs.

Install example:

```bash
pip install ebooklib pillow beautifulsoup4 python-slugify
```

**Image Requirements The Script Should Handle**

The script should check that each picture:

```text
exists
has a normal extension like .jpg, .jpeg, or .png
is not corrupt
is RGB or safely convertible to RGB
has a reasonable pixel size
has a reasonable file size
has a stable filename with no spaces or unusual characters
```

For Kindle, I would usually convert photos/illustrations to JPEG unless transparency is needed. Use PNG only where transparency or sharp line art matters.

The script should probably normalize image names like this:

```text
picture1.jpg  -> images/picture-001.jpg
picture2.png  -> images/picture-002.png
```

For reflowable books, images should usually be inserted with CSS like:

```css
img {
  max-width: 100%;
  height: auto;
}
```

Avoid fixed pixel-width text layouts unless you are intentionally making a fixed-layout book.

**Important Formatting Rules**

The script should avoid:

```text
page numbers
headers
footers
manual line breaks at the end of every line
text boxes
absolute-positioned normal body text
a cover image embedded as the first manuscript page
```

Those are common eBook formatting problems. Amazon’s guide specifically notes that eBooks are reflowable, so page numbers, headers, and footers do not apply.

The script should create:

```text
title page
copyright page
table of contents
chapters
optional about-the-author page
```

Example title page XHTML:

```html
<section class="title-page">
  <h1>My Story Title</h1>
  <p>by Your Name</p>
</section>
```

Example chapter page XHTML:

```html
<section epub:type="chapter">
  <h1>Chapter 1</h1>

  <p>Once upon a time...</p>

  <figure>
    <img src="images/picture-001.jpg" alt="A forest road at sunset" />
  </figure>

  <p>The road disappeared into the forest.</p>
</section>
```

**Validation Tools The Script Should Call**

The Python script can create the EPUB, but you should still validate outside Python.

Use **Kindle Previewer** to check the result before uploading. Amazon recommends validating EPUB files with Kindle Previewer before upload. Kindle Previewer also has command-line options for conversion, quality checks, logs, and previewing.

Conceptually:

```bash
kindlepreviewer book.epub -qualitychecks -log -output dist
```

And for conversion:

```bash
kindlepreviewer book.epub -convert -output dist
```

The exact executable path depends on where Kindle Previewer is installed.

I’d also use EPUBCheck:

```bash
java -jar epubcheck.jar book.epub
```

EPUBCheck catches EPUB specification errors; Kindle Previewer catches Kindle-specific rendering and publishing issues. Use both if possible.

**A Reasonable Script Interface**

I would design the script like this:

```bash
python make_kindle_book.py \
  --story story.txt \
  --images . \
  --metadata metadata.json \
  --output dist/my-book.epub
```

Optional arguments:

```bash
--cover cover.jpg
--fixed-layout
--image-placement inline
--resize-images
--validate
--kindle-preview
```

But for KDP, I would treat `--cover` carefully: the script can use it for local preview builds, but the KDP upload workflow normally wants the cover supplied separately during title setup.

**Minimal Script Skeleton**

A real script would be longer, but structurally it needs something like this:

```python
from pathlib import Path
import json
from PIL import Image
from ebooklib import epub
from bs4 import BeautifulSoup

def load_metadata(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def optimize_image(src, dst, max_width=1800):
    dst.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(src) as img:
        img = img.convert("RGB")

        if img.width > max_width:
            ratio = max_width / img.width
            new_size = (max_width, int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)

        img.save(dst, "JPEG", quality=88, optimize=True)

def parse_story(text):
    chapters = []
    current = {"title": "Start", "blocks": []}

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("# "):
            if current["blocks"]:
                chapters.append(current)
            current = {"title": line[2:].strip(), "blocks": []}

        elif line.startswith("[image:") and line.endswith("]"):
            image_name = line[len("[image:"):-1].strip()
            current["blocks"].append({"type": "image", "src": image_name})

        else:
            current["blocks"].append({"type": "paragraph", "text": line})

    if current["blocks"]:
        chapters.append(current)

    return chapters

def chapter_to_xhtml(chapter, image_map):
    html = [f"<h1>{chapter['title']}</h1>"]

    for block in chapter["blocks"]:
        if block["type"] == "paragraph":
            html.append(f"<p>{block['text']}</p>")
        elif block["type"] == "image":
            src = image_map[block["src"]]
            html.append(
                f'<figure><img src="{src}" alt="" /></figure>'
            )

    return "\n".join(html)

def build_epub(story_path, metadata_path, output_path):
    metadata = load_metadata(metadata_path)
    story_text = Path(story_path).read_text(encoding="utf-8")
    chapters = parse_story(story_text)

    book = epub.EpubBook()
    book.set_identifier(metadata.get("identifier", "my-book"))
    book.set_title(metadata["title"])
    book.set_language(metadata.get("language", "en"))
    book.add_author(metadata["author"])

    css = """
body {
  font-family: serif;
  line-height: 1.4;
}

h1 {
  text-align: center;
  page-break-before: always;
}

figure {
  margin: 1em 0;
  text-align: center;
}

img {
  max-width: 100%;
  height: auto;
}
"""

    style_item = epub.EpubItem(
        uid="style",
        file_name="styles/styles.css",
        media_type="text/css",
        content=css,
    )
    book.add_item(style_item)

    image_map = {}
    image_items = []

    for image_path in sorted(Path(".").glob("picture*.*")):
        clean_name = f"images/{image_path.stem}.jpg"
        optimized_path = Path("build") / clean_name
        optimize_image(image_path, optimized_path)

        item = epub.EpubItem(
            uid=image_path.stem,
            file_name=clean_name,
            media_type="image/jpeg",
            content=optimized_path.read_bytes(),
        )
        book.add_item(item)
        image_items.append(item)
        image_map[image_path.name] = clean_name

    epub_chapters = []

    for index, chapter in enumerate(chapters, start=1):
        xhtml = chapter_to_xhtml(chapter, image_map)

        epub_chapter = epub.EpubHtml(
            title=chapter["title"],
            file_name=f"chapter-{index:03}.xhtml",
            lang=metadata.get("language", "en"),
        )
        epub_chapter.content = xhtml
        epub_chapter.add_item(style_item)

        book.add_item(epub_chapter)
        epub_chapters.append(epub_chapter)

    book.toc = epub_chapters
    book.spine = ["nav"] + epub_chapters

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    epub.write_epub(output_path, book)

if __name__ == "__main__":
    build_epub(
        story_path="story.txt",
        metadata_path="metadata.json",
        output_path="book.epub",
    )
```

That skeleton is not quite production-ready because it needs stronger XHTML escaping, better image-marker handling, better error messages, and validation integration. But it shows the right structure.

**The Main Decision**

The biggest thing your script needs is a decision about book type:

```text
Mostly text story with pictures between sections:
Use reflowable EPUB.

Picture book where each page must look exactly designed:
Use fixed-layout EPUB or Kindle Create.
```

For your described setup, `story.txt` plus ten pictures, I’d start with a **reflowable EPUB generator** unless the pictures are full-page illustrated spreads where the text placement must be exact. Then validate it in Kindle Previewer, upload the EPUB to KDP, and provide the cover separately in the KDP title setup.
```

## 使用 MALA：诊断

```text
The original input is an under-formed implementation goal rather than a fully answerable question. It points in a useful direction, but “convert my files into a Kindle format” mixes together several possible targets: Amazon KDP upload format, Kindle device reading format, EPUB packaging, KPF generation, and manuscript/image layout decisions.

**Problems in the original input**

- What is missing
  - `Target`: Publish successfully through Amazon KDP, create a file readable on Kindle devices, or automate local preview/testing? These are related but not identical.
  - `Object`: The actual structure of `story.txt` is unknown. It could be plain paragraphs, chapter headings, Markdown, scene breaks, captions, or unstructured text.
  - `Unknown`: The specific missing knowledge is not just “what does Python need,” but “what inputs, metadata, formatting rules, and output format should the script require to produce a valid KDP-ready ebook?”
  - `Criterion`: No success condition is stated. For example: “uploads to KDP without validation errors,” “looks good in Kindle Previewer,” “supports reflowable text,” or “places the ten pictures at specified points.”
  - `Constraint`: No constraints are given for book type, layout style, image placement, cover, table of contents, metadata, toolchain, or whether non-Python tools are allowed.
  - `Evidence`: It is not stated what would update the answer: KDP validation result, Kindle Previewer result, EPUB validator output, image rendering quality, or a test upload.
  - `Boundary`: It is unclear whether the script should only package manuscript files, or also handle cover creation, KDP metadata, pricing, ISBN, publishing, and account setup.

- What is mixed
  - “Kindle format” mixes `KPF`, `EPUB`, older Kindle/MOBI expectations, and KDP upload formats.
  - “story.txt and ten pictures” mixes source assets with layout decisions. The script needs to know where each picture belongs, not merely that ten pictures exist.
  - “Publish an e-book on Amazon” mixes file conversion with the broader publishing workflow: manuscript preparation, cover, metadata, previewing, upload, rights, categories, pricing, and KDP account steps.

- What is wrong
  - Treating `story.txt + picture1..picture10` as enough information is mismatched. Those files are raw material, not a complete ebook specification.
  - Treating “Kindle format” as a single script output is mismatched. According to Amazon KDP, commonly supported manuscript formats include `KPF`, `EPUB`, `DOC/DOCX`, `HTML/ZIP`, `RTF`, `TXT`, and `PDF`, while Kindle Create can export `KPF` and `EPUB`; Amazon describes `KPF` as preferred for KDP, and `EPUB` as a supported format when it meets Kindle Publishing Guidelines. Sources: [KDP supported eBook formats](https://kdp.amazon.com/help/topic/G200634390), [Kindle Create export formats](https://kdp.amazon.com/help/topic/GUGQ4WDZ92F733GC).
  - Assuming Python should directly create Amazon’s preferred `KPF` is probably mismatched. For an automated Python workflow, `EPUB` is usually the practical target; `KPF` is normally produced by Amazon Kindle Create.
```

## 使用 MALA：修复后的问题

```text
> Given a plain-text manuscript file named `story.txt` and ten image files named `picture1` through `picture10`, what inputs, metadata, file-structure rules, and validation steps would a Python script need in order to generate a reflowable `EPUB` suitable for Amazon KDP upload and Kindle Previewer testing, with the images inserted at defined locations in the story?
```

## 修复后的最终回答

```text
A Python script would need more than `story.txt` and ten image files. It would need a small book specification that tells it how to turn those raw files into a valid ebook package.

At minimum, the script would need these things:

1. Output target

   For a Python-based workflow, the most practical target is usually `EPUB`, not `MOBI` or direct `KPF`.

   Amazon KDP currently supports `EPUB` and says it should meet Kindle Publishing Guidelines. Amazon also says `KPF` is a preferred format for KDP and is created with Kindle Create, but `KPF` is not the easiest format to generate yourself from Python. So the sensible Python workflow is:

   ```text
   story.txt + images + metadata
   -> Python script
   -> EPUB
   -> validate EPUB
   -> inspect in Kindle Previewer
   -> upload to KDP
   ```

   If you specifically want `KPF`, the more natural route is:

   ```text
   manuscript
   -> Kindle Create
   -> KPF
   -> upload to KDP
   ```

   Source: Amazon KDP lists `KPF` and `EPUB` among supported formats, and Kindle Create exports `KPF` and `EPUB`: [KDP supported eBook formats](https://kdp.amazon.com/help/topic/G200634390), [Getting Started with Kindle Create](https://kdp.amazon.com/help/topic/GUGQ4WDZ92F733GC).

2. Book metadata

   The script needs metadata for the EPUB package, such as:

   ```yaml
   title: "My Story"
   author: "Your Name"
   language: "en"
   publisher: "Optional Publisher Name"
   publication_date: "2026-05-09"
   description: "Short description, optional inside the EPUB"
   rights: "Copyright 2026 Your Name. All rights reserved."
   identifier: "optional ISBN or generated UUID"
   ```

   KDP’s public listing metadata, categories, keywords, price, royalty, and territory rights are usually entered in KDP itself, not embedded only in the EPUB. But the EPUB still needs internal metadata such as title, author, language, and identifier.

3. Manuscript structure

   A plain `.txt` file does not tell the script enough unless you define conventions. The script needs to know how to detect:

   ```text
   title page
   copyright page
   dedication
   table of contents entries
   chapter starts
   paragraphs
   scene breaks
   image insertion points
   captions
   back matter
   ```

   A workable convention might look like this inside `story.txt`:

   ```markdown
   # My Story

   ## Chapter 1

   The first paragraph begins here.

   [[image: picture1.jpg]]
   Caption: The old house at sunset.

   The story continues.

   * * *

   A new scene begins.

   ## Chapter 2

   [[image: picture2.jpg]]
   ```

   Without markers like `## Chapter 1` and `[[image: picture1.jpg]]`, the script has to guess where chapters and pictures belong, which is not reliable.

4. Image manifest

   The script needs the exact filenames, formats, placement, captions, and alt text. Do not rely only on `picture1`, `picture2`, etc.

   Better:

   ```yaml
   images:
     - id: picture1
       file: picture1.jpg
       insert_after: "Chapter 1 opening"
       caption: "The old house at sunset."
       alt: "A small house under an orange evening sky."
     - id: picture2
       file: picture2.png
       insert_after: "Chapter 2 start"
       caption: ""
       alt: "A map of the village."
   ```

   The script also needs to verify that each image exists and is in a web/ebook-friendly format such as `JPG` or `PNG`. Amazon’s Kindle Create guidance says images should be `JPG` or `PNG`, and recommends image quality sufficient for Kindle devices. Source: [Prepare Reflowable and Print Books with Kindle Create](https://kdp.amazon.com/en_US/help/topic/G7R2L7V5X6SJH948).

5. Cover file

   The ten pictures inside the book are not necessarily the cover. KDP usually treats the cover as a separate publishing asset, even if the EPUB can also contain cover metadata.

   The script should know:

   ```yaml
   cover_image: cover.jpg
   ```

   If you do not have a cover yet, the script can still generate an EPUB manuscript, but it should not pretend the book is fully publication-ready.

6. EPUB file structure

   An EPUB is basically a ZIP package with a strict internal structure. A Python script would need to create files like:

   ```text
   book.epub
   ├── mimetype
   ├── META-INF/
   │   └── container.xml
   └── OEBPS/
       ├── content.opf
       ├── nav.xhtml
       ├── styles.css
       ├── chapter-001.xhtml
       ├── chapter-002.xhtml
       ├── images/
       │   ├── picture1.jpg
       │   ├── picture2.jpg
       │   └── ...
       └── cover.jpg
   ```

   The important pieces are:

   ```text
   mimetype
   ```

   Identifies the ZIP as an EPUB.

   ```text
   META-INF/container.xml
   ```

   Points reading systems to the main package file.

   ```text
   OEBPS/content.opf
   ```

   Contains metadata, manifest, reading order, image references, CSS references, and cover declaration.

   ```text
   OEBPS/nav.xhtml
   ```

   Contains the EPUB navigation table of contents.

   ```text
   chapter-001.xhtml, chapter-002.xhtml, ...
   ```

   The actual book content, converted from your text into valid XHTML.

   ```text
   styles.css
   ```

   Basic formatting for paragraphs, headings, images, captions, scene breaks, and front matter.

7. Text-to-XHTML conversion rules

   The script needs rules for converting plain text into valid ebook HTML/XHTML.

   It should handle:

   ```text
   escaping special characters like &, <, >
   preserving paragraph breaks
   converting chapter headings to <h1> or <h2>
   converting scene breaks to styled separators
   inserting images as <figure> blocks
   adding captions as <figcaption>
   adding alt text for accessibility
   splitting chapters into separate XHTML files
   generating a table of contents from chapter headings
   ```

   Example generated XHTML fragment:

   ```html
   <section epub:type="chapter">
     <h1>Chapter 1</h1>

     <p>The first paragraph begins here.</p>

     <figure>
       <img src="images/picture1.jpg" alt="A small house under an orange evening sky." />
       <figcaption>The old house at sunset.</figcaption>
     </figure>

     <p>The story continues.</p>
   </section>
   ```

8. CSS rules for Kindle-friendly layout

   The script should generate restrained CSS. For a reflowable Kindle ebook, avoid fixed pixel-heavy layouts unless you are intentionally making a fixed-layout book.

   Basic CSS might include:

   ```css
   body {
     margin: 0;
     padding: 0;
   }

   p {
     text-indent: 1.2em;
     margin: 0;
   }

   h1 {
     text-align: center;
     margin-top: 2em;
     margin-bottom: 1.5em;
   }

   figure {
     margin: 1.5em 0;
     text-align: center;
   }

   img {
     max-width: 100%;
     height: auto;
   }

   figcaption {
     font-size: 0.9em;
     text-align: center;
     margin-top: 0.5em;
   }

   .scene-break {
     text-align: center;
     margin: 1.5em 0;
     text-indent: 0;
   }
   ```

9. Validation tools

   The script should not merely create `book.epub`; it should validate the result.

   Useful checks:

   ```text
   Are all referenced images present?
   Are all image filenames valid and correctly linked?
   Is every chapter valid XHTML?
   Does content.opf list every file in the manifest?
   Does the spine list chapters in the correct reading order?
   Does nav.xhtml contain the right table of contents?
   Does the EPUB pass epubcheck?
   Does it display correctly in Kindle Previewer?
   ```

   Amazon recommends using Kindle Previewer to check ebook conversion quality before upload. Source: [KDP supported eBook formats](https://kdp.amazon.com/help/topic/G200634390).

10. A clear input folder layout

   A practical folder layout could be:

   ```text
   my_book/
   ├── story.txt
   ├── book.yaml
   ├── cover.jpg
   └── images/
       ├── picture1.jpg
       ├── picture2.jpg
       ├── picture3.jpg
       ├── picture4.jpg
       ├── picture5.jpg
       ├── picture6.jpg
       ├── picture7.jpg
       ├── picture8.jpg
       ├── picture9.jpg
       └── picture10.jpg
   ```

   `book.yaml` would contain the metadata and image placement rules. `story.txt` would contain the manuscript with chapter and image markers.

A minimal Python script would therefore need these capabilities:

```text
read book.yaml
read story.txt
parse chapters
parse image markers
verify all image files exist
convert text to XHTML
copy images into the EPUB structure
generate CSS
generate nav.xhtml table of contents
generate content.opf package metadata
zip everything into a valid .epub
run validation or at least report files to check with epubcheck and Kindle Previewer
```

The most important design decision is this: the script should not try to infer the book from filenames alone. It should require a manifest or markup convention that tells it what the book is, where each picture goes, and what “done” means.

A good first target would be:

```text
Generate a reflowable EPUB that opens cleanly in Kindle Previewer, has a working table of contents, includes all ten images at explicit manuscript markers, and reports missing metadata or missing image files before building.
```

That is judgeable, actionable, and testable.
```

## 结构变化

- 预期结构问题：`missing constraints and hidden representation choices`
- Baseline 标注：`not_applicable`
- Baseline 分数：ambiguity handling `2`，answer adequacy `2`，total `4`
- Treatment 分数：diagnosis `2`，repair `2`，answer discipline `2`，intervention fit `2`，total `8`
- Judge 说明：The baseline already does unusually strong ambiguity management by distinguishing EPUB/KPF, reflowable/fixed layout, metadata, image placement, cover handling, and validation. The treatment correctly diagnoses the hidden representation choices and turns the prompt into a bounded, testable EPUB workflow, with MALA-level structure justified by the deep workflow-design ambiguity.
- Repair notes：

```text
- What was added
  - The output target was specified as a reflowable `EPUB` suitable for KDP upload and Kindle Previewer testing.
  - A success criterion was added: valid EPUB, working table of contents, images inserted at defined locations, no missing files, and successful visual inspection in Kindle Previewer.
  - Required metadata was added: title, author, language, identifier, rights, publication date, and optional publisher/description.
  - Required evidence was added: EPUB validation, Kindle Previewer result, and KDP upload compatibility.

- What was separated
  - The general goal of “publishing on Amazon” was separated from the narrower file-generation task.
  - Raw assets were separated from layout decisions.
  - `EPUB`, `KPF`, and older “Kindle format” assumptions were separated.
  - Interior images were separated from the cover image.

- What was corrected
  - The target was corrected from vague “Kindle format” to a practical Python target: `EPUB`.
  - The assumption that `story.txt` plus numbered pictures is enough was corrected. The script also needs structure, metadata, placement rules, and validation.
  - The script’s role was corrected from “publish my ebook” to “generate a KDP-ready manuscript file that can be previewed and uploaded.”
```

## Artifact links

- [Baseline JSON](../../benchmark/public-prompts-v0.1/runs/baseline/case-11.json)
- [Treatment JSON](../../benchmark/public-prompts-v0.1/runs/treatment/case-11.json)
- [Judgment JSON](../../benchmark/public-prompts-v0.1/judgments/case-11.json)
