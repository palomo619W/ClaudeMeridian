(function () {
  "use strict";

  var $ = function (sel, scope) { return (scope || document).querySelector(sel); };
  var $$ = function (sel, scope) { return Array.prototype.slice.call((scope || document).querySelectorAll(sel)); };
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

  function safe(fn, name) {
    try { fn(); } catch (e) { console.warn("[" + name + "] failed:", e); }
  }

  function initYear() {
    var el = $("#year");
    if (el) el.textContent = new Date().getFullYear();
  }

  function initStickyNav() {
    var header = $("#masthead");
    if (!header) return;
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 12);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  function initMobileMenu() {
    var toggle = $("#mobile-toggle");
    var nav = $("#site-nav");
    if (!toggle || !nav) return;

    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    $$(".menu-item-has-children > a", nav).forEach(function (link) {
      link.addEventListener("click", function (e) {
        if (window.innerWidth <= 960) {
          e.preventDefault();
          link.parentElement.classList.toggle("is-open");
        }
      });
    });

    $$("#site-nav a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  function initReveals() {
    var items = $$(".reveal");
    if (!items.length) return;

    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.03, rootMargin: "0px 0px -2% 0px" });

    items.forEach(function (el) { io.observe(el); });

    setTimeout(function () {
      $$(".reveal:not(.is-visible)").forEach(function (el) {
        if (el.getBoundingClientRect().top < window.innerHeight) {
          el.classList.add("is-visible");
        }
      });
    }, 6000);
  }

  function initSmoothAnchors() {
    document.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest('a[href^="#"]') : null;
      if (!a) return;
      var id = a.getAttribute("href");
      if (!id || id === "#") return;
      var el = document.querySelector(id);
      if (!el) return;
      e.preventDefault();
      var navOffset = 84;
      window.scrollTo({
        top: el.getBoundingClientRect().top + window.scrollY - navOffset,
        behavior: reduced ? "auto" : "smooth"
      });
    });
  }

  function initScrollTop() {
    var btn = $("#scroll-top");
    if (!btn) return;
    window.addEventListener("scroll", function () {
      btn.classList.toggle("is-visible", window.scrollY > 400);
    }, { passive: true });
    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" });
    });
  }

  function initProjectModal() {
    var modal = $("#project-modal");
    var body = $("#modal-body");
    var closeBtn = $("#modal-close");
    if (!modal || !body) return;

    function openModal(html) {
      body.innerHTML = html;
      modal.classList.add("is-open");
      document.body.style.overflow = "hidden";
    }

    function closeModal() {
      modal.classList.remove("is-open");
      body.innerHTML = "";
      document.body.style.overflow = "";
    }

    $$(".btn-project").forEach(function (btn) {
      var url = btn.getAttribute("data-url");
      if (!url) return;

      var tipo = "web";
      if (/\.(jpg|jpeg|png|gif)$/i.test(url)) tipo = "imagen";
      else if (url.indexOf("youtube.com") > -1 || url.indexOf("youtu.be") > -1) tipo = "video";
      else if (/\.pdf$/i.test(url)) tipo = "pdf";

      btn.addEventListener("click", function (e) {
        e.preventDefault();

        if (tipo === "imagen") {
          openModal('<img src="' + url + '" alt="Vista del proyecto">');
        } else if (tipo === "video") {
          var videoID = url;
          try { videoID = new URL(url).searchParams.get("v") || url; } catch (err) {}
          openModal('<iframe src="https://www.youtube.com/embed/' + videoID + '" title="Video del proyecto" allowfullscreen></iframe>');
        } else if (tipo === "pdf") {
          window.open(url, "_blank", "noopener");
        } else {
          openModal('<iframe src="' + url + '" title="Detalle del proyecto"></iframe>');
        }
      });
    });

    if (closeBtn) closeBtn.addEventListener("click", closeModal);
    modal.addEventListener("click", function (e) {
      if (e.target === modal) closeModal();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && modal.classList.contains("is-open")) closeModal();
    });
  }

  function initContactForm() {
    var form = $("#contact-form");
    if (!form) return;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      var name = $("#cf-name").value.trim();
      var phone = $("#cf-phone").value.trim();
      var email = $("#cf-email").value.trim();
      var type = $("#cf-type").value;
      var message = $("#cf-msg").value.trim();

      var body = "Nombre: " + name + "\n" +
        "Teléfono: " + (phone || "-") + "\n" +
        "Correo: " + email + "\n" +
        "Tipo de proyecto: " + type + "\n\n" +
        message;

      var mailto = "mailto:proyectos@meridian-builders.com" +
        "?subject=" + encodeURIComponent("Nuevo contacto desde la web — " + name) +
        "&body=" + encodeURIComponent(body);

      window.location.href = mailto;
    });
  }

  function boot() {
    safe(initYear, "initYear");
    safe(initStickyNav, "initStickyNav");
    safe(initMobileMenu, "initMobileMenu");
    safe(initReveals, "initReveals");
    safe(initSmoothAnchors, "initSmoothAnchors");
    safe(initScrollTop, "initScrollTop");
    safe(initProjectModal, "initProjectModal");
    safe(initContactForm, "initContactForm");
    document.documentElement.classList.add("is-ready");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
