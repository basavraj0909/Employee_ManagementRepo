# Blog App
## Overview
The `blog` app is part of a larger project designed to manage and display blog posts. 
It allows users to create, update, delete, and view posts. 
The app also supports categorization, tagging, and comment management, 
providing a flexible platform for content creation.

## Features
- **CRUD Operations for Blog Posts**: Create, read, update, and delete blog posts.
- **Commenting System**: Users can add, edit, and delete comments on posts.
- **Categorization and Tagging**: Posts can be categorized and tagged for better organization.
- **User Authentication**: Integrated with the registration app, allowing only registered users to perform certain actions.


## Installation
1. Clone the repository: git clone <repository-url>
2. Create a virtual environment:
    
- On Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
4. Install dependencies: pip install -r requirements.txt
5. Apply migrations: python manage.py migrate
6. Run the server: python manage.py runserver


## API Endpoints

List of Blog Posts
URL: /api/blog/posts/
Method: GET
Description: Retrieve a list of all blog posts.

Create a New Blog Post
URL: /api/blog/posts/
Method: POST
Description: Create a new blog post.

Update a Blog Post
URL: /api/blog/posts/<id>/
Method: PUT
Description: Update an existing blog post.

Delete a Blog Post
URL: /api/blog/posts/<id>/
Method: DELETE
Description: Delete a blog post.

## Database Schema
    Tables
        Post
            Fields: id, title, content, created_at, updated_at, category, tags
        Comment
            Fields: id, post_id, content, author, created_at
        Category
            Fields: id, name, description
### GET /posts/
- **Description**: Retrieve a list of all blog posts.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "title": "My First Post",
      "content": "This is the content of my first post...",
      "created_at": "2024-09-01T12:00:00Z"
    },
    ...
  ]
  ```

### POST /posts/
- **Description**: Create a new blog post.
- **Request**:
  ```json
  {
    "title": "My New Post",
    "content": "This is the content of my new post..."
  }
  ```
- **Response**:
  ```json
  {
    "id": 2,
    "title": "My New Post",
    "content": "This is the content of my new post...",
    "created_at": "2024-09-02T12:00:00Z"
  }
  ```

## Database Schema

### Tables:
- **Post**
  - Fields: `id`, `title`, `content`, `created_at`, `updated_at`
- **Comment**
  - Fields: `id`, `post_id`, `content`, `author`, `created_at`
- **Category**
  - Fields: `id`, `name`, `description`
