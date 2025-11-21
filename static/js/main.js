document.addEventListener("DOMContentLoaded", () => {
  const scrollTopLink = document.querySelector(".scroll-top");
  if (scrollTopLink) {
    scrollTopLink.addEventListener("click", (event) => {
      event.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  document.querySelectorAll("[data-debounce='true']").forEach((input) => {
    let timeoutId;
    input.addEventListener("input", () => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        input.closest("form").requestSubmit();
      }, 500);
    });
  });

  const statNumbers = document.querySelectorAll(".stat-number");
  const animateStat = (el) => {
    const target = Number(el.dataset.target || el.textContent) || 0;
    let current = 0;
    const increment = Math.max(1, target / 60);
    const step = () => {
      current += increment;
      if (current >= target) {
        el.textContent = target;
      } else {
        el.textContent = Math.ceil(current);
        requestAnimationFrame(step);
      }
    };
    step();
  };
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateStat(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.35 }
  );
  statNumbers.forEach((el) => observer.observe(el));

  const filterTags = document.querySelectorAll(".filter-tag");
  if (filterTags.length) {
    const categorySelect = document.querySelector("select[name='category']");
    filterTags.forEach((tag) => {
      tag.addEventListener("click", () => {
        filterTags.forEach((t) => t.classList.remove("active"));
        tag.classList.add("active");
        if (categorySelect) {
          categorySelect.value = tag.dataset.filter || "";
        }
        const form = tag.closest("form");
        if (form) {
          form.requestSubmit();
        }
      });
    });
  }

  const timelineCards = document.querySelectorAll(".timeline-section .achievement-card");
  if (timelineCards.length) {
    timelineCards.forEach((card) => {
      card.style.opacity = "0";
      card.style.transform = "translateY(20px)";
      card.style.transition = "opacity 0.5s ease, transform 0.5s ease";
    });
    const cardObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.style.opacity = "1";
            entry.target.style.transform = "translateY(0)";
            cardObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1 }
    );
    timelineCards.forEach((card) => cardObserver.observe(card));
  }

  const skillBars = document.querySelectorAll(".skill-progress");
  if (skillBars.length) {
    skillBars.forEach((bar) => {
      bar.style.width = "0%";
    });
    const skillsObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const pct = entry.target.dataset.percentage || entry.target.getAttribute("aria-valuenow") || 0;
            entry.target.style.width = `${pct}%`;
            skillsObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    skillBars.forEach((bar) => skillsObserver.observe(bar));
  }
});
