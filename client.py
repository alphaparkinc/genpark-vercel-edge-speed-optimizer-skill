class VercelEdgeSpeedOptimizerClient:
    def estimate_latency(self, bundle_size_kb: int) -> dict:
        return {"estimated_cold_start_ms": round(15.0 + (bundle_size_kb * 0.05), 1)}