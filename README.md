# Blog Project

This project is a minimalistic blog website built using **Django**.

## Features

- Create, edit, and delete posts
- User authentication and authorization
- Commenting feature for posts
- Categorization of posts by category

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abdujalil-gafforov/blog.git
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the local server:**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser.

## Usage

- Access the admin panel at: `http://127.0.0.1:8000/admin/`
- Use the admin panel to create, edit, and delete posts.
- Users can view posts and leave comments through the website.

## Contributing

To contribute, follow these steps:

1. Fork the repository.
2. Create your branch: `git checkout -b new-feature`
3. Make your changes and commit them: `git commit -m 'Added new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request.

## License

This project is distributed under the [MIT License](LICENSE).
