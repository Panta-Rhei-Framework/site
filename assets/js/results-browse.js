// Results Browse — vanilla JS filter/sort module
// Progressive enhancement: works on static HTML with no dependencies.

(function () {
  'use strict';

  var controls = document.getElementById('results-browse-controls');
  var grid = document.getElementById('results-browse-grid');
  if (!controls || !grid) return;

  var cards = Array.prototype.slice.call(grid.querySelectorAll('.result-card'));
  var countEl = document.getElementById('results-count');
  var emptyEl = document.getElementById('results-empty');
  var clearBtn = document.getElementById('results-clear-filters');
  var emptyClearBtn = document.getElementById('results-empty-clear');
  var advancedToggle = document.getElementById('results-toggle-advanced');
  var advancedGroup = document.getElementById('results-advanced-filters');

  // Multi-value filter state — set of active values per dimension
  var state = {
    topic: new Set(),
    layer: new Set(),
    kind: new Set(),
    importance: new Set(),
    status: new Set(),
    book: new Set()
  };

  var sortMode = 'importance';
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
    if (sortParam && ['importance', 'alpha', 'book'].indexOf(sortParam) !== -1) {
      sortMode = sortParam;
    }
  }

  function writeStateToUrl() {
    var params = new URLSearchParams();
    Object.keys(state).forEach(function (key) {
      if (state[key].size > 0) {
        params.set(key, Array.prototype.join.call(Array.from(state[key]), ','));
      }
    });
    if (sortMode !== 'importance') {
      params.set('sort', sortMode);
    }
    var qs = params.toString();
    var url = window.location.pathname + (qs ? '?' + qs : '');
    window.history.replaceState(null, '', url);
  }

  // ---------- Filtering logic ----------
  function matchesFilters(card) {
    // Each dimension: if no filter set, pass; else require a match.
    if (state.topic.size > 0 && !state.topic.has(card.dataset.topic)) return false;
    if (state.layer.size > 0 && !state.layer.has(card.dataset.layer)) return false;
    if (state.kind.size > 0 && !state.kind.has(card.dataset.kind)) return false;
    if (state.importance.size > 0 && !state.importance.has(card.dataset.importance)) return false;
    if (state.status.size > 0 && !state.status.has(card.dataset.status)) return false;
    if (state.book.size > 0) {
      var books = (card.dataset.books || '').split(',');
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
  var bookRank = { 'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7 };

  function applySort() {
    var sorted;
    if (sortMode === 'importance') {
      sorted = originalOrder.slice().sort(function (a, b) {
        var ra = parseInt(a.dataset.rank || '9', 10);
        var rb = parseInt(b.dataset.rank || '9', 10);
        if (ra !== rb) return ra - rb;
        return (a.dataset.title || '').localeCompare(b.dataset.title || '');
      });
    } else if (sortMode === 'alpha') {
      sorted = originalOrder.slice().sort(function (a, b) {
        return (a.dataset.title || '').localeCompare(b.dataset.title || '');
      });
    } else if (sortMode === 'book') {
      sorted = originalOrder.slice().sort(function (a, b) {
        var ba = bookRank[a.dataset.firstBook] || 99;
        var bb = bookRank[b.dataset.firstBook] || 99;
        if (ba !== bb) return ba - bb;
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
    sortMode = 'importance';
    refresh();
  }

  if (clearBtn) clearBtn.addEventListener('click', clearAll);
  if (emptyClearBtn) emptyClearBtn.addEventListener('click', clearAll);

  // ---------- Advanced filter toggle ----------
  if (advancedToggle && advancedGroup) {
    advancedToggle.addEventListener('click', function () {
      var isHidden = advancedGroup.hidden;
      advancedGroup.hidden = !isHidden;
      advancedToggle.textContent = isHidden ? 'Fewer filters' : 'More filters';
    });
    // Auto-expand if any advanced filter is active on page load
    var hasAdvancedActive = ['layer', 'kind', 'importance', 'book'].some(function (k) {
      return state[k] && state[k].size > 0;
    });
    if (hasAdvancedActive) {
      advancedGroup.hidden = false;
      advancedToggle.textContent = 'Fewer filters';
    }
  }

  window.addEventListener('popstate', function () {
    readStateFromUrl();
    refresh();
  });

  // ---------- Initial state ----------
  readStateFromUrl();
  refresh();
})();
