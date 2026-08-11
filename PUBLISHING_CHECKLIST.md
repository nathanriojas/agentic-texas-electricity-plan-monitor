# Publishing Checklist

Before making the repository public:

- [ ] Confirm no real `.env` exists.
- [ ] Confirm no `data/`, `logs/`, or `reports/` directories are staged.
- [ ] Search for service address / ESIID / account numbers.
- [ ] Search for personal email addresses.
- [ ] Search for API keys and provider credentials.
- [ ] Use a **brand-new Git repository** for this sanitized edition instead of copying private Git history.
- [ ] Run the test suite.
- [ ] Review screenshots for PII before adding them.
- [ ] Rotate any secret that was ever accidentally committed.

Recommended first publication:

```bash
git init
git add .
git status
git commit -m "Initial public release"
git branch -M main
git remote add origin <YOUR-GITHUB-REPO-URL>
git push -u origin main
```
