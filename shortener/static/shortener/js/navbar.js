const menuToggle = document.querySelector(".menu-toggle");
const menuOverlay = document.querySelector(".menu-overlay");
const navbar = document.querySelector(".navbar");
const navbarAuth = document.querySelector(".navbar-auth");

menuToggle.addEventListener("click", () => {
  navbar.classList.toggle("active");
  menuOverlay.classList.toggle("active");
  navbarAuth.classList.toggle("active");

  if (navbar.classList.contains("active")) {
    menuToggle.innerHTML = '<i class="fa-solid fa-x"></i>';
  } else {
    menuToggle.innerHTML = '<i class="fa-solid fa-bars"></i>';
  }
});
