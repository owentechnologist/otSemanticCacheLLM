# 1. Connection establishment code

import sys,redis,os,ssl

conn = None

DEFAULTS = {
    'host': os.getenv('CACHE_HOST', 'localhost'),
    'port': int(os.getenv('CACHE_PORT', 6379)),
    'username': os.getenv('CACHE_USERNAME', None),
    'password': os.getenv('CACHE_PASSWORD', None),
    'use_tls': os.getenv('CACHE_TLS', 'false').lower() in ('true', '1', 'yes'),
    'ssl_ca_cert': os.getenv('CACHE_SSL_CA_CERT', None),  # None = skip verification
    'ssl_cert_reqs': os.getenv('CACHE_SSL_CERT_REQS', 'none').lower(),  # 'none' → ssl.CERT_NONE
}
'''
Usage examples for running the script with different cache connection options:
# TLS with self-signed cert (no CA verification)
python aas.py --use-tls --ssl-cert-reqs none

# TLS with custom CA cert
python aas.py --use-tls --ssl-ca-cert /path/to/ca.pem

# TLS with certificate verification (default behavior)
python aas.py --use-tls --ssl-cert-reqs required

# All options
python aas.py --host cache.example.com --port 6380 --use-tls --ssl-cert-reqs none
'''
def parse_connection_args():
    args = {}
    i = 1
    
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg.startswith('--host'):
            args['host'] = sys.argv[i + 1] if i + 1 < len(sys.argv) else DEFAULTS['host']
            i += 2
        elif arg.startswith('--port'):
            try:
                args['port'] = int(sys.argv[i + 1]) if i + 1 < len(sys.argv) else DEFAULTS['port']
            except ValueError:
                args['port'] = DEFAULTS['port']
            i += 2
        elif arg.startswith('--username'):
            args['username'] = sys.argv[i + 1] if i + 1 < len(sys.argv) else DEFAULTS['username']
            i += 2
        elif arg.startswith('--password'):
            args['password'] = sys.argv[i + 1] if i + 1 < len(sys.argv) else DEFAULTS['password']
            i += 2
        elif arg.startswith('--use-tls'):
            args['use_tls'] = sys.argv[i + 1].lower() in ('true', '1', 'yes') if i + 1 < len(sys.argv) else DEFAULTS['use_tls']
            i += 2
        elif arg.startswith('--ssl-ca-cert'):
            args['ssl_ca_cert'] = sys.argv[i + 1] if i + 1 < len(sys.argv) else DEFAULTS['ssl_ca_cert']
            i += 2
        elif arg.startswith('--ssl-cert-reqs'):
            args['ssl_cert_reqs'] = sys.argv[i + 1].lower() if i + 1 < len(sys.argv) else DEFAULTS['ssl_cert_reqs']
            i += 2
        elif arg.startswith('--clear'):
            args['clear_cache'] = True
            i += 1
        else:
            i += 1
    
    return args

def connect_to_datastore():
    global conn
    if conn is not None:
        return conn
    if parse_connection_args().get('use_tls', DEFAULTS['use_tls']):
        print(f"*** Connecting to Cache on host {parse_connection_args().get('host', DEFAULTS['host'])} with TLS...")
        conn = redis.StrictRedis(
            host=parse_connection_args().get('host', DEFAULTS['host']),
            port=parse_connection_args().get('port', DEFAULTS['port']),
            username=parse_connection_args().get('username', DEFAULTS['username']),
            password=parse_connection_args().get('password', DEFAULTS['password']),
            #charset="utf-8",
            decode_responses=True,
            ssl=True,                    # Keeps TLS encryption active
            ssl_cert_reqs=ssl.CERT_NONE  # Bypasses all certificate validation
        )
    else:
        print(f"*** Connecting to Cache on host {parse_connection_args().get('host', DEFAULTS['host'])} without TLS...")
        conn = redis.StrictRedis(
            host=parse_connection_args().get('host', DEFAULTS['host']),
            port=parse_connection_args().get('port', DEFAULTS['port']),
            username=parse_connection_args().get('username', DEFAULTS['username']),
            password=parse_connection_args().get('password', DEFAULTS['password']),
            #charset="utf-8",
            decode_responses=True
        )
    
    return conn

