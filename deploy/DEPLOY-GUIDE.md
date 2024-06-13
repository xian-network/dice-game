# Deploy your contract to Xian Testnet

### Instructions :

1. Create a wallet & get some tokens.
    - Create a new wallet : 
        - Download the Xian wallet extension [here](https://chromewebstore.google.com/detail/xian-wallet/kcimjjhplbcgkcnanijkolfillgfanlc)
        - Or use the web wallet [here](https://wallet.xian.network/)
    - Ask in Telegram for some testnet tokens (Faucet bot TBA)
    - https://t.me/xian_network/1

2. Open `deploy.py` 
    - Replace `<your private key here>` with your wallet's private key.
    - On Line 5, enter the correct path to the contract you wish to deploy.
    - Replace `<contract_name>` with a name for your contract. Must start with `con_`.

3. From the terminal :
    ```bash
    > python3 deploy.py
    ```

4. Interact with your contract on the Xian Testnet using the Xian wallet of your choice.

