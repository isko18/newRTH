window.addEventListener("DOMContentLoaded", () => {
  const body = document.querySelector("body");
  const menuPlatform = document.querySelector(".menu_platform");
  const sidebar = document.querySelector(".sidebar");
  const closePlatformMenu = document.querySelector(".close-platform");

  menuPlatform.addEventListener("click", () => {
    if (window.innerWidth > 992) {
      sidebar.classList.toggle("active");
      document.querySelector(".learn").classList.toggle("active");
    }
    if (window.innerWidth < 992) {
      sidebar.classList.toggle("active-mobile");
      body.classList.toggle("hidden");
    }
  });

  closePlatformMenu.addEventListener("click", () => {
    sidebar.classList.toggle("active-mobile");
    body.classList.toggle("hidden");
  });
});
