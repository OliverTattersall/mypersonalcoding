import receipt_formatter
import receipt_reader


# receipt_formatter.main(r'receipts\test_receipt1.jpg')
receipt_formatter.main(r'receipts\test_receipt3.jpg')
print(receipt_reader.get_value("result.png"))