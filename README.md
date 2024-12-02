# Project: CandyWhirl

Welcome to CandyWhirl, a modern web application for browsing and exploring a wide variety of bakery and sweet treats. The project uses Flask as the backend framework and PostgreSQL as the database.

---

## Features

1. **Responsive Design**: Optimized for desktop, tablet, and mobile devices using media queries.
2. **Dynamic Catalog**: A rich collection of candy items with filtering and pagination options.
3. **Interactive Contact Form**: Visitors can submit inquiries, which are stored in a database.
4. **User-Friendly Navigation**: Well-structured navigation to explore the site's offerings.
5. **Scroll To Top**: A button that allows users to smooth-scroll back to the top of the page.
6. **Footer**: A footer that displays more information about the website along with several other links.

---

## Pages Overview

### **Home Page (`index.html`)**
- **Purpose**: The landing page introduces the brand and its offerings.
- **Features**:
  - A hero image with a welcome message and a "Shop Now" call-to-action button.
  - Overview of the collections available on the website.
  - Links to popular categories for easy navigation.
![Home Page](https://i.ibb.co/bvgRMHq/image.png)


### **Collections Page (`collections.html`)**
- **Purpose**: Provides a broad overview of all product categories (e.g., Bakery, Candy, Chocolate, Cookies, and Sale).
- **Features**:
  - Grid layout with images and titles for each collection.
  - Links redirect users to the respective category pages.
![Collections Page](https://i.ibb.co/6mpybwx/image.png)

### **Catalog Page (`catalog.html`)**
- **Purpose**: Displays the products in the selected category (e.g., Bakery).
- **Features**:
  - **Filter by Price**: Allows users to filter products within a specified price range.
  - **Show Products Dropdown**: Adjusts the number of products displayed per page (e.g., 3, 6, or 9).
  - **Add to Cart Button**: Placeholder functionality for adding products to a cart.
![Catalog Page](https://i.ibb.co/PcG52dB/image.png)

### **Sale Page (`sale.html`)**
- **Purpose**: Displays discounted items or special offers.
- **Features**:
  - Similar layout to the catalog page with a focus on products currently on sale.
  - Dynamic pricing to highlight discounted items.
![Sale Page](https://i.ibb.co/B4W2FNZ/image.png)

### **Contact Us Page (`contact.html`)**
- **Purpose**: Enables visitors to get in touch with the store.
- **Features**:
  - **Google Maps Integration**: Displays the store's location.
  - **Contact Form**: Includes fields for Name, Email, and Message with server-side validation.
  - **Follow Us Section**: Links to social media platforms for engagement.
![Contact Page](https://i.ibb.co/zhDtz5g/image.png)

### **List Contacts Page (`list_contacts.html`)**
- **Purpose**: Allows users to review and manage submitted inquiries.
- **Features**:
  - Displays a paginated list of submitted contact inquiries.
  - Includes **Edit** and **Delete** buttons for each inquiry.
![Contact Inquiries Page](https://i.ibb.co/4Ks8WNw/image.png)

### **Chocolate, Candy, and Cookies Pages**
- **Purpose**: Showcase specific product categories.
- **Features**:
  - Similar layout to the catalog page.
  - Highlights unique products within each category.
  - ![Chocolate Page](https://i.ibb.co/R38W1Jn/image.png)

---

## Database Integration

- **PostgreSQL** is used to store contact inquiries.
- Models are defined using SQLAlchemy.
- Database migrations are handled with Flask-Migrate.

---




