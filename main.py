from vonage_modules.send_sms import SendSMSAction, VonageModule

if __name__ == "__main__":
    module = VonageModule()
    module.register(SendSMSAction, "SendSMSAction")
    module.run()
