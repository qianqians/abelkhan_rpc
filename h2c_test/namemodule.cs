/*this imp file is codegen by abelkhan for c#*/

using System;
using System.Collections;
using System.Collections.Generic;

using common;

namespace imp
{
    public class name : common.imodule {
    {
        public string module_name;

        public name()
        {
            module_name = "name";

            hub::hub::modules.add_module("name", this);
        }

        public delegate void func_test_handle(Int64 argv0, Int64 argv1, Boolean argv2, Double argv3);
        public event func_test_handle onfunc_test;
        void func_test(ArrayList _event)
        {
            if (onfunc_test == null)
            {
                reutrn;
            }

            var argv0 = ((Int64)_event[0]);
            var argv1 = ((Int64)_event[1]);
            var argv2 = ((Boolean)_event[2]);
            var argv3 = ((Double)_event[3]);

            onfunc_test(argv0, argv1, argv2, argv3);
        }

        public delegate void func_test1_handle(String argv0, ArrayList argv1, Hashtable argv2);
        public event func_test1_handle onfunc_test1;
        void func_test1(ArrayList _event)
        {
            if (onfunc_test1 == null)
            {
                reutrn;
            }

            var argv0 = ((String)_event[0]);
            var argv1 = ((ArrayList)_event[1]);
            var argv2 = ((Hashtable)_event[2]);

            onfunc_test1(argv0, argv1, argv2);
        }

        public delegate void func_test2_handle(String argv0, ArrayList argv1, Hashtable argv2);
        public event func_test2_handle onfunc_test2;
        void func_test2(ArrayList _event)
        {
            if (onfunc_test2 == null)
            {
                reutrn;
            }

            var argv0 = ((String)_event[0]);
            var argv1 = ((ArrayList)_event[1]);
            var argv2 = ((Hashtable)_event[2]);

            onfunc_test2(argv0, argv1, argv2);
        }

    }
}
