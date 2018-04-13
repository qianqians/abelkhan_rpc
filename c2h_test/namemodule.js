/*this rsp file is codegen by abelkhan for js*/

function rsp_func_test(_hub)
{
    this.hub_handle = _hub;
    this.call(argv0)
    {
        _hub.gates.call_client(_hub.gates.current_client_uuid, "name", "func_test_rsp", argv0);
    }
    this.err(argv0)
    {
        _hub.gates.call_client(_hub.gates.current_client_uuid, "name", "func_test_rsp", argv0);
    }
}

function name(_hub)
{
    var event_cb = require("event_cb");
    event_cb.call(this);

    this.module_name = "name";
    this.hub_handle = _hub;
    _hub.modules.add_module("name", this);

    this.func_test = function(argv0, argv1, argv2)
    {
        _hub.modules.rsp = new rsp_func_test(_hub);
        this.call_event("func_test", [argv0, argv1, argv2]);
        _hub.modules.rsp = null;
    }

    this.func_test2 = function(argv0, argv1, argv2, argv3)
    {
        this.call_event("func_test2", [argv0, argv1, argv2, argv3]);
    }

}
