def build_img_tag(name):
    return f'<img src="resources/{name}.png" alt="{name.title()}" loading="lazy" width="188" height: auto >'


def get_logo(company_name):
    company_logos = [
        'galaxydigitalservices',
        'ethereumfoundation',
        'chainsafesystems',
        'ramp.network',
        'econetwork',
        'penumbralabs',
        'gauntlet', 'kadena',
        'royal', 'swissborg',
        'copperco',
        'messari', 'Coinshift',
        'storyprotocol',
        'tron', 'OpenSea',
        'subspacelabs',
        'digitalasset',
        'exodus54', 'request',
        'offchainlabs',
        'tokenmetrics',
        'crypto', 'syndica',
        'aave', 'Swissquote',
        'alchemy', 'immutable',
        'amun', 'ellipsislabs',
        'dfinity', 'web3auth',
        'parity', 'kiln',
        'ankr', 'ultra',
        'solana', 'osmosisdex',
        'ledger', 'Keyrock',
        'flashbots',
        'oplabs', 'optimism',
        'bitfinex',
        'magiceden',
        'nethermind',
        'trustwallet',
        'coinmarketcap',
        'chainalysis',
        'quiknodeinc',
        'wintermute',
        'mobilecoin',
        'bitpanda',
        'bitgo', 'blox-route',
        'shardeum',
        'bitmex', 'StationLabs',
        'OKX', 'jumpcrypto',
        'tether', 'poap',
        'paradigm.co',
        'paradigm.xyz',
        'dune', 'cere-network',
        'bitfury', 'enso',
        'archblock',
        '0x', 'oasisnetwork',
        'chia', 'iofinnet',
        'AQX', 'conduit',
        'kraken', 'taxbit',
        'ethglobal',
        'harmony', 'theblock',
        'bebop', 'Notabene',
        'chainstack',
        'chainlink',
        'axiomzen',
        'bitwise',
        'tessera',
        'paxos', 'with-foundation',
        'eigenlabs',
        'bitcoin',
        'binance',
        'bitget', 'hextrust',
        'stably',
        'bitstamp',
        'consensys',
        'ripple',
        'aztec', 'toku',
        'stellar',
        'sygnum',
        'okcoin',
        'matterlabs',
        'clearmatics',
        'worldcoin',
        'edgeandnode',
        'risklabs',
        'circle',
        'bittrex', 'rain',
        'exponential',
        'kaiko', 'coinmetrics',
        'hiro', 'serotonin',
        'zora', 'aptoslabs',
        'filecoinfoundation',
        'celestia',
        'polymerlabs',
        'uniswaplabs',
        'moonpay',
        'moonwalk',
        'figment',
        'blockdaemon',
        'avalabs',
        'Polygon',
        'multiversx',
        'status', 'Blockworks',
        'cexio', 'ethenalabs',
        'dappradar',
        'web3', 'xapo',
        '21co', 'goldsky',
        'smart-token-labs',
        'avantgarde',
        'cryptofinance',
        'Luxor', 'wirex',
        'anchorage',
        'biconomy',
        'solanafoundation',
        'fuellabs',
        'immunefi',
        'protocollabs',
        'foundrydigital',
        'o1labs', 'trmlabs',
        '3boxlabs', 'coinspaid',
        'BlockSwap',
        'orderlynetwork',
        'sprucesystems',
        'arbitrumfoundation',
        'magic', 'evmos',
        'outlierventures',
        'walletconnect',
        'almanak', 'dydxopsdao',
        'grayscaleinvestments',
        'prepo', 'safe.global',
        'RabbitHole', 'clockwork-labs',
        'Sui.Foundation', 'center',
        'paraswap', 'stakefish',
        'connext-network',
        'request.network',
        'superfluid', 'thetie',
        'glassnode'
    ]
    if company_name in company_logos:
        return build_img_tag(company_name)
    return company_name.upper()
