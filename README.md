# WeRepair.io - E-Commerce Website

WeRepair.io is a fully functional e-commerce platform for purchasing tech products such as phones, cases, and replacement parts. The platform allows users to browse products, add them to the cart, checkout, and make secure payments. Built with Django and various modern technologies, this platform is designed for users looking to buy high-quality tech items.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

WeRepair.io is designed to provide a seamless online shopping experience. The website features different product categories, including:

- Phones
- Cases
- Replacement Parts

Users can browse products, view detailed product pages, add items to their shopping cart, remove items, and complete purchases securely. The platform uses Stripe for payment processing, PostgreSQL for the database, and integrates several third-party libraries for enhanced functionality.

## Features

- **Product Browsing**: View different categories like Phones, Cases, and Replacement Parts.
- **Search Functionality**: Search for products by title or description.
- **Product Detail Pages**: Each product has a detailed page with description, price, and images.
- **Add to Cart**: Users can add products to their shopping cart.
- **Remove from Cart**: Users can remove products from their cart.
- **Pagination**: Paginated product listings for easy navigation.
- **Secure Checkout**: Users can make payments through Stripe.
- **User Authentication**: Users can log in to view their order history and manage their cart.

## Tech Stack

The project utilizes the following technologies:

- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 4 (for styling)
  - JQuery (for dynamic content)

- **Backend**:
  - Django (Python web framework)
  - Django REST Framework (for API integrations, if applicable)
  - PostgreSQL (relational database)
  - Stripe (for payment processing)

- **Development Tools**:
  - Git (version control)
  - Docker (for containerization, optional)
  - Gitpod (for cloud-based development environment)

- **Deployment**:
  - Heroku (for deployment, optional)
  - AWS (optional for storage and computing needs)

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- Stripe account (for payment integration)

### Steps to Set Up Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/werepair.io.git
