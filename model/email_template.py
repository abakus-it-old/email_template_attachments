from openerp.osv import osv, fields
import ast
from openerp.tools.safe_eval import safe_eval as eval
import logging
_logger = logging.getLogger(__name__)

class EmailTemplate(osv.Model):

    _inherit = "mail.template"

    _columns = {
        'email_attachments': fields.char('Add attachments from other field', help='You can only access to the current object. Example: object.attachments_ids')
    }

class MailComposeMessage(osv.TransientModel):
    _inherit = 'mail.compose.message'

    def onchange_template_id(self, cr, uid, ids, template_id, composition_mode, model, res_id, context=None):
        if not context:
            context = {}

        if template_id and isinstance(template_id, list):
            template_id = template_id[0]

        res = super(MailComposeMessage, self).onchange_template_id(cr, uid, ids, template_id, composition_mode, model, res_id, context=context)
        attach = []
        if template_id:
            template = self.pool.get('mail.template').browse(cr, uid, template_id, context)

            if template.email_attachments:
                object = self.pool.get(model).browse(cr, uid, res_id)
                attachTMP = eval(template.email_attachments, {'object': object})
                if attachTMP:
                    for attach_id in attachTMP:
                        attach.append(attach_id.id)
        attach += res.get('value', {}).pop('attachment_ids', [])
        res.get('value', {}).update({'attachment_ids': attach})

        return res
