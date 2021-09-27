=======================================================
Point of Sale Require Customer / CLIMBING GYM EXTENSION
=======================================================

ADDED NEW FUNCTIONALITY
-----------------------

* check membership
* check membership status


This module was written to extend the functionality of odoo pos
and allows you to require a customer to have a membership or an 
active membership in the climbing_gym.

This is based on product.product. If a product that requires 
a membership and customer is not selected, the pos ui will display
an error message.

This control is made in the validation process of the order

'Required before paying' 
-------------------------------
In the frontend PoS, the user can start selling, but if the user tries to
make payment and if a customer is not selected, the pos ui will display an
error message.


.. image:: https://raw.githubusercontent.com/pos_customer_required/static/description/frontend_pos_error_message.png

**Table of contents**

.. contents::
   :local:

Configuration
=============

Usage
=====

Bug Tracker
===========


Credits
=======

* Apertoso NV
* La Louve

Contributors
~~~~~~~~~~~~



