# Project: CandyWhirl

Welcome to CandyWhirl, a modern web application for browsing and exploring a wide variety of bakery and sweet treats. The project uses Flask as the backend framework and PostgreSQL as the database.

- [GitHub Repository](https://github.com/HKhawaja1/Project_4)
- [Live Web Application on Render](https://project-4-6lif.onrender.com)

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
- **Purpose**: Upon pressing the 'View Your Messages' button, users will be able to review and manage submitted inquiries.
- **Features**:
  - Displays a paginated list of submitted contact inquiries.
  - Includes **Edit** and **Delete** buttons for each inquiry.
  ![Contact Inquiries Page](https://i.ibb.co/4Ks8WNw/image.png)

### **Chocolate, Candy, and Cookies Pages**
- **Purpose**: Showcase specific product categories.
- **Features**:
  - Similar layout to the catalog page.
  - Highlights unique products within each category.
  ![Chocolate Page](https://i.ibb.co/R38W1Jn/image.png)

---

## Database Integration

- **PostgreSQL** is used to store contact inquiries.
- Models are defined using SQLAlchemy.
- Database migrations are handled with Flask-Migrate.

---

## Deployment to Render

Follow these steps to deploy the CandyWhirl application to Render:

### **Step 1: Set Up PostgreSQL on Render**
1. Create a PostgreSQL instance on Render.
2. Copy the `DATABASE_URL` provided by Render.
   ![PostgreSQL Render](https://i.ibb.co/b2F98NT/image.png)

### **Step 2: Create a New Web Service**
1. In your Render dashboard, click **New > Web Service**.
2. Connect your GitHub repository containing the CandyWhirl project.
3. Configure the following:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - Add the following environment variables:
     - `DATABASE_URL`: The URL from Render PostgreSQL instance.
     - `SECRET_KEY`: A secure key for your Flask application.
     - ![Create Web Service](https://i.ibb.co/55j52xb/image.png)

### **Step 3: Initialize the Database**
1. Open the Shell tab for your Render web service.
2. Run the following commands to initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade

### **Step 4: Redeploy the Application**
1. Commit any changes to your GitHub repository.
2. Redeploy the application on Render by pushing changes to your repository.

### **Step 5: Accessing the Web App**
1. Once deployed, Render will provide a unique URL for the web app in the Render dashboard.
   - Link: https://project-4-6lif.onrender.com
2. Visit this URL to access the deployed application.

---

## References
ChatGPT
https://pixabay.com/
https://www.pexels.com/
https://www.needpix.com/
https://logo.com/
https://render.com/
https://www.youtube.com/watch?v=IBfj_0Zf2Mo
https://www.w3schools.com/css/css_rwd_mediaqueries.asp
https://www.w3schools.com/jsref/met_document_addeventlistener.asp
https://www.w3schools.com/jsref/jsref_number_nan.asp
https://www.w3schools.com/jsref/met_document_getelementbyid.asp
https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
https://www.youtube.com/watch?v=Q2QmST-cSwc
https://www.youtube.com/watch?v=q-Q8c56zGJ8&list=PLXpWu84ZnHT-e-f6d_r6Q21cTsGAS4xXX
https://www.w3schools.com/css/css_grid.asp
https://www.w3schools.com/css/css3_flexbox.asp
https://www.w3schools.com/jsref/jsref_parsefloat.asp
https://www.w3schools.com/css/css_boxmodel.asp
https://www.w3schools.com/howto/howto_css_hero_image.asp
https://flask-wtf.readthedocs.io/en/1.2.x/
https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/
https://www.youtube.com/watch?v=uNmWxvvyBGU
https://www.geeksforgeeks.org/declaring-models-in-flask/
https://flask.palletsprojects.com/en/stable/views/
