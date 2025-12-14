# 🤝 Contributing Guidelines

Thank you for your interest in contributing to this project.
This document explains how we collaborate and manage changes.

---

## 🌱 Branching Strategy

We follow a simple branching workflow:

- `main`  
  Stable and production-ready version of the project.  
  **Direct commits to this branch are not allowed.**

- `dev`  
  Active development branch where features are integrated.

- `feature/*`  
  Individual feature branches created from `dev`.  
  Each task or improvement should have its own feature branch.

---

## 🔄 Development Workflow

### 1️⃣ Start Development

1. Make sure you are on the `dev` branch and up to date:

   ```bash
   git checkout dev
   git pull
   ```

2. Create a new feature branch from `dev`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. (If applicable) Activate the virtual environment:

   * **Windows (PowerShell):**

     ```powershell
     venv\Scripts\Activate.ps1
     ```

   * **Linux / macOS:**

     ```bash
     source venv/bin/activate
     ```

---

### 2️⃣ Implement Changes

4. Work on your changes locally.

5. Commit your changes with a clear message:

   ```bash
   git add .
   git commit -m "Describe your change clearly"
   ```

6. Ensure all dependencies are captured:

   ```bash
   pip freeze > requirements.txt
   ```

---

### 3️⃣ Open Pull Request

7. Push the feature branch to GitHub:

   ```bash
   git push -u origin feature/your-feature-name
   ```

8. Ensure CI checks (Black & Flake8) pass before requesting a merge.

9. Open a Pull Request from your feature branch to `dev`.

---

### 🔁 Handling Pull Request Feedback

If changes are requested during code review:

1. Stay on the **same feature branch**:

   ```bash
   git checkout feature/your-feature-name
   ```

2. Apply the requested changes locally.

3. Commit the updates:

   ```bash
   git add .
   git commit -m "Address PR feedback"
   ```

4. Push the updates to GitHub:

   ```bash
   git push
   ```

> The existing Pull Request will be updated automatically.
> **Do not create a new branch or a new Pull Request for review fixes.**

---

### 🧹 Branch Cleanup (After Merge)

After the Pull Request is approved and merged:

1. Switch back to `dev`:

   ```bash
   git checkout dev
   ```

2. Delete the local feature branch:

   ```bash
   git branch -d feature/your-feature-name
   ```

3. Delete the remote feature branch:

   ```bash
   git push origin --delete feature/your-feature-name
   ```

---

## 📐 Coding Standards

- Follow PEP8 style guidelines (using Black and Flake8).
- Linting is enforced only on production code inside `src/`.
- Use `snake_case` for variable and function names.
- Add docstrings for functions when applicable.
- Keep experimental work in notebooks.
- Production-ready code should be placed in `src/`.
- Avoid committing large datasets directly to the repository.

---

## 📣 Communication

* Use GitHub Issues to discuss new ideas or bugs.
* Use Pull Requests for all code changes.
* Review and discuss changes before merging.