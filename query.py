from algosdk.v2client import indexer

# Algonode Indexer API
indexer_client = indexer.IndexerClient("", "https://mainnet-idx.algonode.cloud")

# Asset ID for SandmanAI
asset_id = 2643186677

# Fetch accounts holding the asset
try:
    response = indexer_client.asset_balances(asset_id=asset_id)
    accounts = response["balances"]

    # Print total number of accounts
    total_accounts = len(accounts)
    print(f"Total accounts holding asset {asset_id}: {total_accounts}")

    print(f"Accounts holding asset {asset_id}:")
    for account in accounts:
        print(f"Address: {account['address']}, Balance: {account['amount']}")
except Exception as e:
    print(f"Error fetching accounts: {e}")
