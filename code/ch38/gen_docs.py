policy = """
# Refunds
The refund window is 30 days from the delivery date. Items must be unused
and in original packaging. Refunds are issued to the original payment
method within 5 business days of our receiving the returned item.
Gift cards cannot be refunded after purchase under any circumstances.

# Shipping
Standard shipping takes 5 to 7 business days within the continental US.
Express shipping arrives in 2 business days if ordered before 2 PM.
We do not ship to PO boxes. International delivery takes 10 to 21 days
and any customs duties are payable by the recipient.

# Warranty
The warranty covers manufacturing defects for one year from purchase.
Damage from misuse, liquid, or unauthorized repair is excluded. A defective
unit is replaced rather than repaired when stock is available.

# Accounts
You may reset your password from the sign-in screen. Accounts inactive for
24 months are archived. To close an account, contact support; closure is
permanent and any store credit is forfeited.

# Payments
We accept major credit cards and bank transfer. Invoices for business
accounts are due 30 days from issue. A late fee of 1.5 percent per month
applies to overdue balances.
"""
open("policy.md", "w").write(policy.strip())
print(f"wrote policy.md: {len(policy.split())} words")
