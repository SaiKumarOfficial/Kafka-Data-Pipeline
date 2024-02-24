
import os

#cloud api details
API_KEY = "PGBHCET2U5HV4RIU"#os.getenv('API_KEY',None)
API_SECRET_KEY =  "GSJDYdkOy4qShfCZGuw7CpmJJbGcGdxlYHO8fj2BBsFUqq4zMMhrZ6RJRrhYQ7oC"  #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER =  "pkc-41p56.asia-south1.gcp.confluent.cloud:9092"     #os.getenv('BOOTSTRAP_SERVER',None)
#authentication related variables
SECURITY_PROTOCOL =  "SASL_SSL"    # os.getenv('SECURITY_PROTOCOL',None)
SSL_MACHENISM =  "PLAIN"  #os.getenv('SSL_MACHENISM',None)
#schema related variables
ENDPOINT_SCHEMA_URL  = "https://psrc-j09o2.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY ="FSZK4WHS6KNBGYSL" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "4J0JWMSIfOjoQK4LyR75knocNfNmb91gJri9I+EDLu9vatkIo1Xtkp/b0TTDovpU" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)

#SASL - Simple Authentication Security Layer
def sasl_conf():  #this function gives us kafka cluster configurations

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

