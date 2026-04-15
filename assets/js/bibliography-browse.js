// Bibliography Browse — vanilla JS filter/sort module
// Progressive enhancement: works on static HTML with no dependencies.
// Structurally mirrors /assets/js/results-browse.js with different filter
// dimensions (domain/role/type/status/book/decade) and sort modes
// (year/alpha/citations) appropriate to a bibliographic corpus.

(function () {
  'use strict';

  var controls = document.getElementById('bibliography-browse-controls');
  var grid = document.getElementById('bibliography-browse-grid');
  if (!controls || !grid) return;

  var cards = Array.prototype.slice.call(grid.querySelectorAll('.biblio-card'));
  var countEl = document.getElementById('bibliography-count');
  var emptyEl = document.getElementById('bibliography-empty');
  var clearBtn = document.getElementById('bibliography-clear-filters');
  var emptyClearBtn = document.getElementById('bibliography-empty-clear');

  // Multi-value filter state — Set of active values per dimension.
  // Mirrors the results-browse state model exactly.
  var state = {
    domain: new Set(),
    role: new Set(),
    type: new Set(),
    status: new Set(),
    book: new Set(),
    decade: new Set()
  };

  var DEFAULT_SORT = 'year';
  var VALID_SORTS = ['year', 'alpha', 'citations'];
  var sortMode = DEFAULT_SORT;
  var originalOrder = cards.slice(); // preserve the Liquid order

  // ---------- URL query param sync ----------
  function readStateFromUrl() {
    var params = new URLSearchParams(window.location.search);
    Object.keys(state).forEach(function (key) {
      state[key].clear();
      var raw = params.get(key);
      if (raw) {
        raw.split(',').forEach(function (v) {
          if (v) state[key].add(v);
        });
      }
    });
    var sortParam = params.get('sort');
    if (sortParam && VALID_SORTS.indexOf(sortParam) !== -1) {
      sortMode = sortParam;
    } else {
      sortMode = DEFAULT_SORT;
    }
  }

  function writeStateToUrl() {
    var params = new URLSearchParams();
    Object.keys(state).forEach(function (key) {
      if (state[key].size > 0) {
        params.set(key, Array.prototype.join.call(Array.from(state[key]), ','));
      }
    });
    if (sortMode !== DEFAULT_SORT) {
      params.set('sort', sortMode);
    }
    var qs = params.toString();
    var url = window.location.pathname + (qs ? '?' + qs : '');
    window.history.replaceState(null, '', url);
  }

  // ---------- Filtering logic ----------
  function matchesFilters(card) {
    // AND across dimensions, OR within a dimension.
    // Single-value dimensions: domain, role, type, status, decade
    if (state.domain.size > 0 && !state.domain.has(card.dataset.domain)) return false;
    if (state.role.size > 0 && !state.role.has(card.dataset.role)) return false;
    if (state.type.size > 0 && !state.type.has(card.dataset.type)) return false;
    if (state.status.size > 0 && !state.status.has(card.dataset.status)) return false;
    if (state.decade.size > 0 && !state.decade.has(card.dataset.decade)) return false;

    // Multi-value dimension: book — card has comma-joined list of citing books.
    // Match if any selected book appears in that list. Orphans have empty
    // books list, so they never match a book filter (correct behavior).
    if (state.book.size > 0) {
      var raw = card.dataset.books || '';
      if (!raw) return false;
      var books = raw.split(',');
      var anyMatch = false;
      for (var i = 0; i < books.length; i++) {
        if (state.book.has(books[i])) { anyMatch = true; break; }
      }
      if (!anyMatch) return false;
    }
    return true;
  }

  function applyFilters() {
    var visibleCount = 0;
    cards.forEach(function (card) {
      if (matchesFilters(card)) {
        card.removeAttribute('hidden');
        visibleCount++;
      } else {
        card.setAttribute('hidden', '');
      }
    });
    if (countEl) countEl.textContent = visibleCount;
    if (emptyEl) emptyEl.hidden = visibleCount > 0;
  }

  // ---------- Sorting logic ----------
  function applySort() {
    var sorted;
    if (sortMode === 'year') {
      sorted = originalOrder.slice().sort(function (a, b) {
        var ya = parseInt(a.dataset.year || '0', 10);
        var yb = parseInt(b.dataset.year || '0', 10);
        if (ya !== yb) return yb - ya; // newest first
        return (a.dataset.title || '').localeCompare(b.dataset.title || '');
      });
    } else if (sortMode === 'alpha') {
      sorted = originalOrder.slice().sort(function (a, b) {
        return (a.dataset.title || '').localeCompare(b.dataset.title || '');
      });
    } else if (sortMode === 'citations') {
      sorted = originalOrder.slice().sort(function (a, b) {
        var ca = parseInt(a.dataset.citations || '0', 10);
        var cb = parseInt(b.dataset.citations || '0', 10);
        if (ca !== cb) return cb - ca; // most cited first
        var ya = parseInt(a.dataset.year || '0', 10);
        var yb = parseInt(b.dataset.year || '0', 10);
        if (ya !== yb) return yb - ya; // then newest
        return (a.dataset.title || '').localeCompare(b.dataset.title || '');
      });
    } else {
      sorted = originalOrder.slice();
    }
    var frag = document.createDocumentFragment();
    sorted.forEach(function (card) { frag.appendChild(card); });
    grid.appendChild(frag);
  }

  // ---------- UI sync ----------
  function syncChipStates() {
    var filterButtons = controls.querySelectorAll('.filter-chip');
    filterButtons.forEach(function (btn) {
      var f = btn.dataset.filter;
      var v = btn.dataset.value;
      if (state[f] && state[f].has(v)) {
        btn.classList.add('is-active');
        btn.setAttribute('aria-pressed', 'true');
      } else {
        btn.classList.remove('is-active');
        btn.setAttribute('aria-pressed', 'false');
      }
    });
    var sortButtons = controls.querySelectorAll('.sort-chip');
    sortButtons.forEach(function (btn) {
      if (btn.dataset.sort === sortMode) {
        btn.classList.add('is-active');
        btn.setAttribute('aria-pressed', 'true');
      } else {
        btn.classList.remove('is-active');
        btn.setAttribute('aria-pressed', 'false');
      }
    });
  }

  function refresh() {
    syncChipStates();
    applySort();
    applyFilters();
    writeStateToUrl();
  }

  // ---------- Event handlers ----------
  controls.addEventListener('click', function (e) {
    var filterBtn = e.target.closest('.filter-chip');
    if (filterBtn) {
      e.preventDefault();
      var f = filterBtn.dataset.filter;
      var v = filterBtn.dataset.value;
      if (!state[f]) return;
      if (state[f].has(v)) {
        state[f].delete(v);
      } else {
        state[f].add(v);
      }
      refresh();
      return;
    }
    var sortBtn = e.target.closest('.sort-chip');
    if (sortBtn) {
      e.preventDefault();
      sortMode = sortBtn.dataset.sort;
      refresh();
      return;
    }
  });

  function clearAll() {
    Object.keys(state).forEach(function (key) { state[key].clear(); });
    sortMode = DEFAULT_SORT;
    refresh();
  }

  if (clearBtn) clearBtn.addEventListener('click', clearAll);
  if (emptyClearBtn) emptyClearBtn.addEventListener('click', clearAll);

  window.addEventListener('popstate', function () {
    readStateFromUrl();
    refresh();
  });

  // ---------- Initial state ----------
  readStateFromUrl();
  refresh();
})();
