# Architecture

## Design goal

Turn an electricity-plan search into an autonomous, evidence-backed decision pipeline.

The system separates **discovery**, **validation**, **economic comparison**, and **actionability** so that a failure in one layer cannot silently produce a recommendation.

## Usage layer

Inputs can include 15-minute interval readings, billing-cycle totals, contract metadata, incumbent pricing, and current early termination fee rules.

The interval layer matters most for time-of-use products. Provider EFL examples often assume a generic distribution of usage across free or discounted windows. The decision engine should use the customer's real distribution instead.

## Market layer

Snapshot the market and compare it with the previous snapshot using a material-field fingerprint. Marketing text or harmless metadata should not trigger expensive reprocessing.

## Screening layer

Cheap screening is approximate. Its only purpose is to decide where expensive document extraction is worthwhile. A screen result is never an actionable recommendation.

## Document-model layer

Extract the actual pricing components: provider base/energy charges, TDU fixed/per-kWh charges, bill credits, usage fees, one-time charges, time-of-use periods, termination terms, and conditional fees. A deterministic validator then recomputes the EFL's published sample prices.

## Type-specific validation

### Fixed / bill-credit
Replay the formula across expected billing-cycle usage.

### Time-of-use
First reproduce the EFL sample using the EFL's stated assumed usage share. Then separately replay the candidate against real interval readings. This keeps provider load-shape assumptions separate from actual customer behavior.

### Variable
Stress-test today's economics rather than treating today's rate as guaranteed. Example scenarios: current, +10%, +25%, +50%.

### Prepaid
Treat balance rules, daily fees, disconnect/reconnect rules, and conditional pricing explicitly. If governing documents conflict, block the plan.

## Switch-now economics

Comparison should use a common horizon and include incumbent projected cost, candidate projected cost, incumbent cancellation cost, mandatory candidate charges, and contract-overhang caveats.

## Exact-offer verification

A marketplace listing can be technically live while the same offer is absent from a provider's generic catalog. The final gate therefore verifies the actual enrollment destination for the service address and looks for exact plan identity before declaring a recommendation actionable. It fails closed.

## Notifications

Notifications should be event-driven: opportunity email only when actionable, duplicate suppression, contract-expiration reminders, pipeline failure alerts, and optionally a weekly health/market digest.
