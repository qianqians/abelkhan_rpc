/*this rsp file is codegen by abelkhan for js*/

function rsp_func_test1(_hub, _remote_hub_name, _uuid)
{
    this.hub_handle = _hub;
    this.remote_hub_name = _remote_hub_name;
    this.uuid = _uuid;
    this.call(argv0, argv1, argv2)
    {
        _hub.hubs.call_hub(_remote_hub_name, "name", "func_test1_rsp", _uuid, argv0, argv1, argv2);
    }
    this.err(argv0)
    {
        _hub.hubs.call_hub(_remote_hub_name, "name", "func_test1_err", _uuid, argv0);
    }
}

function name(_hub)
{
    var event_cb = require("event_cb");
    event_cb.call(this);

    this.module_name = "name";
    this.hub_handle = _hub;
    _hub.modules.add_module("name", this);

    this.func_test = function(argv0, argv1, argv2, argv3)
    {
        this.call_event("func_test", [argv0, argv1, argv2, argv3]);
    }

    this.func_test1 = function(remote_hub_name, uuid, argv0, argv1, argv2)
    {
        _hub.modules.rsp = new rsp_func_test1(_hub, remote_hub_name, uuid);
        this.call_event("func_test1", [argv0, argv1, argv2]);
        _hub.modules.rsp = null;
    }

}
