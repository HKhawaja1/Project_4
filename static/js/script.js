// Scroll-to-Top Button Functionality
const scrollToTopButton = document.getElementById("scrollToTop");

// Show or hide the button based on scroll position
window.addEventListener("scroll", () => {
  if (window.scrollY > 200) {
    scrollToTopButton.style.display = "block";
  } else {
    scrollToTopButton.style.display = "none";
  }
});

// Scroll to the top when the button is clicked
scrollToTopButton.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});

// Filter by Price Functionality
document.addEventListener("DOMContentLoaded", () => {
  const priceFilterForm = document.getElementById("price-filter-form");
  const minPriceInput = document.getElementById("min-price");
  const maxPriceInput = document.getElementById("max-price");
  const products = document.querySelectorAll(".product-card");

  priceFilterForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent the form from submitting and reloading the page

    const minPrice = parseFloat(minPriceInput.value) || 0;
    const maxPrice = parseFloat(maxPriceInput.value) || Infinity;

    if (isNaN(minPrice) || isNaN(maxPrice)) {
      alert("Please enter valid numbers for the price range.");
      return;
    }

    let hasVisibleProducts = false;

    products.forEach((product) => {
      const priceText = product.querySelector(".product-price").textContent;
      const price = parseFloat(priceText.replace("€", ""));

      if (price >= minPrice && price <= maxPrice) {
        product.style.display = "block"; // Show product
        hasVisibleProducts = true;
      } else {
        product.style.display = "none"; // Hide product
      }
    });

    if (!hasVisibleProducts) {
      alert("No products found within the selected price range.");
    }
  });
});
