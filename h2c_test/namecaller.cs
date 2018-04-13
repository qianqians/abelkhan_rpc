/*this caller file is codegen by abelkhan for c#*/
using System;
using System.Collections;
using System.IO;

namespace ntf
{
    public class name
    {
        public name()
        {
        }

        public name_cliproxy get_client(string uuid)
        {
            return newname_cliproxy(uuid);
        }

        public name_cliproxy_multi get_multicast(Arraylist uuids)
        {
            return newname_cliproxy_multi(uuids);
        }

        public name_broadcast get_broadcast()
        {
            return newname_broadcast(uuid);
        }

    }

    public class name_cliproxy
    {
        private string uuid;

        public name_cliproxy(string _uuid)
        {
            uuid = _uuid;
        }

        public void func_test(Int64 argv0, Int64 argv1, Boolean argv2, Double argv3)
        {
            ArrayList _argv = new ArrayList();
            _argv.Add(argv0);
            _argv.Add(argv1);
            _argv.Add(argv2);
            _argv.Add(argv3);
            hub.hub.gates.call_client(uuid, "name", "func_test", _argv);
        }

    }

    public class name_cliproxy_multi
    {
        private Arraylist uuids;

        public name_cliproxy_multi(Arraylist _uuids)
        {
            uuids = _uuids;
        }

        public void func_test1(String argv0, ArrayList argv1, Hashtable argv2)
        {
            ArrayList _argv = new ArrayList();
            _argv.Add(argv0);
            _argv.Add(argv1);
            _argv.Add(argv2);
            hub.hub.gates.call_group_client(uuids, "name", "func_test1", _argv);
        }

    }

    public class name_broadcast
    {
        public name_broadcast()
        {
            uuids = _uuids;
        }

        public void func_test2(String argv0, ArrayList argv1, Hashtable argv2)
        {
            ArrayList _argv = new ArrayList();
            _argv.Add(argv0);
            _argv.Add(argv1);
            _argv.Add(argv2);
            hub.hub.gates.call_global_client("name", "func_test2", _argv);
        }

    }

}
