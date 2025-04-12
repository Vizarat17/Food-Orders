OrderEat is a full-stack web application built using the Django framework that offers a complete restaurant experience — from browsing menus and making table reservations to placing orders and receiving a confirmation with a unique reference number. It caters to both casual dining and food court-style ordering, aiming to streamline the experience for customers as well as restaurant managers.

The application allows users to explore various cuisines including Italian, Mughlai, Mexican, and multicuisine options. Once a cuisine or dining category is selected, users can view restaurants and menu items with detailed descriptions and pricing. Users can add items to their cart and proceed to checkout in a seamless interface. A reference number is generated for every customer order or reservation, enabling them to track or verify their booking easily.

Beyond ordering, the system includes functionality for restaurant admins to manage reservations and menus. Admin users can log in to view customer reservations, edit table statuses, and modify menu items (add/edit/delete). The interface offers clean data displays, making it easy to see reservation details like date, time, meal choice, and customer email.

Behind the scenes, the application follows a normalized database structure. The UML diagram outlines entities such as Restaurant, Reservation, Food-Order, Menu categories (Starters, Main-course, Desserts, Beverages), and Invoice. Each table is connected logically to track meals, customer orders, and billing.

OrderEat focuses not only on user-friendly UI but also on functionality for backend operations. It provides robust control to restaurant owners over menu management, reservation handling, and real-time updates for customers.
