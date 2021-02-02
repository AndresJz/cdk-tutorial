#!/usr/bin/env python3

from aws_cdk import core

from test_s3.test_s3_stack import TestS3Stack


app = core.App()
TestS3Stack(app, "test-s3")

app.synth()
