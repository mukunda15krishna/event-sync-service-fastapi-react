# Event Sync Service

## Overview

This project reconciles meeting data from two independent sources:

- CRM Events
- Calendar Events

The application reads both datasets, identifies matching meetings, detects conflicts, and presents a unified view through a FastAPI backend and a React frontend.

---

# Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn

## Frontend

- React
- Vite
- Axios

---

# Project Structure

```
EventSyncService
│
├── backend
│   ├── data
│   ├── services
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── package.json
│   └── vite.config.js
│
├── AI_USAGE.md
├── README.md
└── venv
```

---

# Setup

## Backend

```
cd backend

..\venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# API

GET

```
/meetings
```

Returns the reconciled meeting list.

GET

```
/health
```

Health endpoint.

---

# Matching Strategy

Meetings are matched primarily using:

- Subject
- Meeting Date

The reconciliation process produces:

- Matched meetings
- CRM-only meetings
- Calendar-only meetings

---

# Conflict Detection

Conflicts are identified when the CRM location differs from the Calendar location for matched meetings.

Conflict rows are highlighted in the UI.

---

# Frontend Features

- Dashboard cards
- Search
- Filter
- Conflict highlighting
- Source identification
- Responsive table

---

# Assumptions

- Subject and meeting date uniquely identify most meetings.
- Missing values are displayed as "N/A".
- Unmatched records are retained.

---

# Time Spent

Approximately 8–10 hours.

---

# AI Usage

AI was used to assist with:

- Architecture planning
- FastAPI implementation
- React UI implementation
- README preparation
- General code review

## Additional Documentation

- `AI_DOCUMENTATION.md` — Documents how AI tools were used during development and the developer's decision-making process.

## Future Improvements

- Improve fuzzy matching using client names and meeting times.
- Normalize malformed dates automatically.
- Detect duplicate meetings across sources.
- Persist reconciled data in a database.
- Add automated unit tests.