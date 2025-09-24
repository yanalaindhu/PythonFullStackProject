# Daily Journal Web App 

The Daily Journal is a web application that allows users to record their personal thoughts, experiences, or notes on a daily basis. It functions like a digital diary where entries can be created, viewed, updated, and deleted (CRUD operations).

# Features
**User Management**: Store users with username, email, and password. Each journal entry is linked to a specific user.
**Add Journal Entries**: Users can write a title and content. Entries are saved with a timestamp.
**View Journal Entries**: Users can see all their past entries, displaying title, content, and creation time.
**Update/Edit Entries**: Users can edit the title or content of existing entries.
**Delete Entries**: Users can remove unwanted entries.

# project structure

 DiaryHub/
 |
 |---src/               #core application logic
 |  |---logic.py/      #business logic and task
 operations
 |  |__db.py/           #Database operations
 |
 |---api/               #Backend API
 |  |__main.py/         #FASTAPI endpoints
 |        
 |---frontend/          #Frontend application
 |   |__app.py/          #Streamlit web interface
 |
 |___requirements.txt   #Python Dependencies
 |
 |___README.md          #project documentation
 |
 |___.env               #python variables

## Quick Start

### Prerequisites

-Python 3.8 or higher
-A supabase account
-Git(push,cloning)

### 1.Clone or Download the project
# Option 1: Clone with Git
git clone <https://github.com/yanalaindhu/PythonFullStackProject.git>
# Option 2: Download and extract the ZIP.

# 2: Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3. Set up supabase Database

1.create a supabase project

2.create the users Table:
-Go the SQLeditor in your supabase dashboard
-run this SQL command:
```sql
    CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
3. **get your credentials**:
### 4, configure Environment variables

1. create a `.env` file in the project root
2.Add your supabase credentials to `.env`:
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

**example**
SUPABASE_URL="https://pnjkohkbhjcybpwtilyk.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBuamtvaGtiaGpjeWJwd3RpbHlrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODM1NDAsImV4cCI6MjA3MzY1OTU0MH0.tgOjdocRVOqJnXc9Ke20E0S0jrH0wg88nVrLdte7GNg"

### 5. Run the application

### Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at `http://localhost:8501`

## FastAPI Backend

cd api
python main.py

The API will be available at `http://localhost:8000`

### How to use

### Technical Details

### Technogies used

**frontend**:Streamlit(python web framework)
**backend**:FastAPI(python REST API framework)
**Database**:supabase(PostgreSQL-based backend-as-a-service)
**language**:python 3.8+

### key components:

1.**`src/db.py`**:Database operations 
    -handles all CRUD operations with supabase
2.**`src/logic.py`**:Business logic 
    -

## Troubleshooting

## common Issues

**Module not found errors**: Ensure all dependencies are installed using pip install -r requirements.txt.
    
## future enhancements

ideas for extending this project
1. **Full User Authentication System**

Signup, login, password recovery, email verification.

Role-based access: e.g., admin vs. regular user.

2. **Advanced Journal Features**

Rich text editor with formatting, images, or embedded links.

Voice-to-text journal entries.

Add entry reminders via email or notifications.

3. **Mood & Analytics**

Track moods for each entry.

Generate charts/graphs for mood trends over time.

Show statistics: most active days, word count trends, etc.

4.**Tagging & Organization**

Add tags or categories for entries.

Enable search, filter, and sort entries by date, mood, or tag.

5. **Collaboration / Sharing**

Optionally share entries with selected friends/family.

Allow comments or reactions on shared entries.

6. **Export & Backup**

Export journal entries as PDF, Markdown, or CSV.

Cloud backup and restore to prevent data loss.

### support
If you encoounter any issues or have questions:
--phone no:9703006316
--email id:yanalaindhu11@gmail.com












