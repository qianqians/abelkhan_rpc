/*this imp file is codegen by abelkhan for js*/
function name(_hub){
    var event_cb = require("event_cb");
    event_cb.call(this);

    this.hub_handle = _hub;
    _hub.modules.add_module("name", this);

    this.func_test = function(argv0, argv1, argv2, argv3)
    {
        this.call_event("func_test", [argv0, argv1, argv2, argv3]);
    }

    this.func_test1 = function(argv0, argv1, argv2)
    {
        this.call_event("func_test1", [argv0, argv1, argv2]);
    }

    this.func_test2 = function(argv0, argv1, argv2)
    {
        this.call_event("func_test2", [argv0, argv1, argv2]);
    }

}
