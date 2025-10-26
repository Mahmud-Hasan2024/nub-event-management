# 📅 NUB Event Management System

A **Django-based web application** designed for **Northern University Bangladesh (NUB)** to manage and organize events efficiently.  
This system supports **user authentication, role-based access control (RBAC), RSVP functionality, email activation**, and **Django signals**, offering a modern and secure platform for event coordination.

---

## 🚀 Live Website

https://event-management-9y10.onrender.com
    

---

## 👤 Demo Accounts

| Role | Username | Password |
| --- | --- | --- |
| Admin | `admin1` | `password123` |
| Employer | `organizer1` | `password123` |
| Job Seeker | `participant1` | `password123` |

Use these credentials to log in and explore the website.

---

## 🌟 Features

### 🔐 Authentication

-   User **signup, login, and logout** functionality.
    
-   Signup fields include: `username`, `email`, `password`, `first_name`, and `last_name`.
    
-   **Email verification** required for account activation.
    

### 🧑‍💼 Role-Based Access Control (RBAC)

Roles are implemented using **Django Groups**:

-   **Admin** 🛠️ — Full control: manage users, events, and categories.
    
-   **Organizer** 🎯 — Create, update, and delete events & categories.
    
-   **Participant** 👤 — View events and RSVP to attend.
    

🔒 Access to views is restricted based on user roles using **decorators**.

---

## 📬 RSVP System

-   Participants can RSVP to events they’re interested in.
    
-   RSVP data is stored via a **ManyToMany relationship** between `User` and `Event`.
    
-   Duplicate RSVPs are prevented.
    
-   A **confirmation email** is sent automatically after RSVP.
    
-   Participants can view their RSVPs in their **dashboard**.
    

---

## ✉️ Email Activation

-   On registration, a **secure activation email** is sent to the user.
    
-   Users must activate their account before login.
    
-   Uses Django’s built-in `default_token_generator` for secure activation links.
    

---

## ⚡ Django Signals & Media Files

-   **Signals** are used for automation:
    
    -   Send activation email after registration.
        
    -   Send RSVP confirmation email.
        
-   Added **ImageField** to the `Event` model with a **default event image**.
    

---

## 🖥️ User Dashboards

Upon login, users are redirected to role-based dashboards:

| Role | Dashboard Description |
| --- | --- |
| **Admin** | Manage all events, participants, and categories |
| **Organizer** | Manage own events and categories |
| **Participant** | View and manage RSVP’d events |

---

## 🛠️ Tech Stack

-   **Framework:** Django 5.x
    
-   **Frontend:** HTML, CSS, Bootstrap
    
-   **Database:** SQLite / PostgreSQL
    
-   **Authentication:** Django Auth + Email Verification
    
-   **Email Service:** SMTP
    
-   **Other Tools:** Django Signals, Django Messages Framework
    

---

## 📂 Project Structure

```csharp
NUB_Event_Management_System/
│
├── users/                # Authentication, roles, and user management
├── events/                  # Event models, views, RSVP logic
├── templates/               # HTML templates for UI
├── static/                  # CSS, JS, and images
├── media/                   # Uploaded event images
├── event_management/                  # Project settings, URLs, WSGI
├── core/                   # Core application logic
└── manage.py
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/NUB-Event-Management-System.git
cd NUB-Event-Management-System
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # For Mac/Linux
venv\Scripts\activate        # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

Then open your browser and go to:  
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📸 Screenshots (Optional)

*(Add your project screenshots here)*

-   Login Page
    
-   Admin Dashboard
    
-   Organizer Event Management
    
-   Participant RSVP List
    

---

## 💡 Future Enhancements

-   Event reminder emails.
    
-   Event search and filtering.
    
-   Integration with Google Calendar.
    

---

## 🤝 Contributors

👨‍💻 **\[Mahamud Hasan\]** — Developer & Maintainer  
🎓 Northern University Bangladesh

Learn more about me in my [About Me](About_Author.md) file.

---

## Deployment

For deployment instructions, refer to the [DEPLOYMENT.md](DEPLOYMENT.md) file.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---