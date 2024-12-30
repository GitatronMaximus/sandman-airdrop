from algosdk.v2client import indexer

# Algonode Indexer API
indexer_client = indexer.IndexerClient("", "https://mainnet-idx.algonode.cloud")

# Asset ID for SandmanAI
asset_id = 2643186677

# Fetch accounts holding the asset
try:
    response = indexer_client.asset_balances(asset_id=asset_id)
    accounts = response["balances"]

    # Extract all account addresses
    addresses = [account['address'] for account in accounts]

    # Print total number of addresses
    total_accounts = len(addresses)
    print(f"Total accounts holding asset {asset_id}: {total_accounts}")

    # Print all addresses separated by commas with no spaces
    print("Account addresses:")
    print(",".join(addresses))
except Exception as e:
    print(f"Error fetching accounts: {e}")
