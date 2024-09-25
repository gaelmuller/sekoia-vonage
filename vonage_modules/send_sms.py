import requests
from pydantic import BaseModel, Field
from sekoia_automation.action import Action
from sekoia_automation.module import Module


class VonageModuleConfiguration(BaseModel):
    api_key: str = Field(secret=True, description="Vonage API Key")
    api_secret: str = Field(secret=True, description="Vonage API Secret")


class VonageModule(Module):
    configuration: VonageModuleConfiguration


class SendSMSArguments(BaseModel):
    from_name: str = Field("Sekoia XDR")
    text: str = Field(..., description="The text content of the SMS")
    to: str = Field(..., description="The phone number to send the SMS to")


class SendSMSAction(Action):
    module: VonageModule

    name = "Send SMS"
    description = "Send an SMS using the Vonage API"

    def run(self, arguments: SendSMSArguments):
        # Send SMS using the Vonage API
        requests.post(
            "https://rest.nexmo.com/sms/json",
            data={
                "api_key": self.module.configuration.api_key,
                "api_secret": self.module.configuration.api_secret,
                "from": arguments.from_name,
                "text": arguments.text,
                "to": arguments.to,
            },
        )
