source "https://rubygems.org"

ruby "3.3.11"

gem "jekyll", "~> 4.3"
gem "jekyll-sass-converter", "~> 3.0"
gem "jekyll-seo-tag"
gem "jekyll-sitemap"
gem "webrick"

group :development, :test do
  # Dead-link + broken-image checker — runs against _site/ to catch
  # internal link regressions before deploy. See .github/scripts/link-check.sh.
  gem "html-proofer", "~> 5.0"
end
