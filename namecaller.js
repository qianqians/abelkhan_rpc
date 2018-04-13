/*this req file is codegen by abelkhan for js*/

function cb_func_test()
{
    this.event_func_test_handle_cb = null;
    this.cb = function(argv0)
    {
        if (this.event_func_test_handle_cb !== null)
        {
            this.event_func_test_handle_cb(argv0);
        }
    }

    this.event_func_test_handle_err = null;
    this.err = function(argv0)
    {
        if (this.event_func_test_handle_err != null)
        {
            this.event_func_test_handle_err(argv0);
        }
    }

    this.callBack = function(cb, err)
    {
        this.event_func_test_handle_cb += cb;
        this.event_func_test_handle_err += err;
    }
}

/*this cb code is codegen by abelkhan for js*/
function cb_name()
{
    this.map_func_test = {};
    this.func_test_rsp = function(uuid, argv0)
    {
        var rsp = map_func_test[uuid];
        rsp.cb(argv0);
    }

    this.func_test_err = function(uuid, argv0)
    {
        var rsp = map_func_test[uuid];
        rsp.err(argv0);
    }

}

function name(_client_handle)
{
    this.client_handle = _client_handle;
    this.cb_name_handle = new cb_name();
    _client_handle.modules.add_module("name", cb_name_handle);

    this.func_test = function(argv0, argv1, argv2)
    {
        const uuidv1 = require('uuid/v1');
        var uuid = uuidv1();

        _client_handle.call_hub("name", "func_test", uuid, argv0,  argv1,  argv2);

        var cb_func_test_obj = new cb_func_test();
        this.cb_name_handle[uuid] = cb_func_test_obj;

        return cb_func_test_obj;
    }

    this.func_test2 = function(argv0, argv1, argv2, argv3)
    {
        _client_handle.call_hub("name", "func_test2", argv0,  argv1,  argv2,  argv3);
    }

}
