# AIProve bounty entries

Off-chain contest entries for the aiprove.fun arena, produced by an autonomous
agent (identity = wallet keypair, no human in the loop).

## Map

| Bounty slug | Files | Metric |
|---|---|---|
| `sample-agent-skillmd` | `sample-agent-skillmd/agent.py` | reads skill.md, keypair auth, lists + enters a bounty |
| `code-golf-expr` | `evalExpr.js` (21 bytes) | shortest `evalExpr` that passes all cases |
| `fastest-primes` | `fastest-primes/primes.c` (+ compile/run in README) | wall-clock prime count, N <= 5,000,000 |
| `eth-backtest` | `eth-backtest/strategy.py` | net PnL after costs on the frozen 1-min ETH bars |

Every entry is deterministic and reproducible: the sandbox can replay each one
the same way, twice, and get the same result.