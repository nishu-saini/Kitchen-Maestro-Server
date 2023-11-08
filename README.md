# Kitchen-Maestro-Server

Kitchen-Maestro is a server-side application built using Django that serves as a virtual recipe box.

It allows users to create and manage recipes, complete with titles, price points, cooking times, ingredients, and tags such as "comfort food," "vegan," or "dessert."

This README file provides an overview of the key features and functionalities of the application.

## Features

- **User Authentication**: Kitchen-Maestro provides robust user authentication, ensuring that only authorized users can access and modify recipes.

- **Creating Objects (Recipes)**: Users can easily create recipes by providing essential information, including titles, price points, cooking times, ingredients, and tags. This feature allows users to document their favorite recipes and culinary creations.

- **Filtering and Sorting Objects**: The application offers powerful filtering and sorting capabilities, enabling users to quickly find and organize their recipes based on various criteria.

- **Uploading and Viewing Images**: Kitchen-Maestro supports image uploads, allowing users to attach pictures of their dishes to their recipes.

## APIs

### USER

- **POST**: `/api/user/create`

- **GET**: `/api/user/me`

- **PUT**: `/api/user/me`

- **PATCH**: `/api/user/me`

- **POST**: `/api/user/token`

### RECIPE

- **GET**: `/api/recipe/ingredients`

- **PUT**: `/api/recipe/ingredients/{id}`

- **PATCH**: `/api/recipe/ingredients/{id}`

- **DELETE**: `/api/recipe/ingredients/{id}`

- **GET**: `/api/recipe/recipes/`

- **POST**: `/api/recipe/recipes/`

- **GET**: `/api/recipe/recipes/{id}`

- **PUT**: `/api/recipe/recipes/{id}`

- **PATCH**: `/api/recipe/recipes/{id}`

- **DELETE**: `/api/recipe/recipes/{id}`

- **POST**: `/api/recipe/recipes/{id}/upload-image`

- **GET**: `/api/recipe/tags`

- **PUT**: `/api/recipe/tags/{id}`

- **PATCH**: `/api/recipe/tags/{id}`

- **DELETE**: `/api/recipe/tags/{id}`

### SWAGGER DOCS

- **Endpoint**: `/api/docs`

### ADMIN

- **Endpoint**: `/admin/`

**NOTE**: For more detail about API endpoint follow [api-docs](api-docs).

## Installation Guide

**NOTE**: The `main` branch of the repository is ahead by some commits and is set for deployment. For testing purposes, use the `delete-commit-branch`.

- Make sure you have the following tools and software installed:
  - Docker
  - Docker-Compose
  - Python (for Django)
  - Postgres database

1. Clone the repository to your local machine (`delete-commit-branch`):

   ```bash
   git clone https://github.com/nishu-saini/Kitchen-Maestro-Server/tree/delete-commit-branch
   ```

2. Open terminal in project root directory and create a python virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Make database migrations for Django project

   ```bash
   docker-compose run --rm app sh -c "python manage.py makemigrations"
   ```

5. Build docker image:

   - Note: This will also create the necessary migrations needed to create the database in Django.

   ```bash
   docker-compose build
   ```

6. Create a superuser for the Django admin:

   - Note: Remember email and password for admin route, otherwise need to make new admin user to access admin route.

   ```bash
   docker-compose run --rm app sh -c 'python manage.py createsuperuser'
   ```

7. To run unit tests, use the following command:

   ```bash
   docker-compose run --rm app sh -c 'python manage.py test'
   ```

8. Start development server

   ```bash
   docker-compose up
   ```

## Usage

- Access the API at http://localhost:8000/api/docs.
- Access the Django admin at http://localhost:8000/admin/ to manage recipes and users.
