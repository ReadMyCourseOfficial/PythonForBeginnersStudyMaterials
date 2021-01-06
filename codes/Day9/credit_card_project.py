#16 or 19 digits are present in the credit card
#0 can not be present in the starting of credit card no
#masked card no

example_credit_card_no="0234567891234567"
masked_credit_card_no= "123**********567"

# 1. take the credit card no from the user
# 2. validate the credit card no
# 3. print the masked card no

print(len(example_credit_card_no))
print(example_credit_card_no[0])
masked_credit_card_no=example_credit_card_no[0:3]+"*"*(len(example_credit_card_no)-6)+example_credit_card_no[-3:]
print(masked_credit_card_no)
