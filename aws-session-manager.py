#!/usr/bin/env python

import configparser
import os
import random
import boto3


def get_aws_config():
    config = configparser.ConfigParser()
    config.readfp(open(os.path.expanduser('~/.aws/config')))
    profiles = []
    for i in config.sections():
        profiles.append(i.replace('profile ', ''))
    return profiles, config

def sts(role_arn):
    client = boto3.client('sts')
    response = client.assume_role(RoleArn=role_arn,
                                  RoleSessionName=str(random.randrange(1000, 9999)),
                                  DurationSeconds=3600)
    fp = open(os.path.expanduser('~/.aws/temp_session'), 'w')
    fp.write("""export AWS_ACCESS_KEY_ID={0}
export AWS_SECRET_ACCESS_KEY={1}
export AWS_SESSION_TOKEN={2}
export AWS_ROLE_ARN={3}""".format(str(response['Credentials']['AccessKeyId']),
                                  str(response['Credentials']['SecretAccessKey']),
                                  str(response['Credentials']['SessionToken']),
                                  str(role_arn))
          )
    fp.close()


if __name__ == "__main__":
    profiles, config = get_aws_config()
    print('\n############ Choose a profile ###########\n')
    for i in profiles:
        print('{0} - {1}'.format(profiles.index(i), i))

    index = input('Profile Number: ')
    section = config['profile {0}'.format(profiles[int(index)])]
    sts(section['role_arn'])
