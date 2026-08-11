# Security

Never commit `.env`, credentials, service addresses, meter identifiers, production databases, browser profiles, API keys, or notification destinations.

Before publishing:

```bash
git status
git grep -n -I -E '(password|secret|api[_-]?key|esiid|street|@)' .
```

Review every match manually. If a secret was ever committed, rotate it and remove it from Git history.
