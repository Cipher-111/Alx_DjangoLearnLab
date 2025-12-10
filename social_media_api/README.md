--------------------
API Documentation
--------------------
Authentication Endpoints

  1. Register User

    Endpoint: POST /api/accounts/register/

    Description: Creates a new user account. Returns an authentication token and user details.

  2. Login

    Endpoint: POST /api/accounts/login/

    Description: Authenticates an existing user. Returns an authentication token.

  3. User Profile

    Endpoint: GET /api/accounts/profile/

    Description: Retrieves the current user's profile information. Requires authentication.

  Post Endpoints

    1. List Posts

    Endpoint: GET /api/posts/

    Description: Lists all posts. Supports pagination and search filters (by title/content).

    2. Create Post

    Endpoint: POST /api/posts/

    Description: Creates a new post. Requires authentication.

  3. Retrieve Single Post

    Endpoint: GET /api/posts/<post_id>/

    Description: Retrieves details of a single post by ID.

  4. Update Post

    Endpoint: PUT/PATCH /api/posts/<post_id>/

   Description: Updates a post. Only the author can update. Requires authentication.

  5. Delete Post

    Endpoint: DELETE /api/posts/<post_id>/

    Description: Deletes a post. Only the author can delete. Requires authentication.

    Comment Endpoints

  1. List Comments

    Endpoint: GET /api/comments/

    Description: Lists all comments.

  2. Create Comment

    Endpoint: POST /api/comments/

    Description: Creates a new comment on a post. Requires authentication.

  3. Retrieve Single Comment

   Endpoint: GET /api/comments/<comment_id>/

    Description: Retrieves details of a single comment by ID.

  4. Update Comment

   Endpoint: PUT/PATCH /api/comments/<comment_id>/

    Description: Updates a comment. Only the author can update. Requires authentication.

  5. Delete Comment

    Endpoint: DELETE /api/comments/<comment_id>/

   Description: Deletes a comment. Only the author can delete. Requires authentication.


--------------------------
Follow and Feed Endpoints
--------------------------
Follow a User

Endpoint: /api/accounts/follow/<user_id>/

Description: Allows a user to follow another user by their ID. Requires authentication. Updates the following relationship between users.

Unfollow a User

Endpoint: /api/accounts/unfollow/<user_id>/

Description: Allows a user to unfollow another user by their ID. Requires authentication. Updates the following relationship between users.

View Feed

Endpoint: /api/posts/feed/

Description: Retrieves posts from users that the current user follows. Posts are sorted by creation date, with the most recent posts first. Requires authentication.

User Model Changes

Field Added: following

Description: A many-to-many relationship representing users that a given user follows. Supports tracking followers and followees.

--------------------------------------------------------
               SOCIAL MEDIA API DOCUMENTATION
-------------------------------------------------------
Authentication Endpoints

  Register User: Create a new user account.

  Login: Authenticate an existing user.

  User Profile: Retrieve information about the current user.

Follow Endpoints

  Follow User: Follow another user.

  Unfollow User: Unfollow a user.

Feed Endpoint

  Retrieve Feed: View posts from users the current user follows, ordered by creation date (most recent first).

Post Endpoints

  List Posts: View all posts with optional pagination and search.

  Create Post: Add a new post.

  Retrieve Post: View details of a specific post.

  Update Post: Edit an existing post.

  Delete Post: Remove a post.

Comment Endpoints

  List Comments: View all comments.

  Create Comment: Add a comment to a post.

  Retrieve Comment: View details of a specific comment.

  Update Comment: Edit a comment.

  Delete Comment: Remove a comment.

Likes Endpoints

  Like a Post: Like a specific post.

  Unlike a Post: Remove a like from a post.

Notifications Endpoints

  Retrieve Notifications: Get all notifications for the current user.

  Mark Notification as Read: Mark a notification as read.