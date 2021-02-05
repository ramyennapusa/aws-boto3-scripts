# create secrets in AWS SecretsManager

import boto3

session = boto3.Session(profile_name='prod')
client = session.client("secretsmanager")

response = client.create_secret(
    Name='/secrets',
    Description='Secrets',
    KmsKeyId='123456',
    SecretString='''{
                        "name" : "Ram Yennapusa",
                        "project" : "secret"
                    }''',

    Tags=[
        {
            'Key': 'Project',
            'Value': 'Test'
        },
        {
            'Key': 'Contanct',
            'Value': 'Ram Yennapusa'
        },

    ]
)

print(response)
