# Public vs. Private Boundary

## Safe to publish

- architecture
- algorithms
- data models
- synthetic examples
- deterministic validators
- stress-test policy
- unit tests
- deployment patterns
- screenshots with PII removed

## Keep private

- Smart Meter credentials
- ESIID
- service address
- personal email addresses
- API keys
- raw usage and bills
- production dedupe state
- browser storage/cookies
- private host details if undesired

The public package replaces real provider/customer data with synthetic fixtures and exposes extension interfaces where private integrations would connect.
