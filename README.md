# PrepAI: AI-Powered Adaptive Learning Platform

This repository contains the full-stack implementation of PrepAI, an AI-powered adaptive learning and assessment platform.

## Local Development and Testing

To run the application locally for development and testing, follow these steps:

### 1. Set up the Backend

- **Navigate to the backend directory:**
  ```bash
  cd backend
  ```
- **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
- **Create a `.env` file:**
  - Copy the `.env.example` file to `.env`.
  - Add your Google Gemini API key to the `.env` file.
- **Run the backend server:**
  ```bash
  uvicorn main:app --host 0.0.0.0 --port 8000
  ```

### 2. Set up the Frontend

- **Navigate to the frontend directory:**
  ```bash
  cd frontend
  ```
- **Install dependencies:**
  ```bash
  npm install
  ```
- **Run the frontend development server:**
  ```bash
  npm run dev
  ```
The frontend will be available at `http://localhost:5173`.

### 3. Run End-to-End Tests

- **Make sure the backend server is running.**
- **Navigate to the frontend directory:**
  ```bash
  cd frontend
  ```
- **Run the Playwright tests:**
  ```bash
  npm run test
  ```
This will run the end-to-end tests and generate a screenshot in the `playwright-report` directory.
