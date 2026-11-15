/* Lumen · biblioteca de widgets. Vanilla JS, sin dependencias. */
(function () {
  'use strict';

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  var reduce = window.matchMedia ? matchMedia('(prefers-reduced-motion: reduce)') : { matches: false, addEventListener: function () {} };

  // ---------- Utilidades ----------
  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) for (var k in attrs) {
      var v = attrs[k];
      if (v == null || v === false) continue;
      if (k === 'text') n.textContent = v;
      else if (k === 'class') n.className = v;
      else if (k === 'dataset') for (var d in v) n.dataset[d] = v[d];
      else n.setAttribute(k, v === true ? '' : v);
    }
    (kids || []).forEach(function (c) { if (c != null) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return n;
  }
  function norm(s) {
    return String(s == null ? '' : s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/\s+/g, ' ').trim();
  }
  // Iconos: cadenas constantes del propio script (no datos).
  function svg(inner, cls) {
    var w = document.createElement('span');
    w.innerHTML = '<svg viewBox="0 0 20 20" aria-hidden="true"' + (cls ? ' class="' + cls + '"' : '') + '>' + inner + '</svg>';
    return w.firstChild;
  }
  var ICO = {
    flecha: '<path d="M8 4l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
    completo: '<circle cx="10" cy="10" r="6" fill="currentColor"/>',
    parcial: '<circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10 4a6 6 0 0 0 0 12z" fill="currentColor"/>',
    pendiente: '<circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-dasharray="2.6 2.4"/>',
    descarga: '<path d="M10 3v9m0 0l-3.5-3.5M10 12l3.5-3.5M4 16h12" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>'
  };
  function plural(n, s, p) { return n + ' ' + (n === 1 ? s : p); }
  function esc(s) { return String(s).replace(/[^a-z0-9_-]/gi, ''); }

  var TIPOS = [
    { id: 'ensenanza', etiqueta: 'Enseñanza' },
    { id: 'definiciones', etiqueta: 'Definiciones' },
    { id: 'apertura', etiqueta: 'Apertura' }
  ];
  var TIPO_ET = { ensenanza: 'Enseñanza', definiciones: 'Definiciones', apertura: 'Apertura' };
  var KIT_ET = { v11: 'v11', v10: 'v10 · congelado' };
  var ESTADO_ET = { completo: 'Completo', parcial: 'Parcial', pendiente: 'Pendiente' };
  var ACENTOS = {
    'ginecologia': '#ff7ab8',
    'salud-mental': '#8fb4ff',
    'digestivo': '#ffb070',
    'urologia': '#5fe0d0',
    'pediatria-ortopedia': '#b8e86a'
  };

  // ---------- Datos ----------
  var DATA = window.CATALOGO;
  var app = $('#app');
  if (!DATA || !DATA.temas || !DATA.widgets || !DATA.semestres) {
    var f = $('#falta');
    f.hidden = false;
    f.textContent = '';
    f.appendChild(document.createTextNode('Falta '));
    f.appendChild(el('code', { text: 'biblioteca/catalogo.js' }));
    f.appendChild(document.createTextNode('; ejecuta '));
    f.appendChild(el('code', { text: 'python3 kit/biblioteca/generar.py' }));
    f.appendChild(document.createTextNode('.'));
    $('.controles').hidden = true;
    initFlujo();
    return;
  }

  var temasPorId = {}, widgetsPorId = {};
  DATA.temas.forEach(function (t) {
    t._hay = norm(t.titulo + ' ' + (t.resumen || '') + ' ' + (t.caso || ''));
    temasPorId[t.id] = t;
  });
  DATA.widgets.forEach(function (w) { widgetsPorId[w.id] = w; });

  var state = { sem: DATA.semestres[0].id, rot: 'todo', tipos: {}, mazo: false, q: '' };
  function semActual() {
    for (var i = 0; i < DATA.semestres.length; i++) if (DATA.semestres[i].id === state.sem) return DATA.semestres[i];
    return DATA.semestres[0];
  }
  function temasDe(sem) {
    var ids = {};
    sem.rotaciones.forEach(function (r) { r.temas.forEach(function (id) { ids[id] = 1; }); });
    return ids;
  }
  function tabEtiqueta(r) { return r.etiqueta.replace(/\s*rotaci[oó]n/i, ''); }

  // ---------- Portada: textos ----------
  function pintaPortada() {
    var sem = semActual();
    var ids = temasDe(sem);
    var temas = DATA.temas.filter(function (t) { return ids[t.id]; });
    var nW = temas.reduce(function (a, t) { return a + (t.widgets || []).length; }, 0);
    var pend = temas.filter(function (t) { return t.estado === 'pendiente'; }).length;
    $('#h-nivel').textContent = sem.etiqueta + (sem.institucion ? ' · ' + sem.institucion : '');
    $('#h-fecha').textContent = 'Generado ' + DATA.generado;
    var lead = $('#h-lead');
    lead.textContent = 'Biblioteca de estudio por semestre, rotación y tema del sílabo.';
    if (sem.asignatura) lead.appendChild(el('small', { text: sem.asignatura }));
    var c = $('#h-cifras');
    c.textContent = '';
    [[nW, 'widgets'], [temas.length, 'temas'], [pend, 'pendientes']].forEach(function (p) {
      c.appendChild(el('li', null, [el('b', { text: String(p[0]) }), el('span', { text: p[1] })]));
    });
    $('#p-nombre').textContent = DATA.nombre || 'Lumen';
    $('#p-fecha').textContent = 'Generado ' + DATA.generado;
    document.title = (DATA.nombre || 'Lumen') + ' · biblioteca de widgets';
  }

  // ---------- Controles ----------
  function pintaControles() {
    var sem = semActual();
    var cont = $('#c-sem');
    cont.textContent = '';
    if (DATA.semestres.length > 1) {
      var sel = el('select', { id: 'c-semsel', 'aria-label': 'Semestre' });
      DATA.semestres.forEach(function (s) { sel.appendChild(el('option', { value: s.id, text: s.etiqueta, selected: s.id === state.sem })); });
      sel.addEventListener('change', function () { state.sem = sel.value; state.rot = 'todo'; pintaPortada(); pintaControles(); render(); });
      cont.appendChild(el('span', { class: 'sem-select' }, [sel]));
    } else {
      cont.appendChild(el('span', { class: 'sem-etiqueta', text: sem.etiqueta }));
    }
    var tabs = $('#c-rot');
    tabs.textContent = '';
    var opciones = [{ id: 'todo', etiqueta: 'Todo', largo: 'Todas las rotaciones' }].concat(sem.rotaciones.map(function (r) { return { id: r.id, etiqueta: tabEtiqueta(r), largo: r.etiqueta }; }));
    opciones.forEach(function (o) {
      var b = el('button', { type: 'button', class: 'tab', 'aria-pressed': state.rot === o.id ? 'true' : 'false', 'aria-label': o.largo, text: o.etiqueta, dataset: { rot: o.id } });
      b.addEventListener('click', function () { state.rot = o.id; $$('.tab', tabs).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); render(); });
      tabs.appendChild(b);
    });
    var chips = $('#c-tipos');
    chips.textContent = '';
    TIPOS.concat([{ id: '_mazo', etiqueta: 'Con mazo Anki' }]).forEach(function (t) {
      var on = t.id === '_mazo' ? state.mazo : !!state.tipos[t.id];
      var b = el('button', { type: 'button', class: 'chip', 'aria-pressed': on ? 'true' : 'false', text: t.etiqueta });
      b.addEventListener('click', function () {
        var now = b.getAttribute('aria-pressed') !== 'true';
        if (t.id === '_mazo') state.mazo = now; else if (now) state.tipos[t.id] = true; else delete state.tipos[t.id];
        b.setAttribute('aria-pressed', now ? 'true' : 'false');
        render();
      });
      chips.appendChild(b);
    });
  }

  // En pantallas anchas chips y conteo suben a la barra pegajosa
  (function () {
    if (!window.matchMedia) return;
    var mq = matchMedia('(min-width: 1360px)');
    var barIn = $('.bar-in'), filtrosIn = $('.filtros-in'), chips = $('#c-tipos'), conteo = $('#conteo'), buscar = $('.buscar');
    function coloca() {
      if (mq.matches) { barIn.insertBefore(chips, buscar); barIn.appendChild(conteo); }
      else { filtrosIn.appendChild(chips); filtrosIn.appendChild(conteo); }
    }
    coloca();
    if (mq.addEventListener) mq.addEventListener('change', coloca);
  })();

  // ---------- Filtrado ----------
  function filtrar() {
    var sem = semActual();
    var tokens = norm(state.q).split(' ').filter(Boolean);
    var tiposOn = Object.keys(state.tipos);
    var filtrando = tokens.length > 0 || tiposOn.length > 0 || state.mazo;
    var grupos = [];
    var nW = 0, nT = 0;
    sem.rotaciones.forEach(function (r) {
      if (state.rot !== 'todo' && state.rot !== r.id) return;
      var items = [];
      r.temas.forEach(function (id) {
        var t = temasPorId[id];
        if (!t) return;
        if (state.mazo && !(t.mazos && t.mazos.length)) return;
        var temaOk = tokens.every(function (k) { return t._hay.indexOf(k) !== -1; });
        var ws = [];
        (t.widgets || []).forEach(function (wid) {
          var w = widgetsPorId[wid];
          if (!w) return;
          if (tiposOn.length && !state.tipos[w.tipo]) return;
          var hay = (w.busqueda || '') + ' ' + t._hay;
          if (tokens.every(function (k) { return hay.indexOf(k) !== -1; }) || temaOk) ws.push(w);
        });
        var visible;
        if (tokens.length || tiposOn.length) visible = ws.length > 0 || (tokens.length > 0 && !tiposOn.length && temaOk);
        else visible = true;
        if (visible) { items.push({ tema: t, widgets: ws }); nT++; nW += ws.length; }
      });
      if (items.length) grupos.push({ rot: r, items: items });
    });
    return { grupos: grupos, nW: nW, nT: nT, filtrando: filtrando };
  }

  // ---------- Render del catálogo ----------
  function estadoNodo(t, conNota) {
    var e = t.estado in ESTADO_ET ? t.estado : 'pendiente';
    var nodes = [el('span', { class: 'estado estado-' + e }, [svg(ICO[e]), document.createTextNode(ESTADO_ET[e])])];
    if (conNota && t.nota) nodes.push(el('span', { class: 'estado-nota', text: t.nota }));
    return nodes;
  }

  function tarjeta(w) {
    var meta = [el('span', { class: 't', text: TIPO_ET[w.tipo] || w.tipo })];
    var kit = KIT_ET[w.kit];
    if (kit) meta.push(el('span', { text: kit }));
    var a = el('a', { class: 'card', href: '#w-' + esc(w.id), dataset: { foco: 'w-' + w.id } }, [
      el('div', { class: 'card-meta mono' }, meta),
      el('h4', { text: w.titulo }),
      w.contenido ? el('p', { class: 'card-txt', text: w.contenido }) : null
    ]);
    if (w.acento && ACENTOS[w.acento]) a.style.setProperty('--acc', ACENTOS[w.acento]);
    if (w.principal || w.amenaza) {
      var dl = el('dl', { class: 'card-dl' });
      if (w.principal) dl.appendChild(el('div', null, [el('dt', { text: 'Principal' }), el('dd', { text: w.principal })]));
      if (w.amenaza) dl.appendChild(el('div', null, [el('dt', { text: 'Amenaza' }), el('dd', { text: w.amenaza })]));
      a.appendChild(dl);
    }
    if (w.marcas > 0) a.appendChild(el('p', { class: 'card-marcas', text: plural(w.marcas, 'dato por verificar', 'datos por verificar') }));
    return a;
  }

  function seccionTema(it) {
    var t = it.tema;
    var pend = t.estado === 'pendiente' || !(t.widgets && t.widgets.length);
    var cab = el('div', { class: 'tema-cab' }, []);
    if (t.caso) cab.appendChild(el('span', { class: 'caso mono', text: t.caso }));
    cab.appendChild(el('h3', null, [el('a', { href: '#t-' + esc(t.id), text: t.titulo, dataset: { foco: 't-' + t.id } })]));
    if (!pend && t.resumen) cab.appendChild(el('p', { class: 'tema-res', text: t.resumen }));
    var est = estadoNodo(t, !pend);
    if (pend) est = [el('span', { class: 'estado estado-pendiente' }, [svg(ICO.pendiente), document.createTextNode('Aún sin widgets')])];
    est.forEach(function (n) { cab.appendChild(n); });
    if (!pend) cab.appendChild(el('a', { class: 'btn ver-tema', href: '#t-' + esc(t.id), 'aria-label': 'Sílabo, plan y mazos de ' + t.titulo }, [document.createTextNode('Sílabo y mazos'), svg(ICO.flecha)]));
    var sec = el('section', { class: 'tema' + (pend ? ' tema-pend' : ''), 'aria-label': t.titulo }, [cab]);
    if (!pend) {
      var cards = el('div', { class: 'cards' });
      it.widgets.forEach(function (w) { cards.appendChild(tarjeta(w)); });
      sec.appendChild(cards);
    }
    return sec;
  }

  var catalogo = $('#catalogo');
  function render() {
    var res = filtrar();
    catalogo.textContent = '';
    res.grupos.forEach(function (g) {
      var cab = el('div', { class: 'rot-cab' }, [
        el('h2', { text: g.rot.etiqueta }),
        g.rot.descripcion ? el('p', { text: g.rot.descripcion }) : null,
        el('span', { class: 'mono', text: plural(g.items.length, 'tema', 'temas') })
      ]);
      var rot = el('div', { class: 'rot' }, [cab]);
      g.items.forEach(function (it) { rot.appendChild(seccionTema(it)); });
      catalogo.appendChild(rot);
    });
    if (!res.grupos.length) {
      var v = el('div', { class: 'vacio' }, [el('h2', { text: 'Sin resultados' })]);
      var q = state.q.trim();
      v.appendChild(el('p', { text: q ? 'Nada coincide con «' + q + '». Prueba con otra palabra, un nombre de entidad o quita los filtros.' : 'Ningún tema cumple los filtros activos.' }));
      var b = el('button', { type: 'button', class: 'btn', text: 'Quitar filtros' });
      b.addEventListener('click', limpiar);
      v.appendChild(b);
      catalogo.appendChild(v);
    }
    $('#conteo').textContent = res.grupos.length ? plural(res.nW, 'widget', 'widgets') + ' en ' + plural(res.nT, 'tema', 'temas') : '0 resultados';
  }
  function limpiar() {
    state.q = ''; state.tipos = {}; state.mazo = false; state.rot = 'todo';
    $('#buscar').value = '';
    pintaControles(); render();
  }

  var inBuscar = $('#buscar');
  inBuscar.addEventListener('input', function () { state.q = inBuscar.value; render(); });
  inBuscar.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      if (inBuscar.value) { inBuscar.value = ''; state.q = ''; render(); }
      else inBuscar.blur();
      e.stopPropagation();
    }
  });

  // ---------- Capas: panel y visor ----------
  var panel = $('#panel'), visor = $('#visor');
  var hoja = $('.hoja', panel);
  var iframe = $('#v-iframe'), estadoV = $('#v-estado');
  var cierreTimers = {};
  var foco = { panel: null, visor: null };
  var desdePanel = null;     // tema del panel desde el que se abrió el visor
  var abierto = { panel: null, visor: null };
  var cargaTimer = 0, cargaId = 0;

  function bloquear() {
    var hay = panel.classList.contains('abierta') || visor.classList.contains('abierta');
    document.documentElement.classList.toggle('bloqueado', hay);
    if (hay) app.setAttribute('inert', ''); else app.removeAttribute('inert');
  }
  function abrirCapa(capa, key) {
    clearTimeout(cierreTimers[key]);
    capa.hidden = false;
    void capa.offsetWidth;
    capa.classList.add('abierta');
    bloquear();
  }
  function cerrarCapa(capa, key, inmediato) {
    capa.classList.remove('abierta');
    clearTimeout(cierreTimers[key]);
    var fin = function () { capa.hidden = true; bloquear(); };
    if (inmediato || reduce.matches) fin(); else cierreTimers[key] = setTimeout(fin, 210);
    bloquear();
  }

  function recuerdaFoco(key) {
    var a = document.activeElement;
    var f = a && a.dataset && a.dataset.foco;
    if (f) foco[key] = f;
  }
  function devuelveFoco(key, ambito) {
    var f = foco[key]; foco[key] = null;
    var n = f && $('[data-foco="' + f + '"]', ambito || document);
    if (n) { n.focus({ preventScroll: false }); return true; }
    return false;
  }

  // Panel de tema
  function pintaPanel(t) {
    var body = $('#p-cuerpo');
    body.textContent = '';
    var sem = semActual();
    $('#p-sup').textContent = [t.caso, rotEtiqueta(t.rotacion)].filter(Boolean).join(' · ');
    body.appendChild(el('h2', { class: 'p-titulo', id: 'p-titulo', text: t.titulo }));
    if (t.resumen) body.appendChild(el('p', { class: 'p-sub', text: t.resumen }));
    body.appendChild(el('div', { class: 'p-estado' }, estadoNodo(t, true)));

    var ws = (t.widgets || []).map(function (id) { return widgetsPorId[id]; }).filter(Boolean);
    var sec = el('section', { class: 'p-sec' }, [el('h3', { text: 'Widgets' })]);
    if (ws.length) {
      ws.forEach(function (w) {
        sec.appendChild(el('a', { class: 'fila-w', href: '#w-' + esc(w.id), dataset: { foco: 'w-' + w.id } }, [
          el('span', null, [el('b', { text: w.titulo }), el('small', { text: [TIPO_ET[w.tipo] || w.tipo, KIT_ET[w.kit]].filter(Boolean).join(' · ') })]),
          svg(ICO.flecha)
        ]));
      });
    } else {
      sec.appendChild(el('p', { class: 'p-sub', text: 'Aún sin widgets.' }));
    }
    body.appendChild(sec);

    if (t.mazos && t.mazos.length) {
      var sm = el('section', { class: 'p-sec' }, [el('h3', { text: 'Mazos' })]);
      t.mazos.forEach(function (m) {
        var links = el('div', { class: 'mazo-links' });
        (m.archivos || []).forEach(function (a) {
          links.appendChild(el('a', { class: 'btn', href: a.ruta, download: '' }, [svg(ICO.descarga), document.createTextNode(a.etiqueta)]));
        });
        var det = [];
        if (m.notas) det.push(m.notas + ' notas');
        if (m.version) det.push('v' + m.version);
        sm.appendChild(el('div', { class: 'mazo' }, [el('b', { text: m.titulo }), el('small', { text: det.join(' · ') }), links]));
      });
      body.appendChild(sm);
    }

    var tabs = [];
    if (t.silaboHtml) tabs.push({ id: 'silabo', etiqueta: 'Sílabo', html: t.silaboHtml });
    if (t.planHtml) tabs.push({ id: 'plan', etiqueta: 'Plan', html: t.planHtml });
    if (t.casos && t.casos.length) tabs.push({ id: 'casos', etiqueta: 'Casos', casos: t.casos });
    if (tabs.length) {
      var st = el('section', { class: 'p-sec' });
      var lista = el('div', { class: 'p-tabs', role: 'tablist', 'aria-label': 'Material del tema' });
      var paneles = [];
      tabs.forEach(function (tb, i) {
        var b = el('button', { type: 'button', class: 'p-tab', role: 'tab', id: 'pt-' + tb.id, 'aria-controls': 'pp-' + tb.id, 'aria-selected': i === 0 ? 'true' : 'false', tabindex: i === 0 ? '0' : '-1', text: tb.etiqueta });
        var pn = el('div', { class: 'prosa', role: 'tabpanel', id: 'pp-' + tb.id, 'aria-labelledby': 'pt-' + tb.id, hidden: i !== 0 });
        if (tb.html) pn.innerHTML = tb.html; // HTML ya saneado por el generador
        else tb.casos.forEach(function (c) {
          var bl = el('div', { class: 'caso-bloque' }, [el('h3', { text: c.titulo })]);
          var inner = el('div', { class: 'prosa' }); inner.innerHTML = c.html; // saneado por el generador
          bl.appendChild(inner); pn.appendChild(bl);
        });
        $$('table', pn).forEach(function (tbl) {
          var w = el('div', { class: 'tabla-scroll', tabindex: '0', role: 'region', 'aria-label': 'Tabla (desplazable)' });
          tbl.parentNode.insertBefore(w, tbl); w.appendChild(tbl);
        });
        paneles.push(pn);
        b.addEventListener('click', function () { selTab(i); });
        b.addEventListener('keydown', function (e) {
          var j = -1;
          if (e.key === 'ArrowRight') j = (i + 1) % tabs.length;
          else if (e.key === 'ArrowLeft') j = (i - 1 + tabs.length) % tabs.length;
          else if (e.key === 'Home') j = 0;
          else if (e.key === 'End') j = tabs.length - 1;
          if (j >= 0) { e.preventDefault(); selTab(j); $$('.p-tab', lista)[j].focus(); }
        });
        lista.appendChild(b);
      });
      var selTab = function (n) {
        $$('.p-tab', lista).forEach(function (b, k) { b.setAttribute('aria-selected', k === n ? 'true' : 'false'); b.tabIndex = k === n ? 0 : -1; });
        paneles.forEach(function (p, k) { p.hidden = k !== n; });
      };
      st.appendChild(lista);
      paneles.forEach(function (p) { st.appendChild(p); });
      body.appendChild(st);
    }
    body.scrollTop = 0;
  }
  function rotEtiqueta(id) {
    var r = semActual().rotaciones.filter(function (x) { return x.id === id; })[0];
    return r ? r.etiqueta : '';
  }

  function mostrarPanel(id) {
    var t = temasPorId[id];
    if (abierto.panel === id && !panel.hidden) return;
    var nuevo = panel.hidden;
    if (nuevo) recuerdaFoco('panel');
    abierto.panel = id;
    pintaPanel(t);
    abrirCapa(panel, 'panel');
    if (nuevo || true) {
      var h = $('#p-titulo');
      h.setAttribute('tabindex', '-1');
      // foco al abrir: en el propio título para que el lector anuncie el tema
      hoja.focus({ preventScroll: true });
    }
  }
  function ocultarPanel(inmediato) {
    if (panel.hidden && !panel.classList.contains('abierta')) return;
    abierto.panel = null;
    cerrarCapa(panel, 'panel', inmediato);
  }

  // Visor
  function widgetsHermanos(w) {
    var t = temasPorId[w.tema];
    return t ? (t.widgets || []).filter(function (id) { return widgetsPorId[id]; }) : [w.id];
  }
  function cargarIframe(w) {
    cargaId++;
    var mine = cargaId;
    clearTimeout(cargaTimer);
    estadoV.textContent = '';
    estadoV.appendChild(el('div', { class: 'v-carga' }));
    estadoV.appendChild(el('p', { text: 'Cargando widget…' }));
    var ok = function () { if (mine !== cargaId) return; clearTimeout(cargaTimer); estadoV.textContent = ''; };
    var fallo = function (msg) {
      if (mine !== cargaId) return;
      clearTimeout(cargaTimer);
      estadoV.textContent = '';
      estadoV.appendChild(el('h3', { text: 'No se pudo cargar' }));
      estadoV.appendChild(el('p', { text: msg || 'El archivo del widget no respondió.' }));
      var acc = el('div', { class: 'acc' });
      var re = el('button', { type: 'button', class: 'btn', text: 'Reintentar' });
      re.addEventListener('click', function () { cargarIframe(w); });
      acc.appendChild(re);
      acc.appendChild(el('a', { class: 'btn', href: w.ruta, target: '_blank', rel: 'noopener', text: 'Abrir en pestaña nueva' }));
      estadoV.appendChild(acc);
    };
    iframe.onload = function () {
      if (!iframe.getAttribute('src')) return;
      ok();
      try { // mismo origen: Escape dentro del iframe también cierra
        iframe.contentDocument.addEventListener('keydown', onKey);
      } catch (e) { /* file:// u otro origen */ }
    };
    iframe.onerror = function () { fallo(); };
    cargaTimer = setTimeout(function () { fallo('Tarda más de lo esperado.'); }, 20000);
    var empieza = function () { if (mine === cargaId) iframe.src = w.ruta; };
    if (/^https?:$/.test(location.protocol) && window.fetch) {
      fetch(w.ruta, { method: 'HEAD' }).then(function (r) {
        if (!r.ok) fallo('El archivo no existe o no está disponible (' + r.status + ').'); else empieza();
      }, function () { empieza(); });
    } else empieza();
  }
  function mostrarVisor(id) {
    var w = widgetsPorId[id];
    var t = temasPorId[w.tema];
    if (abierto.visor === id && !visor.hidden) return;
    var nuevo = visor.hidden;
    if (nuevo) {
      if (!panel.hidden && abierto.panel) { desdePanel = abierto.panel; ocultarPanel(true); }
      else { desdePanel = null; recuerdaFoco('visor'); }
      if (desdePanel) foco.visor = 'w-' + id;
    }
    abierto.visor = id;
    $('#v-titulo').textContent = w.titulo;
    $('#v-tema').textContent = t ? t.titulo : '';
    var ext = $('#v-ext'); ext.href = w.ruta;
    var hermanos = widgetsHermanos(w);
    var i = hermanos.indexOf(w.id);
    var ant = $('#v-ant'), sig = $('#v-sig');
    ant.hidden = sig.hidden = hermanos.length < 2;
    ant.dataset.id = hermanos[(i - 1 + hermanos.length) % hermanos.length];
    sig.dataset.id = hermanos[(i + 1) % hermanos.length];
    ant.setAttribute('aria-label', 'Anterior: ' + (widgetsPorId[ant.dataset.id] || {}).titulo);
    sig.setAttribute('aria-label', 'Siguiente: ' + (widgetsPorId[sig.dataset.id] || {}).titulo);
    iframe.title = w.titulo;
    abrirCapa(visor, 'visor');
    cargarIframe(w);
    if (nuevo) $('#v-volver').focus({ preventScroll: true });
  }
  function ocultarVisor() {
    if (visor.hidden && !visor.classList.contains('abierta')) return;
    abierto.visor = null;
    cargaId++; clearTimeout(cargaTimer);
    iframe.onload = null;
    iframe.removeAttribute('src'); // limpia el widget al cerrar
    try { iframe.contentWindow.location.replace('about:blank'); } catch (e) {}
    if (document.fullscreenElement) { try { document.exitFullscreen(); } catch (e) {} }
    cerrarCapa(visor, 'visor', false);
  }

  // ---------- Hash ----------
  function parseHash() {
    var m = /^#(t|w)-([a-z0-9-]+)$/i.exec(location.hash);
    return m ? { k: m[1].toLowerCase(), id: m[2] } : null;
  }
  function limpiaHash() {
    try { history.replaceState(null, '', location.pathname + location.search); } catch (e) { location.hash = ''; }
  }
  function ir(hash) {
    try { history.replaceState(null, '', hash ? hash : location.pathname + location.search); } catch (e) { location.hash = hash; return; }
    route();
  }
  function route() {
    var h = parseHash();
    if (h && h.k === 't' && temasPorId[h.id]) {
      var teniaVisor = !visor.hidden;
      if (teniaVisor) { ocultarVisor(); desdePanel = null; }
      mostrarPanel(h.id);
      if (teniaVisor) { /* volvió del visor al panel */ }
    } else if (h && h.k === 'w' && widgetsPorId[h.id]) {
      mostrarVisor(h.id);
    } else {
      if (location.hash && !h) { /* hash ajeno: se ignora */ }
      else if (h) limpiaHash();
      var estabaVisor = !visor.hidden, estabaPanel = !panel.hidden;
      if (estabaVisor) {
        ocultarVisor();
        var volver = desdePanel; desdePanel = null;
        if (volver) { ir('#t-' + volver); setTimeout(function () { devuelveFoco('visor', panel) || hoja.focus(); }, 30); return; }
        setTimeout(function () { devuelveFoco('visor') || catalogo.focus({ preventScroll: true }); }, 30);
      }
      if (estabaPanel) {
        ocultarPanel(false);
        setTimeout(function () { devuelveFoco('panel') || catalogo.focus({ preventScroll: true }); }, 30);
      }
    }
  }
  function cerrarActual() {
    if (!visor.hidden) ir(desdePanel ? '#t-' + desdePanel : '');
    else if (!panel.hidden) ir('');
  }
  window.addEventListener('hashchange', route);

  function onKey(e) {
    if (e.key === 'Escape' && (!visor.hidden || !panel.hidden)) {
      if (document.fullscreenElement) return; // Escape sale de pantalla completa primero
      e.preventDefault();
      cerrarActual();
    }
  }
  document.addEventListener('keydown', onKey);
  document.addEventListener('keydown', function (e) {
    if (e.key !== '/' || e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable)) return;
    if (!panel.hidden || !visor.hidden) return;
    e.preventDefault();
    inBuscar.focus(); inBuscar.select();
  });

  $$('[data-cerrar-panel]').forEach(function (n) { n.addEventListener('click', function () { ir(''); }); });
  $('#v-volver').addEventListener('click', cerrarActual);
  $('#v-ant').addEventListener('click', function () { ir('#w-' + this.dataset.id); });
  $('#v-sig').addEventListener('click', function () { ir('#w-' + this.dataset.id); });
  var fs = $('#v-fs');
  if (!document.fullscreenEnabled) fs.hidden = true;
  fs.addEventListener('click', function () {
    var m = $('#v-marco');
    try {
      var p = document.fullscreenElement ? document.exitFullscreen() : m.requestFullscreen();
      if (p && p.catch) p.catch(function () {});
    } catch (e) {}
  });
  $('[data-salto]').addEventListener('click', function (e) { e.preventDefault(); catalogo.focus(); catalogo.scrollIntoView(); });

  // ---------- Portada: flujo de partículas ----------
  function initFlujo() {
    var cv = $('#flujo'), hero = $('#portada');
    if (!cv || !cv.getContext) return;
    var ctx = cv.getContext('2d');
    var W = 0, H = 0, dpr = 1, parts = [], raf = 0, enPantalla = true, t = 0, last = 0;
    var COLS = [[53, 225, 255], [74, 125, 255], [255, 79, 208], [255, 178, 122], [255, 255, 255]];
    var NB = COLS.length * 2; // color x intensidad

    function ss(a, b, x) { x = Math.min(1, Math.max(0, (x - a) / (b - a))); return x * x * (3 - 2 * x); }
    function rnd() { return Math.random(); }
    function gauss() { return (rnd() + rnd() + rnd() + rnd() - 2) / 2; } // aprox. [-1,1]
    function vena(u) { // eje de la vena: de abajo-izquierda hacia el destello
      return H * (0.86 - 0.46 * ss(-0.05, 0.78, u) - 0.06 * ss(0.78, 1.1, u)) + Math.sin(u * 5.2 + t * 0.12) * H * 0.025;
    }
    function env(u) { // apertura: ancha al inicio, hilo cerca del destello, abanico final
      var cierre = 1 - ss(0, 0.76, u);
      var abre = ss(0.8, 1.15, u);
      return 0.035 + 0.965 * Math.pow(cierre, 1.6) + 0.5 * abre;
    }
    function nueva(p, inicio) {
      p.u = inicio ? rnd() * 1.1 - 0.05 : -0.03 - rnd() * 0.04;
      p.o = gauss() * H * 0.34;
      p.f = rnd() * 6.28;
      p.v = 0.03 + rnd() * 0.05;
      p.k = Math.floor(rnd() * COLS.length);
      p.px = null;
    }
    function posiciona(p) {
      var e = env(p.u);
      p.x = p.u * W;
      p.y = vena(p.u) + p.o * e + Math.sin(p.u * 11 + p.f + t * 0.5) * H * 0.018 * e;
    }
    function dimensiona() {
      var r = hero.getBoundingClientRect();
      W = Math.max(1, Math.round(r.width)); H = Math.max(1, Math.round(r.height));
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      var n = Math.round(Math.min(W < 700 ? 380 : 1100, Math.max(260, W * H / 850)));
      parts = [];
      for (var i = 0; i < n; i++) { var p = {}; nueva(p, true); parts.push(p); }
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, W, H);
    }
    function paso(dt, fade) {
      t += dt;
      ctx.globalCompositeOperation = 'destination-out';
      ctx.fillStyle = 'rgba(0,0,0,' + fade + ')';
      ctx.fillRect(0, 0, W, H);
      ctx.globalCompositeOperation = 'lighter';
      ctx.lineWidth = 0.9;
      ctx.lineCap = 'round';
      var buckets = [];
      for (var b = 0; b < NB; b++) buckets.push([]);
      for (var i = 0; i < parts.length; i++) {
        var p = parts[i];
        p.px = p.x; p.py = p.y;
        p.u += p.v * dt * (0.55 + 0.9 * ss(0, 0.8, p.u)); // acelera hacia la vena
        if (p.u > 1.08) { nueva(p, false); posiciona(p); p.px = null; continue; }
        posiciona(p);
        if (p.px == null || p.u < 0) continue;
        var cerca = env(p.u) < 0.3 ? 1 : 0;
        // el color sigue a la posición: cian-azul al inicio, magenta-melocotón hacia el destello
        var k = Math.min(COLS.length - 2, Math.max(0, Math.floor(p.u * 4.2 + (p.k - 2) * 0.35 + 0.5)));
        if (cerca && p.k === 4) k = 4;
        buckets[k * 2 + cerca].push(p);
      }
      for (var c = 0; c < NB; c++) {
        var arr = buckets[c];
        if (!arr.length) continue;
        var col = COLS[c >> 1], a = (c & 1) ? 0.85 : 0.42;
        ctx.strokeStyle = 'rgba(' + col[0] + ',' + col[1] + ',' + col[2] + ',' + a + ')';
        ctx.beginPath();
        for (var j = 0; j < arr.length; j++) { ctx.moveTo(arr[j].px, arr[j].py); ctx.lineTo(arr[j].x, arr[j].y); }
        ctx.stroke();
      }
    }
    function cuadroEstatico() {
      for (var i = 0; i < parts.length; i++) posiciona(parts[i]);
      t = 0;
      for (var s = 0; s < 150; s++) paso(1 / 30, 0.05);
    }
    function bucle(now) {
      raf = 0;
      if (!enPantalla || document.hidden || reduce.matches) return;
      var dt = Math.min(0.05, (now - last) / 1000 || 0.016);
      last = now;
      paso(dt, 0.1);
      raf = requestAnimationFrame(bucle);
    }
    function arranca() {
      if (raf || reduce.matches || !enPantalla || document.hidden) return;
      last = performance.now();
      raf = requestAnimationFrame(bucle);
    }
    function para() { if (raf) { cancelAnimationFrame(raf); raf = 0; } }
    function reinicia() {
      para(); dimensiona();
      if (reduce.matches) cuadroEstatico(); else { for (var i = 0; i < parts.length; i++) posiciona(parts[i]); arranca(); }
    }
    reinicia();
    var rt = 0, ancho = W;
    window.addEventListener('resize', function () {
      clearTimeout(rt);
      rt = setTimeout(function () { var r = hero.getBoundingClientRect(); if (Math.abs(r.width - ancho) > 1 || Math.abs(r.height - H) > 40) { ancho = r.width; reinicia(); } }, 200);
    });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { enPantalla = es[0].isIntersecting; if (enPantalla) arranca(); else para(); }).observe(hero);
    }
    document.addEventListener('visibilitychange', function () { if (document.hidden) para(); else arranca(); });
    var onRM = function () { reinicia(); };
    if (reduce.addEventListener) reduce.addEventListener('change', onRM);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () {
      var r = hero.getBoundingClientRect(); if (Math.abs(r.height - H) > 20) reinicia();
    });
  }

  // ---------- Arranque ----------
  pintaPortada();
  pintaControles();
  render();
  initFlujo();
  route();
})();
