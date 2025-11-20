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
});
