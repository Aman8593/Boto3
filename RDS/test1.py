import boto3
import pymysql
# Create a Secrets Manager client
client = boto3.client('secretsmanager')

# Create a new secret
response = client.create_secret(
    Name='my-rds-secret',
    SecretString='{"username": "admin", "password": "admin123"}'
)

# Get the secret ARN
secret_arn = response['ARN']

# Create a new RDS MySQL instance
client = boto3.client('rds')

response = client.create_db_instance(
    DBName='database-1',
    DBInstanceIdentifier='database-1',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='mariadb',
    MasterUsername='admin',
    MasterUserPassword='admin123',
    VpcSecurityGroupIds=['sg-0d07e9259630eead7'],
    AvailabilityZone='ap-south-1',
    BackupRetentionPeriod=0,
    PubliclyAccessible=True
)

# Wait for the RDS instance to become available
waiter = client.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier='database-1')

# Get the RDS instance endpoint
response = client.describe_db_instances(DBInstanceIdentifier='database-1')
endpoint = response['DBInstances'][0]['Endpoint']['Address']

# Connect to the RDS instance using the secret ARN
conn = psycopg2.connect(
    host=endpoint,
    user='database-1',
    password=client.get_secret_value(SecretId=secret_arn)['SecretString']['aman123'],
    dbname='database-1'
)

# Create a sample table
cur = conn.cursor()
cur.execute('CREATE TABLE sample_table (id INT PRIMARY KEY, name TEXT)')
conn.commit()