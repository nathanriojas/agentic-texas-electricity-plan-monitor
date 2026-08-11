# Private Deployment Pattern

This public repository is intentionally not wired to live accounts.

Recommended separation:

```text
Git repository
  code only

~/.config/electricity-monitor/
  secrets.env
  service_location.json

private runtime storage
  usage database
  market snapshots
  pricing models
  dedupe state
```

## Host

- Linux VPS or AWS Lightsail
- Python 3.11+
- systemd
- optional Chromium/Playwright for enrollment verification
- persistent swap if the host is memory constrained

## Example timer

```ini
[Unit]
Description=Run electricity monitor daily

[Timer]
OnCalendar=*-*-* 12:15:00 UTC
RandomizedDelaySec=10m
Persistent=true

[Install]
WantedBy=timers.target
```

Keep all real credentials, addresses, ESIIDs, emails, API keys, and customer usage outside source control.
