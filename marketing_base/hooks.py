from odoo import SUPERUSER_ID, _, api


def pre_init_constraints(cr):
    """
    With this module you agree that your partner table should be unique on email
    in the models we'll add a unique contraint on email
    so before doing so, we'll inactivate the doubles
    i just pay attention to res_user and res_company in the order
    as i do create a message it should be easy for the user to unarchive if needed
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    env.cr.execute(
        """;WITH ranking AS
            (
                SELECT rp.*,
                    rc.id as res_company_id,
                    ru.id as res_users_id,
                    ROW_NUMBER() OVER (PARTITION BY rp.email
                                        ORDER BY ru.id, rc.id, rp.write_date DESC) AS rn
                FROM res_partner rp
                LEFT JOIN res_users ru ON ru.partner_id = rp.id
                LEFT JOIN res_company rc ON rc.partner_id = rp.id
                WHERE rp.email IS NOT null AND active
            )
            SELECT id
            FROM ranking
            WHERE rn > 1"""
    )
    doubles = env.cr.dictfetchall()
    if doubles:
        doubles_ids = [d["id"] for d in doubles]
        partners = env["res.partner"].search([("id", "in", doubles_ids)])
        partners.active = False
        partners.message_post(
            body=_("Archived by marketing_base"), message_type="comment"
        )
    env.cr.commit()
