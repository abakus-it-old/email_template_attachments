{
    'name': "Email template attachments",
    'version': '9.0.1.0',
    'depends': ["mail"],
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Email',
    'description': 
    """
Email template attachments

Added field in email_template to allow get attachment in mail_compose_message of the follow way:
    - From other fields with relation to ir.attachment of the current object
    
The added field (text) will be evaluated. You can access to "object".
Example: object.attachments_ids
    
This module has been developed by Bernard DELHEZ @ AbAKUS it-solution.    
 """,
    "data": [
        "view/email_template_view.xml"
    ],
}
