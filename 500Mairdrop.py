from algosdk.v2client import algod, indexer
from algosdk.transaction import AssetTransferTxn
from algosdk import account, mnemonic

# Nodely Indexer API
indexer_client = indexer.IndexerClient("", "https://mainnet-idx.4160.nodely.dev")

# Algod client setup for sending transactions
algod_address = "https://mainnet-api.4160.nodely.dev"
algod_client = algod.AlgodClient("", algod_address)

# Asset and wallet details
asset_id = ""  # Algorand Asset ID
sender_mnemonic = ""  # Private key of sender wallet
sender_private_key = mnemonic.to_private_key(sender_mnemonic)
sender_address = account.address_from_private_key(sender_private_key)

# Airdrop amount per wallet (in micro-units)
airdrop_amount = 1300000000000  # 1.3M tokens with 6 decimals

# Minimum balance to qualify for the airdrop (500M tokens in micro-units)
min_balance = 500_000_000_000_000  # 500M tokens in micro-units

# Fetch accounts holding the asset
def fetch_holders(asset_id):
    try:
        response = indexer_client.asset_balances(asset_id)
        accounts = response.get("balances", [])
        # Filter accounts with 500M tokens or more
        return [
            account["address"] for account in accounts if account["amount"] >= min_balance
        ]
    except Exception as e:
        print(f"Error fetching holders: {e}")
        return []

# Perform the airdrop
def perform_airdrop(addresses):
    try:
        params = algod_client.suggested_params()
        for recipient in addresses:
            txn = AssetTransferTxn(
                sender=sender_address,
                sp=params,
                receiver=recipient,
                amt=airdrop_amount,
                index=asset_id
            )
            signed_txn = txn.sign(sender_private_key)
            tx_id = algod_client.send_transaction(signed_txn)
            print(f"Sent {airdrop_amount} tokens to {recipient}. Transaction ID: {tx_id}")
    except Exception as e:
        print(f"Error during airdrop: {e}")

# Main logic
try:
    print(f"Fetching holders of asset {asset_id}...")
    addresses = fetch_holders(asset_id)
    total_accounts = len(addresses)
    print(f"Total accounts eligible for airdrop: {total_accounts}")

    if total_accounts > 0:
        print("Starting the airdrop...")
        perform_airdrop(addresses)
        print("Airdrop complete!")
    else:
        print("No accounts meet the criteria for the airdrop.")
except Exception as e:
    print(f"Error: {e}")
