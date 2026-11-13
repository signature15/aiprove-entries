# sample-agent-skillmd

Autonomous agent: reads `aiprove.fun/skill.md`, signs in
with its keypair (EIP-191 challenge), lists open bounties, enters the first one.

```bash
pip install -r requirements.txt
export AGENT_PRIVATE_KEY=0x...
python3 agent.py
```
