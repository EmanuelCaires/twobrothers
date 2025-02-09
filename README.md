# WEREPAIR.IO

## Description
WEREPAIR.IO is an online platform specializing in selling smartphones, phone cases, and replacement parts. The website provides a seamless shopping experience with categorized product listings, a user-friendly cart system, and secure payment processing. It features a responsive design, ensuring accessibility across desktops, tablets, and mobile devices.

## Features
- **User Authentication**: Secure login and signup functionality.
- **Browse Products by Categories**: Phones, cases, and replacement parts.
- **Add Products to Cart**: Easily add and remove products from the cart.
- **Search and Filtering**: Quick search and advanced filtering options.
- **Order Summary & Checkout**: Review orders before making a purchase.
- **Secure Payments**: Integrated payment gateway for seamless transactions.
- **Mobile-Friendly Design**: Optimized for all screen sizes.
- **Social Media Integration**: Footer with social media links for easy engagement.
- **Performance Optimizations**: Ongoing improvements for faster load times.

## Wireframes
### Desktop View
Illustrating the main product listing page with categories, product cards, and a footer.

![Home Wireframe](wireframes/wireframe_home.jpeg)

### Desktop Cases View
![Cases Wireframe](wireframes/wireframe_Cases.jpeg)

### Desktop Phones View
![Phones Wireframe](wireframes/wireframe_Phones.jpeg)

### Desktop Replacement Parts View
![Replacement Parts Wireframe](wireframes/wireframe_Re_Parts.jpeg)

### Tablet View
![Home Tablet Wireframe](wireframes/wireframe_tablet_home.jpeg)

### Mobile View
![Mobile View Wireframe](wireframes/wireframes_mobile_view.jpeg)

## Lighthouse Performance Report
Lighthouse results indicate areas of improvement for performance and accessibility:
- **Performance**: 39 (Needs optimization in image loading, caching, and script handling.)
- **Accessibility**: 83 (Good, but enhancements can be made for better readability and contrast.)
- **Best Practices**: 96 (Well-structured but minor improvements possible.)


### Performance Improvements in Progress:
- **Image Optimization**: Implementing lazy loading and compression.
- **Code Splitting**: Reducing unnecessary scripts and improving load times.
- **Caching Strategies**: Enhancing browser caching for faster page loads.
- **Database Queries Optimization**: Reducing redundant queries for better efficiency.


## Database Schema
The following diagram illustrates the database schema for WEREPAIR.IO:

![Database Schema](wireframes/database_schema.png)


## Color Palette
The following colors were used in the website design:

| Element                | Color Code   |
|------------------------|--------------|
| Primary Navbar/Buttons | `#007BFF`    |
| Background             | `#F8F9FA`    |
| Text (Primary)         | `#212529`    |
| Footer Background      | `#6C757D`    |
| Link Hover             | `#0056B3`    |

![Colours](wireframes/Pallet_Colours.png)

## Deployment
The project is deployed on Render and can be accessed at: [WEREPAIR.IO](https://werepair-io.onrender.com/)

## Installation
1. Clone the repository: `git clone https://github.com/username/werepair-io.git`
2. Navigate to the project directory: `cd werepair-io`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the development server: `python manage.py runserver`

## Testing
### Unit Tests
Run all tests using:
```
python manage.py test
```

### Example Test Results
| Test Suite          | Status |
|---------------------|--------|
| User Authentication | Passed |
| Product Filtering   | Passed |
| Footer Links        | Passed |

## Screenshots
### Home Page
![Home Page Screenshot](wireframes/home_screen_shot.png)

### Phones List Page
![Phones List Screenshot](wireframes/Phones_tab.png)

### Cases List Page
![Cases List Screenshot](wireframes/Cases_tab.png)

### Parts List Page
![Parts List Screenshot](wireframes/Replacement_parts_tab.png)

### Sign In Page
![Sign In Screenshot](wireframes/Sign_in.png)

### Sign Up Page
![Sign Up Screenshot](wireframes/Sign_up.png)

### Order Summary Page
![Order Summary Screenshot](wireframes/Order_sum.png)

### Checkout Page
![Checkout Screenshot](wireframes/checkout_form.png)

### Payment Page
![Payment List Screenshot](wireframes/Payment.png)

## Author
This project was designed and implemented by Emanuel Caires.

---
Made with 💙 for tech enthusiasts!


