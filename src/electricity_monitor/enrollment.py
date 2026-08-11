from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class EnrollmentVerification:
    plan_id: str
    verified: bool
    reason: str

class EnrollmentVerifier(Protocol):
    def verify(self, plan_id: str) -> EnrollmentVerification: ...

class FailClosedVerifier:
    def verify(self, plan_id: str) -> EnrollmentVerification:
        return EnrollmentVerification(plan_id, False, "No private enrollment verifier configured")

def require_verified(plan_ids: list[str], verifier: EnrollmentVerifier) -> list[str]:
    return [plan_id for plan_id in plan_ids if verifier.verify(plan_id).verified]
