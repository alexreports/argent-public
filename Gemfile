source "https://rubygems.org"

# Use the github-pages gem to match GitHub Pages' build environment exactly.
# Comment this out and use the `jekyll` gem below if you build/deploy yourself
# (e.g. via GitHub Actions) and want the latest Jekyll.
gem "github-pages", group: :jekyll_plugins

# --- Alternative: standalone Jekyll (uncomment if not using github-pages) ---
# gem "jekyll", "~> 4.4"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end

# Windows / JRuby compatibility shims (harmless elsewhere)
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Faster file watching on macOS during local development
gem "webrick", "~> 1.8"
