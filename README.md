# Release Notes


# Disclaimer
```
This is not an official TC app and will not be supported.  This is for demo purposes only.  Use only as a learning tool.
```

Full documentation of the TC Platform API and SDKs can be found at [ThreatConnect Developer Documentation](https://docs.threatconnect.com/en/latest/)

# TCPB_-_SNS
This is a simple demo app for TC PlayBooks that will send a message to an AWS SNS topic.

## Input Parameters
* AWS Region: valid AWS SNS region
* Topic ARN: SNS Topic ARN in the defined AWS Region
* AWS Access Key ID: Your AWS Access Key ID stored in a TC Variable
* AWS Secret Access Key: Your AWS Secret Access Key stored in a TC Variable
* Message: A string message to be sent to the Topic ARN

## Output Parameters
* sns.debug: Either the SNS MessageId or an Exception message

## Known Issues
 If you mismatch your region and Topic ARN you will get the following message 

 ```
 An error occurred (InvalidParameter) when calling the Publish operation: Invalid parameter: TopicArn
 ```
 This is a [boto3 bug](https://github.com/boto/boto3/issues/646)


## 0.0.1
+ Initial release
