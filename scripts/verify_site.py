"""Check built pages, publication migration, and local asset links."""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

site = Path('_site')
missing = set()

class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key not in ('href', 'src') or not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            path = unquote(url.path)
            target = site / path.lstrip('/') if path.startswith('/') else self.page.parent / path
            if not target.exists():
                missing.add((str(self.page), value))

for page in site.rglob('*.html'):
    parser = Links()
    parser.page = page
    parser.feed(page.read_text())
assert not missing, f'Missing local targets: {sorted(missing)}'

for path in (
    'index.html', 'publications/index.html', 'presentations/index.html', 'cv/index.html', 'about/index.html',
    'about.html', 'resume.html', 'resume/index.html', 'publication/index.html',
    'publication/2022-COLING.html', 'publication/2023-EMNLP.html',
    'files/Xiaoyu_Guo_CV.pdf', 'sitemap.xml',
):
    assert (site / path).exists(), f'Missing migrated page: {path}'
for section in ('talks', 'teaching', 'portfolio', 'posts', 'markdown', 'talkmap'):
    assert not (site / section).exists(), f'Sample section still published: {section}'

publications = (site / 'publications/index.html').read_text()
bibliography = Path('_bibliography/papers.bib').read_text()
entry_count = len(re.findall(r'^@(?:article|inproceedings)\{', bibliography, re.M))
selected_count = len(re.findall(r'selected\s*=\s*\{true\}', bibliography))
assert publications.count('class="title"') == entry_count, 'Publication count differs from bibliography'
assert (site / 'index.html').read_text().count('class="title"') == selected_count, 'Selected paper count differs from bibliography'
for page in ('index.html', 'publications/index.html', 'cv/index.html'):
    text = (site / page).read_text()
    assert '{{version}}' not in text, f'Unresolved library version in {page}'
    assert 'Write your biography here' not in text, f'Sample biography in {page}'
print(f'PASS: migrated pages, redirects, PDF, {entry_count} publications, {selected_count} selected papers, and local links; sample sections absent.')
