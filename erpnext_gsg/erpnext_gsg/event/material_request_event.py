import frappe
@frappe.whitelist()
def create_stock_entry(doc, event):
    print("*"*100)
    print(doc.items[0].item_code)
    
    if(doc.material_request_type != "Material Issue"):
        return
        
    from erpnext.stock.doctype.material_request.material_request import make_stock_entry
    new_stock_entry = make_stock_entry(doc.name)
    new_stock_entry.insert()
    new_stock_entry.submit()
    #     stock_entry_doc = frappe.new_doc("Stock Entry")
    #     stock_entry_doc.stock_entry_type = doc.material_request_type
    #     stock_entry_doc.from_warehouse = doc.set_from_warehouse
    #     for item in doc.get("items"):
    #         stock_entry_doc.append("items",{
    #             "s_warehouse":item.from_warehouse, 
    #             "t_warehouse": item.warehouse,
    #             "qty": item.qty,
    #             "item_code": item.item_code
    #         })

    #     stock_entry_doc.insert()
