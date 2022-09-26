# test
test repository

Membuat moduul baru menggunakan scaffold
Model belum selesai karena ada error yang belum dimengerti

e.g Error:
Odoo Server Error

Traceback (most recent call last):
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\tools\convert.py", line 677, in _tag_root
    f(rec)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\tools\convert.py", line 580, in _tag_record
    record = model._load_records([data], self.mode == 'update')
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\models.py", line 4231, in _load_records
    records = self._load_records_create([data['values'] for data in to_create])
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\models.py", line 4152, in _load_records_create
    return self.create(values)
  File "<decorator-gen-47>", line 2, in create
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\api.py", line 348, in _model_create_multi
    return create(self, arg)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\addons\base\models\ir_actions.py", line 259, in create
    return super(IrActionsActWindow, self).create(vals_list)
  File "<decorator-gen-45>", line 2, in create
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\api.py", line 348, in _model_create_multi
    return create(self, arg)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\addons\base\models\ir_actions.py", line 47, in create
    res = super(IrActions, self).create(vals_list)
  File "<decorator-gen-64>", line 2, in create
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\api.py", line 348, in _model_create_multi
    return create(self, arg)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\addons\base\models\ir_fields.py", line 534, in create
    recs = super().create(vals_list)
  File "<decorator-gen-13>", line 2, in create
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\api.py", line 348, in _model_create_multi
    return create(self, arg)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\models.py", line 3833, in create
    raise ValueError("Invalid field %r on model %r" % (key, self._name))
ValueError: Invalid field 'view_type' on model 'ir.actions.act_window'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\addons\base\models\ir_http.py", line 237, in _dispatch
    result = request.dispatch()
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\http.py", line 683, in dispatch
    result = self._call_function(**self.params)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\http.py", line 359, in _call_function
    return checked_call(self.db, *args, **kwargs)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\service\model.py", line 94, in wrapper
    return f(dbname, *args, **kwargs)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\http.py", line 347, in checked_call
    result = self.endpoint(*a, **kw)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\http.py", line 912, in __call__
    return self.method(*args, **kw)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\http.py", line 531, in response_wrap
    response = f(*args, **kw)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\addons\web\controllers\main.py", line 1394, in call_button
    action = self._call_kw(model, method, args, kwargs)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\addons\web\controllers\main.py", line 1382, in _call_kw
    return call_kw(request.env[model], method, args, kwargs)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\api.py", line 399, in call_kw
    result = _call_kw_multi(method, model, args, kwargs)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\api.py", line 386, in _call_kw_multi
    result = method(recs, *args, **kwargs)
  File "<decorator-gen-77>", line 2, in button_immediate_upgrade
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\addons\base\models\ir_module.py", line 74, in check_and_log
    return method(self, *args, **kwargs)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\addons\base\models\ir_module.py", line 654, in button_immediate_upgrade
    return self._button_immediate_function(type(self).button_upgrade)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\addons\base\models\ir_module.py", line 593, in _button_immediate_function
    modules.registry.Registry.new(self._cr.dbname, update_module=True)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\modules\registry.py", line 89, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\modules\loading.py", line 457, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\modules\loading.py", line 349, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\modules\loading.py", line 222, in load_module_graph
    load_data(cr, idref, mode, kind='data', package=package)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\modules\loading.py", line 69, in load_data
    tools.convert_file(cr, package.name, filename, idref, mode, noupdate, kind)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\tools\convert.py", line 733, in convert_file
    convert_xml_import(cr, module, fp, idref, mode, noupdate)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\tools\convert.py", line 799, in convert_xml_import
    obj.parse(doc.getroot())
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\tools\convert.py", line 719, in parse
    self._tag_root(de)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\tools\convert.py", line 677, in _tag_root
    f(rec)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\tools\convert.py", line 685, in _tag_root
    )) from e
Exception

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\http.py", line 639, in _handle_exception
    return super(JsonRequest, self)._handle_exception(exception)
  File "C:\Program Files\Odoo 14.0.20220923\server\odoo\http.py", line 315, in _handle_exception
    raise exception.with_traceback(None) from new_cause
odoo.tools.convert.ParseError: while parsing file:/c:/program%20files/odoo%2014.0.20220923/odoo14/custom/odootest/vehicletest/views/vehicle_brand_views.xml:6, near
<record id="vehicletest_brand_action" model="ir.actions.act_window">
			<field name="name">vehicletest_brand.action</field>
			<field name="type">ir.actions.act_window</field>
			<field name="res_model">vehicletest_brand</field>
			<field name="view_mode">tree,form</field>
			<field name="view_type">form</field>
			<field name="help" type="html">
				<p class="oe_view_nocontent_create">
					<!-- Add Text Here -->
				</p>
				<p>
					<!-- More details about what a user can do with this object will be OK --> 
				</p>
			</field>
		</record>
