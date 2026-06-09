#!/usr/bin/env python3
"""
PRWire News Pickup Predictor
Predict press release pickup probability and syndication reach.
https://prwire.online
"""

import sys

TIER_MULTIPLIERS = {
    "local": 0.4,
    "national": 0.7,
    "global": 1.0,
}

BASE_REACH = {
    "local": 5000,
    "national": 20000,
    "global": 50000,
}


def predict_pickup(press_releases: int, tier: str = "global") -> dict:
    """
    Predict news pickup score and syndication reach.

    Args:
        press_releases: Number of press releases distributed
        tier: Distribution tier — local, national, or global

    Returns:
        dict with pickup_score and estimated_reach
    """
    tier = tier.lower()
    multiplier = TIER_MULTIPLIERS.get(tier, 1.0)
    pickup_score = min(100, round(40 + press_releases * multiplier))
    estimated_reach = round(
        BASE_REACH.get(tier, 50000) + press_releases * multiplier * 1000
    )

    return {
        "press_releases": press_releases,
        "tier": tier,
        "pickup_score": pickup_score,
        "estimated_reach": estimated_reach,
    }


if __name__ == "__main__":
    press_releases = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    tier = sys.argv[2] if len(sys.argv) > 2 else "global"

    result = predict_pickup(press_releases, tier)

    print(f"Press Releases: {result['press_releases']}")
    print(f"Tier: {result['tier']}")
    print(f"Estimated Pickup Score: {result['pickup_score']}/100")
    print(f"Syndication Reach: ~{result['estimated_reach']:,}")
