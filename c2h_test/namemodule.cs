/*this rsp file is codegen by abelkhan for c#*/

using System;
using System.Collections;
using System.Collections.Generic;

using abelkhan;

namespace rsp
{
    public class rsp_func_test : abelkhan.Response
    {
        public string uuid;

        public rsp_func_test(string _uuid)
        {
            uuid = _uuid;
        }

        void call(Int64 argv0)
        {
            hub.hub.gates.call_client(hub.hub.gates.current_client_uuid, "name", "func_test_rsp", uuid, argv0);
        }
        void err(Int64 argv0)
        {
            hub.hub.gates.call_client(hub.hub.gates.current_client_uuid, "name", "func_test_err", uuid, argv0);
        }
    }

    public class name : abelkhan.Module
    {
        public string module_name;
        public hub.hub hub_handle;
        public name(hub.hub _hub)
        {
            module_name = "name";
            hub_handle = _hub;
            hub.hub.modules.add_module("name", this);
        }

        public delegate void func_testhandle(Int64 argv0, ArrayList argv1, Boolean argv2);
        public event func_testhandle onfunc_test;
        public void func_test(string uuid, Int64 argv0, ArrayList argv1, Boolean argv2)
        {
            if(onfunc_test != null)
            {
                rsp = new rsp_func_test(uuid);
                onfunc_test( argv1,  argv2,  argv3);
                rsp = null;
            }
        }

        public delegate void func_test2handle(Int64 argv0, Int64 argv1, Boolean argv2, Double argv3);
        public event func_test2handle onfunc_test2;
        public void func_test2(Int64 argv0, Int64 argv1, Boolean argv2, Double argv3)
        {
            if(onfunc_test2 != null)
            {
                onfunc_test2( argv0,  argv1,  argv2,  argv3);
            }
        }

    }
}
