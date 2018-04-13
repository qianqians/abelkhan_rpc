/*this rsp file is codegen by abelkhan for c#*/

using System;
using System.Collections;
using System.Collections.Generic;

using abelkhan;

namespace rsp
{
    public class rsp_func_test1 : abelkhan.Response
    {
        public string hub_name;
        public string uuid;

        public rsp_func_test1(string _hub_name, string _uuid)
        {
            hub_name = _hub_name;
            uuid = _uuid;
        }

        void call(String argv0, ArrayList argv1, Hashtable argv2)
        {
            hub.hub.hubs.call_hub(hub_name, "name", "func_test1_rsp", uuid, argv0, argv1, argv2);
        }
        void err(Int64 argv0)
        {
            hub.hub.hubs.call_hub(hub_name, "name", "func_test1_err", uuid, argv0);
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

        public delegate void func_testhandle(Int64 argv0, Int64 argv1, Boolean argv2, Double argv3);
        public event func_testhandle onfunc_test;
        public void func_test(ArrayList _event)
        {
            if(onfunc_test != null)
            {
                var argv0 = ((Int64)_event[0]);
                var argv1 = ((Int64)_event[1]);
                var argv2 = ((Boolean)_event[2]);
                var argv3 = ((Double)_event[3]);
                onfunc_test( argv0,  argv1,  argv2,  argv3);
            }
        }

        public delegate void func_test1handle(String argv0, ArrayList argv1, Hashtable argv2);
        public event func_test1handle onfunc_test1;
        public void func_test1(ArrayList _event)
        {
            if(onfunc_test1 != null)
            {
                var hub_name = (string)_event[0];
                var uuid = (string)_event[1];
                var argv0 = ((String)_event[2]);
                var argv1 = ((ArrayList)_event[3]);
                var argv2 = ((Hashtable)_event[4]);

                rsp = new rsp_func_test1(hub_name, uuid);
                onfunc_test1( argv0,  argv1,  argv2);
                rsp = null;
            }
        }

    }
}
