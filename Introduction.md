# Introduction #

Currently the project is layout is a simple django start-project layout.  As time goes on I will break out the customer, invoice, and crm modules.

At this point though, simply placing any of those modules on your python path and then including them in your installed apps directory is enough to start playing around, which is all you can really do at this point anyway, since nothing actually works yet.


# Details #

## Customer App ##

The customer app provides a reusable "registration" workflow and will associate a django user with a "customer" which is created by the registration process.

For now the customer app works a bit like the auth contrib app in django.  You can specify 2 settings in your settings.py: `CUSTOMER_PROFILE_FORM` AND `CUSTOMER_PROFILE_MODEL`.

`CUSTOMER_PROFILE_FORM` - By default the registration process has a small customer form that asks for a name (optional) and a username and password.  The Name field is optional, and can be used to hold a business or entity name.  If your customers are just people, you probably just want to use the first/last name fields on the User model.  The form also provides username, password and confirm password fields.  These are required and are used to generate a user model.  If you want/need other form fields set `CUSTOMER_PROFILE_FORM` to a form you control.  The create view will return this form to your template and will call this form's save method passing it a customer object and a user object (so, your form must have a save method that accepts a customer object and a user object.)  You can process the input via that save method as you need.  The view also calls is\_valid() on your form before calling save, so any validation will be done prior to save().

`CUSTOMER_PROFILE_MODEL` - Provides a model that will be linked to customer.  The customer model has a get\_profile() method just like the User model in auth.  It uses this setting to look up which model it should return as the profile.  This allows you to extend the customer information with whatever you need for your specific application

## Invoice App ##

The invoice app provides a reusable "invoicing" solution.  It will provide the following features:

  * nvoice and Invoice Line models
  * ccount model
  * ayment information storage (and eventually billing through popular payment gateways)
  * nvoice aging, payment history, partial payments
  * ssociates an account with a customer from the customer app.

## CRM App ##

Very much not started yet.