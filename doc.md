# API Documentation

This documentation details the API endpoints available in the application.

## Base URL
`127.0.0.1:8000/api/`
---

## Authentication
Some endpoints require authentication, specifically those marked for usage by Admins (`IsAdminUser`).

---

## Scheduling Endpoints

### Get Access Token
Used by users to get an access token.

*   **URL:** `/token/`
*   **Method:** `POST`
*   **Permission:** Public
*   **Body:**
    ```json
    {
        "username": "String",
        "password": "String"
    }
    ```
*   **Response:**
    ```json
    {
        "access": "String",
        "refresh": "String"
    }
    ```

### Refresh Access Token
Used by users to refresh their access token.

*   **URL:** `/token/refresh/`
*   **Method:** `POST`
*   **Permission:** Public
*   **Body:**
    ```json
    {
        "refresh": "String"
    }
    ```
*   **Response:**
    ```json
    {
        "access": "String"
    }
    ```

### Book a Schedule
Used by users to book a specific slot on a specific date.

*   **URL:** `/book-schedule/`
*   **Method:** `POST`
*   **Permission:** Public
*   **Body:**
    ```json
    {
        "date": "YYYY-MM-DD",
        "slot": "ID (integer)",
        "user_info": {
            "department": "ID (integer)",
            "name": "String",
            "phone_number": "String",
            "email": "user@example.com",
            "address": "String",
            "purpose": "Text"
        }
    }
    ```

### Get All Schedules (Admin)
Retrieve all booked schedules.

*   **URL:** `/all-schedule/`
*   **Method:** `GET`
*   **Permission:** Admin
*   **Response:** List of booking details.

### Check Available Slots
Get schedule details for a specific date, including which slots are available.

*   **URL:** `/available-slot/<date>/` (e.g., `/available-slot/2023-10-27/`)
*   **Method:** `GET`
*   **Response:**
    ```json
    {
        "date": "YYYY-MM-DD",
        "available_slots": [
            { "id": 1, "start_time": "09:00:00", "end_time": "10:00:00" },
            ...
        ]
    }
    ```

### Get Weekly Schedule
Retrieve the schedule status for a week starting from a specific date.

*   **URL:** `/weekly-schedule/?start_date=YYYY-MM-DD`
*   **Method:** `GET`
*   **Response:**
    ```json
    [
        {
            "date": "YYYY-MM-DD",
            "slots": [
                { "start_time": "...", "end_time": "...", "status": "Booked/Free" }
            ]
        },
        ...
    ]
    ```

### Create Schedule (Admin)
Initialize a schedule for a date.

*   **URL:** `/create-schedule/`
*   **Method:** `POST`
*   **Permission:** Admin
*   **Body:**
    ```json
    {
        "date": "YYYY-MM-DD",
        "slots": [ID, ID, ...]
    }
    ```

### Manage Schedule (Admin)
Retrieve, update, or delete a schedule for a specific date.

*   **URL:** `/manage-schedule/<date>/`
*   **Method:** `GET`, `PUT`, `PATCH`, `DELETE`
*   **Permission:** Admin

---

## Core Data Endpoints

### Departments
Manage departments.

*   **List & Create:**
    *   **URL:** `/department/`
    *   **Method:** `GET`, `POST`
    *   **Body (POST):** `{ "name": "Department Name" }`
*   **Retrieve, Update, Destroy:**
    *   **URL:** `/department/<pk>/`
    *   **Method:** `GET`, `PUT`, `PATCH`, `DELETE`

### Slots
Manage time slots.

*   **Create (Admin):**
    *   **URL:** `/slot/`
    *   **Method:** `POST`
    *   **Permission:** Admin
    *   **Body:** `{ "start_time": "HH:MM", "end_time": "HH:MM" }`
*   **Retrieve, Update, Destroy:**
    *   **URL:** `/slot/<pk>/`
    *   **Method:** `GET`, `PUT`, `PATCH`, `DELETE`

---

## Communication Endpoints

### Send Email
Send an enquiry or application email via the system.

*   **URL:** `/send-email/`
*   **Method:** `POST`
*   **Body:**
    ```json
    {
        "first_name": "String",
        "last_name": "String",
        "email": "String",
        "subject": "String",
        "motive": "General Enquiry | Job Application | Project Enquiry",
        "message": "Text"
    }
    ```

### List Emails
View list of sent emails/enquiries (Database records).

*   **URL:** `/emails/`
*   **Method:** `GET`

---

## CMS Endpoints (Projects, Heroes, Services, Team)

### Projects
Manage portfolio projects.

*   **List:**
    *   **URL:** `/projects/`
    *   **Method:** `GET`
*   **Create (Admin):**
    *   **URL:** `/create-project/`
    *   **Method:** `POST`
    *   **Permission:** Admin
    *   **Body:** `title`, `project_picture` (file), `short_description`, `project_manager`, `overview`, `start_date`, `end_date`, `status`
*   **Retrieve, Update, Destroy (Admin):**
    *   **URL:** `/project/<pk>/`
    *   **Method:** `GET`, `PUT`, `PATCH`, `DELETE`

### Heroes (Landing Page)
Manage hero section sliders/banners.

*   **List:**
    *   **URL:** `/hero/`
    *   **Method:** `GET`
*   **Create (Admin):**
    *   **URL:** `/create-hero/`
    *   **Method:** `POST`
    *   **Permission:** Admin
    *   **Body:** `title`, `description`, `image` (file)
*   **Retrieve, Update, Destroy (Admin):**
    *   **URL:** `/hero/<pk>/`
    *   **Method:** `GET`, `PUT`, `PATCH`, `DELETE`

### Services
Manage services offered.

*   **List:**
    *   **URL:** `/service/`
    *   **Method:** `GET`
*   **Create (Admin):**
    *   **URL:** `/create-service/`
    *   **Method:** `POST`
    *   **Permission:** Admin
    *   **Body:** `title`, `description`, `image` (file)
*   **Retrieve, Update, Destroy (Admin):**
    *   **URL:** `/service/<pk>/`
    *   **Method:** `GET`, `PUT`, `PATCH`, `DELETE`

### Team Members
Manage team member profiles.

*   **List:**
    *   **URL:** `/team-member/`
    *   **Method:** `GET`
*   **Retrieve, Update, Destroy (Admin):**
    *   **URL:** `/team-member/<pk>/`
    *   **Method:** `GET`, `PUT`, `PATCH`, `DELETE`
*   *(Note: Creation endpoint exists in views but is not explicitly mapped in the provided `urls.py` snippet for `/team-member/` directly as a create view, though `DepartmentCreateView` was ListCreate. `TeamMemberList` is generic ListAPIView. `TeamMemberCreateView` class exists but is not mapped to `create-team-member/` or similar in the provided list, unless `team-member/` was intended to change to ListCreate).*