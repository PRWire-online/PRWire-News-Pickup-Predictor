#!/usr/bin/env node

interface PredictorInput {
  pressReleases: number;
  tier: "local" | "national" | "global";
}

interface PredictorOutput {
  pressReleases: number;
  tier: string;
  pickupScore: number;
  estimatedReach: number;
}

const TIER_MULTIPLIERS: Record<string, number> = {
  local: 0.4,
  national: 0.7,
  global: 1.0,
};

const BASE_REACH: Record<string, number> = {
  local: 5000,
  national: 20000,
  global: 50000,
};

export function predictPickup(input: PredictorInput): PredictorOutput {
  const multiplier = TIER_MULTIPLIERS[input.tier] ?? 1.0;
  const pickupScore = Math.min(100, Math.round(40 + input.pressReleases * multiplier));
  const estimatedReach = Math.round(
    BASE_REACH[input.tier] + input.pressReleases * multiplier * 1000
  );

  return {
    pressReleases: input.pressReleases,
    tier: input.tier,
    pickupScore,
    estimatedReach,
  };
}

const args = process.argv.slice(2);
const pressReleases = parseInt(args[0]) || 10;
const tier = (args[1] as PredictorInput["tier"]) || "global";

const result = predictPickup({ pressReleases, tier });

console.log(`Press Releases: ${result.pressReleases}`);
console.log(`Tier: ${result.tier}`);
console.log(`Estimated Pickup Score: ${result.pickupScore}/100`);
console.log(`Syndication Reach: ~${result.estimatedReach.toLocaleString()}`);
