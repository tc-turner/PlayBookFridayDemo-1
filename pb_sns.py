"""
 Copyright 2017 ThreatConnect, Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================
"""

""" third party """
import boto3

""" custom """
from tcex import TcEx

tcex = TcEx()

tcex.parser.add_argument(
    '--aws_region', help='AWS Region', required=True)
tcex.parser.add_argument(
    '--topic_arn', help='Topic ARN', required=True)
tcex.parser.add_argument(
    '--access_key_id', help='IAM Access Key ID', required=True)
tcex.parser.add_argument(
    '--secret_access_key', help='IAM Secret Access Key', required=True)
tcex.parser.add_argument(
    '--sns_message', help='Message', required=True)

# get args
args = tcex.args

def main():
    """ Main PB App Entrypoint """
    try:
        client = boto3.client(
            'sns',
            region_name=args.aws_region,
            aws_access_key_id=args.access_key_id,
            aws_secret_access_key=args.secret_access_key
        )

        response = client.publish(
            TopicArn=args.topic_arn,
            Message=tcex.playbook.read(args.sns_message),
            Subject='TC PB Example'
        )

        tcex.playbook.create_output('sns.debug', response['MessageId'])
    except Exception as e:
        tcex.log.error(e.message)
        tcex.playbook.create_output('sns.debug', e.message)
        tcex.exit(1)

if __name__ == "__main__":
    main()