// Falsifications Browse — vanilla JS filter/sort module
(function () {
  'use strict';
  var controls = document.getElementById('falsifications-browse-controls');
  var grid = document.getElementById('falsifications-browse-grid');
  if (!controls || !grid) return;

  var cards = Array.prototype.slice.call(grid.querySelectorAll('.falsification-card'));
  var countEl = document.getElementById('falsifications-count');
  var emptyEl = document.getElementById('falsifications-empty');
  var clearBtn = document.getElementById('falsifications-clear-filters');
  var emptyClearBtn = document.getElementById('falsifications-empty-clear');

  var state = { domain: new Set(), status: new Set() };
  var DEFAULT_SORT = 'id';
  var VALID_SORTS = ['id', 'domain', 'status'];
  var sortMode = DEFAULT_SORT;
  var originalOrder = cards.slice();

  function readStateFromUrl() {
    var params = new URLSearchParams(window.location.search);
    Object.keys(state).forEach(function (key) {
      state[key].clear();
      var raw = params.get(key);
      if (raw) raw.split(',').forEach(function (v) { if (v) state[key].add(v); });
    });
    var s = params.get('sort');
    sortMode = (s && VALID_SORTS.indexOf(s) !== -1) ? s : DEFAULT_SORT;
  }

  function writeStateToUrl() {
    var params = new URLSearchParams();
    Object.keys(state).forEach(function (key) {
      if (state[key].size > 0) params.set(key, Array.from(state[key]).join(','));
    });
    if (sortMode !== DEFAULT_SORT) params.set('sort', sortMode);
    var qs = params.toString();
    window.history.replaceState(null, '', window.location.pathname + (qs ? '?' + qs : ''));
  }

  function matchesFilters(card) {
    if (state.domain.size > 0 && !state.domain.has(card.dataset.domain)) return false;
    if (state.status.size > 0 && !state.status.has(card.dataset.status)) return false;
    return true;
  }

  function applyFilters() {
    var count = 0;
    cards.forEach(function (c) {
      if (matchesFilters(c)) { c.removeAttribute('hidden'); count++; }
      else c.setAttribute('hidden', '');
    });
    if (countEl) countEl.textContent = count;
    if (emptyEl) emptyEl.hidden = count > 0;
  }

  var domainRank = {'particle-physics':1,'cmb-inflation':2,'bbn':3,'dark-sector':4,'black-holes':5,'collective-dynamics':6};
  var statusRank = {'confirmed':1,'consistent':2,'testable':3};

  function applySort() {
    var sorted;
    if (sortMode === 'id') {
      sorted = originalOrder.slice().sort(function (a, b) {
        return parseInt(a.dataset.n||'99',10) - parseInt(b.dataset.n||'99',10);
      });
    } else if (sortMode === 'domain') {
      sorted = originalOrder.slice().sort(function (a, b) {
        var da = domainRank[a.dataset.domain]||9, db = domainRank[b.dataset.domain]||9;
        if (da !== db) return da - db;
        return parseInt(a.dataset.n||'99',10) - parseInt(b.dataset.n||'99',10);
      });
    } else if (sortMode === 'status') {
      sorted = originalOrder.slice().sort(function (a, b) {
        var sa = parseInt(a.dataset.statusRank||'9',10), sb = parseInt(b.dataset.statusRank||'9',10);
        if (sa !== sb) return sa - sb;
        return parseInt(a.dataset.n||'99',10) - parseInt(b.dataset.n||'99',10);
      });
    } else {
      sorted = originalOrder.slice();
    }
    var frag = document.createDocumentFragment();
    sorted.forEach(function (c) { frag.appendChild(c); });
    grid.appendChild(frag);
  }

  function syncChipStates() {
    controls.querySelectorAll('.filter-chip').forEach(function (btn) {
      var f = btn.dataset.filter, v = btn.dataset.value;
      if (state[f] && state[f].has(v)) { btn.classList.add('is-active'); btn.setAttribute('aria-pressed','true'); }
      else { btn.classList.remove('is-active'); btn.setAttribute('aria-pressed','false'); }
    });
    controls.querySelectorAll('.sort-chip').forEach(function (btn) {
      if (btn.dataset.sort === sortMode) { btn.classList.add('is-active'); btn.setAttribute('aria-pressed','true'); }
      else { btn.classList.remove('is-active'); btn.setAttribute('aria-pressed','false'); }
    });
  }

  function refresh() { syncChipStates(); applySort(); applyFilters(); writeStateToUrl(); }

  controls.addEventListener('click', function (e) {
    var fb = e.target.closest('.filter-chip');
    if (fb) { e.preventDefault(); var f=fb.dataset.filter, v=fb.dataset.value; if(!state[f])return; state[f].has(v)?state[f].delete(v):state[f].add(v); refresh(); return; }
    var sb = e.target.closest('.sort-chip');
    if (sb) { e.preventDefault(); sortMode = sb.dataset.sort; refresh(); }
  });

  function clearAll() { Object.keys(state).forEach(function(k){state[k].clear();}); sortMode=DEFAULT_SORT; refresh(); }
  if (clearBtn) clearBtn.addEventListener('click', clearAll);
  if (emptyClearBtn) emptyClearBtn.addEventListener('click', clearAll);
  window.addEventListener('popstate', function () { readStateFromUrl(); refresh(); });

  readStateFromUrl();
  refresh();
})();
