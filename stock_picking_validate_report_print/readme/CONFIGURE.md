To configure this module, you need to:

Go to Inventory > Configuration > Operation Types and activate the "Print
Reports at Validation" option under the "Report Print at Validate" tab.
Stock picking reports using this operation type will be automatically sent
to a printer.
There are two ways of selecting the documents and printers, split into two
sections in the operation type form view under the "Report Print at
Validate" tab:

1.  **General Configuration**. When a user included in the "Users" field
    validates a stock picking with this operation type, the reports
    selected in the field "Reports" will be sent to the printer selected
    in the "Printers" field. It is possible to specify the number of
    copies of each documents that will be printed by introducing a value
    in the "Copies" field. If no users are selected in the "Users" field,
    the reports selected in the "Reports" field will be sent to print no
    matter the user who performs the validation.
2.  **User Configuration**. When a user in the "User" column validates a
    stock picking with this operation type, the report selected in the
    column "Report" will be sent to the printer selected in the column
    "Printer". It is possible to specify the number of copies that will be
    printed by introducing a value in the "Copies" column.

In case a document needs to be printed by both the General Configuration
and the User Configuration, the configuration set in the User
Configuration has priority over the General Configuration. This way, a
document is only printed once, even if it is included in both the
"General Configuration" and the "User Configuration".
