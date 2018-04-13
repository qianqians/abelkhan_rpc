/*this req file is codegen by abelkhan for js*/

function cb_func_test1()
{
    this.event_func_test1_handle_cb = null;
    this.cb = function(argv0, argv1, argv2)
    {
        if (this.event_func_test1_handle_cb !== null)
        {
            this.event_func_test1_handle_cb(argv0, argv1, argv2);
        }
    }

    this.event_func_test1_handle_err = null;
    this.err = function(argv0)
    {
        if (this.event_func_test1_handle_err != null)
        {
            this.event_func_test1_handle_err(argv0);
        }
    }

    this.callBack = function(cb, err)
    {
        this.event_func_test1_handle_cb += cb;
        this.event_func_test1_handle_err += err;
    }
}

/*this cb code is codegen by abelkhan for js*/
function cb_name()
{
    this.map_func_test1 = {};
    this.func_test1_rsp = function(uuid, argv0, argv1, argv2)
    {
        var rsp = map_func_test1[uuid];
        rsp.cb(argv0, argv1, argv2);
    }

    this.func_test1_err = function(uuid, argv0)
    {
        var rsp = map_func_test1[uuid];
        rsp.err(argv0);
    }

}

function name(_hub_handle)
{
    this.hub_handle = _hub_handle;
    this.cb_name_handle = new cb_name();
    _hub_handle.modules.add_module("name", cb_name_handle);

    this.get_hub = function(hub_name){
        return new name_hubproxy(hub_name, _hub_handle);
    }
}

function name_hubproxy (hub_name, _hub_handle)
{
    this.hub_name = hub_name;
    this.hub_handle = _hub_handle;

    this.func_test = function(argv0, argv1, argv2, argv3)
    {
        _hub_handle.call_hub(hub_name, "name", "func_test", argv0,  argv1,  argv2,  argv3);
    }

    this.func_test1 = function(argv0, argv1, argv2)
    {
        const uuidv1 = require('uuid/v1');
        var uuid = uuidv1();

        _hub_handle.call_hub(hub_name, "name", "func_test1", _hub_handle.name, uuid, argv0,  argv1,  argv2);

        var cb_func_test1_obj = new cb_func_test1();
        this.cb_name_handle[uuid] = cb_func_test1_obj;

        return cb_func_test1_obj;
    }

}
