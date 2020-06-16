#!/usr/bin/env python3

from aws_cdk import core

from itiro.itiro_stack import ItiroStack


app = core.App()
ItiroStack(app, "itiro")

app.synth()
