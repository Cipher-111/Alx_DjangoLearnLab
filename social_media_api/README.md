API Documentation
Authentication Endpoints
1. Register User

POST /api/accounts/register/

Request

{
  "username": "john",
  "password": "123456",
  "bio": "Hello world"
}


Response

{
  "token": "generated_token_here",
  "user": {
    "id": 1,
    "username": "john",
    "bio": "Hello world",
    "profile_picture": null
  }
}

2. Login

POST /api/accounts/login/

Request

{
  "username": "john",
  "password": "123456"
}


Response

{
  "token": "generated_token_here"
}

3. User Profile

GET /api/accounts/profile/

Headers

Authorization: Token your_token_here


Response

{
  "id": 1,
  "username": "john",
  "bio": "Hello world",
  "profile_picture": null
}

Post Endpoints
1. List Posts

GET /api/posts/

Example:

/api/posts/?page=1
/api/posts/?search=hello


Response

{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": "john",
      "title": "My First Post",
      "content": "This is the content",
      "created_at": "2025-12-08T12:00:00Z",
      "updated_at": "2025-12-08T12:00:00Z"
    }
  ]
}

2. Create Post

POST /api/posts/

Headers

Authorization: Token your_token_here


Request

{
  "title": "My Post",
  "content": "This is a new post"
}


Response

{
  "id": 1,
  "author": "john",
  "title": "My Post",
  "content": "This is a new post",
  "created_at": "2025-12-08T12:00:00Z",
  "updated_at": "2025-12-08T12:00:00Z"
}

3. Retrieve Single Post

GET /api/posts/1/

Response

{
  "id": 1,
  "author": "john",
  "title": "My Post",
  "content": "This is a new post",
  "created_at": "2025-12-08T12:00:00Z",
  "updated_at": "2025-12-08T12:00:00Z"
}

4. Update Post

PUT/PATCH /api/posts/1/

Headers

Authorization: Token your_token_here


Request

{
  "title": "Updated Title",
  "content": "Updated content"
}


Response

{
  "id": 1,
  "author": "john",
  "title": "Updated Title",
  "content": "Updated content",
  "created_at": "2025-12-08T12:00:00Z",
  "updated_at": "2025-12-08T13:00:00Z"
}

5. Delete Post

DELETE /api/posts/1/

Headers

Authorization: Token your_token_here


Response

{
  "detail": "Post deleted successfully"
}

Comment Endpoints
1. List Comments

GET /api/comments/

Response

[
  {
    "id": 1,
    "post": 1,
    "author": "john",
    "content": "Nice post!",
    "created_at": "2025-12-08T12:30:00Z",
    "updated_at": "2025-12-08T12:30:00Z"
  }
]

2. Create Comment

POST /api/comments/

Headers

Authorization: Token your_token_here


Request

{
  "post": 1,
  "content": "This is a comment"
}


Response

{
  "id": 2,
  "post": 1,
  "author": "john",
  "content": "This is a comment",
  "created_at": "2025-12-08T12:40:00Z",
  "updated_at": "2025-12-08T12:40:00Z"
}

3. Retrieve Single Comment

GET /api/comments/1/

4. Update Comment

PUT/PATCH /api/comments/1/

Headers

Authorization: Token your_token_here


Request

{
  "content": "Updated comment"
}

5. Delete Comment

DELETE /api/comments/1/

Headers

Authorization: Token your_token_here


Response

{
  "detail": "Comment deleted successfully"
}
