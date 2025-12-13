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

- `feature-*`  
  Individual feature branches created from `dev`.  
  Each task or improvement should have its own feature branch.

---

## 🔄 Development Workflow

1. Make sure you are on the `dev` branch and up to date:
   ```bash
   git checkout dev
   git pull
   ```

2. Create a new feature branch:

   ```bash
   git checkout -b feature-your-feature-name
   ```

3. Work on your changes locally.

4. Commit your changes with a clear message:

   ```bash
   git add .
   git commit -m "Describe your change clearly"
   ```

5. Push the feature branch to GitHub:

   ```bash
   git push -u origin feature-your-feature-name
   ```

6. Open a Pull Request from your feature branch to `dev`.

7. Ensure CI checks (Black & Flake8) pass before requesting a merge.


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