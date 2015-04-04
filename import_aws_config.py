#!/usr/bin/python

# Support: danromuald@drmbanga.com
# Id import_aws_config.py Thursday March 26 2015 20:04 SAST
Idver = 1.0
# Mbanga 2015

#Notes:
"""
 This piece of code reads the aws configs from the default boto aws 
 config file. Use it as a module to avoid putting credentials in your boto codes.
"""

import os
import ConfigParser

#Begin

def getAwsCreds():
    
    creds = ()
    
    # Initialize a config parser object
    
    config = ConfigParser.ConfigParser()
    
    # Load the correct config file to the parser.
    # This could be made better by validating the config file
    # and passing it to the function; I'm just lazy!
    
    config.read(os.environ['HOME']+'/.aws/credentials')
    
    access_key_id = config.get('default', 'aws_access_key_id')
    
    secret_access_key = config.get('default', 'aws_secret_access_key')
    
    creds = (access_key_id, secret_access_key)
    
    return creds

"""
# Uncomment for testing

def main():
    credentials = getAwsCreds()
    print "Access Key = " + credentials[0]
    print "Secret Access Key = " + credentials[1] 
         
if __name__ == '__main__':
     main()

"""
