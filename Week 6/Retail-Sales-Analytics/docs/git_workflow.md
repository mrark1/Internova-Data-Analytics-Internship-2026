# Git & GitHub: exact workflow

## One-time setup
Install Git from https://git-scm.com/downloads, then verify:
```bash
git --version
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR GITHUB EMAIL"
```
Create an **empty** GitHub repository named `retail-sales-analytics` (do not initialize it with README, license, or .gitignore if you plan to push this local project as-is). Copy the HTTPS repository URL.

## Clone and place project files
```bash
cd "$HOME/Documents"  # Windows PowerShell: cd $HOME\Documents
git clone https://github.com/YOUR-USERNAME/retail-sales-analytics.git
cd retail-sales-analytics
```
Copy the contents of the provided `Retail-Sales-Analytics` folder into this cloned repository folder. Ensure `README.md` is at the repository root, not one directory deeper.

If you prefer to initialize the already-unzipped folder instead, use `git init`, add the remote URL, and skip `git clone`; do not mix both methods.

## Suggested 3 meaningful commits
Commit 1 — project scaffold and dataset:
```bash
git add README.md requirements.txt data/ docs/
git commit -m "Add project documentation and sales dataset"
git push -u origin main
```
Commit 2 — analysis code and charts:
```bash
git add notebooks/ src/ visualizations/
git commit -m "Add data cleaning EDA and visualizations"
git push
```
Commit 3 — Power BI materials, report and presentation:
```bash
git add powerbi/ report/ presentation/
git commit -m "Add dashboard guide report and presentation"
git push
```
If the branch is named `master`, replace `main` with `master`, or rename it:
```bash
git branch -M main
```

## Practice pull
After creating a README edit on GitHub (or after a collaborator pushes a change), run:
```bash
git pull origin main
```
Run `git status` before and after work. If a pull creates a conflict, resolve the marked conflict in the file, then `git add <file>` and `git commit`.

## Final verification
```bash
git status
git log --oneline -5
git remote -v
```
Copy the GitHub repository URL for assignment submission. Do not submit until the notebook, dataset, visuals, README, report, presentation, and the actual Power BI `.pbix` file (if required by your evaluator) are present.
