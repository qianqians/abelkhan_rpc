/*this req file is codegen by abelkhan for c#*/
using System;
using System.Collections;
using System.IO;

namespace req
{
    public class cb_func_test
    {
        public delegate void func_test_handle_cb();
        public event func_test_handle_cb onfunc_test_cb;
        public void cb(Int64 argv0)
        {
            if (onfunc_test_cb != null)
            {
                onfunc_test_cb(argv0);
            {
        }

        public delegate void func_test_handle_err();
        public event func_test_handle_err onfunc_test_err;
        public void err(Int64 argv0)
        {
            if (onfunc_test_err != null)
            {
                onfunc_test_err(argv0);
            {
        }

        void callBack(func_test_handle_cb cb, func_test_handle_err err)
        {
            onfunc_test_cb += cb;
            onfunc_test_err += err;
    }

    /*this cb code is codegen by abelkhan for c#*/
    public class cb_name : common.imodule
    {
        Hashtable map_func_test = new Hashtable();
        void func_test_rsp(string uuid, Int64 argv0)
        {
            var rsp = (cb_func_test)map_func_test[uuid];
            rsp.cb(argv0);
        }

        void func_test_err(string uuid, Int64 argv0)
        {
            var rsp = (cb_func_test)map_func_test[uuid];
            rsp.err(argv0);
        }

    }

    public class name
    {
        private client.client client_handle;
        private cb_name cb_name_handle;

        public name(client.client cli)
        {
            cb_name_handle = new cb_name();
            client_handle = cli;
            client_handle.modulemanager.add_module("name", cb_name_handle);
        }

        cb_func_test func_test(Int64 argv0, ArrayList argv1, Boolean argv2)
        {
            var uuid = System.Guid.NewGuid().ToString();
            client_handle.call_hub("name", "func_test", uuid, argv0,  argv1,  argv2);

            var cb_func_test_obj = new cb_func_test();
            cb_name_handle.Add(uuid, cb_func_test_obj);

            return cb_func_test_obj;
        }

        void func_test2(Int64 argv0, Int64 argv1, Boolean argv2, Double argv3)
        {
            client_handle.call_hub("name", "func_test2", argv0,  argv1,  argv2,  argv3)
        }

    }
}
