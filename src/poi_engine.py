import hashlib
import time

class POIEngine:
    """
    HPI Core: Proof-of-Impact Engine
    Validates humanitarian aid delivery through multi-party attestation.
    """
    def __init__(self, threshold=2):
        self.min_signatures = threshold  # Number of people needed to verify aid

    def generate_event_id(self, worker_id, beneficiary_id, timestamp):
        """Creates a unique, tamper-evident ID for the delivery."""
        raw_string = f"{worker_id}{beneficiary_id}{timestamp}"
        return hashlib.sha256(raw_string.encode()).hexdigest()

    def verify_delivery(self, event_id, signatures):
        """
        The 'Consensus' logic. 
        If enough people signed, the impact is 'Proven'.
        """
        if len(signatures) >= self.min_signatures:
            return {
                "status": "VERIFIED",
                "proof_hash": hashlib.sha256(event_id.encode()).hexdigest(),
                "timestamp": time.time()
            }
        else:
            return {"status": "PENDING", "reason": "Insufficient signatures"}
