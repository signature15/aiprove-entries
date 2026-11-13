#!/usr/bin/env python3
"""Autonomous AIProve agent — reads skill.md, signs in with its keypair, lists
open bounties, and enters one. Zero human in the loop.

    export AGENT_PRIVATE_KEY=0x...
    python3 agent.py
"""
import json
import os
import urllib.request
import urllib.error
from eth_account import Account
from eth_account.messages import encode_defunct

API = os.environ.get("API_BASE_URL", "https://aiprove.fun")


def req(method, path, body=None, token=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(API + path, data=data, method=method)
    r.add_header("content-type", "application/json")
    if token:
        r.add_header("authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def main():
    acct = Account.from_key(os.environ["AGENT_PRIVATE_KEY"].strip())

    # 0. read the one file that explains everything
    with urllib.request.urlopen(f"{API}/skill.md", timeout=30) as r:
        r.read()

    # 1. authenticate: challenge -> sign (EIP-191) -> session token
    _, b = req("GET", f"/api/auth/challenge?address={acct.address}")
    challenge = json.loads(b)["challenge"]
    sig = acct.sign_message(encode_defunct(text=challenge))
    _, b = req("POST", "/api/auth/verify",
               {"address": acct.address, "signature": "0x" + sig.signature.hex()})
    token = json.loads(b)["token"]

    # 2. list open bounties
    _, b = req("GET", "/api/bounties?status=open")
    bounties = json.loads(b)["bounties"]
    print(f"{len(bounties)} open bounties")

    # 3. enter the first open bounty
    if not bounties:
        print("nothing open")
        return
    slug = bounties[0]["slug"]
    _, b = req("POST", f"/api/bounties/{slug}/enter",
               {"handle": "skillmd-agent"}, token)
    print("entered", slug, "->", json.loads(b))


if __name__ == "__main__":
    main()