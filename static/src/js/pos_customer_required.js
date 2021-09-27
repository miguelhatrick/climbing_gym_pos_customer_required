/*
    Copyright (C) 2021-Today Miguel Hatrick
    The licence is in the file __manifest__.py
*/

odoo.define('pos_require_membership', function (require) {

"use strict";
	var module = require('point_of_sale.models');
    var models = module.PosModel.prototype.models;
    for(var i=0; i<models.length; i++){
        var model=models[i];
        if(model.model === 'res.partner'){
             model.fields.push(
                 'climbing_gym_main_member_membership_name',
                 'climbing_gym_main_member_membership_id',
                 'climbing_gym_member_membership_active',
                 'climbing_gym_member_membership_valid');
        }

        if(model.model === 'product.product'){
             model.fields.push(
                 'climbing_gym_only_members',
                 'climbing_gym_only_active_members');
        }

    }
});

odoo.define('climbing_gym_pos_customer_required.pos_customer_required', function (require) {
    "use strict";

    var screens = require('point_of_sale.screens');
    var gui = require('point_of_sale.gui');
    var core = require('web.core');
    var _t = core._t;

    screens.PaymentScreenWidget.include({
        validate_order: function(options) {

            var require_membership_valid = false;
            var require_membership_active = false;

            this.pos.get_order().get_orderlines().forEach(function (orderline) {
                var product = orderline.product;
                if (product.climbing_gym_only_members){
                    require_membership_valid = true;
                    }

                if (product.climbing_gym_only_active_members){
                    require_membership_active = true;
                    }
            });

            if((require_membership_valid || require_membership_active)
                    && !this.pos.get_order().get_client()){
                this.gui.show_popup('error',{
                    'title': _t('An anonymous order cannot be confirmed'),
                    'body':  _t('Please select a customer for this order.'),
                });
                return;
            }

            if(require_membership_valid && !this.pos.get_order().get_client().climbing_gym_member_membership_valid){
                this.gui.show_popup('error',{
                    'title': _t('This partner doesn\'t have a VALID membership'),
                    'body':  _t('Please select a customer for this order.'),
                });
                return;
            }

            if(require_membership_active && !this.pos.get_order().get_client().climbing_gym_member_membership_active){
                this.gui.show_popup('error',{
                    'title': _t('This partner doesn\'t have an active membership'),
                    'body':  _t('Please select a customer for this order.'),
                });
                return;
            }



            return this._super(options);
        }
    });


});
