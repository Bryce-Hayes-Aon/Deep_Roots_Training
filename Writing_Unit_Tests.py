class CustomerObjective(unittest.TestCase):
    def test_transfertoexternalaccount_withoutoverdrafing(self):
        #Irrelevant
        #Setup bank-to-bank transfer

        #Initial state
        #The source account exists and has some balance available to transfer
        #The destination account exists and has been verified by the source account

        #Action
        #Transfer to the destination account and ensure that the transaction does not overdraft the source account
        
        #Outcome
        #Verify that the source account has been debited by the correct amount and that the transaction has been recorded in the transaction history of the source account