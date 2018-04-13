/*this req file is codegen by abelkhan for c#*/
using System;
using System.Collections;
using System.IO;

namespace req
{
    public class cb_func_test1
    {
        public delegate void func_test1_handle_cb();
        public event func_test1_handle_cb onfunc_test1_cb;
        public void cb(String argv0, ArrayList argv1, Hashtable argv2)
        {
            if (onfunc_test1_cb != null)
            {
                onfunc_test1_cb(argv0, argv1, argv2);
            }
        }

        public delegate void func_test1_handle_err();
        public event func_test1_handle_err onfunc_test1_err;
        public void err(Int64 argv0)
        {
            if (onfunc_test1_err != null)
            {
                onfunc_test1_err(argv0);
            }
        }

        void callBack(func_test1_handle_cb cb, func_test1_handle_err err)
        {
            onfunc_test1_cb += cb;
            onfunc_test1_err += err;
        }

    }

    /*this cb code is codegen by abelkhan for c#*/
    public class cb_name : common.imodule
    {
        public Hashtable map_func_test1 = new Hashtable();
        public void func_test1_rsp(string uuid, String argv0, ArrayList argv1, Hashtable argv2)
        {
            var rsp = (cb_func_test1)map_func_test1[uuid];
            rsp.cb(argv0, argv1, argv2);
        }

        public void func_test1_err(string uuid, Int64 argv0)
        {
            var rsp = (cb_func_test1)map_func_test1[uuid];
            rsp.err(argv0);
        }

    }

    public class name
    {
        private cb_name cb_name_handle;

        public name()
        {
            cb_name_handle = new cb_name();
            hub.hub.modules.add_module("name", cb_name_handle);
        }

        public name_hubproxy get_hub(string hub_name)
        {
            return new name_hubproxy(hub_name);
        }

    }

    public class name_hubproxy
    {
        public string hub_name;
        public name_hubproxy(string _hub_name)
        {
            hub_name = _hub_name;
        }

        void func_test(Int64 argv0, Int64 argv1, Boolean argv2, Double argv3)
        {
            hub.hub.hubs.call_hub(hub_name, "name", "func_test", argv0,  argv1,  argv2,  argv3);
        }

        cb_func_test1 func_test1(String argv0, ArrayList argv1, Hashtable argv2)
        {
            var uuid = System.Guid.NewGuid().ToString();
            hub.hub.hubs.call_hub(hub_name, "name", "func_test1", hub.hub.name, uuid, argv0,  argv1,  argv2);

            var cb_func_test1_obj = new cb_func_test1();
            cb_name_handle.map_func_test1.Add(uuid, cb_func_test1_obj);

            return cb_func_test1_obj;
        }

    }
}
