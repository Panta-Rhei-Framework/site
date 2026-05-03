# frozen_string_literal: true

# og_card_generator.rb — Auto-generated OG / social-preview cards (Tier 1).
#
# Renders a parameterized 1200×630 card per page (page title, lane chip, type
# tag, lane-keyed motif, Panta Rhei mark) into _site/assets/og-cards/<slug>.svg.
# When `rsvg-convert` is on PATH it also rasterizes a PNG for load-bearing
# pages (anything outside the bibliography collection plus a small set of
# always-rasterize prefixes). Bibliography entries fall back to the SVG —
# modern OG consumers (Twitter/X, Discord, WhatsApp, Telegram) render SVG;
# LinkedIn/Slack prefer PNG, hence the rasterize cutoff.
#
# Resolution chain (see _includes/head.html):
#   1. page.og_image (explicit override — Tier 2 hand-crafted images)
#   2. /assets/og-cards/<slug>.png   (auto-generated PNG, when rasterized)
#   3. /assets/og-cards/<slug>.svg   (auto-generated SVG, always written)
#   4. /assets/og-image.png          (legacy site-wide fallback)
#
# Pages opt out by setting `og_card: false` in front matter.

require "fileutils"
require "open3"

module PantaRhei
  module OgCardGenerator
    OUTPUT_DIR        = File.join("assets", "og-cards").freeze
    CARD_WIDTH        = 1200
    CARD_HEIGHT       = 630
    SITE_TITLE        = "Panta Rhei Research Program"
    SITE_HOST         = "panta-rhei.site"

    # Lane palette — mirrors --lane-* tokens in _sass/_variables.scss.
    LANES = {
      "discover"     => { name: "Discover",     color: "#a8792a", soft: "#f7efe1" },
      "program"      => { name: "Program",      color: "#163e64", soft: "#e8f0f6" },
      "agenda"       => { name: "Agenda",       color: "#7a3f72", soft: "#f4e8f1" },
      "corpus"       => { name: "Corpus",       color: "#3a3d42", soft: "#ecefed" },
      "results"      => { name: "Results",      color: "#2f6f6a", soft: "#e5f2ef" },
      "verify"       => { name: "Verify",       color: "#4d4a8a", soft: "#eeedf7" },
      "publications" => { name: "Publications", color: "#7a4b36", soft: "#f3ebe6" },
      "impact"       => { name: "Impact",       color: "#66723a", soft: "#eef1e2" },
      "engage"       => { name: "Engage",       color: "#2f7a78", soft: "#e3f2f1" },
      "support"      => { name: "Panta Rhei",   color: "#737373", soft: "#f0f0ee" }
    }.freeze

    # Lane-keyed motif: each lane gets a distinct subtle background pattern
    # drawn behind the card content. Kept low-opacity so text always wins.
    LANE_MOTIFS = {
      "discover"     => :rays,
      "program"      => :grid,
      "agenda"       => :ledger,
      "corpus"       => :stack,
      "results"      => :wave,
      "verify"       => :checks,
      "publications" => :columns,
      "impact"       => :arrows,
      "engage"       => :nodes,
      "support"      => :grid
    }.freeze

    # Pages outside these collections always get a rasterized PNG. Bibliography
    # entries (~8.4k) fall back to SVG-only to keep build time bounded.
    SKIP_PNG_COLLECTIONS = ["bibliography"].freeze

    # Regex for whether the rasterizer is present. Probed once.
    @rsvg_available = nil

    module_function

    def rsvg_available?
      return @rsvg_available unless @rsvg_available.nil?

      out, _err, status = Open3.capture3("rsvg-convert", "--version")
      @rsvg_available = status.success? && !out.empty?
    rescue Errno::ENOENT
      @rsvg_available = false
    end

    # Best-effort lane derivation when front matter doesn't specify one.
    # Mirrors the URL-based lane mapping in _layouts/default.html.
    def lane_for(page)
      lane = page.data["v2_lane"] || page.data["lane"]
      lane = nil if lane && lane.to_s.strip.empty?
      url = page.url.to_s
      lane ||= case url
               when %r{^/discover/}                     then "discover"
               when %r{^/program/research-agenda/}      then "agenda"
               when %r{^/program/}, %r{^/research-program/} then "program"
               when %r{^/corpus/}, %r{^/registry/}      then "corpus"
               when %r{^/results/}                      then "results"
               when %r{^/verify/}                       then "verify"
               when %r{^/publications/}, %r{^/bibliography/}, %r{^/research-notes/} then "publications"
               when %r{^/impact/}                       then "impact"
               when %r{^/engage/}, %r{^/contact/}, %r{^/about/} then "engage"
               else "support"
               end
      # Normalize legacy aliases.
      lane = "program" if lane == "research-program"
      lane = "corpus" if lane == "registry"
      lane = "support" if %w[utility bibliography].include?(lane)
      lane = "support" unless LANES.key?(lane)
      lane
    end

    def page_type(page)
      type = page.data["type"]
      return type.to_s.strip if type && !type.to_s.strip.empty?
      layout = page.data["layout"].to_s
      case layout
      when "homepage"                          then "Homepage"
      when "publication-book", "publication-archive-book" then "Book"
      when "publication-chapter"               then "Chapter"
      when "publication-part"                  then "Part"
      when "corpus-monograph-book"             then "Monograph"
      when "corpus-monograph-part"             then "Monograph Part"
      when "corpus-monograph-chapter"          then "Monograph Chapter"
      when "registry-object"                   then "Registry Object"
      when "registry-book"                     then "Registry"
      when "registry-noteworthy-result"        then "Noteworthy Result"
      when "result-page", "result-topic"       then "Result"
      when "prediction-page"                   then "Prediction"
      when "falsification-page"                then "Falsification"
      when "research-note"                     then "Research Note"
      when "bibliography-entry"                then "Bibliography"
      when "glossary-entry"                    then "Glossary"
      when "problem-ledger-item"               then "Problem Ledger"
      when "recovery-requirement-item"         then "Recovery Requirement"
      when "impact-paper"                      then "Paper"
      when "impact-portfolio"                  then "Portfolio"
      when "public-good-briefing"              then "Briefing"
      when "taulib-doc"                        then "Documentation"
      when "changelog-entry"                   then "Changelog"
      when "program-doc"                       then "Program"
      else                                          "Page"
      end
    end

    # Title used on the card. Prefers the Unicode-safe variant when present,
    # then strips any HTML/Liquid tags the bibliography titles can carry.
    def card_title(page)
      raw = page.data["og_card_title"] ||
            page.data["title_plain"]   ||
            page.data["title"]         ||
            SITE_TITLE
      strip_html(raw.to_s)
    end

    def strip_html(text)
      text.gsub(/<[^>]+>/, "").gsub(/&amp;/, "&").gsub(/&[a-z]+;/, "").strip
    end

    def xml_escape(text)
      text.to_s
          .gsub("&", "&amp;")
          .gsub("<", "&lt;")
          .gsub(">", "&gt;")
          .gsub("\"", "&quot;")
          .gsub("'", "&apos;")
    end

    # Naive but effective word-wrap: hard cap on lines, soft cap on width
    # measured in characters. We tune by glyph-width heuristics rather than
    # real metrics — the SVG renderer ignores fancy text-layout anyway.
    def wrap_title(title, max_chars_per_line: 22, max_lines: 3)
      words = title.split(/\s+/)
      lines = []
      current = +""
      words.each do |word|
        candidate = current.empty? ? word : "#{current} #{word}"
        if candidate.length > max_chars_per_line && !current.empty?
          lines << current
          current = word.dup
        else
          current = candidate
        end
        break if lines.length >= max_lines
      end
      lines << current unless current.empty? || lines.length >= max_lines
      lines = lines.first(max_lines)
      # If we truncated mid-title, append an ellipsis to the last line.
      if lines.length == max_lines && words.length > lines.join(" ").split(/\s+/).length
        last = lines[-1]
        lines[-1] = last.length > max_chars_per_line - 1 ? "#{last[0, max_chars_per_line - 1]}…" : "#{last}…"
      end
      lines
    end

    def slug_for(page)
      url = page.url.to_s
      url = "/" if url.empty?
      slug = url.sub(%r{^/}, "").sub(%r{/$}, "")
      slug = "index" if slug.empty?
      slug.gsub(%r{[/\\]}, "__").gsub(/[^a-zA-Z0-9_.-]/, "-")
    end

    # The SVG itself. Kept compact — every page gets one of these so the bytes
    # add up at the bibliography scale. ~3 KB each.
    def render_svg(title:, lane_key:, type_label:)
      lane     = LANES.fetch(lane_key)
      motif    = LANE_MOTIFS.fetch(lane_key)
      lines    = wrap_title(title)
      title_y0 = case lines.length
                 when 1 then 320
                 when 2 then 270
                 else        220
                 end

      title_tspans = lines.each_with_index.map do |line, i|
        y = title_y0 + (i * 76)
        %(<tspan x="80" y="#{y}">#{xml_escape(line)}</tspan>)
      end.join

      <<~SVG
        <?xml version="1.0" encoding="UTF-8"?>
        <svg xmlns="http://www.w3.org/2000/svg" width="#{CARD_WIDTH}" height="#{CARD_HEIGHT}" viewBox="0 0 #{CARD_WIDTH} #{CARD_HEIGHT}" role="img" aria-label="#{xml_escape(title)} — #{xml_escape(SITE_TITLE)}">
          <defs>
            <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#f6f7f3"/>
              <stop offset="60%" stop-color="#{lane[:soft]}" stop-opacity="0.6"/>
              <stop offset="100%" stop-color="#{lane[:soft]}"/>
            </linearGradient>
          </defs>
          <rect width="#{CARD_WIDTH}" height="#{CARD_HEIGHT}" fill="url(#bg)"/>
          #{render_motif(motif, lane[:color])}
          <!-- Top accent bar in lane color. -->
          <rect x="0" y="0" width="#{CARD_WIDTH}" height="8" fill="#{lane[:color]}"/>
          <!-- Lane chip -->
          <g transform="translate(80, 80)">
            <rect width="#{12 + (lane[:name].length * 11) + 12}" height="36" rx="18" fill="#{lane[:color]}"/>
            <text x="#{12 + (lane[:name].length * 11) / 2 + 6}" y="24" font-family="Inter, Helvetica, Arial, sans-serif" font-size="16" font-weight="600" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">#{xml_escape(lane[:name].upcase)}</text>
          </g>
          <!-- Type tag -->
          <text x="80" y="160" font-family="Inter, Helvetica, Arial, sans-serif" font-size="20" font-weight="500" fill="#5b6772" letter-spacing="1.5">#{xml_escape(type_label.upcase)}</text>
          <!-- Page title -->
          <text font-family="Iowan Old Style, Palatino, Georgia, serif" font-size="62" font-weight="500" fill="#182027">
            #{title_tspans}
          </text>
          <!-- Footer rule -->
          <line x1="80" y1="540" x2="#{CARD_WIDTH - 80}" y2="540" stroke="#{lane[:color]}" stroke-opacity="0.25" stroke-width="1"/>
          <!-- Panta Rhei mark -->
          <g transform="translate(80, 568)">
            <!-- Small flow-line glyph: three offset arcs evoking continuous flow. -->
            <path d="M 0 14 Q 8 4, 16 14 T 32 14" stroke="#{lane[:color]}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
            <text x="48" y="20" font-family="Inter, Helvetica, Arial, sans-serif" font-size="22" font-weight="700" fill="#182027">Panta Rhei</text>
            <text x="48" y="42" font-family="Inter, Helvetica, Arial, sans-serif" font-size="14" font-weight="500" fill="#5b6772">Research Program</text>
          </g>
          <!-- Site URL anchor -->
          <text x="#{CARD_WIDTH - 80}" y="588" font-family="Inter, Helvetica, Arial, sans-serif" font-size="16" font-weight="500" fill="#5b6772" text-anchor="end">#{SITE_HOST}</text>
        </svg>
      SVG
    end

    # Lane-keyed motifs — drawn at low opacity behind the title block.
    # The geometry suggests the lane's character without screaming for attention.
    def render_motif(motif, color)
      case motif
      when :grid
        # Programmatic gridlines — Program / Support feel.
        lines = []
        (0..12).each do |i|
          x = 60 + (i * 90)
          lines << %(<line x1="#{x}" y1="380" x2="#{x}" y2="510" stroke="#{color}" stroke-opacity="0.06" stroke-width="1"/>)
        end
        (0..3).each do |j|
          y = 380 + (j * 40)
          lines << %(<line x1="60" y1="#{y}" x2="1140" y2="#{y}" stroke="#{color}" stroke-opacity="0.06" stroke-width="1"/>)
        end
        lines.join
      when :rays
        # Radial rays — Discover (way-finding).
        lines = []
        cx = 1080
        cy = 540
        (0..10).each do |i|
          angle = (i * 9) - 180
          rad = angle * Math::PI / 180
          x2 = cx + (Math.cos(rad) * 360)
          y2 = cy + (Math.sin(rad) * 360)
          lines << %(<line x1="#{cx}" y1="#{cy}" x2="#{x2.round(1)}" y2="#{y2.round(1)}" stroke="#{color}" stroke-opacity="0.07" stroke-width="1"/>)
        end
        lines.join
      when :ledger
        # Ledger lines — Agenda.
        (0..5).map do |i|
          y = 410 + (i * 30)
          %(<line x1="60" y1="#{y}" x2="1140" y2="#{y}" stroke="#{color}" stroke-opacity="0.07" stroke-width="1"/>)
        end.join
      when :stack
        # Stacked pages — Corpus.
        offsets = [0, 18, 36]
        offsets.each_with_index.map do |dx, i|
          x = 1000 - dx
          y = 460 - (i * 8)
          %(<rect x="#{x}" y="#{y}" width="120" height="120" fill="none" stroke="#{color}" stroke-opacity="0.09" stroke-width="1.5" rx="6"/>)
        end.join
      when :wave
        # Sine wave — Results (process / dynamics).
        d = +"M 0 480"
        (0..1200).step(20) do |x|
          y = 480 + (Math.sin(x * 0.012) * 22)
          d << " L #{x} #{y.round(1)}"
        end
        %(<path d="#{d}" fill="none" stroke="#{color}" stroke-opacity="0.10" stroke-width="2"/>)
      when :checks
        # Check ticks — Verify.
        (0..4).map do |i|
          x = 880 + (i * 60)
          y = 470
          %(<path d="M #{x} #{y} l 10 12 l 18 -22" stroke="#{color}" stroke-opacity="0.10" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>)
        end.join
      when :columns
        # Column rules — Publications.
        (0..3).map do |i|
          x = 60 + (i * 360)
          %(<line x1="#{x}" y1="380" x2="#{x}" y2="510" stroke="#{color}" stroke-opacity="0.07" stroke-width="1"/>)
        end.join
      when :arrows
        # Outward arrows — Impact.
        (0..2).map do |i|
          y = 410 + (i * 35)
          %(<path d="M 880 #{y} l 100 0 l -8 -8 m 8 8 l -8 8" stroke="#{color}" stroke-opacity="0.10" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>)
        end.join
      when :nodes
        # Connected nodes — Engage.
        nodes = [[920, 420], [1000, 460], [1080, 420], [960, 500], [1040, 500]]
        edges = [[0, 1], [1, 2], [1, 3], [1, 4], [3, 4]]
        out = +""
        edges.each do |a, b|
          x1, y1 = nodes[a]
          x2, y2 = nodes[b]
          out << %(<line x1="#{x1}" y1="#{y1}" x2="#{x2}" y2="#{y2}" stroke="#{color}" stroke-opacity="0.10" stroke-width="1.5"/>)
        end
        nodes.each do |x, y|
          out << %(<circle cx="#{x}" cy="#{y}" r="5" fill="#{color}" fill-opacity="0.18"/>)
        end
        out
      else
        ""
      end
    end

    # Decide whether to rasterize a PNG. Bibliography entries skip — SVG is
    # served as the OG image instead. Pages can opt in/out via front matter.
    def rasterize?(page)
      return false unless rsvg_available?
      return !!page.data["og_card_rasterize"] if page.data.key?("og_card_rasterize")
      collection = page.respond_to?(:collection) ? page.collection&.label : nil
      return false if collection && SKIP_PNG_COLLECTIONS.include?(collection)
      true
    end

    def emit_card(site, page, stats)
      return if page.data["og_card"] == false
      return if page.data["og_image"] && !page.data["og_image"].to_s.strip.empty?

      slug      = slug_for(page)
      lane_key  = lane_for(page)
      title     = card_title(page)
      type_lbl  = page_type(page)
      svg       = render_svg(title: title, lane_key: lane_key, type_label: type_lbl)

      site_dir  = site.dest
      out_dir   = File.join(site_dir, OUTPUT_DIR)
      FileUtils.mkdir_p(out_dir)
      svg_path  = File.join(out_dir, "#{slug}.svg")
      File.write(svg_path, svg)
      stats[:svg] += 1

      if rasterize?(page)
        png_path = File.join(out_dir, "#{slug}.png")
        _stdout, stderr, status = Open3.capture3(
          "rsvg-convert", "-w", CARD_WIDTH.to_s, "-h", CARD_HEIGHT.to_s,
          "-o", png_path, svg_path
        )
        if status.success?
          stats[:png] += 1
        else
          warn "[og-cards] rsvg-convert failed for #{page.url}: #{stderr.strip}"
        end
      end
    end

    def all_pages(site)
      pages = []
      pages.concat(site.pages)
      site.collections.each_value { |c| pages.concat(c.docs) }
      pages
    end

    def run(site)
      stats = { svg: 0, png: 0, skipped_explicit: 0 }
      all_pages(site).each do |page|
        next if page.respond_to?(:output_ext) && page.output_ext != ".html"
        if page.data["og_image"] && !page.data["og_image"].to_s.strip.empty?
          stats[:skipped_explicit] += 1
          next
        end
        next if page.data["og_card"] == false
        emit_card(site, page, stats)
      rescue StandardError => e
        warn "[og-cards] failed for #{page.url}: #{e.class}: #{e.message}"
      end
      Jekyll.logger.info "OG cards:",
                        "#{stats[:svg]} svg + #{stats[:png]} png (#{stats[:skipped_explicit]} explicit overrides preserved)"
    end
  end
end

Jekyll::Hooks.register :site, :post_write do |site|
  PantaRhei::OgCardGenerator.run(site)
end
