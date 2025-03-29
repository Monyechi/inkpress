# InkPress

InkPress is a full-stack Django project that simulates a professional newspaper website. Built with modern web technologies and a classic newspaper layout, InkPress demonstrates a comprehensive range of Django skills, from model design to custom views and responsive front-end styling.

## Features

- **Newspaper-Style Post Detail:**  
  - **Drop Cap:** The first letter of each article is styled as a drop cap for a classic look.
  - **Inline Images & Featured Image:** Articles support inline images with a featured image that is prominently displayed.
  - **Advertisement Sidebar:** An advertisement box is positioned on the right-hand side of the article, mimicking real newspaper layouts.
  - **3-Column Layout:** Articles are rendered in a fixed three-column layout on desktop, with responsive adjustments for smaller screens.

- **Index Page Thumbnails:**  
  - Published articles are displayed as uniformly sized thumbnails in a grid of four columns.
  - Each thumbnail features the article title, a cropped featured image, publication date, and the author's name.

- **User Authentication:**  
  - Custom login and logout views that redirect users to the index page.
  - A sign-up page for new user registration using Django's built-in authentication system.

- **Admin & Draft Management:**  
  - Admin users have access to a "Create Post" view with two actions: **Save as Draft** or **Publish**.
  - Draft posts (i.e., posts with `submitted` set to `False`) can be viewed in a dedicated drafts page.
  - Only published posts are displayed on the public index.

- **Media Handling:**  
  - Featured images and inline images are stored in a dedicated media directory with proper configuration.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/inkpress.git
   cd inkpress
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Usage

- **Index Page:**  
  Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see published articles displayed as thumbnails.

- **Article Detail:**  
  Click on any thumbnail to view the full article with a newspaper-style layout.

- **User Authentication:**  
  - **Sign Up:** Navigate to `/signup/` to create a new account.
  - **Login:** Navigate to `/login/` to log in.
  - **Logout:** Use the logout link available in the navigation bar.

- **Admin Functionality:**  
  Admin users can access `/posts/create/` to create a new article. They can choose to save it as a draft or publish it immediately. Drafts can be viewed at `/drafts/`.

## Technologies Used

- **Backend:** Django 5.1.7, Python 3.12.7
- **Frontend:** HTML5, CSS3 (with responsive design using CSS Grid and media queries)
- **Database:** SQLite (default Django configuration; configurable)

## Future Improvements

- Integration of a rich text editor for post content.
- Enhanced media management with cloud storage support.
- Additional front-end polish with custom JavaScript interactions.
- Automated tests for views and models.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
