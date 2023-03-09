import frappe
from frappe.model.naming import make_autoname

def payment_entry_before_insert(doc, method):
    if doc.naming_series:
        doc.naming_series = 'GSG-JV-.YYYY.-'

    doc.name = make_autoname(doc.naming_series + '#####')

def payment_entry_on_update(doc, method):
    frappe.db.set_value('Payment Entry', doc.name, 'naming_series', doc.naming_series)