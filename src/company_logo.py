def build_img_tag(name):
    return f'<img src="resources/{name}.png" alt="{name.title()}" loading="lazy" width="188" height: auto >'


def get_logo(company_name):
    company_logos = [
        'wintermute',
        'mobilecoin',
        'bitpanda',
        'bitgo',
        'bitmex',
        'OKX',
        'tether',
        'paradigm.com',
        'paradigm.xyz',
        'dune',
        'bitfury',
        'archblock',
        '0x',
        'chia',
        'AQX',
        'kraken',
        'ethglobal',
        'harmony',
        'bebop',
        'chainstack',
        'chainlink',
        'axiomzen',
        'bitwise',
        'tessera',
        'paxos',
        'eigenlabs',
        'bitcoin',
        'binance',
        'bitget',
        'stably',
        'bitstamp',
        'consensys',
        'ripple',
        'aztec',
        'stellar',
        'sygnum',
        'okcoin',
        'matterlabs',
        'clearmatics',
        'worldcoin',
        'edgeandnode',
        'risklabs',
        'circle',
        'bittrex',
        'kaiko',
        'hiro',
        'avalabs',
        'Polygon',
        'multiversx',
        'status',
        'cexio',
        'dappradar',
        'web3',
        'smart-token-labs',
        'avantgarde',
        'cryptofinance',
        'Luxor',
        'anchorage',
        'biconomy',
        'solanafoundation',
        'fuellabs'
    ]
    if company_name in company_logos:
        return build_img_tag(company_name)
    return company_name.upper()
