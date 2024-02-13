# LAB - Class 26

## Project: Django Snacks

### Author: [Your Name or Group Name]

### Overview

In this project, we explore the fundamentals of Django by building a simple website with two pages: a home page and an about page. We've utilized Django's robust framework to efficiently create a functional multi-page site. Additionally, we've incorporated TailwindCSS and Flowbite for styling, embracing a utility-first approach to CSS.

### Links and Resources

- GitHub Repo: [django-snacks](https://github.com/your-github-username/django-snacks) (replace with your actual GitHub repo link)

### Setup
#### Dependencies
- Django
- TailwindCSS (via django-tailwind)
- Flowbite

#### `.env` requirements
- `SECRET_KEY`: Your Django secret key
- `DEBUG`: Set to `True` for development, `False` for production

#### Running the Application
1. Clone the repository:
   ```
   git clone https://github.com/your-github-username/django-snacks.git
   ```
2. Navigate to the project directory:
   ```
   cd django-snacks
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```
   python manage.py runserver
   ```

### Tests
- Tests are located in the `snacks/tests.py` file.
- Run tests with:
  ```
  python manage.py test
  ```

#### Notable Tests
- `test_home_page_status_code`: Ensures the home page is accessible.
- `test_about_page_status_code`: Ensures the about page is accessible.
- `test_home_page_template_use`: Verifies the correct template is used for the home page.
- `test_about_page_template_use`: Verifies the correct template is used for the about page.

### Stretch Goals Achievements
- Added additional apps within the project to demonstrate Django's scalability.
- Integrated dark mode using TailwindCSS.
- Enhanced UI with Flowbite components.

---

Remember to replace placeholder links and names with your actual project information. Tailoring the README to reflect the specifics of your project will make it more useful for users and contributors.