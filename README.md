# slushpool-python
A simple API wrapper for Slushpool
## Quick Start
```python
from slushpool import Slushpool

s = Slushpool("access-token")

s.stats     # SlushpoolStats object
s.account   # SlushpoolAccount object
s.update()  # Update stats and account information
```

## Details
### Slushpool Class
The `Slushpool` class is useful for updating stats and account information at the same time.
```python
from slushpool import Slushpool

s = Slushpool("access-token")

s.stats     # SlushpoolStats object
s.account   # SlushpoolAccount object
s.update()  # Update stats and account information
```
API access tokens are only required for the `SlushpoolAccount` class.
If no token is provided, `Slushpool.account` with be `None`.
```python
s = Slushpool()

s.stats   # SlushpoolStats object
s.account # None
```
If public pool stats all you're interested in, it's probably better to use the `SlushpoolStats` class.
The difference with providing an access token for stats is you will see your rewards for recent block information instead of `'0.00000000'`.

### SlushpoolStats Class
Slushpool stats are from [https://slushpool.com/stats/json/optional-token](https://slushpool.com/stats/json/).
An example response looks like this:
```json
{
  "blocks": {
    "554996": {
      "is_mature": 0,
      "date_found": "2018-12-22 23:14:16",
      "hash": "000000000000000000310b4e9014504aefc58ef4c14abc3032237ee8ae0e4669",
      "confirmations": 30,
      "total_shares": 2446223480232,
      "total_score": 1076135671625.1742,
      "reward": "0.00000000",
      "mining_duration": 2737,
      "date_started": "2018-12-22 22:28:39",
      "nmc_reward": "0.00000000",
    },
    ... // Most recent 30 blocks
  },
  "active_workers": 0,
  "round_started": "2018-12-22 23:14:16",
  "luck_30": "0.94",
  "shares_cdf": "94.70",
  "luck_b50": "1.01",
  "luck_b10": "0.94",
  "active_stratum": 0,
  "ghashes_ps": "3.86871139874e+27",
  "shares": 15000289359851,
  "round_duration": "04:42:49",
  "score": "1.87632558846e+13",
  "luck_b250": "0.97",
  "luck_7": "0.93",
  "luck_1": "0.98"
}
```
The `SlushpoolStats` objects don't require an access token
```python
from slushpool import SlushpoolStats

stats = SlushpoolStats() # or
stats = SlushpoolStats("token")

stats.ghashes_ps   # 3.89142412984e+27
```

If an access token is provided you will see that account's rewards instead of `"0.00000000"`.

The `SlushpoolStats.blocks.block` object properties are put into a `SlushpoolStats.Block` object.
This makes property access nicer. The height is also added as a property of the block.
```python
stats.blocks["554996"].height
```
There is also a method to quickly get information about the last block found by the pool
```python
# same as stats.blocks["{highest-height}"].height
stats.last_block.height   
```
`SlushpoolStats` has it's own update method to refresh information
```python
stats.update()
```

### SlushpoolAccount Class
Slushpool Account information is taken from [https://slushpool.com/accounts/profile/json/required-token](https://slushpool.com/accounts/profile/json/)

An example response looks like
```json
{
  "username": "Username",
  "unconfirmed_reward": "1.23456789",
  "rating": "none",
  "nmc_send_threshold": "1.23456789",
  "unconfirmed_nmc_reward": "1.23456789",
  "estimated_reward": "1.23456789",
  "hashrate": "123456789",
  "confirmed_nmc_reward": "1.23456789",
  "send_threshold": "1.23456789",
  "confirmed_reward": "1.23456789",
  "workers": {
    "Username.Worker": {
      "last_share": 123456789,
      "score": "1234567.89",
      "alive": true,
      "shares": 123456789,
      "hashrate": 123456789
    }
  },
  "wallet": "hidden"
}
```
An access token is required for `SlushpoolAccount`
```python
from slushpool import SlushpoolAccount

account = SlushpoolAccount("token")
account.hashrate   # in Mh/s
```

The `SlushpoolAccount.workers.worker` object properties are put into a `SlushpoolAccount.Worker` object.
This makes property access nicer.
```python
account.workers["Username.Worker"]
```
There is also a method to get worker just by name since the username is included in the response
```python
# same as account.workers["Username.Worker"]
account.worker("Worker")
```
`SlushpoolAccount` has it's own update method to refresh information
```python
account.update()
```
