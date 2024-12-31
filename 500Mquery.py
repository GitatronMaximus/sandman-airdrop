from algosdk.v2client import indexer

# Algonode Indexer API
indexer_client = indexer.IndexerClient("", "https://mainnet-idx.algonode.cloud")

# Asset ID for SandmanAI
asset_id = 2643186677
min_balance = 1_000_000_000_000_000  # 500 million tokens in micro-units

# Fetch accounts holding the asset
try:
    response = indexer_client.asset_balances(asset_id=asset_id)
    accounts = response["balances"]

    # Filter accounts with 500M tokens or more
    filtered_accounts = [
        account for account in accounts if account["amount"] >= min_balance
    ]

    # Print total number of filtered accounts
    total_filtered_accounts = len(filtered_accounts)
    print(f"Total accounts holding 500M+ tokens for asset {asset_id}: {total_filtered_accounts}")

    # Print details of filtered accounts
    print(f"Accounts holding 500M+ tokens for asset {asset_id}:")
    for account in filtered_accounts:
        print(f"Address: {account['address']}, Balance: {account['amount']}")

except Exception as e:
    print(f"Error fetching accounts: {e}")
