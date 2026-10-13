# Migration to al-folio

## Preserved content

The existing biography, research interests, profile photo, contact links, CV text and CV PDFs are preserved. All 12 publications from 2018–2023 are represented in `_bibliography/papers.bib`; authors are transcribed from the original citations. The four 2021–2023 papers appear as selected publications. No new career information or news was invented.

The original `_publications` collection remains for existing detail links. A venue typo in the 2022 COLING bibliography entry was corrected from “CONLING 2021” to “COLING 2022”. Older source citations and descriptions remain on their detail pages.

## Sample content removed

All five sample blog posts, the draft, four sample talks, two sample teaching entries, and two sample portfolio items were removed. Demo archives, markdown instructions, terms, the sample non-menu page, comment fixtures, and the generated sample talk map were also removed. These sections are absent from navigation. Old generator utilities were removed because publications now use BibTeX.

The original `images/` and `files/` directories remain on disk to avoid discarding potentially useful user assets. `images/` is excluded from the new build; the active profile photo is copied to `assets/img/profile.jpeg`. Existing PDF URLs under `/files/` still work.

## URLs

`/`, `/publications/`, `/cv/`, `/sitemap/`, `/about/`, `/about.html`, and `/resume` are preserved. Publication detail URLs are preserved except for two entries that previously collided at `/publication/`: they now have `/publication/2022-COLING` and `/publication/2023-EMNLP`. `/publication/` redirects to the full publication list.

## Build and hosting

Theme source is pinned to al-folio v0.14.6. Only plugins required by this site's content are installed. No external blog feeds or sample resume data are fetched. Responsive image generation is disabled, so ImageMagick is not needed. News and blog sections are disabled until real content is available.

Deployment uses GitHub Actions; select GitHub Actions as the Pages source before pushing. This migration does not push changes or alter repository hosting settings.

## Verification

The production Jekyll build and `scripts/verify_site.py` pass locally. The checker confirms all local HTML links and assets resolve, all 12 publications and four selected papers render, the CV PDF and legacy aliases exist, and sample sections are absent. Playwright checks cover desktop and 390px mobile layouts, publication filtering, BibTeX expansion, navigation, loaded profile images, and light/dark switching. GitHub's Linux dependency platform is included in `Gemfile.lock`; the hosted workflow has not been run or deployed from this workspace.
