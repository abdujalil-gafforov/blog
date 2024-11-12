# Blog Project

This project is a minimalistic blog website built using **Django**.

## Features

- User registration and authentication
- Social login via Google and GitHub
- Phone number verification using SMS OTP
- Create, edit, and delete posts
- Download posts as PDFs with QR codes
- View trending posts (most viewed in the last month)
- Responsive pagination
- Auto-deletion of posts cancelled for more than 7 days

## Technologies Used

- **Backend**: Django, PostgreSQL
- **Frontend**: CKEditor, SweetAlert2
- **Asynchronous Tasks**: Celery, Redis
- **SMS Services**: Twilio
- **Version Control**: Git, GitHub
- **Monitoring**: Sentry
- **Containerization**: Docker

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

- **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` to manage posts, users, and other administrative tasks.
- **Manage Posts**: Users can create, edit, and delete posts.
- **Comments**: Users can leave comments on posts.
- **PDF Download**: Each post can be downloaded as a PDF, allowing offline viewing or sharing.

## Contributing

To contribute, follow these steps:

1. Fork the repository.
2. Create your branch: `git checkout -b new-feature`
3. Make your changes and commit them: `git commit -m 'Added new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request.

## License

This project is distributed under the [MIT License](LICENSE).
