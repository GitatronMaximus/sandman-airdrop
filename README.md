# Sandman Token Airdrop Scripts

This repository contains scripts for managing and airdropping **SandmanAI** tokens on the Algorand blockchain. These tools allow you to fetch token holders and perform airdrops efficiently.

## Features

- **Fetch Holders**: Retrieve all accounts holding the SandmanAI token.
- **Airdrop Tokens**: Distribute tokens to all token holders from a wallet you control.
- Supports assets with **6 decimals**.

## Prerequisites

1. Python 3.7 or later installed on your system.
2. Install the required Python dependency:
   ```bash
   pip install py-algorand-sdk

### Scripts

```bash
airdrop.py
```

This is the main script for performing the airdrop. It:

Fetches all wallet addresses holding the SandmanAI token.
Sends a specified amount of tokens to each wallet.

Usage:
Open the script and update the following variables:

asset_id: Your token's asset ID.
sender_mnemonic: The 25-word mnemonic of the wallet performing the airdrop.
airdrop_amount: The number of tokens to send (in micro-units).

Run the script:
```bash 
python3 airdrop.py
```

Example:
To send 1.3 million tokens (with 6 decimals), set:

airdrop_amount = 1300000000000  # 1.3M tokens in micro-units

Notes:
Ensure the sender wallet has enough funds for the total airdrop and transaction fees (0.001 ALGO per transaction).

Logs each transaction ID after sending.

```bash
query.py
```

This script fetches and lists all wallet addresses holding the SandmanAI token.

Usage:
Open the script and update the asset_id to your token's asset ID.

Run the script:

```bash
python3 query.py
```

Output
Prints the total number of holders.
Lists all wallet addresses in a readable format.

```bash
query2.py
```

This script fetches wallet addresses and outputs them as a comma-separated list with no spaces.

Usage:
Open the script and update the asset_id to your token's asset ID.

Run the script:

```bash
python3 query2.py
```

Output: Prints all wallet addresses separated by commas (no spaces), suitable for direct use in other tools.

## Example Workflow
Use query.py or query2.py to fetch the list of wallet addresses holding the token.
Run airdrop.py to distribute tokens to the fetched wallets.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contributions
Feel free to fork this repository and submit pull requests with improvements or fixes.

# Author
Developed by Gitatron Maximus

For questions, contact me at https://x.com/GitatronMaximus
