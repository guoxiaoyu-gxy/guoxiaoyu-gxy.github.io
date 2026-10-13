# Xiao-Yu Guo's academic website

A Jekyll site based on [al-folio v0.14.6](https://github.com/alshedivat/al-folio/releases/tag/v0.14.6), customized for https://guoxiaoyu-gxy.github.io.

## Local preview

Install Ruby 4.0, then run:

```sh
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

On a Mac using Homebrew Ruby, add `$(brew --prefix ruby)/bin` to your PATH before running these commands. Open http://localhost:4000.

To check a production build, run `JEKYLL_ENV=production bundle exec jekyll build` followed by `python3 scripts/verify_site.py`.

## Edit content

- Biography and selected-paper section: `_pages/about.md`.
- Publications: `_bibliography/papers.bib`. Add `selected = {true}` to show a paper on the homepage. Use `doi` for the DOI identifier and `pdf` for a paper download link and `bibtex_show = {true}` for a BibTeX button.
- Presentations: `_data/presentations.yml`; add recording URLs and optional `slides` links here. Add a `video` field to the matching bibliography entry for its Video button.
- CV: `_pages/cv.md`; downloadable CV: `files/Xiaoyu_Guo_CV.pdf`.
- Profile photo: `assets/img/profile.jpeg`.
- Contact links: `_data/socials.yml`.
- Site settings: `_config.yml`.

## GitHub Pages

In the repository's **Settings → Pages → Build and deployment**, choose **GitHub Actions** as the source. The workflow in `.github/workflows/pages.yml` builds pull requests and deploys pushes to `main` or `master`. Jekyll Scholar requires this custom build instead of GitHub Pages' built-in Jekyll builder.

See [MIGRATION.md](MIGRATION.md) for the content audit and URL changes. Theme licensing is preserved in `LICENSE.al-folio`; the original repository license remains in `LICENSE`.
